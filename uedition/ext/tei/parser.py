# noqa: A005
# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""TEI parsing extension for Sphinx."""

import re
from typing import Callable

from docutils import nodes
from lxml import etree
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.parsers import Parser as SphinxParser
from sphinx.util import logging
from sphinx.writers.html import HTMLWriter

logger = logging.getLogger(__name__)
namespaces = {"tei": "http://www.tei-c.org/ns/1.0", "uedition": "https://uedition.readthedocs.org"}


def format_iso8601_date(dummy: None, text: str) -> str:  # noqa: ARG001
    """Format a date."""
    if isinstance(text, str):
        match = re.search("([0-9]{4})-?([0-9]{2})?-?([0-9]{2})?", text)
        if match:
            return ".".join(reversed([v for v in match.groups() if v is not None]))
    return ""


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


class TEIParser(SphinxParser):
    """Sphinx parser for Text Encoding Initiative XML."""

    supported: tuple[str, ...] = ("tei",)
    """Specify that only .tei files are parsed"""

    def parse(self: "TEIParser", inputstring: str, document: nodes.document) -> None:
        """
        Parse source TEI text.

        This function creates the basic structure and then the :func:`~uEdition.extensions.tei.TEIParser._walk_tree`
        function is used to actually process the XML.

        :param inputstring: The TEI XML string to parse
        :type inputstring: str
        :param document: The root docutils node to add AST elements to
        :type document: :class:`~docutils.nodes.document`
        """
        functions = etree.FunctionNamespace("https://uedition.readthedocs.org")
        functions["format_iso8601_date"] = format_iso8601_date
        root = etree.fromstring(inputstring.encode("UTF-8"))  # noqa: S320
        title = root.xpath(
            "string(/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title)",
            namespaces=namespaces,
        )
        doc_section = nodes.section(ids=["document"])
        doc_title = nodes.title()
        doc_title.append(nodes.Text(title if title else "[Untitled]"))
        doc_section.append(doc_title)
        for conf_section in self.config.tei["sections"]:
            section = nodes.section(ids=[nodes.make_id(conf_section["name"])])
            if conf_section["title"]:
                section_title = nodes.title()
                section_title.append(nodes.Text(conf_section["title"]))
                section.append(section_title)
            if conf_section["type"] == "text":
                # Process a text section
                sources = root.xpath(conf_section["selector"], namespaces=namespaces)
                if len(sources) > 0:
                    doc_section.append(section)
                    tmp = nodes.section()
                    for source in sources:
                        for child in source:
                            self._walk_tree(child, tmp)
                    self._wrap_sections(section, tmp)
            elif conf_section["type"] == "textlist":
                # Process a text section
                sources = root.xpath(conf_section["selector"], namespaces=namespaces)
                if len(sources) > 0:
                    if conf_section["sort"]:
                        source.sort(key=self._sort_key(conf_section["sort"]))
                    doc_section.append(section)
                    for source in sources:
                        tmp = None
                        if "id" in source.attrib:
                            tmp = nodes.section(ids=[source.attrib["id"]])
                        elif "{http://www.w3.org/XML/1998/namespace}id" in source.attrib:
                            tmp = nodes.section(ids=[source.attrib["{http://www.w3.org/XML/1998/namespace}id"]])
                        if tmp is not None and len(source) > 0:
                            for child in source:
                                self._walk_tree(child, tmp)
                            section.append(tmp)
                    # self._wrap_sections(section, tmp)
            elif conf_section["type"] == "metadata":
                # Process a field or metadata section
                sources = root.xpath(conf_section["selector"], namespaces=namespaces)
                if len(sources) > 0:
                    doc_section.append(section)
                    fields = nodes.definition_list()
                    section.append(fields)
                    for field in conf_section["fields"]:
                        if field["type"] == "single":
                            self._parse_single_field(fields, field, sources[0])
                        elif field["type"] == "list":
                            self._parse_list_field(fields, field, sources[0])
                        elif field["type"] == "download":
                            self._parse_download_field(fields, field, sources[0])
        document.append(doc_section)

    def _sort_key(self: "TEIParser", xpath: str) -> Callable[[etree.Element], tuple[tuple[int, ...], ...]]:
        """Create a sortkey that understands about `page,line` patterns for sorting."""

        def sorter(node: etree.Element) -> tuple[tuple[int, ...], ...]:
            value = node.xpath(xpath, namespaces=namespaces)
            if value is not None and len(value) > 0:
                if isinstance(value, list):
                    value = value[0]
                else:
                    value = str(value)
                match = re.match("[0-9-,]+", value)
                if match is not None:
                    order = []
                    for part in value.split("-"):
                        tpl = tuple([int(v) for v in part.split(",")])
                        if len(order) > 0 and len(order[-1]) > len(tpl):
                            order.append(tuple(list(order[-1][: -len(tpl)]) + list(tpl)))
                        else:
                            order.append(tpl)
                    return tuple(order)
            return ((0,),)

        return sorter

    def _walk_tree(self: "TEIParser", node: etree.Element, parent: nodes.Element) -> None:
        """Walk the XML tree and create the appropriate AST nodes."""
        for conf in self.config.tei["blocks"]:
            if len(node.xpath(f"self::{conf['selector']}", namespaces=namespaces)) > 0:
                attrs = self._parse_attributes(node, conf["attributes"])
                attrs.update({f"data-tei-block-{conf['name']}": ""})
                element = TeiElement(
                    html_tag=conf["tag"] if conf["tag"] else "div", tei_tag=node.tag, tei_attributes=attrs
                )
                for child in node:
                    self._walk_tree(child, element)
                parent.append(element)
                return
        for conf in self.config.tei["marks"]:
            if len(node.xpath(f"self::{conf['selector']}", namespaces=namespaces)) > 0:
                attrs = self._parse_attributes(node, conf["attributes"])
                attrs.update({f"data-tei-mark-{conf['name']}": ""})
                element = TeiElement(
                    html_tag=conf["tag"] if conf["tag"] else "span", tei_tag=node.tag, tei_attributes=attrs
                )
                if len(node) == 0:
                    if conf["text"]:
                        for match in node.xpath(conf["text"], namespaces=namespaces):
                            element.append(nodes.Text(match))
                    elif node.text:
                        element.append(nodes.Text(node.text))
                else:
                    for child in node:
                        self._walk_tree(child, element)
                parent.append(element)
                return
        if len(node) == 0:
            parent.append(nodes.Text(node.text))
        else:
            logger.warning(f"No block or mark configured for {node.tag} ({node.attrib})")

    def _parse_attributes(self, node: etree.Element, attribute_configs: list) -> dict:
        attrs = {}
        for conf in attribute_configs:
            if conf["name"] in node.attrib:
                if conf["type"] == "id-ref" and node.attrib[conf["name"]].startswith("#"):
                    attrs[f"data-tei-attribute-{conf['name']}"] = node.attrib[conf["name"]][1:]
                elif conf["type"] == "static":
                    attrs[f"data-tei-attribute-{conf['name']}"] = conf["value"]
                elif conf["type"] == "html-attribute":
                    attrs[conf["target"]] = node.attrib[conf["name"]]
                else:
                    attrs[f"data-tei-attribute-{conf['name']}"] = node.attrib[conf["name"]]
            elif conf["default"]:
                attrs[f"data-tei-attribute-{conf['name']}"] = conf["default"]
        return attrs

    def _wrap_sections(self: "TEIParser", section: nodes.Element, tmp: nodes.Element) -> None:
        """Ensure that sections are correctly wrapped."""
        section_stack = [(0, section)]
        for node in tmp.children:
            if isinstance(node, TeiElement) and node.attributes["html_tag"] in [
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
            ]:
                section_level = int(node.attributes["html_tag"][1])
                while section_level <= section_stack[-1][0]:
                    section_stack.pop()
                new_section = nodes.section(ids=[nodes.make_id(node.astext())])
                title = nodes.title(attributes={"data-test": ""})
                title.children = node.children
                new_section.append(title)
                section_stack[-1][1].append(new_section)
                section_stack.append((section_level, new_section))
            elif isinstance(node, nodes.section):
                pass
            else:
                # Need to check that the
                in_heading = False
                tmp = node
                while tmp.parent is not None and isinstance(tmp.parent, TeiElement):
                    if tmp.parent.attributes["html_tag"] in [
                        "h1",
                        "h2",
                        "h3",
                        "h4",
                        "h5",
                        "h6",
                    ]:
                        in_heading = True
                        break
                    tmp = tmp.parent
                if not in_heading:
                    section_stack[-1][1].append(node)

    def _parse_single_field(self: "TEIParser", parent: etree.Element, field: dict, root: etree.Element) -> None:
        """Parse a single metadata field."""
        content = root.xpath(field["selector"], namespaces=namespaces)
        if len(content) > 0:
            if isinstance(content, list):
                content = content[0]
            li = nodes.definition_list_item()
            dt = nodes.term()
            dt.append(nodes.Text(field["title"]))
            li.append(dt)
            dd = nodes.definition()
            dd.append(nodes.Text(content))
            li.append(dd)
            parent.append(li)

    def _parse_list_field(self: "TEIParser", parent: etree.Element, field: dict, root: etree.Element) -> None:
        """Parse a list of metadata fields."""
        content = root.xpath(field["selector"], namespaces=namespaces)
        if len(content) > 0:
            li = nodes.definition_list_item()
            dt = nodes.term()
            dt.append(nodes.Text(field["title"]))
            li.append(dt)
            dd = nodes.definition()
            values = nodes.enumerated_list()
            for value in content:
                item = nodes.list_item()
                item.append(nodes.Text(value))
                values.append(item)
            dd.append(values)
            li.append(dd)
            parent.append(li)

    def _parse_download_field(self: "TEIParser", parent: etree.Element, field: dict, root: etree.Element) -> None:
        """Parse a download metadata field."""
        content = root.xpath(field["selector"], namespaces=namespaces)
        target = root.xpath(field["target"], namespaces=namespaces)
        if len(content) > 0 and len(target) > 0:
            if isinstance(content, list):
                content = content[0]
            if isinstance(target, list):
                target = target[0]
            if content.strip() and target.strip():
                li = nodes.definition_list_item()
                dt = nodes.term()
                dt.append(nodes.Text(field["title"]))
                li.append(dt)
                dd = nodes.definition()
                dd.append(addnodes.download_reference(content, content, reftarget=target))
                li.append(dd)
                parent.append(li)


def setup(app: Sphinx) -> None:
    """Set up the TEI Sphinx extension."""
    app.add_node(TeiElement, html=(tei_element_html_enter, tei_element_html_exit))
    app.add_source_suffix(".tei", "tei")
    app.add_source_parser(TEIParser)
