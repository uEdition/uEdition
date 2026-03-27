# Die μEdition veröffentlichen

Die μEdition zu veröffentlichen ist der letzte Kernschritt dieses Tutorials. Die zwei weiteren Aspekte der Nutzung
von Git und TEI sind optional und für die Nutzung der μEdition nicht notwendig.

:::{room3b-video} /uedition/tutorial/publishing/de
:::

## Einzelschritte

1. Im Terminal den Server mittels der Tastenkombination {kbd}`Str+c` stoppen.
2. Dann folgenden Befehl ausführen, um die μEdition für die Veröffentlichung zu generieren:

   :::{code-block} console
   $ hatch run build
   :::

3. Dann im Dateiexplorer des Betriebssystems den Ordner der μEdition finden und dort existiert jetzt ein Ordner
   {file}`site`. Dieser enthält die generierte μEdition. Die Dateien in diesem Order können jetzt auf ein
   beliebiges Webhosting geladen werden, um die μEdition zu veröffentlichen.
4. Es kann auch die {file}`index.html` im Order {file}`site/de` direkt im Browser geöffnet werden um die
   generierte μEdition zu sehen.
