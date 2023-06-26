"""Py.test fixtures."""
import os

from pytest import fixture
from shutil import rmtree
from typer.testing import CliRunner


@fixture
def runner() -> None:
    """Yield the Typer CliRunner for executing tests."""
    runner = CliRunner()
    yield runner


@fixture
def empty_app() -> None:
    """Yield a uEdition application with no configuration set."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/empty")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def basic_app() -> None:
    """Yield a basic uEdition application."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/basic")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def yaml_app() -> None:
    """Yield a basic application initiated from a folder with a .yaml file."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/yaml")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def multilang_app() -> None:
    """Yield a fully featured application with multiple languages configured."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/multilang")
    if os.path.exists("docs"):  # noqa: cov
        rmtree("docs")
    if os.path.exists("en/_build"):  # noqa: cov
        rmtree("en/_build")
    if os.path.exists("de/_build"):  # noqa: cov
        rmtree("de/_build")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def missing_core_files_app() -> None:
    """Yield a basic application where the core _config.yml and _toc.yml files are missing."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/missing_core_files")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def invalid_core_files_app() -> None:
    """Yield a basic application where the core _config.yml and _toc.yml files are invalid YAML."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/invalid_core_files")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def missing_toc_root_app() -> None:
    """Yield a basic application where the _toc.yml file is missing the root entry."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/missing_toc_root")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def missing_toc_root_file_app() -> None:
    """Yield a basic application where the _toc.yml file points to a missing root file."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/missing_toc_root_file")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)


@fixture
def missing_files_app() -> None:
    """Yield a basic application where some files are missing root file."""
    cwd = os.getcwd()
    os.chdir("tests/fixtures/missing_files")
    from uedition.cli import app
    from uedition.settings import reload_settings

    reload_settings()
    yield app
    os.chdir(cwd)
