"""Tests for the check functionality."""

from typer import Typer
from typer.testing import CliRunner


def test_check_multilang(runner: CliRunner, multilang_app: Typer) -> None:
    """Test that a correctly setup uEdition throws no errors."""
    result = runner.invoke(multilang_app, ["check"])
    assert result.exit_code == 0
    assert "All checks successfully passed" in result.stdout


def test_check_missing_core_files(runner: CliRunner, missing_core_files_app: Typer) -> None:
    """Test that missing core files (_config.yml, _toc.yml) are correctly reported."""
    result = runner.invoke(missing_core_files_app, ["check"])
    assert result.exit_code == 1
    assert "The following errors were found" in result.stdout
    assert "Missing configuration file en/_config.yml" in result.stdout
    assert "Missing toc file en/_toc.yml" in result.stdout


def test_check_invalid_core_files_app(runner: CliRunner, invalid_core_files_app: Typer) -> None:
    """Test that missing core files (_config.yml, _toc.yml) are correctly reported."""
    result = runner.invoke(invalid_core_files_app, ["check"])
    assert result.exit_code == 1
    assert "The following errors were found" in result.stdout
    assert "en/_config.yml" in result.stdout
    assert "en/_toc.yml" in result.stdout
    assert "mapping values are not allowed here" in result.stdout


def test_missing_toc_root(runner: CliRunner, missing_toc_root_app: Typer) -> None:
    """Test that a missing toc root entry is correctly reported."""
    result = runner.invoke(missing_toc_root_app, ["check"])
    assert result.exit_code == 1
    assert "The following errors were found" in result.stdout
    assert "No root in en/_toc.yml" in result.stdout


def test_missing_toc_root_file(runner: CliRunner, missing_toc_root_file_app: Typer) -> None:
    """Test that a missing root file is correctly reported."""
    result = runner.invoke(missing_toc_root_file_app, ["check"])
    assert result.exit_code == 1
    assert "The following errors were found" in result.stdout
    assert "Root in en/_toc.yml points to missing file missing.md" in result.stdout


def test_missing_files(runner: CliRunner, missing_files_app: Typer) -> None:
    """Test that missing files are correctly reported."""
    result = runner.invoke(missing_files_app, ["check"])
    assert result.exit_code == 1
    assert "The following errors were found" in result.stdout
    assert "File a-page.md missing in en/_toc.yml" in result.stdout
