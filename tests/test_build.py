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
