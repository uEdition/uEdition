"""Builder for generating TEI XML outputs."""

import logging
import os
import xml.sax.saxutils
from collections.abc import Iterator

import sphinx
from docutils import nodes
from docutils.io import StringOutput
from sphinx.application import Sphinx
from sphinx.builders.xml import XMLBuilder
from sphinx.locale import __
from sphinx.util.osutil import ensuredir, os_path
from sphinx.writers.xml import XMLWriter

from uedition.ext.tei.parser import TeiElement

logger = logging.getLogger(__name__)

MAPPINGS = [
    {"cls": nodes.document, "tagname": "body", "type": "block"},
    {"cls": nodes.section, "tagname": "div", "type": "block"},
    {"cls": nodes.paragraph, "tagname": "p", "type": "block"},
    {"cls": nodes.title, "tagname": "head", "type": "block"},
    {"cls": nodes.bullet_list, "tagname": "list", "type": "block", "attrs": [{"target": "rend", "value": "bulleted"}]},
    {
        "cls": nodes.enumerated_list,
        "tagname": "list",
        "type": "block",
        "attrs": [{"target": "rend", "value": "numbered"}],
    },
    {"cls": nodes.list_item, "tagname": "item", "type": "block"},
    {
        "cls": nodes.literal_block,
        "tagname": "div",
        "type": "block",
        "attrs": [{"target": "type", "value": "literal-block"}, {"source": "language", "target": "subtype"}],
    },
    {"cls": nodes.compound, "tagname": "div", "type": "block"},
    {"cls": nodes.admonition, "tagname": "div", "type": "block"},
    {
        "cls": nodes.definition_list,
        "tagname": "list",
        "type": "block",
        "attrs": [{"target": "type", "value": "definition"}],
    },
    {"cls": nodes.definition_list_item, "tagname": "item", "type": "block"},
    {"cls": sphinx.addnodes.toctree},
    {
        "cls": nodes.footnote,
        "tagname": "note",
        "type": "block",
        "attrs": [
            {"target": "type", "value": "footnote"},
            {"target": "target", "source": "backrefs", "format": "#{value}", "join": " "},
        ],
    },
    {
        "cls": nodes.transition,
        "tagname": "div",
        "type": "empty",
        "attrs": [{"target": "rend", "value": "horizontal-line"}],
    },
    {"cls": nodes.inline, "tagname": "hi", "type": "inline"},
    {"cls": nodes.literal, "tagname": "hi", "type": "inline"},
    {"cls": nodes.strong, "tagname": "hi", "type": "inline", "attrs": [{"target": "rend", "value": "bold"}]},
    {"cls": nodes.emphasis, "tagname": "hi", "type": "inline", "attrs": [{"target": "rend", "value": "italic"}]},
    {"cls": nodes.label, "tagname": "label", "type": "inline"},
    {
        "cls": nodes.reference,
        "tagname": "ref",
        "type": "inline",
        "attrs": [{"source": "refuri", "target": "target"}],
    },
    {
        "cls": nodes.footnote_reference,
        "tagname": "ref",
        "type": "inline",
        "attrs": [{"source": "refid", "target": "target", "format": "#{value}"}],
    },
]


