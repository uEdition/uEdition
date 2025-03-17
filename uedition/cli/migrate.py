# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition migration functionality."""

import os
from os import path

from rich import print as output

from uedition.cli.base import app
from uedition.settings import NoConfigError


def cleanup_old_configuration() -> None:
    """Remove old configuration."""
    # Scan for old files to remove
    old_copier_files = []
    old_config_files = []
    for basepath, _, filenames in os.walk("."):
        for filename in filenames:
            if filename == ".uEdition.answers":
                old_copier_files.append(path.join(basepath, filename))
            elif filename in ("_config.yaml", "_config.yml"):
                old_config_files.append(path.join(basepath, filename))
    # Remove old copier files (v2.0.0)
    if len(old_copier_files) > 0:
        output(":broom: Removing old configuration answers")
        for filename in old_copier_files:
            os.unlink(filename)
    # Remove old config files (v2.0.0)
    if len(old_config_files) > 0:
        output(":broom: Removing old configuration files")
        for filename in old_config_files:
            os.unlink(filename)
    # Update .gitignore (v2.0.0)
    if path.isfile(".gitignore"):
        with open(".gitignore") as in_f:
            lines = in_f.readlines()
        original_length = len(lines)
        lines = [line for line in lines if line.strip() not in ("_config.yml", "_config.yaml")]
        found = False
        for line in lines:
            if line.strip() == "conf.py":
                found = True
        if not found or len(lines) != original_length:
            output(":broom: Updating the .gitignore")
            if not found:
                lines.append("conf.py\n")
            with open(".gitignore", "w") as out_f:
                for line in lines:
                    out_f.write(line)


@app.command()
def migrate() -> None:
    """Migrate the μEdition to the latest version."""
    if not path.exists("uEdition.yml") and not path.exists("uEdition.yaml") and not path.exists("pyproject.toml"):
        raise NoConfigError()
    output(":hammer: Migrating the μEdition")
    cleanup_old_configuration()
    output(":checkered_flag: Migration complete")
