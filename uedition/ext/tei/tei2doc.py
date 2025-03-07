"""Parse a TEI document into a list of text nodes."""

from lxml import etree

from uedition.ext.settings import TEINodeAttribute, TEISettings

namespaces = {"tei": "http://www.tei-c.org/ns/1.0", "uedition": "https://uedition.readthedocs.org"}


def parse_metadata_node(node: etree.Element) -> dict:
    """Parse a single metadata node."""
    name = node.tag
    for prefix, uri in namespaces.items():
        name = name.replace(f"{{{uri}}}", f"{prefix}:")
    result = {"type": name, "text": "", "attrs": [], "content": []}
    if node.text and len(node.text.strip()) > 0:
        result["text"] = node.text
    for key, value in node.attrib.items():
        for prefix, uri in namespaces.items():
            key = key.replace(f"{{{uri}}}", f"{prefix}:")  # noqa: PLW2901
        attr_result = {"type": key, "value": value}
        result["attrs"].append(attr_result)

    for child in node:
        result["content"].append(parse_metadata_node(child))
    return result


def parse_tei_attributes(attributes: etree._Attrib, settings: list[TEINodeAttribute]) -> list[dict]:
    """Parse the attributes of a node, extracting the attribute settings."""
    result = {}
    for conf in settings:
        if conf.name in attributes:
            if conf.type == "id-ref" and attributes[conf.name].startswith("#"):
                result[conf.name] = attributes[conf.name][1:]
            else:
                result[conf.name] = attributes[conf.name]
        else:
            result[conf.name] = conf.default
    return result


def parse_tei_subtree(node: etree.Element, settings: TEISettings) -> dict:
    """Recursively parse a TEI subtree to create a Prosemirror document structure."""
    for conf in settings.blocks:
        if len(node.xpath(f"self::{conf.selector}", namespaces=namespaces)) > 0:
            return {
                "type": conf.name,
                "attrs": parse_tei_attributes(node.attrib, conf.attributes),
                "content": [parse_tei_subtree(child, settings) for child in node],
            }
    for conf in settings.marks:
        if len(node.xpath(f"self::{conf.selector}", namespaces=namespaces)) > 0:
            if len(node) > 0:
                child = parse_tei_subtree(node[0], settings)
                text = child["text"]
                if conf.text is not None:
                    if conf.text.startswith("@") and conf.text[1:] in node.attrib:
                        text = node.attrib[conf.text[1:]]
                return {
                    "type": "text",
                    "marks": child["marks"]
                    + [
                        {
                            "type": conf.name,
                            "attrs": parse_tei_attributes(node.attrib, conf.attributes),
                        }
                    ],
                    "text": text,
                }
            else:
                text = node.text
                if conf.text is not None:
                    if conf.text.startswith("@") and conf.text[1:] in node.attrib:
                        text = node.attrib[conf.text[1:]]
                return {
                    "type": "text",
                    "marks": [
                        {
                            "type": conf.name,
                            "attrs": parse_tei_attributes(node.attrib, conf.attributes),
                        }
                    ],
                    "text": text,
                }
    if len(node) == 0:
        return {"type": "text", "marks": [], "text": node.text}
    msg = f"Unknown node type {node.tag}{node.attrib}"
    raise Exception(msg)


def parse_tei_subdoc(node: etree.Element, settings: TEISettings) -> dict:
    """Parse part of the TEI document into a subdoc."""
    return {
        "type": "doc",
        "content": [parse_tei_subtree(child, settings) for child in node],
    }


def clean_tei_subdoc(node: dict) -> dict:
    """Remove empty attributes and marks."""
    if "attrs" in node and len(node["attrs"]) == 0:
        del node["attrs"]
    if "marks" in node and len(node["marks"]) == 0:
        del node["marks"]
    if "content" in node and len(node["content"]) == 0:
        del node["content"]
    if "marks" in node:
        for mark in node["marks"]:
            clean_tei_subdoc(mark)
    if "content" in node:
        for child in node["content"]:
            clean_tei_subdoc(child)
    return node


def parse_tei_file(doc: etree.ElementTree, settings) -> list[dict]:
    """Parse a TEI file into its constituent parts."""
    result = []
    for section in settings.tei.sections:
        section_root = doc.xpath(section.selector, namespaces=namespaces)
        if len(section_root) == 0:
            if section.type == "metadata":
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": [],
                    }
                )
            elif section.type == "text":
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": {},
                    }
                )
            elif section.type == "textlist":
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": [],
                    }
                )
        else:  # noqa: PLR5501
            if section.type == "metadata":
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": [parse_metadata_node(node) for node in section_root[0]],
                    }
                )
            elif section.type == "text":
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": clean_tei_subdoc(parse_tei_subdoc(section_root[0], settings.tei)),
                    }
                )
            elif section.type == "textlist":
                content = []
                for node in section_root:
                    content.append(
                        {
                            "attrs": {"id": node.attrib["{http://www.w3.org/XML/1998/namespace}id"]},
                            "content": clean_tei_subdoc(parse_tei_subdoc(node, settings.tei)),
                        }
                    )
                result.append(
                    {
                        "name": section.name,
                        "title": section.title,
                        "type": section.type,
                        "content": content,
                    }
                )
    return result
