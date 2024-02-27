"""Tests for the 'build' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_basic_build(runner: CliRunner, multilang_app: Typer) -> None:
    """Test that the basic build works."""
    result = runner.invoke(multilang_app, ["build"])
    assert result.exit_code == 0


def test_basic_build_rebuild(runner: CliRunner, multilang_app: Typer) -> None:
    """Test that rebuilding works."""
    result = runner.invoke(multilang_app, ["build"])
    assert result.exit_code == 0
    result = runner.invoke(multilang_app, ["build"])
    assert result.exit_code == 0


def test_empty_build_fails(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in a directory with no configuration file fails."""
    result = runner.invoke(empty_app, ["build"])
    assert result.exit_code != 0
