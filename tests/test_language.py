"""Tests for the 'language' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_empty_language_add_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["language", "add", "--code", "en", "--name", "en", "--title", "English"])
    assert result.exit_code != 0
