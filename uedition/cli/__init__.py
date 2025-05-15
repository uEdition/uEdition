# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""

from rich import print as output

from uedition.__about__ import __version__
from uedition.cli import build, init, language, migrate, serve, update  # noqa:F401
from uedition.cli.base import app
from uedition.settings import settings


@app.command()
def version() -> None:
    """Output the current μEdition version."""
    output(f"μEdition:      {__version__}")
    output(f"Configuration: {settings['version']}")
