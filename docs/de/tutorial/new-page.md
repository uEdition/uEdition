# Eine neue Seite hinzufügen

## Einzelschritte

1. Im Dateibrowser den Ordner auswählen in dem die neue Datei angelegt werden soll.
2. Dann auf den {guilabel}`Create a new File` Button klicken.
3. Den Dateinamen für die neue Datei eingeben. Da eines der Ziele der μEdition die Veröffentlichung im Web ist,
   ist die Empfehlung für Dateinamen, keine Leerzeichen oder Sonderzeichen im Dateinamen zu nutzen. Die Außnahme dabei
   ist die Verwendung von `-` und `_`. Markdowndateien müssen {file}`.md` als Dateierweiterung haben.
4. Dann auf den {guilabel}`Create` Button klicken oder die {kbd}`Eingabe` Taste drücken.
5. Die neue Datei im Dateibrowser auswählen.
6. Der neuen Markdowndatei einen Titel (eine Überschrift der ersten Ebene geben):

   :::{code-block} markdown
   # Über die μEdition
   :::
7. Die Änderung abspeichern.
8. Im Dateibrowser die Datei {file}`toc.yml` auswählen. Der Erstinhalt der Datei ist

   :::{code-block} yaml
   format: jb-book
   root: index
   :::

   Die erste Zeile definiert das Format der Datei. In diesem Fall ist das `jb-book`, welches eine Struktur
   `Abteilungen` -> `Kapitel` -> `Sektion` definiert. Weitere Dokumentation dazu findet sich unter
   [https://sphinx-external-toc.readthedocs.io/en/latest/intro.html](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html).

   Die zweite Zeile definiert die Startseite, in diesem Fall die Datei {file}`index.md`.

   :::{important}
   Die Datei {file}`toc.yml` ist im Wurzelverzeichnis der μEdition. Die Datei {file}`_toc.yml` in den Dateiordnern der
   einzelnen Sprachen werden automatisch aus der {file}`toc.yml` generiert und alle Änderungen in den {file}`_toc.yml`
   werden dabei überschrieben.
   :::
9. Um unsere neue Seite der μEdition hinzuzufügen, muss folgender Block an das Ende der {file}`toc.yml` Datei hinzugefügt
   werden:

   :::{code-block} yaml
   chapters:
     - file: DATEINAME
   :::

   Dabei ist der `DATEINAME` durch den Namen der neuen Datei **ohne die Dateierweiterung** zu ersetzen. Der Dateiname
   ist dabei relativ zum Sprachordner und nicht relativ zum Wurzelverzeichnis der μEdition.
10. Die Datei abspeichern
11. Die μEdition wird automatisch neu generiert und die neue Seite wird in der μEdition erscheinen.

:::{note}
Falls die neue Datei nicht erscheint, dann im Terminal nachsehen, was für Fehlermeldungen dort angezeigt werden.
Meist ist die Quelle für das Problem ein Tippfehler in einer der Dateinamen.
:::
