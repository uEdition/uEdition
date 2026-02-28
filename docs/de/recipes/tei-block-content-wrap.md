# TEI Blockinhalte umwandeln

Zusätzlich zu der Einschränkung, dass die μEdition kein mixed-content XML unterstützt, hat die μEdition eine weitere
technische Einschränkung. Sie ignoriert jeglichen Text, der direkt in einem TEI element liegt, welches in der μEdition
als Blockelement konfiguriert ist.

Zum Beispiel würde folgender TEI Inhalt in der μEdition nicht angezeigt:

:::{code-block} xml
<tei:p>Dieser Text liegt direkt in einem Blockelement.</tei:p>
:::

Der Inhalt muss daher in die folgende Struktur umgewandelt werden, damit der Inhalt angezeigt wird:

:::{code-block} xml
<tei:p>
  <tei:seg>Dieser Text liegt direkt in einem Blockelement.</tei:seg>
</tei:p>
:::

## Das Rezept

Um diesen Schritt zu vereinfachen bieten wir ein einfaches Python Skript an, welches
{download}`hier heruntergeladen werden kann<../_static/tei-block-content-wrap.py>`. Das heruntergeladene
{file}`tei-block-content-wrap.py` Skript in das Wurzelverzeichnis der μEdition verschieben und dann wie folgt
ausführen:

:::{code-block} console
$ hatch run python tei-block-content-wrap.py pfad/zur/quelldatei.tei pfad/zur/konvertierten/datei.tei
:::

:::{warning}
Unbedingt zwei unterschiedliche Dateien für die Quelle und das Ziel der Konvertierung nutzen. Ansonsten besteht
das Risiko, dass falls bei der Konvertierung ein Fehler auftritt, alle Daten verloren gehen könnten. Falls Sie
ein Backup haben und das Risiko eingehen wollen, dann kann `--insecure` als zusätzlicher Parameter mitgegeben werden
und dann könnne Quell- und Ziel-datei die selbe sein.
:::

Das Skript ist durchgängig kommentiert und kann natürlich angepasst werden um auf die Details der eigenen TEI Nutzung
eingehen zu können.
