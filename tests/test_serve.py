"""Tests for the 'serve' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_empty_serve_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["serve"])
    assert result.exit_code != 0
