from docutils import nodes
from docutils.parsers.rst import Parser as RstParser
from lxml import etree
from sphinx.application import Sphinx
from sphinx.parsers import Parser as SphinxParser
from sphinx.util import logging
from sphinx_design.shared import create_component


namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}


class TeiElement(nodes.Element): pass


def tei_element_html_enter(self, node: TeiElement) -> None:
    buffer = [f'<{node.get("html_tag")} data-tei-tag="{node.get("tei_tag")[29:]}"']
    if node.get('ids'):
        buffer.append(f' id="{node.get("ids")[0]}"')
    for key, value in node.get('tei_attributes').items():
        buffer.append(f' {key}="{value}"')
    self.body.append(f'{"".join(buffer)}>')


def tei_element_html_exit(self, node: TeiElement) -> None:
    self.body.append(f'</{node.get("html_tag")}>')


class TEIParser(SphinxParser):
    """Sphinx parser for Text Encoding Initiative XML."""

    supported: tuple[str, ...] = ('tei',)
    """Specify that only .tei files are parsed"""

    def parse(self: 'TEIParser', inputstring: str, document: nodes.document) -> None:
        """Parse source TEI text.

        This function creates the basic structure and then the :func:`~uEdition.extensions.tei.TEIParser._walk_tree`
        function is used to actually process the XML.

        :param inputstring: The TEI XML string to parse
        :type inputstring: str
        :param document: The root docutils node to add AST elements to
        :type document: :class:`~docutils.nodes.document`
        """
        root = etree.fromstring(inputstring.encode('UTF-8'))
        title = root.xpath('string(/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title)', namespaces=namespaces)
        doc_section = nodes.section(ids=['document'])
        doc_title = nodes.title()
        doc_title.append(nodes.Text(title if title else '[Untitled]'))
        doc_section.append(doc_title)
        tab_set = create_component('tab-set', classes=['sd-tab-set'])
        if 'tei' in self.config.uEdition and 'sections' in self.config.uEdition['tei']:
            for section in self.config.uEdition['tei']['sections']:
                if section['type'] == 'text':
                    source = root.xpath(section['content'], namespaces=namespaces)
                    if len(source) > 0:
                        tab_item = create_component('tab-item', classes=['sd-tab-item'])
                        tab_label = nodes.rubric(section['title'], nodes.Text(section['title']), classes=['sd-tab-label'])
                        tab_item.append(tab_label)
                        tab_content = create_component('tab-content', classes=['sd-tab-content', 'tei', nodes.make_id(section['title'])])
                        tab_item.append(tab_content)
                        for child in source:
                            self._walk_tree(child, tab_content, section['mappings'])
                        tab_set.append(tab_item)
                elif section['type'] == 'fields':
                    tab_item = create_component('tab-item', classes=['sd-tab-item'])
                    tab_label = nodes.rubric(section['title'], nodes.Text(section['title']), classes=['sd-tab-label'])
                    tab_item.append(tab_label)
                    tab_content = create_component('tab-content', classes=['sd-tab-content', 'tei', nodes.make_id(section['title'])])
                    tab_item.append(tab_content)
                    fields = nodes.definition_list()
                    tab_content.append(fields)
                    for field in section['fields']:
                        if field['type'] == 'single':
                            self._parse_single_field(fields, field, root)
                        elif field['type'] == 'list':
                            self._parse_list_field(fields, field, root)
                    tab_set.append(tab_item)
        doc_section.append(tab_set)
        document.append(doc_section)

    def _walk_tree(self: 'TEIParser', node: etree.Element, parent: nodes.Element, rules) -> None:
        """Walk the XML tree and create the appropriate AST nodes.

        Uses the mapping rules defined in :mod:`~uEdition.extensions.config` to determine what to
        map the XML to.
        """
        is_leaf = len(node) == 0
        text_only_in_leaf_nodes = self.config.uEdition['tei']['text_only_in_leaf_nodes'] \
            if 'tei' in self.config.uEdition else False
        attributes = {}
        # Get the first matching rule for the current node
        rule = self._rule_for_node(node, rules)
        # Loop over the XML node attributes and apply any attribute transforms defined in the matching rule
        for key, value in node.attrib.items():
            # Always strip the namespace from the `id` attribute
            if key == '{http://www.w3.org/XML/1998/namespace}id':
                key = 'id'
            if rule and 'attributes' in rule:
                processed = False
                for attr_rule in rule['attributes']:
                    if attr_rule['action'] == 'copy':
                        if key == attr_rule['source']:
                            # Copied attributes are added without a `data-` prefix
                            attributes[attr_rule['attr']] = value
                    elif attr_rule['action'] == 'delete':
                        if key == attr_rule['attr']:
                            processed = True
                    elif attr_rule['action'] == 'set':
                        if key == attr_rule['attr']:
                            value = attr_rule['value']
                # if the attribute did not match any attribute transform
                if not processed:
                    # The id attribute is always output as is, all other attributes are prefixed with `data-`
                    if key == 'id':
                        attributes['id'] = value
                    else:
                        attributes[f'data-{key}'] = value
            else:
                # The id attribute is always output as is, all other attributes are prefixed with `data-`
                if key == 'id':
                    attributes['id'] = value
                else:
                    attributes[f'data-{key}'] = value
        # Create the docutils AST element
        new_element = TeiElement(
            html_tag=rule['tag'] if rule is not None and 'tag' in rule else 'div',
            tei_tag=node.tag,
            tei_attributes=attributes,
        )
        parent.append(new_element)
        if rule is not None and 'text' in rule and rule['text']:
            # If there is a `text` key in the rule, use that to set the text
            if rule['text']['action'] == 'from-attribute' and rule['text']['attr'] in node.attrib:
                new_element.append(nodes.Text(node.attrib[rule['text']['attr']]))
        else:
            if node.text and (is_leaf or not text_only_in_leaf_nodes):
                # Only create text content if there is text and we either are in a leaf node or are adding all text
                new_element.append(nodes.Text(node.text))
        # Process any children
        for child in node:
            self._walk_tree(child, new_element, rules)
        # If there is text after this XML node and we are adding all text, then add text content to the parent
        if node.tail and not text_only_in_leaf_nodes:
            parent.append(nodes.Text(node.tail))

    def _rule_for_node(self: 'TEIParser', node: etree.Element, rules: list[dict]) -> dict:
        """Determine the first matching mapping rule for the node from the configured rules."""
        tei_tag = node.tag
        for rule in rules:
            if rule['selector']['tag'] == tei_tag:
                if 'attributes' in rule['selector']:
                    attr_match = True
                    for attr_rule in rule['selector']['attributes']:
                        if attr_rule['attr'] not in node.attrib or \
                                node.attrib[attr_rule['attr']] != attr_rule['value']:
                            attr_match = False
                            break
                    if not attr_match:
                        continue
                return rule
        return None

    def _parse_single_field(self: 'TEIParser', parent: etree.Element, field: dict, root: etree.Element) -> None:
        content = root.xpath(field['content'], namespaces=namespaces)
        if len(content) > 0:
            content = content[0]
            li = nodes.definition_list_item()
            dt = nodes.term()
            dt.append(nodes.Text(field['title']))
            li.append(dt)
            dd = nodes.definition()
            dd.append(nodes.Text(content))
            li.append(dd)
            parent.append(li)

    def _parse_list_field(self: 'TEIParser', parent: etree.Element, field: dict, root: etree.Element) -> None:
        content = root.xpath(field['content'], namespaces=namespaces)
        if len(content) > 0:
            li = nodes.definition_list_item()
            dt = nodes.term()
            dt.append(nodes.Text(field['title']))
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



def setup(app: Sphinx) -> None:
    """Setup the TEI Sphinx extension."""
    app.add_node(TeiElement, html=(tei_element_html_enter, tei_element_html_exit))
    app.add_source_suffix('.tei', 'tei')
    app.add_source_parser(TEIParser)
