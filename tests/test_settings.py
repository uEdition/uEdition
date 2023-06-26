"""Tests for the core settings functionality."""
from typer import Typer
from typer.testing import CliRunner


def test_empty_defaults(runner: CliRunner, empty_app: Typer) -> None:
    """Test that running in an empty directory works."""
    result = runner.invoke(empty_app, ["version"])
    assert result.exit_code == 0


def test_load_from_yaml(runner: CliRunner, yaml_app: Typer) -> None:
    """Test that loading the configuration from a .yaml file works."""
    result = runner.invoke(yaml_app, ["version"])
    assert result.exit_code == 0
