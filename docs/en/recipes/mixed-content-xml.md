# Mixed-content (TEI) XML

Mixed-content XML is XML where individual elements can contain both text, as well as further child elements. The
following XML gives an example:

:::{code-block} xml
<tei:p>On the <tei:date when="2026-02-25">26sten Februar 2026<tei:date> this text was created.</p>
:::

The problem with mixed-content XML is that in this structure it is difficult to determin whether spaces are part of the
text or are just being used for formatting. In the following XML a line-break has been added after created:

:::{code-block} xml
<tei:p>On the <tei:date when="2026-02-25">26sten Februar 2026<tei:date> this text was created
and split into two lines.</p>
:::

It is impossible to always automatically determine whether the line-break is part of the text or has just been added
to improve readability. This makes processing mixed-content XML significantly harder. For this reason the μEdition
has decided that mixed-content XML **is not supported**.

It is thus necessary to convert mixed-content XML into an equivalent, single-content form. The following block show
an example for how this could look:

:::{code-block} xml
<tei:p>
<tei:seg>On the </tei:seg>
<tei:date when="2026-02-25">26sten Februar 2026<tei:date>
<tei:seg> this text was created
and split into two lines.</tei:seg>

</p>
:::

The main difference is that there is an explicit distinction between text (particularly spaces and line-breaks) that
are used for formatting (the spaces used to indent the text) and the line-break after "created", that is part of the
document content.

That is one variant. The line-break after "created" could also just have been formatting. In that case the converted
XML would look like this:

:::{code-block} xml
<tei:p>
<tei:seg>On the </tei:seg>
<tei:date when="2026-02-25">26sten Februar 2026<tei:date>
<tei:seg> this text was created and split into two lines.</tei:seg>
</tei:p>
:::

## The recipe

For this conversion we provide a simple Python script, which
{download}`you can download here<../_static/mixed-content-convert.py>`. After downloading the
{file}`mixed-content-convert.py` script, move it into the root folder of your μEdition and run it using the
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
