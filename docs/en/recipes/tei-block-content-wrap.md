# Converting TEI block content.

In addition to the limitation of not supporting mixed-content XML, the μEdition also does not support content that is
contained directly within a TEI element, that in the μEdition has been configured to be a block element.

For example, the following TEI content would not be displayed in the μEdition:

:::{code-block} xml
<tei:p>This text is contained directly in a block-element.</tei:p>
:::

The content thus has to be converted into the following structure, in order to show it:

:::{code-block} xml
<tei:p>
<tei:seg>This text is contained directly in a block-element.</tei:seg>
</tei:p>
:::

## The recipe

For this conversion we provide a simple Python script, which
{download}`you can download here<../_static/tei-block-content-wrap.py>`. After downloading the
{file}`tei-block-content-wrap.py` script, move it into the root folder of your μEdition and run it using the
following command:

:::{code-block} console
$ hatch run python mixed-content-convert.py path/to/source.tei path/to/converted.tei
:::

:::{warning}
You **must** use two different files for the source and converted files. Otherwise there is the risk that if anything
were to happen during the conversion, all data would be lost. If you have a backup and want to take that risk, then you
can pass the `--insecure` parameter, in which case the source and converted filename can be the same.
:::

The script is fully commented and can, obviously, be adapted to deal with the specific needs of your TEI usage.
