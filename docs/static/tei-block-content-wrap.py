"""A script to wrap any block content."""

import argparse
import os
import sys

from lxml import etree
from yaml import safe_load

from uedition.ext.settings import TEISettings

# Set up the commandline argument parser
parser = argparse.ArgumentParser(description="Wrap any content in a TEI block element in an inline element.")
parser.add_argument("source")
parser.add_argument("target")
parser.add_argument("--insecure", action="store_true")
args = parser.parse_args()

# Abort if the source and target file are the same, unless the user has explicitly passed --insecure.
if args.source == args.target and not args.insecure:
    sys.stderr.write(
        "Directly overwriting the source is dangerous and not recommended. Pass --insecure to allow it to happen.\n"
    )
    sys.exit(1)

# The TEI tag to use for new text elements.
SEGMENT_TAG_NAME = "{http://www.tei-c.org/ns/1.0}seg"
# The list of TEI elements that are to be processed.
CONVERT_TAGS = [
    "{http://www.tei-c.org/ns/1.0}text",
]
NAMESPACES = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "uedition": "https://uedition.readthedocs.org",
}


# Load the configuration file
if not os.path.exists("uEdition.yml"):
    sys.stderr.write("You must run this script in the folder with the uEdition.yml.\n")
    sys.exit(1)
with open("uEdition.yml") as in_f:
    data = safe_load(in_f)
    if "sphinx_config" not in data and "tei" not in data["sphinx_config"]:
        sys.stderr.write("You must have configured TEI in the μEdition for this script to work.\n")
        sys.exit(1)
    blocks = TEISettings(**data["sphinx_config"]["tei"]).blocks


def process(node):
    """Process the `node` and wrap any text, if the `node` is a block-level node."""
    if len(node) > 0:
        for child in node:
            process(child)
    elif node.text is not None:
        for block in blocks:
            if len(node.xpath(f"self::{block.selector}", namespaces=NAMESPACES)) > 0:
                elem = etree.Element(SEGMENT_TAG_NAME)
                elem.text = node.text
                node.append(elem)
                node.text = None
    return node


# Load the source file
doc = etree.parse(args.source)  # noqa: S320

# Process the configured elements.
for child in doc.getroot():
    if child.tag in CONVERT_TAGS:
        process(child)

# Indent the converted document for readability.
etree.indent(doc.getroot(), space="  ")

# Write converted file back out.
with open(args.target, "w", encoding="utf-8") as out_f:
    out_f.write(etree.tostring(doc, encoding="unicode", pretty_print=True))
