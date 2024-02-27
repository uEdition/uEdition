"""Tests for the 'update' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_empty_update_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["update"])
    assert result.exit_code != 0
