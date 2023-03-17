"""Tests for the 'about' functionality."""
from typer import Typer
from typer.testing import CliRunner


def test_version(runner: CliRunner, basic_app: Typer) -> None:
    """Test that the correct version string is reported."""
    result = runner.invoke(basic_app, ['version'])
    assert result.exit_code == 0
    assert "μEdition: 0.0.3" in result.stdout
    assert "Configuration: 1" in result.stdout
