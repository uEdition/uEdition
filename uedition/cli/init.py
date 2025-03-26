# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Local server that automatically rebuilds on changes."""

from os import path

from yaml import safe_dump

from uedition.cli.base import app
from uedition.settings import NoConfigError


@app.command()
def init(force: bool = False) -> None:  # noqa: ARG001 FBT001 FBT002
    """Run the development server."""
    if path.exists("uEdition.yml") and path.exists("uEdition.yaml"):
        raise NoConfigError()
    with open("uEdition.yml", "w") as out_f:
        safe_dump({"version": "2", "output": "site"}, out_f)
