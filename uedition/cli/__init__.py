# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdtion Command-line Tool."""
import typer
from rich import print as print_cli

from uedition.__about__ import __version__
from uedition.cli import build as build_module
from uedition.cli import check as check_module
from uedition.cli import create as create_module
from uedition.cli import language as language_module
from uedition.cli import serve as serve_module
from uedition.cli import update as update_module
from uedition.settings import settings

app = typer.Typer()
language_app = typer.Typer()
app.add_typer(language_app, name="language")


@app.command()
def create(path: str) -> None:
    """Create a new μEdition."""
    create_module.run(path)


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
def update() -> None:
    """Update the μEdition."""
    update_module.run()


@app.command()
def version() -> None:
    """Output the current μEdition version."""
    print_cli(f"μEdition: {__version__}")
    print_cli(f'Configuration: {settings["version"]}')


@language_app.command("add")
def language_add(path: str) -> None:
    """Add a language to the μEdition."""
    language_module.add(path)


@language_app.command("update")
def language_update(path: str) -> None:
    """Update a language."""
    language_module.update(path)
