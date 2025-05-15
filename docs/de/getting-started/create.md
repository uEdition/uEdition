# Eine μEdition erstellen

Jetzt wo alle Vorraussetzungen installiert sind, kann die erste μEdition erstellt werden. Erstellen sie einen
neuen Dateiordner für die neue μEdition. Dann laden sie die {download}`../_static/pyproject.toml` herunter
und speichern sie diese im neuen Dateiordner ab.

Dann navigieren sie auf der Kommandozeile in den neuen Dateiordner und führen folgenden Befehl aus:

:::{code-block} console
$ hatch run init
:::

Dies erstellt eine virtuelle Python Installation mit allen Softwarepaketen die die μEdition benötigt und führt
dann den Initialisierungsvorgang aus. Dies erzeugt die Dateien {file}`uEdition.yml`, welche die Konfigurationseinstellungen
beinhaltet, und {file}`toc.yml`, welche das Inhaltsverzeichnis beinhaltet.

Der nächste Schriftt ist es der μEdition eine Sprache hinzuzufügen, damit die Inhalte bearbeitet werden können.
