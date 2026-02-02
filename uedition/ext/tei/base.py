"""Base TEI extensions."""

import re

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html import HTMLWriter


class TeiElement(nodes.Element):
    """An abstract TEI element for HTML rendering."""

    pass


def tei_element_html_enter(self: "HTMLWriter", node: TeiElement) -> None:
    """Visit a TeiElement and generate the correct HTML."""
    if node.get("html_tag") is not None:
        buffer = [f"<{node.get('html_tag')}"]
        if node.get("ids"):
            buffer.append(f' id="{node.get("ids")[0]}"')
        for key, value in node.get("tei_attributes").items():
            buffer.append(f' {key}="{value}"')
        self.body.append(f"{''.join(buffer)}>")


def tei_element_html_exit(self: "HTMLWriter", node: TeiElement) -> None:
    """Close the HTML tag."""
    if node.get("html_tag") is not None:
        self.body.append(f"</{node.get('html_tag')}>")


STATE_INIT = 0
STATE_TAG_NAME = 1
STATE_IN_TAG = 2
STATE_TAG_ATTRIBUTE_NAME = 3
STATE_TAG_IN_ATTRIBUTE = 4
STATE_TAG_ATTRIBUTE_VALUE = 5


def parse_tei_tag_definition(text: str) -> list[dict]:
    """Parse a TEI tag definition string into tag and attributes."""
    tags = []
    buffer = []
    tag = {}
    attribute_name = ""
    state = STATE_INIT
    for char in text:
        if state == STATE_INIT and char == "<":
            state = STATE_TAG_NAME
            buffer = []
            tag = {}
        elif state == STATE_TAG_NAME:
            if char == " ":
                if len(buffer) > 0:
                    state = STATE_IN_TAG
                    tag["name"] = "".join(buffer)
                    tag["attributes"] = {}
                else:
                    state = STATE_INIT
            elif char == ">":
                if len(buffer) > 0:
                    tag["name"] = "".join(buffer)
                    tags.append(tag)
                state = STATE_INIT
            else:
                buffer.append(char)
        elif state == STATE_IN_TAG:
            if char == ">":
                state = STATE_INIT
                if "name" in tag:
                    tags.append(tag)
            elif char != " ":
                state = STATE_TAG_ATTRIBUTE_NAME
                buffer = [char]
                attribute_name = ""
        elif state == STATE_TAG_ATTRIBUTE_NAME:
            if char == "=":
                if len(buffer) > 0:
                    state = STATE_TAG_IN_ATTRIBUTE
                    attribute_name = "".join(buffer)
                else:
                    state = STATE_INIT
            elif char not in [" ", '"']:
                buffer.append(char)
            else:
                state = STATE_INIT
        elif state == STATE_TAG_IN_ATTRIBUTE and char == '"':
            state = STATE_TAG_ATTRIBUTE_VALUE
            buffer = []
        elif state == STATE_TAG_ATTRIBUTE_VALUE:
            if char == '"':
                if attribute_name != "":
                    tag["attributes"][attribute_name] = "".join(buffer)
                state = STATE_IN_TAG
            else:
                buffer.append(char)
    return tags


def tei_role(
    name: str,  # noqa: ARG001
    rawtext: str,  # noqa: ARG001
    text: str,
    lineno: int,  # noqa: ARG001
    inliner: str,  # noqa: ARG001
    options: dict = {},  # noqa: ARG001, B006
    content: list = [],  # noqa: ARG001, B006
) -> tuple:
    """Role to add a comment."""
    match = re.match(r"(<.+>)?(.*)", text)
    result = []
    if match.group(1) is not None:
        tags = parse_tei_tag_definition(match.group(1))
        if len(tags) > 0:
            parent = result
            for tag in tags:
                html_attrs = {f"data-tei-mark-{tag['name']}": ""}
                if "attributes" in tag:
                    for key, value in tag["attributes"].items():
                        html_attrs[f"data-tei-attribute-{key}"] = value
                tei_node = TeiElement(html_tag="span", tei_tag=tag["name"], tei_attributes=html_attrs)
                parent.append(tei_node)
                parent = tei_node
            parent.append(nodes.Text(match.group(2)))
    else:
        tei_node = TeiElement(html_tag="span", tei_tag="span", tei_attributes={"data-tei-mark-span": ""})
        tei_node.append(nodes.Text(match.group(2)))
        result = [tei_node]
    return result, []


def parse_tei_attribute_definition(text: str) -> dict:
    """Parse a TEI attribute definition string into attributes."""
    buffer = []
    attributes = {}
    attribute_name = ""
    state = STATE_INIT
    for char in text:
        if state == STATE_INIT and char != " ":
            state = STATE_TAG_ATTRIBUTE_NAME
            buffer = [char]
            attribute_name = ""
        elif state == STATE_TAG_ATTRIBUTE_NAME:
            if char == "=":
                if len(buffer) > 0:
                    state = STATE_TAG_IN_ATTRIBUTE
                    attribute_name = "".join(buffer)
                else:
                    state = STATE_INIT
            elif char not in [" ", '"']:
                buffer.append(char)
            else:
                state = STATE_INIT
        elif state == STATE_TAG_IN_ATTRIBUTE and char == '"':
            state = STATE_TAG_ATTRIBUTE_VALUE
            buffer = []
        elif state == STATE_TAG_ATTRIBUTE_VALUE:
            if char == '"':
                if attribute_name != "":
                    attributes[attribute_name] = "".join(buffer)
                state = STATE_INIT
            else:
                buffer.append(char)
    return attributes


class TeiDirective(SphinxDirective):
    """The TeiDirective directive is used to generate TEI blocks for more complex markup."""

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    option_spec = {"attributes": directives.unchanged}  # noqa:RUF012
    final_argument_whitespace = True

    def run(self):
        """Create the AST for the directive."""
        html_attrs = {f"data-tei-block-{self.arguments[0]}": ""}
        if "attributes" in self.options:
            for key, value in parse_tei_attribute_definition(self.options["attributes"]).items():
                html_attrs[f"data-tei-attribute-{key}"] = value
        node = TeiElement(html_tag="div", tei_tag=self.arguments[0], tei_attributes=html_attrs)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app: Sphinx) -> None:
    """Set up the TEI Sphinx extension."""
    app.add_node(TeiElement, html=(tei_element_html_enter, tei_element_html_exit))
    app.add_role("tei", tei_role)
    app.add_directive("tei", TeiDirective)
