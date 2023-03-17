# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import os
import typer

from rich import print as print_cli
from shutil import rmtree, copytree
from subprocess import run

from ..__about__ import __version__
from ..settings import settings


app = typer.Typer()


@app.command()
def build() -> None:
    """Build the uEdition."""
    if os.path.exists(settings['output']):
        rmtree(settings['output'])
    for language in settings['languages']:
        run(['jupyter-book', 'clean', language['path']])
        run(['jupyter-book', 'build', language['path']])
        copytree(
            os.path.join(language['path'], '_build', 'html'),
            os.path.join(settings['output'], language['path'])
        )


@app.command()
def version() -> None:
    """Output the current uEdition version."""
    print_cli(f'μEdition: {__version__}')
    print_cli(f'Configuration: {settings["version"]}')
