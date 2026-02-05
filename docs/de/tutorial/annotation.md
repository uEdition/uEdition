# Textauszeichnungne

Markdown war ursprünglich als sehr einfaches Format für die Auszeichnung von Text entwickelt worden. Die Markdownversion
die der μEdition zugrundeliegt, hat diese aber derart signifikant erweitert, dass wir nur einen kleinen Teil davon
ansehen können.

Markdown unterscheidet zwischen Textblöcken und Textauszeichnungen innerhalb eines Blockes. Erstere werden in der
μEdition als _Blocks_ bezeichnet, zweitere als _Marks_. Eine vollständige Übersicht über die Verfügbaren Auszeichnungen
findet sich unter [https://myst-parser.readthedocs.io/en/latest/syntax/typography.html](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
(und den darauf folgenden Seiten).

## Einfache Textauszeichnungen

Die einfachsten (under vermutlich häufigsten) Textauszeichnungen sind fett-gedruckter und kursiver Text. Fett-gedruckter
Text wird mittels doppelter `**` ausgezeichnet, während für den kursiven Text der Unterstrich `_` genutzt wird. Zum
Beispiel generiert folgender Markdown text:

:::{code-block} markdown
Dies ist **fett-gedruckter** und _kursiver_ Text. Diese könnne auch **_kombiniert_** werden.
:::

folgendes Ergebnis (ohne den Rahmen):

:::{card}
Dies ist **fett-gedruckter** und _kursiver_ Text. Diese könnne auch **_kombiniert_** werden.
:::

## Komplexere Textauszeichnungen

Markdown bietet auch eine Struktur für komplexere Textauszeichnungen an. In dieser Struktur wird zuerst der
Name der Auszeichnung in geschwungen Klammern eingegeben (z.B. `{sub-ref}`) und danach wird der auszuzeichnende Text
zwischen zwei \` Zeichen eingegeben (z.B. \`today\`).

So generiert folgender Markdowntext

:::{code-block} markdown
Dieser Text wurde am {sub-ref}`today` generiert.
:::

folgendes Ergebnis:

:::{card}
Dieser Text wurde am {sub-ref}`today` generiert.
:::

### TEI Annotationen

Die μEdition bietet TEI annotationen in Markdown, mittels der `{tei}` Auszeichnung an. Der Textinhalt der `{tei}`
Auszeichnung besteht aus zwei Teilen. Zuerst einem oder mehreren `<tei-tag>` Elementen und dann dem damit zu annotierenden
Text.

Zum Beispiel würde der folgende Markdowntext eine TEI Annotation mit dem Tag [`rdg`](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-rdg.html)
(Textvariante) generiere:

:::{code-block}
{tei}`<rdg>Hullo`
:::

Das Ergebnis sieht dann so aus:

:::{card}
{tei}`<rdg>Hullo`
:::

Visuell unterscheidet sich das nicht von normalem Text, aber es wird das notwendige HTML generiert, damit das später
visuell hervorgehoben werden kann.

Manche TEI Annotationen erwarten auch Attribute und diese können einfach wie in normalem TEI in die Tagdefinition
eingefügt werden:

:::{code-block}
{tei}`<rdg wit="a">Hullo`
:::

Das Ergebnis ist wiederum gleich, aber im HTML ist das Attribute jetzt auch vorhanden:

:::{card}
{tei}`<rdg wit="a">Hullo`
:::

## Einfache Textblöcke

Die zwei primären Elemente um den Textinhalt zu strukturieren sind Überschriften und Absätze. Überschriften werden in
Markdown mittels des Rautensymbols for der Überschrift ausgezeichnet. Dabei definiert die Anzahl der Rautensymbole das
Überschriftenlevel. Absätze werden in Markdown einfach durch eine Leerzeile voneinander getrennt.

Folgendes Markdownbeispiel enthält eine Überschrift der ersten Ebene, eine Überschrift der zweiten Ebene und drei
Absätze:

:::{code-block} markdown
# Überschrift erste Ebene

Hier ist ein kurzer Absatz mit etwas Text.

## Überschrift zweite Ebene

Hier ist ein Absatz unter der zweiten Ebene.

Und ein dritter Absatz.
:::

Es gibt natürlich noch weitere einfache Textblöcke, welche unter
[https://myst-parser.readthedocs.io/en/latest/syntax/typography.html](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
dokumentiert sind.

## Komplexe Textblöcke

Wie bei den Textauszeichnungen bietet Markdown auch eine Struktur für komplexere Textblöcke an. Dabei wird der Anfang des Textblocks mit
drei Doppelpunkten markert `:::`. Darauf folgt in geschwungenen Klammern der Name des Textblocks (z.B. `{note}`). Zum Beispiel generiert
der folgende Markdownblock:

::::{code-block} markdown
:::{note}
Hier eine kleine Notiz.
:::
::::

folgende Bemerkung:

:::{note}
Hier eine kleine Notiz.
:::

Weitere Details dazu können unter
[https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#directives-a-block-level-extension-point](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#directives-a-block-level-extension-point)
nachgelesen werden.

### TEI Annotationen

Wie bei den Textauszeichnungen, bietet die μEdition auch einen Textblock mit dem Namen `{tei}` an, um größere TEI Blöcke
auszuzeichnen. Dabei wird der Name des gewünschten TEI Tags nach dem `{tei}` angegeben. Zum Beispiel generiert folgender
Markdownblock ein TEI [`lg`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-lg.html) Element (Zeilengruppe)
und darin ein [`l`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-l.html) Element (Zeile):

:::::{code-block} markdown
::::{tei} lg
:::{tei} l
Dies ist eine Zeile in einem Vers.
:::
::::
:::::

Wie schon bei den Textauszeichnungen ist das visuell nicht sichtbar, aber im HTML wurde die korrekte Struktur generiert:

:::::{card}
::::{tei} lg
:::{tei} l
Dies ist eine Zeile in einem Vers.
:::
::::
:::::

Ebenso wie bei den Textauszeichnungen können dem TEI Attribute mitgegeben werden. Diese werden über den `:attributes`
Schlüssel innerhalb des Textblockes definiert:

:::::{code-block} markdown
::::{tei} lg
:attributes: style="fancy"

:::{tei} l
:attributes: style="bold"

Dies ist eine Zeile in einem Vers.
:::
::::
:::::

:::::{card}
::::{tei} lg
:attributes: style="fancy"

:::{tei} l
:attributes: style="bold"

Dies ist eine Zeile in einem Vers.
:::
::::
:::::

Später im Tutorial werden wir auch sehen, wie wir diese Tags visuell auszeichnen können.

:::{note}
Die Markdownbeispiele in diesem Bereich zeigen auch, wie Markdownblöcke ineinander verschachtelt werden können. Dazu
muss einfach die Anzahl der Doppelpunkte für die äußeren Textblöcke erhöht werden, so dass visuell eine Verschachtelung
entsteht.
:::
