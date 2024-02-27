"""Tests for the 'build' functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_yaml_load(runner: CliRunner, yaml_app: Typer) -> None:
    """Test that the basic build works."""
    result = runner.invoke(yaml_app, ["build"])
    assert result.exit_code == 0
