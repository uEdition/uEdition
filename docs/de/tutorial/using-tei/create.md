# Eine TEI Seite anlegen

Wie für alle anderen Dateien, wird eine TEI Datei genau gleich wie jede andere Datei angelegt.

:::{room3b-video} /uedition/tutorial/tei/create-page/de
:::

## Einzelschritte

1. Im {file}`de` Dateiordner eine neue Datei {file}`text.tei` anlegen. Die `.tei` Dateierweiterung ist notwendig,
   damit die μEdition die Datei als TEI Datei erkennt.
2. In der {file}`toc.yml` Datei die neue TEI Datei unter dem `chapters` Schlüssel hinzufügen:

   :::{code-block} yaml
   - file: text.tei
   :::

3. Die neue TEI Datei {file}`de/text.tei` im Dateibrowser auswählen. Dies öffnet den TEI Editor, der die zwei
   konfigurierten Reiter {guilabel}`Metadata` und {guilabel}`Main text` enhält.
