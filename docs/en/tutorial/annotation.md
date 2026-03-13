# Text markup

Markdown was originally designed as a very simple format for the basic markup of text. The version of ;arkdown used in
the μEdition extends this basic functionality with a wide range of additional functionality, of which we will only be
able to look at a very small sub-set.

Markdown distinguishes between text blocks and markup within a block. In the μEdition the first are referred to as
_blocks_, while the second category are referred to as _marks_. A complete overview over the Markdown syntax can be
found at [https://myst-parser.readthedocs.io/en/latest/syntax/typography.html](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
(and the following pages).

:::{room3b-video} /uedition/tutorial/edit-page/en
:::

## Simple inline markup

The simplest markup are bold and italic text. Bold text is marked up using double `**`, while for italic text the underscore
`_` is used. For example the following Markdown text:

:::{code-block} markdown
This is **bold** and _italic_ text. These can also be **_combined_**.
:::

produces the following output (without the border):

:::{card}
This is **bold** and _italic_ text. These can also be **_combined_**.
:::

## Complex inline markup

Markdown provides a structure for more complex inline markup. In this structure the name of the markup is provided
between curly brackets (e.g. `{sub-ref}`) and the marked-up text is then included between two \` backticks (e.g.
\`today\`).

Thus the following Markdown:

:::{code-block} markdown
This text was generated on {sub-ref}`today`.
:::

the following result

:::{card}
This text was generated on {sub-ref}`today`.
:::

### TEI annotations

The μEdition extends Markdown with the ability to generate simple TEI annotations, using the `{tei}` markup tag. The
content of the `{tei}` tag consists of two parts. First one or more `<tei:tag>` elements specifying the TEI tags to
apply to the text, followed by the actual text to annotate.

For example, the following Markdown generates a TEI annotation using the [`rdg`](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-rdg.html)
(reading) tag:

:::{code-block}
{tei}`<rdg>Hullo`
:::

The result looks like this:

:::{card}
{tei}`<rdg>Hullo`
:::

Visually there is no immediate change, but the necessary HTML code is there to allow future visual styling.

Some TEI tags require attributes and these can simply be provided like in TEI itself:

:::{code-block}
{tei}`<rdg wit="a">Hullo`
:::

The result is visually the same, but the attribute has now been added to the HTML.

:::{card}
{tei}`<rdg wit="a">Hullo`
:::

## Simple text blocks

The two primary elements to structure the content are headings and paragraphs. Headings are marked up in Markdown using
the hash symbol `#`, followed by the heading text. The number of hash symbols is used to define the heading level.
Paragraphs are defined by separating them using an empty line.

The following Markdown example contains a heading of level 1, a heading of level 2, and three paragraphs:

:::{code-block} markdown
# Level 1 heading

Here is a short paragraph with some text.

## Level 2 heading

Here is a short paragraph within the level 2 heading.

This is a third paragraph.
:::

There are a lot of other text blocks, which are documented at
[https://myst-parser.readthedocs.io/en/latest/syntax/typography.html](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html).

## Complex text blocks

As with the inline markup, Markdown provides a structure for defining further, complex text blocks. The start of these
text blocks is defined using three colons `:::`, followed by the name of the text block in curly brackets (e.g. `{note}`).
For example, the following Markdown

::::{code-block} markdown
:::{note}
Here is a small note.
:::
::::

generates the following output:

:::{note}
Here is a small note.
:::

You can find further details on these complex text blocks here:
[https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#directives-a-block-level-extension-point](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#directives-a-block-level-extension-point).

### TEI annotations

The μEdition provides a text block extension for TEI markup, which has the block name `{tei}`. The desired TEI tag is
provided after the `{tei}`. For example, the following example generates a
[`lg`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-lg.html) element (line-group)
and a [`l`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-l.html) element (line) with that:

:::::{code-block} markdown
::::{tei} lg
:::{tei} l
This is a line in a verse.
:::
::::
:::::

As with the inline markup, there is no visual result to this, but the HTML has the correct structure:

:::::{card}
::::{tei} lg
:::{tei} l
This is a line in a verse.
:::
::::
:::::

As with the inline markup, TEI attributes can also be provided. These are configured via the `:attributes:` key
within the text block:

:::::{code-block} markdown
::::{tei} lg
:attributes: style="fancy"

:::{tei} l
:attributes: style="bold"

This is a line in a verse.
:::
::::
:::::

:::::{card}
::::{tei} lg
:attributes: style="fancy"

:::{tei} l
:attributes: style="bold"

This is a line in a verse.
:::
::::
:::::

Later in the tutorial we will look at configuring the μEdition to add styling to these.

:::{note}
The Markdown examples in this page demonstrate how Markdown blocks can be nested. To nest them, simply ensure that the
number of colons for the outer text block is larger than the number of colons in the inner block.
:::
