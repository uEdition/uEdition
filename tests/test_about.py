"""Tests for the 'about' functionality."""

from typer import Typer
from typer.testing import CliRunner

from uedition.__about__ import __version__


def test_version(runner: CliRunner, basic_app: Typer) -> None:
    """Test that the correct version string is reported."""
    result = runner.invoke(basic_app, ["version"])
    assert result.exit_code == 0
    assert f"μEdition: {__version__}" in result.stdout
    assert "Configuration: 1" in result.stdout
