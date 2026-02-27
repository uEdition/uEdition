"""A script to convert mixed-content XML to single-content XML."""

import argparse
import sys

from lxml import etree

# Set up the commandline argument parser
parser = argparse.ArgumentParser(description="Convert mixed-content XML into single-content XML")
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


def convert(node):
    """Convert the `node` and its children into single-mode XML."""
    # We only need to convert nodes that have children (and thus potential mixed-content).
    if len(node) > 0:
        # Make a copy of the children and then clear the node's list of children.
        children = list(node)
        for child in node:
            node.remove(child)
        # If the node has text that is not just whitespace, then this is moved into a new element.
        if node.text is not None and node.text.strip() != "":
            elem = etree.Element(SEGMENT_TAG_NAME)
            elem.text = node.text
            node.append(elem)
            node.text = None
        # If the node only has whitespace text, then simply remove the text.
        elif node.text is not None:
            node.text = None
        # Process each of the node's original children.
        for child in children:
            # Recursively convert the child and add the converted child to the current node.
            node.append(convert(child))
            # If the child has text after it (a tail) and it is not just whitespace, then this is moved
            # into a new element.
            if child.tail is not None and child.tail.strip() != "":
                elem = etree.Element(SEGMENT_TAG_NAME)
                elem.text = child.tail
                node.append(elem)
                child.tail = None
            # If the child has text after it and it is just whitespace, then simply remove that text.
            elif child.tail is not None:
                child.tail = None
    return node


# Load the source file
doc = etree.parse(args.source)  # noqa: S320

# Process the configured elements.
for child in doc.getroot():
    if child.tag in CONVERT_TAGS:
        convert(child)

# Indent the converted document for readability.
etree.indent(doc.getroot(), space="  ")

# Write converted file back out.
with open(args.target, "w", encoding="utf-8") as out_f:
    out_f.write(etree.tostring(doc, encoding="unicode", pretty_print=True))
