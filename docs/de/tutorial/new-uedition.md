# Eine μEdition erstellen

Jetzt wo alle notwendigen Basiskomponenten installiert sind, zeigt das nächste Video, wie eine neue μEdition erstellt
wird:

:::{room3b-video} /uedition/tutorial/installation/de
:::

# Zum Mitkopieren

1. Die {download}`../_static/pyproject.toml` Datei herunterladen.
2. Einen neuen Ordern für die μEdition erstellen.
3. Die {file}`pyproject.toml` Datei in den neuen Ordner verschieben.
4. Ein neues Terminal im neu angelegten Ordern öffnen.
5. Folgenden Befehl ausführen, um die neue μEdition zu initialisieren:

   :::{code-block} console
   $ hatch run init
   :::

   Dieser Vorgang kann ein paar Minuten dauern.
6. Folgenden Befehl ausführen, um der μEdition eine neue Sprache hinzuzufügen (jede μEdition braucht mindestens
   eine Sprache):

   :::{code-block} console
   $ hatch run language add
   :::

   Der Befehl fragt um drei Informationen:

   * **Language code**: ISO Sprachkürzel der neuen Sprache. Dieser wird für den Ordnernamen für die
     sprachspezifischen Inhalte genutzt.
   * **Language name**: Name der neuen Sprache. Diese wird für die Sprachwechselfunktionen der μEdition genutzt.
   * **Title**: Titel der neuen μEdition in der Sprache.

7. Folgenden Befehl ausführen, um die HTML Version der μEdition zu erstellen:

   :::{code-block} console
   $ hatch run serve
   :::

   Dies startet einen kleinen lokalen Webserver und die HTML Version der μEdition kann dann über folgende
   URL aufgerufen werden: [http://localhost:8000](http://localhost:8000). Der Start kann ein paar Sekunden dauern.
   Bitte geduldig sein :-).

Wenn sie nach dem letzten Schritt die μEdition im Browser sehen, dann sind sie bereit für die nächsten Schritte.
Falls die μEdition nicht im Browser erscheint, dann sollte im Terminal ein Fehler auftauchen. Beheben sie den
Fehler und dann sollte alles funktionieren.

:::{note}
Um den Webserver zu stoppen, wechseln sie zum Terminal zurück und drücken dann {kbd}`Strg+c`.

Vor dem Weiterarbeiten an der μEdition muss der Webserver dann mittels `hatch run serve` wieder gestartet werden.
:::
