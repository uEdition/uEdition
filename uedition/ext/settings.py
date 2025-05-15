# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Additional settings validation."""

from typing import Literal

from pydantic import BaseModel


class ValueTitlePair(BaseModel):
    """A simple pair of value and title."""

    value: str
    """The value for the pair."""
    title: str
    """The title to show for the pair."""


class TEINodeAttribute(BaseModel):
    """Single attribute for a TEINode."""

    name: str
    """The name of the attribute."""
    value: str | None = None
    """A fixed value to use for the attribute."""
    type: Literal["string"] | Literal["static"] | Literal["id-ref"] | Literal["text"] | Literal["html-attribute"] = (
        "string"
    )
    """The type of attribute this is."""
    default: str = ""
    """The default value to use if none is set."""
    target: str | None = None
    """The target HTML attribute."""


class TEINode(BaseModel):
    """A single node in a TEI document."""

    name: str
    """The name to use to address this node."""
    selector: str
    """The selector to identify this node."""
    attributes: list[TEINodeAttribute] = []
    """A list of attributes that are used on this node."""
    tag: str | None = None
    """The HTML tag to use to render the node."""
    text: str | None = None
    """Where to get the text from."""
    content: str | None = None
    """Allowed child nodes. Only relevant for block nodes."""


class TEIMetadataSectionSingleFieldRule(BaseModel):
    """Validation model for a TEI field rule with a single value."""

    title: str
    type: Literal["single"] = "single"
    selector: str


class TEIMetadataSectionListFieldRule(BaseModel):
    """Validation model for a TEI field rule with a list of values."""

    title: str
    type: Literal["list"]
    selector: str


class TEIMetadataSectionDownloadFieldRule(BaseModel):
    """Validation model for a TEI field rule that creates a download link."""

    title: str
    type: Literal["download"]
    selector: str
    target: str


class TEIMetadataSection(BaseModel):
    """A metadata section in the TEI document."""

    name: str
    """The name of the section."""
    title: str | None = None
    """The title to show in the UI."""
    type: Literal["metadata"]
    """The type must be set to metadata."""
    selector: str
    """The XPath selector to retrieve this section."""
    fields: list[
        TEIMetadataSectionSingleFieldRule | TEIMetadataSectionListFieldRule | TEIMetadataSectionDownloadFieldRule
    ]
    """Fields to display."""


class TEITextSection(BaseModel):
    """A section in the TEI document containing a single text."""

    name: str
    """The name of the section."""
    title: str | None = None
    """The title to show in the UI."""
    type: Literal["text"]
    """The type must be set to text."""
    selector: str
    """The XPath selector to retrieve this section."""


class TEITextListSection(BaseModel):
    """A section in the TEI document containing multiple texts."""

    name: str
    """The name of the section."""
    title: str | None = None
    """The title to show in the UI."""
    type: Literal["textlist"]
    """The type must be set to textlist."""
    selector: str
    """The XPath selector to retrieve the texts in this section."""
    sort: str | None = None


class TEISettings(BaseModel):
    """Settings for the TEI processing."""

    blocks: list[TEINode] = []
    """List of blocks supported in the TEI document."""
    marks: list[TEINode] = []
    """List of inline marks supported in the TEI document."""
    sections: list[TEIMetadataSection | TEITextSection | TEITextListSection] = []
    """List of sections within the TEI document."""
