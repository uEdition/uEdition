# Inhalte hinzufügen

Die μEdition nutzt [Jupyter Book](https://jupyterbook.org) um aus den Inhalten eine Webseite zu generieren,
welche dann veröffentlicht werden kann. Wenn die Webseite generiert wird, generiert die μEdition zuerst die
Webseiten für die einzelnen Sprachen und fügt dann die notwendigen Element hinzu um die einzelnen Sprachen
zusammenzufügen. Da die μEdition auf dem Jupyter Book aufbaut, sind der Großteil der Dokumentation des
Jupyter Book Projekts auch für die μEdition nutzbar. Der einzige Unterschied ist, dass die μEdition eine
Konfigurationsdatei und ein Inhaltsverzeichnisse für alle Sprachen nutzt.

## Die μEdition strukturieren

Die Struktur der μEdition wird über das Inhaltsverzeichnis definiert, welches in der {file}`toc.yml` Datei
(im Wurzelverzeichnis der μEdition) konfiguriert wird. Die {file}`toc.yml` Datei nutzt das Format
[der zugrundeliegenden Jupyter Book Technik](https://jupyterbook.org/en/stable/structure/toc.html). Der
einzige Unterschied ist, dass die `title` und `caption` Einträge in der μEdition mit sprachspezifischen
Werten konfiguriert werden. Wenn die μEdition dann generiert wird, werden für jede konfigurierte Sprache
die jeweils relevanten Werte genutzt:

:::{code-block} yaml
format: jb-book
root: index
parts:
  - caption:
      en: Name of Part 1
      de: Name von Teil 1
    chapters:
    - title:
        en: Chapter 1
        de: Chapter 2
      file: path/to/part1/chapter1
    - file: path/to/part1/chapter2
:::

## Texte schreiben

Das Jupyter Book nutzt primär MyST (Markedly Structured Text) um die Textinhalte zu erstellen. Dies ist eine Erweiterung
des Markdownformats für komplexere Texte. Eine gute Übersicht über die Kernfunktionalität
[findet sich hier](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html). Das Jupyter Book stellte eine
Reihe von Erweiterungen bereit, welche [hier dokumentiert sind](https://jupyterbook.org/en/stable/content/index.html)
und welche die einfache Erstellung von Aspekten wie Glossar, Index, Zitierbarkeit, Fußnoten und Layoutstrukturen.

Die μEdition stellt selbst eine Erweiterung zur Verfügung, welche die nutzung von TEI-XML (Text Encoding Initiative)
sowohl als Eingabe, wie auch als Ausgabeformat bereitstellt.

## Lokaler Server

Während des Schreibprozesses kann es hilfreich sein zu sehen, wie das Ergebnis aussieht. Um dies zu vereinfachen stellt
die μEdition einen eingebauten Webserver zur verfügung, der die generierte μEdition automatisch aktualisiert, wenn die
Inhalte bearbeitet werden. Um den Server zu starten wird folgender Befehl genutzt:

:::{code-block} console
$ hatch run serve
:::

This generiert die μEdition und macht sie dann unter http://localhost:8000 verfügbar. Wenn die Inhalte geändert werden,
wird die μEdition automatisch neugeneriert und die Seite im Browser automatisch neugeladen.
