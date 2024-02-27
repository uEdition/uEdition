"""Tests for the 'language' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_empty_language_add_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["language", "add"])
    assert result.exit_code != 0


def test_empty_language_update_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["language", "update"])
    assert result.exit_code != 0
