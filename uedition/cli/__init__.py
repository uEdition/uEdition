# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import typer

from rich import print as print_cli

from ..__about__ import __version__
from ..settings import settings


app = typer.Typer()


@app.command()
def build() -> None:
    """Build the uEdition."""
    print_cli('Build')
    print_cli(settings)


@app.command()
def version() -> None:
    """Output the current uEdition version."""
    print_cli(f'μEdition: {__version__}')
    print_cli(f'Configuration: {settings["version"]}')
