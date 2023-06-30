# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""uEdition configuration handling.

This module handles reading the uEdition-specific configuration settings, validating them and
adding any required default values.
"""
from pydantic import BaseModel, validator, ValidationError
from sphinx.application import Sphinx
from sphinx.util import logging
from typing import Union, Literal, Optional


logger = logging.getLogger(__name__)


class RuleSelectorAttribute(BaseModel):
    """Validation rule for selecting based on an attribute with a given value."""

    attr: str
    value: str


class RuleSelector(BaseModel):
    """Validation rule for the selector for matching a TEI tag."""

    tag: str
    attributes: list[RuleSelectorAttribute] = []

    @validator("tag", pre=True)
    def expand_tag_namespace(
        cls: "RuleSelector", v: str, values: dict, **kwargs: dict
    ) -> str:
        """Expand any ```tei:``` namespace prefixes."""
        return v.replace("tei:", "{http://www.tei-c.org/ns/1.0}")

    @validator("attributes", pre=True)
    def convert_dict_attributes_to_list(
        cls: "RuleSelector", v: dict | list, values: dict, **kwargs: dict
    ) -> list[dict]:
        """Convert a single attributes dictionary to a list with that dictionary."""
        if isinstance(v, dict):
            return [v]
        return v


class RuleText(BaseModel):
    """Validation rule for retrieving the text content from an attribute."""

    action: Literal["from-attribute"]
    attr: str


class RuleAttributeCopy(BaseModel):
    """Validation rule for copying and attribute."""

    action: Literal["copy"] = "copy"
    attr: str
    source: str


class RuleAttributeSet(BaseModel):
    """Validation rule for settings an attribute to a specific value."""

    action: Literal["set"]
    attr: str
    value: str


class RuleAttributeDelete(BaseModel):
    """Validation rule for deleting an attribute."""

    action: Literal["delete"]
    attr: str


class Rule(BaseModel):
    """Validation model for a rule transforming a TEI tag into a HTML tag."""

    selector: RuleSelector
    tag: Union[str, None] = "div"
    text: Union[RuleText, None] = None
    attributes: list[
        Union[RuleAttributeCopy, RuleAttributeSet, RuleAttributeDelete]
    ] = []

    @validator("selector", pre=True)
    def convert_str_selector_to_dict(
        cls: "Rule", v: str | dict, values: dict, **kwargs: dict
    ) -> dict:
        """Convert a simple string selector into the dictionary representation."""
        if isinstance(v, str):
            return {"tag": v}
        return v


class TextSection(BaseModel):
    """Validation model for a TEI text section."""

    title: str
    type: Literal["text"] = "text"
    content: str
    mappings: list[Rule] = []


class SingleFieldRule(BaseModel):
    """Validation model for a TEI field rule."""

    title: str
    type: Literal["single"] = "single"
    content: str


class ListFieldRule(BaseModel):
    """Validation model for a TEI field rule."""

    title: str
    type: Literal["list"]
    content: str


class FieldsSection(BaseModel):
    """Validation model for a TEI fields section."""

    title: str
    type: Literal["fields"]
    fields: list[SingleFieldRule | ListFieldRule]


class TEIConfig(BaseModel):
    """Validation model for the TEI-specific settings."""

    text_only_in_leaf_nodes: bool = False
    mappings: list[Rule] = []
    sections: list[TextSection | FieldsSection] = []


class Config(BaseModel):
    """Configuration validation model."""

    tei: Optional[TEIConfig]


BASE_RULES = [
    {"selector": "tei:body", "tag": "section"},
    {"selector": "tei:head", "tag": "h1"},
    {"selector": "tei:p", "tag": "p"},
    {"selector": "tei:seg", "tag": "span"},
    {"selector": "tei:pb", "tag": "span"},
    {"selector": "tei:hi", "tag": "span"},
    {
        "selector": "tei:ref",
        "tag": "a",
        "attributes": [{"attr": "href", "source": "target"}],
    },
    {"selector": "tei:citedRange", "tag": "span"},
    {"selector": "tei:q", "tag": "span"},
    {"selector": "tei:hi", "tag": "span"},
    {"selector": "tei:foreign", "tag": "span"},
    {"selector": "tei:speaker", "tag": "span"},
    {"selector": "tei:stage", "tag": "span"},
    {"selector": "tei:lem", "tag": "span"},
    {"selector": "tei:sic", "tag": "span"},
]
"""Base mapping rules for mapping TEI tags to default HTML elements."""


def validate_config(app: Sphinx, config: Config) -> None:
    """Validate the configuration and add any default values."""
    if config.uEdition:
        if "tei" in config.uEdition:
            if "sections" in config.uEdition["tei"] and isinstance(
                config.uEdition["tei"]["sections"], list
            ):
                if "mappings" in config.uEdition["tei"] and isinstance(
                    config.uEdition["tei"]["mappings"], list
                ):
                    for section in config.uEdition["tei"]["sections"]:
                        if "mappings" in section and isinstance(
                            section["mappings"], list
                        ):
                            section["mappings"] = (
                                section["mappings"]
                                + config.uEdition["tei"]["mappings"]
                                + BASE_RULES
                            )
                        else:
                            section["mappings"] = (
                                config.uEdition["tei"]["mappings"] + BASE_RULES
                            )
        try:
            config.uEdition = Config(**config.uEdition).dict()
        except ValidationError as e:
            for error in e.errors():
                logger.error(" -> ".join([str(loc) for loc in error["loc"]]))
                logger.error(f'  {error["msg"]}')
            config.uEdition = {}
    else:
        config.uEdition = {}


def setup(app: Sphinx) -> None:
    """Set up the Sphinx configuration handling for the uEdition."""
    app.add_config_value("uEdition", default=None, rebuild="html", types=[dict])
    app.connect("config-inited", validate_config)
