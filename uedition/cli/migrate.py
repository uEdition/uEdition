# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition migration functionality."""

import os
from os import path

import tomlkit
from rich import print as output

from uedition.cli.base import app
from uedition.settings import NoConfigError


def cleanup_old_files() -> None:
    """Cleanup any old files."""
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


def cleanup_gitignore() -> None:
    """Cleanup the gitignore."""
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


def cleanup_pyproject() -> None:
    """Cleanup the pyproject file."""
    if not path.exists("pyproject.toml"):
        raise NoConfigError()
    with open("pyproject.toml") as in_f:
        pyproject = tomlkit.parse(in_f.read())
    updated = False
    if "tool" not in pyproject:
        pyproject["tool"] = tomlkit.table()
    if "hatch" not in pyproject["tool"]:
        pyproject["tool"]["hatch"] = tomlkit.table()
    if "envs" not in pyproject["tool"]["hatch"]:
        pyproject["tool"]["hatch"]["envs"] = tomlkit.table()
    if "default" not in pyproject["tool"]["hatch"]["envs"]:
        pyproject["tool"]["hatch"]["envs"]["default"] = tomlkit.table()
    if "scripts" not in pyproject["tool"]["hatch"]["envs"]["default"]:
        pyproject["tool"]["hatch"]["envs"]["default"]["scripts"] = tomlkit.table()
        updated = True
    if "add-language" in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        del pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["add-language"]
        updated = True
    if "update-language" in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        del pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["update-language"]
        updated = True
    if "migrate" not in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["migrate"] = "uEdition migrate {args}"
        updated = True
    if "language" not in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["language"] = "uEdition language {args}"
        updated = True
    if "init" not in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["init"] = "uEdition init {args}"
        updated = True
    if "edit" not in pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]:
        pyproject["tool"]["hatch"]["envs"]["default"]["scripts"]["edit"] = (
            "uvicorn --port 8000 uedition_editor:app {args} {args}"
        )
        updated = True
    if updated:
        output(":broom: Updating the pyproject.toml")
    with open("pyproject.toml", "w") as out_f:
        tomlkit.dump(pyproject, out_f)


def migrate_ueditor() -> None:
    """Migrate the μEditor to the latest supported version."""
    ueditor_version = "uedition_editor>=2.0.0b5,<2.1"
    output(":hammer: Updating the μEditor")
    with open("pyproject.toml") as in_f:
        pyproject = tomlkit.parse(in_f.read())
    found_ueditor = False
    for idx, dep in enumerate(pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"]):
        dep = dep.lower()  # noqa:PLW2901
        if (
            dep == "uedition_editor"
            or dep.startswith("uedition_editor=")
            or dep.startswith("uedition_editor<")
            or dep.startswith("uedition_editor>")
        ):
            pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"][idx] = ueditor_version
            found_ueditor = True
    if not found_ueditor:
        pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"].append(ueditor_version)
    with open("pyproject.toml", "w") as out_f:
        tomlkit.dump(pyproject, out_f)


@app.command()
def migrate() -> None:
    """Migrate the μEdition to the latest version."""
    if not path.exists("uEdition.yml") and not path.exists("uEdition.yaml") and not path.exists("pyproject.toml"):
        raise NoConfigError()
    output(":hammer: Migrating the μEdition")
    cleanup_old_files()
    cleanup_gitignore()
    cleanup_pyproject()
    migrate_ueditor()
    output(":checkered_flag: Migration complete")
