# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Local server that automatically rebuilds on changes."""

from os import path
from typing import Callable

from livereload import Server

from uedition.cli.base import app
from uedition.cli.build import full_build, partial_build
from uedition.settings import NoConfigError, settings


def build_cmd(lang: dict, full: bool = True) -> Callable[[], None]:  # noqa: FBT001, FBT002
    """Create a function that (re-)builds one of the sub-sites."""
    if full:

        def cmd() -> None:
            full_build(lang)

        return cmd
    else:

        def cmd() -> None:
            partial_build(lang)

        return cmd


@app.command()
def serve() -> None:
    """Run the local μEdition writing server."""
    if not path.exists("uEdition.yml") and not path.exists("uEdition.yaml"):
        raise NoConfigError()
    full_rebuilds = [build_cmd(lang, full=True) for lang in settings["languages"]]
    partial_rebuilds = [build_cmd(lang, full=False) for lang in settings["languages"]]

    def complete_rebuild():
        for cmd in full_rebuilds:
            cmd()

    complete_rebuild()

    server = Server()
    server.watch("*.yml", complete_rebuild)
    server.watch(path.join("static", "**", "*.*"), complete_rebuild)
    for lang, partial_cmd in zip(settings["languages"], partial_rebuilds):
        server.watch(path.join(lang["path"], "**", "*.*"), partial_cmd)
    server.watch("uEdition.*", lambda: [cmd() for cmd in full_rebuilds])
    server.serve(root=settings["output"]["path"], port=8000)
