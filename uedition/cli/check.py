# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The uEdition check functionality for validating a uEdition and its files."""
import os
from threading import Thread

import typer
from rich import print as print_cli
from rich.progress import Progress
from yaml import safe_load

from uedition.settings import settings


def collect_files(toc: dict) -> list[str]:
    """Collect all files from a TOC."""
    files = []
    if "parts" in toc:
        for part in toc["parts"]:
            files.extend(collect_files(part))
    elif "chapters" in toc:
        for chapter in toc["chapters"]:
            files.append(chapter["file"])
            files.extend(collect_files(chapter))
    elif "sections" in toc:
        for sections in toc["sections"]:
            files.append(sections["file"])
    return files


def compare_tocs(prefix: str, toc_a: dict, toc_b: dict) -> list[tuple[str | None, str | None]]:
    """Recursively compare the structure of two TOCs."""
    mismatches = []
    if "parts" in toc_a and "parts" in toc_b:
        pass
    elif "chapters" in toc_a and "chapters" in toc_b:
        pass
    elif "sections" in toc_a and "sections" in toc_b:
        pass
    elif "parts" in toc_a:
        mismatches.append(f"{prefix}has parts, which are missing from")
    elif "chapters" in toc_a:
        mismatches.append(f"{prefix}has chapters, which are missing from")
    elif "sections" in toc_b:
        mismatches.append(f"{prefix}has sections, which are missing from")
    return mismatches


class ConfigurationFileChecks(Thread):
    """Basic configuration file checks."""

    def __init__(self: "ConfigurationFileChecks", progress: Progress, task: int) -> None:
        """Initialise the thread."""
        super().__init__(group=None)
        self._progress = progress
        self._task = task
        self.errors = []

    def run(self: "ConfigurationFileChecks") -> None:
        """Run the checks."""
        for lang in settings["languages"]:
            yaml_path = os.path.join(lang["path"], "_config.yml")
            if os.path.exists(yaml_path):
                with open(yaml_path) as in_f:
                    try:
                        safe_load(in_f)
                    except Exception as e:
                        self.errors.append(str(e))
            else:
                self.errors.append(f"Missing configuration file {yaml_path}")
            self._progress.update(self._task, advance=1)


class TocFileChecks(Thread):
    """TOC file checks."""

    def __init__(self: "TocFileChecks", progress: Progress, task: int) -> None:
        """Initialise the thread."""
        super().__init__(group=None)
        self._progress = progress
        self._task = task
        self.errors = []

    def run(self: "TocFileChecks") -> None:
        """Run the checks."""
        for lang in settings["languages"]:
            yaml_path = os.path.join(lang["path"], "_toc.yml")
            if os.path.exists(yaml_path):
                with open(yaml_path) as in_f:
                    try:
                        toc = safe_load(in_f)
                        if "root" in toc:
                            root_path = os.path.join(lang["path"], f'{toc["root"]}.md')
                            if not os.path.exists(root_path):
                                self.errors.append(f'Root in {yaml_path} points to missing file {toc["root"]}.md')
                            root_base = os.path.dirname(root_path)
                            for filename in collect_files(toc):
                                if not os.path.exists(os.path.join(root_base, f"{filename}.md")):
                                    self.errors.append(f"File {filename}.md missing in {yaml_path}")
                        else:
                            self.errors.append(f"No root in {yaml_path}")
                    except Exception as e:
                        self.errors.append(str(e))
            else:
                self.errors.append(f"Missing toc file {yaml_path}")
            self._progress.update(self._task, advance=1)


class LanguageConsistencyChecks(Thread):
    """Multi-language consistency checks."""

    def __init__(self: "LanguageConsistencyChecks", progress: Progress, task: int) -> None:
        """Initialise the thread."""
        super().__init__(group=None)
        self._progress = progress
        self._task = task
        self.errors = []

    def run(self: "LanguageConsistencyChecks") -> None:
        """Run the checks."""
        if len(settings["languages"]) == 0:
            return
        base_toc_path = os.path.join(settings["languages"][0]["path"], "_toc.yml")
        if not os.path.exists(base_toc_path):
            return
        with open(base_toc_path) as in_f:
            try:
                base_toc = safe_load(in_f)
            except Exception:
                return
        for lang in settings["languages"][1:]:
            lang_toc_path = os.path.join(lang["path"], "_toc.yml")
            if not os.path.exists(lang_toc_path):
                continue
            try:
                with open(lang_toc_path) as in_f:
                    lang_toc = safe_load(in_f)
                missmatches = compare_tocs("", base_toc, lang_toc)
                if len(missmatches) > 0:
                    for mismatch in missmatches:
                        if mismatch[0] is None:
                            self.errors.append(f"{base_toc_path} {mismatch[1]} {lang_toc_path}")
                        elif mismatch[0] is None:
                            self.errors.append(f"{lang_toc_path} {mismatch[0]} {base_toc_path}")
                self._progress.update(self._task, advance=1)
            except Exception as e:
                self.errors.append(f"Fail to check langauge {lang}: {e!s}")


def run() -> None:
    """Check that the μEdition is correctly set up."""
    errors = []
    with Progress() as progress:
        threads = [
            ConfigurationFileChecks(
                progress,
                progress.add_task("[green]Configuration file checks", total=len(settings["languages"])),
            ),
            TocFileChecks(
                progress,
                progress.add_task("[green]TOC file checks", total=len(settings["languages"])),
            ),
            LanguageConsistencyChecks(
                progress,
                progress.add_task(
                    "[green]Language consistency checks",
                    total=len(settings["languages"]) - 1,
                ),
            ),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            errors.extend(thread.errors)
    if len(errors) > 0:
        print_cli("[red]:bug: The following errors were found:")
        for error in errors:
            print_cli(f"[red]* {error}")
        raise typer.Exit(code=1)
    else:
        print_cli("[green]:+1: All checks successfully passed")
