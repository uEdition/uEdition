# Working with TEI

In addition to working with Markdown, the μEdition also supports using [TEI XML](https://tei-c.org) for authoring content.
Unlike Markdown, which works straight out of the box, to use the TEI functionality, you need to provide some configuration.
There are also some (small) limitations on the XML structures that the μEdition supports.

## Configuration

THE μEdition's TEI parser extension is loaded by default, but you need to add some configuration settings to the
`sphinx_config.tei` section in the {file}`uEdition.yml` file:

:::{code-block} yaml
sphinx_config:
  tei:
    blocks:
     - # TEI block markup
    marks:
     - # TEI inline markup
    sections:
     - # TEI sections to show
:::

The TEI configuration consists of three sub-sections:

* {doc}`Sections <sections>` configures which sections of a TEI document are included in the output.
* {doc}`Blocks <blocks>` configures the TEI elements that define the block level, structural elements of the document
  (sections, paragraphs, lists, ...).
* {doc}`Marks <marks>` configures the TEI elements that define any inline markup.

You need to configure at least one section. If you have configured at least one `text` or `textlist` section, then you
need to configure at least one block element. The marks are optional and if you do not configure any, then it must
be removed from the configuration file.

## Limitations

The μEdition's support for TEI XML has one major limitation and that is that it does not support mixed content, meaning
that an XML element is not allowed to have both XML elements and text as its children. The following valid XML, where a
`tei:p` element contains both text and a nested `tei:hi` element, is not supported by the μEdition:

:::{code-block} xml
<tei:p>This is a paragraph with some <tei:hi rend="bold">important</tei:hi> text.</tei:p>
:::

In order for the μEdition to support this text, it would have to be restructured something like this:

:::{code-block} xml
<tei:p>
  <tei:seg>This is a paragraph with some </tei:seg>
  <tei:hi rend="bold">important</tei:hi>
  <tei:seg> text.</tei:seg>
</tei:p>
:::

In the μEdition, text content **must** only appear in the leaf elements of the XML document. Any text that appears
anywhere else in the document is ignored.

This is a fundamental design decision and is unlikely to change. Supporting mixed content would require significantly
more complex processing functionality in both the μEdition and the μEditor, while providing only minimal benefits.
