"""Tests for the 'build' functionality."""

from typer import Typer
from typer.testing import CliRunner

from uedition.settings import Settings


def test_yaml_load(runner: CliRunner, yaml_app: Typer) -> None:
    """Test that the basic build works."""
    result = runner.invoke(yaml_app, ["build"])
    assert result.exit_code == 0


def test_path_conversion() -> None:
    """Test that the path conversion works as designed."""
    settings = Settings(output="test")
    assert settings.output.path == "test"
