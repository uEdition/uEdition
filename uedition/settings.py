# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Application settings.

All application settings are accessed via the `settings` dictionary.
"""
import os

from pydantic import BaseSettings, BaseModel
from pydantic.env_settings import SettingsSourceCallable
from yaml import safe_load
from typing import Any


def uedition_yaml_settings(settings: BaseSettings) -> dict[str, Any]:
    """Load the settings from a uEdition.yaml or uEdition.yml file."""
    if os.path.exists("uEdition.yaml"):
        with open(
            "uEdition.yaml", encoding=settings.__config__.env_file_encoding
        ) as in_f:
            return safe_load(in_f)
    elif os.path.exists("uEdition.yml"):
        with open(
            "uEdition.yml", encoding=settings.__config__.env_file_encoding
        ) as in_f:
            return safe_load(in_f)
    return dict()


class LanguageSetting(BaseModel):
    """Settings for a single language."""

    code: str
    """The language's code."""
    label: str
    """The language's human-readable label."""
    path: str
    """The path the language's content is at."""


class RepositorySettings(BaseModel):
    """Settings for the git repository."""

    url: str | None = None
    """The repository's URL."""
    branch: str | None = None
    """The repository's branch."""


class AuthorSettings(BaseModel):
    """Settings for the author configuration."""

    name: str = "Unnamed"
    """The author's name."""
    email: str = ""
    """The author's contact e-mail."""


class Settings(BaseSettings):
    """Application settings."""

    version: str = "1"
    """The configuration file version."""
    author: AuthorSettings = AuthorSettings()
    """The author settings."""
    languages: list[LanguageSetting] = []
    """The configured languages."""
    output: str = "docs"
    """The output directory."""
    repository: RepositorySettings = RepositorySettings()
    """The repository settings."""
    title: dict = {}
    """The titles for the individual languages."""
    jb_config: dict = {}
    """Additional JupyterBook configuration."""

    class Config:
        """Configuration overrides."""

        @classmethod
        def customise_sources(
            cls,  # noqa: ANN102
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            """Add the YAMl loading functionality."""
            return (
                env_settings,
                init_settings,
                file_secret_settings,
                uedition_yaml_settings,
            )


settings = Settings().dict()


def reload_settings() -> None:
    """Reload the settings."""
    global settings
    settings.clear()
    settings.update(Settings().dict())
