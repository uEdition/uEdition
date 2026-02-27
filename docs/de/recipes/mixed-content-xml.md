# Mixed-content (TEI) XML

Mixed-content XML ist XML bei dem einzelne Elemente im XML Dokument sowohl text, wie auch weitere Elemente als
Subelemente beinhalten. Folgendes XML ist ein Beispiel

:::{code-block} xml
<tei:p>Der Text wurde am <tei:date when="2026-02-25">26sten Februar 2026<tei:date> erstellt.</p>
:::

Die Problematik mit mixed-content XML ist, dass es in dieser Struktur schwierig ist zu unterscheiden ob Leerzeichen
Teil des Textes sind, oder nur zur Formattierung genutzt werden. In folgendem Beispiel hat der Text nach "erstellt"
einen Zeilenumbruch:

:::{code-block} xml
<tei:p>Der Text wurde am <tei:date when="2026-02-25">26sten Februar 2026<tei:date> erstellt
und hier in zwei Zeilen gebrochen.</p>
:::

Ob dieser Umbruch Textinhalt ist, oder nur zur Lesbarkeit eingefügt wurde kann nicht automatisch festgestellt werden
und dadurch wird die Verarbeitung von derartigem mixed-content XML signifikant schwieriger. Aus diesem Grund hat die
μEdition die Entscheidung getroffen, dass mixed-content XML **nicht unterstützt wird**.

Mixed-content XML muss daher in eine äquivalente, single-content Form umgewandelt werden. Folgender Block zeigt ein
Beispiel für wie das obrige Beispiel ohne mixed-content aussehen könnte:

:::{code-block} xml
<tei:p>
<tei:seg>Der Text wurde am </tei:seg>
<tei:date when="2026-02-25">26sten Februar 2026<tei:date>
<tei:seg> erstellt
und hier in zwei Zeilen gebrochen.</tei:seg>
</tei:p>
:::

Der zentrale Unterschied den man sieht, ist das explizit zwischen Text (insbesondere Leerzeichen und Zeilenumbrüchen)
unterschieden wird der zur Formattierung da ist (die Leerzeichen, die zur Einrückung genutzt werden), und welcher der
Dokumentinhalt ist (der Zeilenumbruch nach "erstellt").

Das ist nur eine Variante. Der Zeilenumbruch nach "erstellt" könnte auch als formattierend gelesen werden, in welchem
Fall der konvertierte XML Inhalt derart aussehen würde:

:::{code-block} xml
<tei:p>
<tei:seg>Der Text wurde am </tei:seg>
<tei:date when="2026-02-25">26sten Februar 2026<tei:date>
<tei:seg> erstellt und hier in zwei Zeilen gebrochen.</tei:seg>
</tei:p>
:::

## Das Rezept

Für diese Konvertierung bieten wir ein einfaches Python Skript an, welches
{download}`hier heruntergeladen werden kann<../_static/mixed-content-convert.py>`. Das heruntergeladene
{file}`mixed-content-convert.py` Skript in das Wurzelverzeichnis der μEdition verschieben und dann wie folgt
ausführen:

:::{code-block} console
$ hatch run python mixed-content-convert.py pfad/zur/quelldatei.tei pfad/zur/konvertierten/datei.tei
:::

:::{warning}
Unbedingt zwei unterschiedliche Dateien für die Quelle und das Ziel der Konvertierung nutzen. Ansonsten besteht
das Risiko, dass falls bei der Konvertierung ein Fehler auftritt, alle Daten verloren gehen könnten. Falls Sie
ein Backup haben und das Risiko eingehen wollen, dann kann `--insecure` als zusätzlicher Parameter mitgegeben werden
und dann könnne Quell- und Ziel-datei die selbe sein.
:::

Das Skript ist durchgängig kommentiert und kann natürlich angepasst werden um auf die Details der eigenen TEI Nutzung
eingehen zu können.
