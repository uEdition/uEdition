# Textauszeichnungne

Markdown war ursprünglich als sehr einfaches Format für die Auszeichnung von Text entwickelt worden. Die Markdownversion
die der μEdition zugrundeliegt, hat diese aber derart signifikant erweitert, dass wir nur einen kleinen Teil davon
ansehen können.

Markdown unterscheidet zwischen Textblöcken und Textauszeichnungen innerhalb eines Blockes. Erstere werden in der
μEdition als _Blocks_ bezeichnet, zweitere als _Marks_. Eine vollständige Übersicht über die Verfügbaren Auszeichnungen
findet sich unter [https://mystmd.org/guide/typography](https://mystmd.org/guide/typography).

## Einfache Textauszeichnungen

Die einfachsten (under vermutlich häufigsten) Textauszeichnungen sind fett-gedruckter und kursiver Text. Fett-gedruckter
Text wird mittels doppelter `**` ausgezeichnet, während für den kursiven Text der Unterstrich `_` genutzt wird. Zum
Beispiel generiert folgender Markdown text:

:::{code} markdown
Dies ist **fett-gedruckter** und _kursiver_ Text. Diese könnne auch **_kombiniert_** werden.
:::

folgendes Ergebnis:

Dies ist **fett-gedruckter** und _kursiver_ Text. Diese könnne auch **_kombiniert_** werden.

## Komplexere Textauszeichnungen

Markdown bietet auch eine Struktur für komplexere Textauszeichnungen an. In dieser Struktur wird zuerst der
Name der Auszeichnung in geschwungen Klammern eingegeben (z.B. `{del}`) und danach wird der auszuzeichnende Text
zwischen zwei \` Zeichen eingegeben (z.B. \`Alte Information\`).

So generiert folgender Markdowntext

:::{code} markdown
Dieser Text {del}`wurde entfernt`.
:::

folgendes Ergebnis:

Dieser Text {del}`wurde entfernt`.

## Textblöcke

[eine kleine Anzahl an]

{tei}`<rdg wit="a"><hi style="italic">Some simple text`

{tei}`<rdg>Some simple text`

::::{tei} lg
:attributes: style="fancy"

:::{tei} l
:attributes: style="bold"

This is a line in a verse.
:::
::::
