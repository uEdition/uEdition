"""Py.test fixtures."""

import os
from shutil import rmtree
from typing import Generator

from pytest import fixture
from typer import Typer
from typer.testing import CliRunner


@fixture
def runner() -> Generator[CliRunner, None, None]:
    """Yield the Typer CliRunner for executing tests."""
    runner = CliRunner()
    yield runner


@fixture
def empty_app() -> Generator[Typer, None, None]:
    """Yield a uEdition application with no configuration set."""
    cwd = os.getcwd()
    try:
        os.chdir("tests/fixtures/empty")
        from uedition.cli import app
        from uedition.settings import reload_settings

        reload_settings()
        yield app
    finally:
        os.chdir(cwd)


@fixture
def basic_app() -> Generator[Typer, None, None]:
    """Yield a basic uEdition application."""
    cwd = os.getcwd()
    try:
        os.chdir("tests/fixtures/basic")
        from uedition.cli import app
        from uedition.settings import reload_settings

        reload_settings()
        yield app
    finally:
        os.chdir(cwd)


@fixture
def yaml_app() -> Generator[Typer, None, None]:
    """Yield a basic application initiated from a folder with a .yaml file."""
    cwd = os.getcwd()
    try:
        os.chdir("tests/fixtures/yaml")
        from uedition.cli import app
        from uedition.settings import reload_settings

        reload_settings()
        yield app
    finally:
        os.chdir(cwd)


@fixture
def multilang_app() -> Generator[Typer, None, None]:
    """Yield a fully featured application with multiple languages configured."""
    cwd = os.getcwd()
    try:
        os.chdir("tests/fixtures/multilang")
        if os.path.exists("docs"):  # no cov
            rmtree("docs")
        if os.path.exists("en/_build"):  # no cov
            rmtree("en/_build")
        if os.path.exists("de/_build"):  # no cov
            rmtree("de/_build")
        from uedition.cli import app
        from uedition.settings import reload_settings

        reload_settings()
        yield app
    finally:
        os.chdir(cwd)
