# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Local server that automatically rebuilds on changes."""
from livereload import Server
from os import path
from typing import Callable

from .build import full_build, partial_build
from ..settings import settings


def build_cmd(lang: dict, full: bool = True) -> Callable[[], None]:
    """Create a function that (re-)builds one of the sub-sites."""
    if full:

        def cmd() -> None:
            full_build(lang)

        return cmd
    else:

        def cmd() -> None:
            partial_build(lang)

        return cmd


def run() -> None:
    """Run the development server."""
    full_rebuilds = [build_cmd(lang, full=True) for lang in settings["languages"]]
    partial_rebuilds = [build_cmd(lang, full=False) for lang in settings["languages"]]
    for cmd in full_rebuilds:
        cmd()
    server = Server()
    for lang, full_cmd, partial_cmd in zip(
        settings["languages"], full_rebuilds, partial_rebuilds
    ):
        server.watch("*.yml", full_cmd)
        server.watch(path.join(lang["path"], "**", "*.*"), partial_cmd)
    server.watch("uEdition.*", lambda: [cmd() for cmd in full_rebuilds])
    server.serve(root="site", port=8000)
