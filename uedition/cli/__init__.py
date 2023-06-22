# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import typer

from rich import print as print_cli

from . import check as check_module, build as build_module, serve as serve_module
from ..__about__ import __version__
from ..settings import settings


app = typer.Typer()


@app.command()
def build() -> None:
    """Build the μEdition."""
    build_module.run()


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
