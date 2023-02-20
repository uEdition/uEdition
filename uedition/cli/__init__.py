# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import typer

from ..__about__ import __version__
from ..settings import settings


app = typer.Typer()


@app.command()
def build() -> None:
    """Build the uEdition."""
    print('Build')  # noqa: T201
    print(settings)  # noqa: T201


@app.command()
def version() -> None:
    """Output the current uEdition version."""
    print(f'uEdition: {__version__}')  # noqa: T201