class TEITranslator(nodes.GenericNodeVisitor):
    """Translator for converting a Docutils document to TEI XML."""

    def __init__(self, document: nodes.document) -> None:
        """Initialise the translator."""
        nodes.NodeVisitor.__init__(self, document)

        # Reporter
        self.warn = self.document.reporter.warning
        self.error = self.document.reporter.error

        # Settings
        self.settings = settings = document.settings
        self.indent = self.newline = ""
        if settings.newlines:
            self.newline = "\n"
        if settings.indents:
            self.newline = "\n"
            self.indent = "  "
        self.level = 0
        self.inline_level = 0
        self.fixed_level = 0

        self.output = []
        if settings.xml_declaration:
            self.output.append(f'<?xml version="1.0" encoding="{settings.output_encoding}"?>\n')

    def rule_for_node(self, node: nodes.Element) -> dict:
        """Get the transformation rule for a node."""
        for rule in MAPPINGS:
            if isinstance(node, rule["cls"]):
                return rule
        if isinstance(node, TeiElement):
            tag = node.get("tei_tag")
            tag = tag[tag.find("}") + 1 :]
            attrs = []
            for key, value in node.get("tei_attributes").items():
                if key.startswith("data-tei-block-") or key.startswith("data-tei-mark-"):
                    continue
                elif key.startswith("data-tei-attribute-"):
                    attrs.append({"target": key[19:], "value": value})
            return {"tagname": tag, "type": "block", "attrs": attrs}
        self.warn(f"Unknown node {node.__class__.__module__}.{node.__class__.__qualname__} ({node.attlist()})")
        return {"tagname": "div", "type": "block"}

    def default_visit(self, node: nodes.Element) -> None:
        """Visit a generic node."""
        rule = self.rule_for_node(node)
        # Skip the node if it has no associated TEI "tagname"
        if "tagname" not in rule:
            raise nodes.SkipNode
        # Special handling for the root document, which needs the TEI structure wrapping
        if isinstance(node, nodes.document):
            self.output.append('<tei:TEI xmlns:tei="http://www.tei-c.org/ns/1.0">\n')
            self.output.append("  <tei:text>\n")
            self.level += 2
        self.output.append(self.indent * self.level)
        self.output.append(f"<tei:{rule['tagname']}")
        # Process the default "ids" and "classes" list
        output_attrs = {}
        for attr in node.attlist():
            if attr[0] == "ids":
                output_attrs["xml:id"] = attr[1][0]
                # self.output.append(f' xml:id={xml.sax.saxutils.quoteattr()}')
            elif attr[0] == "classes":
                if isinstance(attr[1], list):
                    output_attrs["rend"] = " ".join(attr[1])
                else:
                    output_attrs["rend"] = str(attr[1])
        # Process all configured attributes
        if "attrs" in rule:
            for attr_rule in rule["attrs"]:
                if "value" in attr_rule:
                    output_attrs[attr_rule["target"]] = attr_rule["value"]
                for attr in node.attlist():
                    if "source" in attr_rule and attr[0] == attr_rule["source"]:
                        output_attrs[attr_rule["target"]] = attr[1]
                if attr_rule["target"] in output_attrs and isinstance(output_attrs[attr_rule["target"]], list):
                    joiner = attr_rule["join"] if "join" in attr_rule else " "
                    if "format" in attr_rule:
                        output_attrs[attr_rule["target"]] = joiner.join(
                            [attr_rule["format"].replace("{value}", v) for v in output_attrs[attr_rule["target"]]]
                        )
                    else:
                        output_attrs[attr_rule["target"]] = joiner.join(output_attrs[attr_rule["target"]])
                elif "format" in attr_rule:
                    output_attrs[attr_rule["target"]] = attr_rule["format"].replace(
                        "{value}", output_attrs[attr_rule["target"]]
                    )
        # Write the sorted attributes
        sorted_output_attrs = list(output_attrs.items())
        sorted_output_attrs.sort()
        for name, value in sorted_output_attrs:
            self.output.append(f" {name}={xml.sax.saxutils.quoteattr(value)}")
        if rule["type"] == "empty":
            self.output.append("/>")
            self.output.append(self.newline)
            raise nodes.SkipNode
        else:
            self.output.append(">")
        # Update the indentation levels
        self.level += 1
        if isinstance(node, nodes.FixedTextElement):
            self.fixed_level += 1
        if rule["type"] == "inline":
            self.inline_level += 1
        elif rule["type"] == "block":
            self.output.append(self.newline)

    def default_departure(self, node: nodes.Element) -> None:
        """Depart a generic node."""
        rule = self.rule_for_node(node)
        self.level -= 1
        # Only indent if we are not inside an inline element
        if self.inline_level == 0:
            self.output.append(self.indent * self.level)
        self.output.append(f"</tei:{rule['tagname']}>")
        # Update the indentation levels
        if isinstance(node, nodes.FixedTextElement):
            self.fixed_level -= 1
        self.output.append(self.newline)
        if rule["type"] == "inline":
            self.inline_level -= 1
        if isinstance(node, nodes.document):
            self.output.append("  </tei:text>\n")
            self.output.append("</tei:TEI>")
            self.level -= 2

    # specific visit and depart methods
    # ---------------------------------

    def visit_Text(self, node: nodes.TextElement) -> None:  # noqa: N802
        """Output the Text node content."""
        text = xml.sax.saxutils.escape(node.astext())
        if self.inline_level > 0:
            if self.fixed_level > 0:
                self.output.append(text)
            else:
                self.output.append(text)
        else:
            self.output.append(f"{self.indent * self.level}<tei:span>{text}</tei:span>\n")

    def depart_Text(self, node: nodes.TextElement) -> None:  # noqa: N802
        """Unused."""
        pass

    def visit_raw(self, node: nodes.raw) -> None:
        """Visit a raw node."""
        if "tei" not in node.get("format", "").split():
            raise nodes.SkipNode
        xml_string = node.astext()
        self.output.append(xml_string)
        raise nodes.SkipNode


class TEIBuilder(XMLBuilder):
    """Builds TEI representations of the μEdition."""

    name = "tei"
    format = "tei"
    epilog = __("The TEI files are in %(outdir)s.")

    out_suffix = ".tei"
    allow_parallel = True

    _writer_class: type[XMLWriter] = XMLWriter
    writer: XMLWriter
    default_translator_class = TEITranslator

    def get_outdated_docs(self) -> Iterator[str]:
        """Determine the list of outdated documents."""
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = os.path.join(self.outdir, docname + self.out_suffix)
            try:
                targetmtime = os.path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = os.path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except OSError:
                # source doesn't exist anymore
                pass

    def get_target_uri(self, docname: str, typ: str | None = None) -> str:  # noqa: ARG002
        """Return the `docname` as the target_uri."""
        return docname

    def prepare_writing(self, docnames: set[str]) -> None:  # noqa: ARG002
        """Prepare for writing."""
        self.writer = self._writer_class(self)

    def write_doc(self, docname: str, doctree: nodes.Node) -> None:
        """Write a single document."""
        # work around multiple string % tuple issues in docutils;
        # replace tuples in attribute values with lists
        doctree = doctree.deepcopy()
        for domain in self.env.domains.values():
            xmlns = "xmlns:" + domain.name
            doctree[xmlns] = "https://www.sphinx-doc.org/"  # type: ignore
        for node in doctree.findall(nodes.Element):
            for att, value in node.attributes.items():
                if isinstance(value, tuple):
                    node.attributes[att] = list(value)
                value = node.attributes[att]  # noqa: PLW2901
                if isinstance(value, list):
                    for i, val in enumerate(value):
                        if isinstance(val, tuple):
                            value[i] = list(val)
        destination = StringOutput(encoding="utf-8")
        self.writer.write(doctree, destination)
        outfilename = os.path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(os.path.dirname(outfilename))
        try:
            with open(outfilename, "w", encoding="utf-8") as f:
                f.write(self.writer.output)
        except OSError as err:
            logger.warning(__("error writing file %s: %s"), outfilename, err)

    def finish(self) -> None:
        """Unused."""
        pass


def setup(app: Sphinx) -> None:
    """Set up the TEI Sphinx extension."""
    app.add_builder(TEIBuilder)
