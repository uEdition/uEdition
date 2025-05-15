# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition language functionality."""

import os
from typing import Annotated

from rich import print as output
from typer import Option, Typer
from yaml import safe_dump, safe_load

from uedition.cli.base import app
from uedition.settings import NoConfigError

lang_app = Typer(help="Language configuration functionality")
app.add_typer(lang_app, name="language")


@lang_app.command()
def add(
    code: Annotated[str, Option(prompt="Language code")],
    label: Annotated[
        str,
        Option(prompt="Language name"),
    ],
    title: Annotated[str, Option(prompt="Title")],
    path: str | None = None,
) -> None:
    """Add a language."""
    if path is None:
        path = code
    if os.path.exists("uEdition.yml"):
        with open("uEdition.yml") as in_f:
            config = safe_load(in_f)
    elif os.path.exists("uEdition.yaml"):
        with open("uEdition.yaml") as in_f:
            config = safe_load(in_f)
    else:
        raise NoConfigError()
    if "languages" not in config:
        config["languages"] = []
    for lang in config["languages"]:
        if lang["code"] == code:
            output(
                "[red bold]The language code [/red bold]"
                f"[cyan bold]{code}[/cyan bold]"
                "[red bold] is already configured[/red bold]"
            )
            return
    if os.path.exists(path):
        output(
            f"[red bold]The target path [/red bold][cyan bold]{code}[/cyan bold][red bold] already exists.[/red bold]"
        )
    os.mkdir(path)
    config["languages"].append({"code": code, "label": label, "path": path})
    if "title" not in config:
        config["title"] = {}
    config["title"][code] = title
    with open("uEdition.yml", "w") as out_f:
        safe_dump(config, out_f)
    with open(os.path.join(path, "index.md"), "w") as out_f:
        out_f.write(f"# {title}\n")
