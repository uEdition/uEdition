# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import os
import typer

from rich import print as print_cli
from shutil import rmtree, copytree
from subprocess import run

from . import check as check_module, serve as serve_module
from ..__about__ import __version__
from ..settings import settings


app = typer.Typer()


@app.command()
def build() -> None:
    """Build the μEdition."""
    if not os.path.exists(settings['output']):
        os.mkdir(settings['output'])
    for language in settings['languages']:
        run(['jupyter-book', 'clean', language['path']])
        run(['jupyter-book', 'build', language['path']])
        if os.path.exists(os.path.join(settings['output'], language['path'])):
            rmtree(os.path.join(settings['output'], language['path']))
        copytree(
            os.path.join(language['path'], '_build', 'html'),
            os.path.join(settings['output'], language['path'])
        )


@app.command()
def serve() -> None:
    """Serve the μEdition for writing."""
    serve_module.run()


@app.command()
def check() -> None:
    """Check that the μEdition is set up correctly."""
    check_module.run()


@app.command()
def version() -> None:
    """Output the current μEdition version."""
    print_cli(f'μEdition: {__version__}')
    print_cli(f'Configuration: {settings["version"]}')
