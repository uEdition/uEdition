# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Application settings.

All application settings are accessed via the `settings` dictionary.
"""
import os
from typing import Annotated, Any, Dict, Tuple, Type

from pydantic import BaseModel
from pydantic.fields import FieldInfo
from pydantic.functional_validators import BeforeValidator
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
from yaml import safe_load


class YAMLConfigSettingsSource(PydanticBaseSettingsSource):
    """Loads the configuration settings from a YAML file."""

    def get_field_value(
        self: "YAMLConfigSettingsSource", field: FieldInfo, field_name: str  # noqa: ARG002
    ) -> Tuple[Any, str, bool]:
        """Get the value of a specific field."""
        encoding = self.config.get("env_file_encoding")
        file_content_json = None
        if os.path.exists("uEdition.yaml"):
            with open("uEdition.yaml", encoding=encoding) as in_f:
                file_content_json = safe_load(in_f)
        elif os.path.exists("uEdition.yml"):
            with open("uEdition.yml", encoding=encoding) as in_f:
                file_content_json = safe_load(in_f)
        if file_content_json is not None:
            field_value = file_content_json.get(field_name)
        else:
            field_value = None
        return field_value, field_name, False

    def prepare_field_value(
        self: "YAMLConfigSettingsSource",
        field_name: str,  # noqa: ARG002
        field: FieldInfo,  # noqa: ARG002
        value: Any,  # noqa: ANN401
        value_is_complex: bool,  # noqa: ARG002, FBT001
    ) -> Any:  # noqa: ANN401
        """Just return the value."""
        return value

    def __call__(self: "YAMLConfigSettingsSource") -> Dict[str, Any]:
        """Call the loader."""
        d: Dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(field, field_name)
            field_value = self.prepare_field_value(field_name, field, field_value, value_is_complex)
            if field_value is not None:
                d[field_key] = field_value

        return d


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


class OuputSettings(BaseModel):
    """Settings for the output configuration."""

    path: str = "docs"
    """The output path."""
    tei: bool = True
    """Whether to generate TEI output."""


def convert_output_str_to_dict(value: str | dict) -> dict:
    """Convert the simple output directory string to a dictionary."""
    if isinstance(value, str):
        return {"path": value}
    return value


class Settings(BaseSettings):
    """Application settings."""

    version: str = "1"
    """The configuration file version."""
    author: AuthorSettings = AuthorSettings()
    """The author settings."""
    languages: list[LanguageSetting] = []
    """The configured languages."""
    output: Annotated[OuputSettings, BeforeValidator(convert_output_str_to_dict)] = OuputSettings()
    """The output directory."""
    repository: RepositorySettings = RepositorySettings()
    """The repository settings."""
    title: dict = {}
    """The titles for the individual languages."""
    jb_config: dict = {}
    """Additional JupyterBook configuration."""

    @classmethod
    def settings_customise_sources(
        cls: Type["Settings"],
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Customise the settings sources."""
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YAMLConfigSettingsSource(settings_cls),
        )


settings = Settings().model_dump()


def reload_settings() -> None:
    """Reload the settings."""
    settings.clear()
    settings.update(Settings().dict())
