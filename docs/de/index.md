# μEdition

Das Erstellen einer kritischen, digitalen Edition bringt mit sich eine Reihe signifikanter Hürden, besonders wenn es um
die technischen Anforderungen und Hostingkosten geht. Die μEdition bietet ein Gerüst um diese Hürden zu reduzieren, indem
es ein einfaches Werkzeug anbietet, welches Projekte darin unterstützt einfach (multilinguale) digitale Editionen zu
erstellen, welche dann über gratis oder billige Hostinglösungen online verfügbar gemacht werden können.

:::{admonition} Hilfe und Unterstützung
:class: tip

Die μEdition ist noch ein junges Projekt und benötigt Feedback von Nutzern und Nutzerinnen um die Hürden zur Nutzung
weiter zu reduzieren. Egal ob dies zusätzliche Dokumentation ist, Fehler beheben, oder zusätzliche Funktionalität,
bitte informiert uns und dann können wir die μEdition besser machen.

Für alle Fragen zur μEdition und zu ihrer Nutzung, nutzt bitte unser GitHub Discussions Forum:
https://github.com/uEdition/uEdition/discussions.

Wenn Fehler auftreten, dann bitte diese über unsere GitHub Issues melden und dann können wir sie reparieren:
https://github.com/uEdition/uEdition/issues.
:::

## Inhaltsverzeichnis

:::{tableofcontents}
:::

## Schnellstart

Für einen Schnellstart mit der μEdition, folgens sie diesen Schritten:

1. [Python](https://www.python.org/downloads) für das korrekte Betriebssystem installieren, falls noch nicht installiert.
   Die μEdition unterstützt alle Python Versionen, die [aktuell unterstützt sind](https://devguide.python.org/versions/).
2. [Hatch](https://hatch.pypa.io/latest/install/) für das korrekte Betriebssystem installieren.
3. Einen neuen Dateiordner für die μEdition anlegen.
4. Die Projektkonfiguration {download}`_static/pyproject.toml` herunterladen und im neuen Dateiordner abspeichern.
5. Auf der Kommandozeile in den neuen Dateiordner wechseln und dort folgenden Befehl ausführen:

   :::{code-block} console
   hatch run init
   :::

   Dies erzeugt die notwendige Konfigurationsdatei ({file}`uEdition.yml`) und das Inhaltsverzeichnis ({file}`toc.yml`).

6. Dann folgenden Befehl ausführen um eine neue Sprache hinzuzufügen

   :::{code-block} console
   hatch run language add
   :::

   Nach dem Beantworten von ein paar Fragen über die neue Sprache werden die notwendigen Dateien erzeugt.

7. Abschließend folgenden Befehl ausführen um den lokalen Server zu starten:

   :::{code-block} console
   hatch run serve
   :::

   Die neue, digitale Edition ist dann unter http://localhost:8000 verfügbar.

8. Um den [μEditor](https://ueditor.readthedocs.org) für das Bearbeiten der μEdition zu starten, den folgenden Befehl in einem
   separaten Terminal ausführen:

   :::{code-block} console
   hatch run edit
   :::

   Der μEditor ist dann unter http://localhost:8080 verfügbar.
