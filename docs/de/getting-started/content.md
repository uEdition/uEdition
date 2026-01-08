# Inhalte hinzufügen

Die μEdition baut auf [Sphinx](https://www.sphinx-doc.org/) auf um aus den Inhalten eine Webseite zu generieren,
welche dann veröffentlicht werden kann. Jede Sprache in der μEdition ist ein eigenes Sphinx Dokument und die
μEdition fügt die einzelnen Ausgaben in eine gemeinsame Webseite zusammen. Die μEdition lädt auch automatisch
die [MyST](https://myst-parser.readthedocs.io/en/latest/) Erweiterung, damit Inhalte in Markdown erstellt werden können.

## Die μEdition strukturieren

Die Struktur der μEdition wird über das Inhaltsverzeichnis definiert, welches in der {file}`toc.yml` Datei
(im Wurzelverzeichnis der μEdition) konfiguriert wird. Die {file}`toc.yml` Datei nutzt das Format
[der zugrundeliegenden Jupyter Book Technik](https://jupyterbook.org/en/stable/structure/toc.html) und die
Anfängliche {file}`toc.yml` sieht wie folgt aus:

:::{code-block} yaml
format: jb-book
root: index
:::

Wichtig hier ist die `root: index` Einstellung, welche festlegt, dass eine Datei mit dem Namen {file}`index`
als Anfangsseite genutzt wird. Im Dateiordner der ersten Sprache gibt es eine Datei {file}`index.md`, deren
Inhalt die Anfangsseite der μEdition beinhaltet.

Um der μEdition Seiten hinzuzufügen, müssen diese in Kapitel organisiert werden. Zum Beispiel um zwei Kapitel
"richtlinien" und "kontakt" hinzuzufügen, aktualisieren sie die {file}`toc.yml` wie folgt:

:::{code-block} yaml
format: jb-book
root: index
chapters:
  - file: richtlinien
  - file: kontakt
:::

Dann legen sie zwei Dateien {file}`richtlinien.md` und {file}`kontakt.md` im Dateiordner der Sprache an und
fügen dort die gewünschten Inhalte ein. Stellen sie sicher, dass der Dateiname jedes `file:` Eintrages ein
relativer Dateipfad ist, der vom Dateiordner der Sprache auf die Datei verweist.

Weiter Details über die Konfigurationsmöglichkeiten des Inhaltsverzeichnisses finden sie in der
[Dokumentation des Jupyter Book Inhaltsverzeichnises](https://jupyterbook.org/en/stable/structure/toc.html).

Standardmäßig wird der Titel des Dokuments als Titel im Inhaltsverzeichnis genutzt. Es ist jedoch möglich
einen alternativen Titel zu konfigurieren, indem ein `caption` oder `title` Eintrag bereitgestellt wird.
Die μEdition erweitert diese Funktionalität und ermöglicht es für jede konfigurierte Sprache einen eigenen
Titel zu konfigurieren:

:::{code-block} yaml
format: jb-book
root: index
parts:
  - caption:
      en: Part 1
      de: Teil 1
    chapters:
    - title:
        en: Chapter 1
        de: Kapitel 1
      file: path/to/part1/chapter1
    - file: path/to/part1/chapter2
:::

## Texte schreiben

Markedly Structured Text ist das primäre Format um die Textinhalte zu erstellen. Eine gute Übersicht über die
Kernfunktionalität [findet sich hier](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html) und Erweiterungen
die Jupyter Book bereitstellt [sind hier dokumentiert](https://jupyterbook.org/en/stable/content/index.html)
und dokumentiert das einfache Erstellen von Aspekten wie Glossar, Index, Zitierbarkeit, Fußnoten und Layoutstrukturen.

## Lokaler Server

Während des Schreibprozesses kann es hilfreich sein zu sehen, wie das Ergebnis aussieht. Um dies zu vereinfachen stellt
die μEdition einen eingebauten Webserver zur verfügung, der die generierte μEdition automatisch aktualisiert, wenn die
Inhalte bearbeitet werden. Um den Server zu starten wird folgender Befehl genutzt:

:::{code-block} console
$ hatch run serve
:::

This generiert die μEdition und macht sie dann unter http://localhost:8000 verfügbar. Wenn die Inhalte geändert werden,
wird die μEdition automatisch neugeneriert und die Seite im Browser automatisch neugeladen.

## μEditor

Zum Bearbeiten der μEdition kann jeder Texteditor verwendet werden. Die μEdition kommt aber auch mit einem web-basierten Editor,
welcher mittels des folgenden Befehls (in einem zweiten Terminal) gestartet werden:

:::{code-block} console
$ hatch run edit
:::

Dies startet den μEditor Server, welcher dann unter http://localhost:8080 verfügbar ist.
