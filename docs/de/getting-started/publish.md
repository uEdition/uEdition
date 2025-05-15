# Die μEdition publizieren

Wenn die μEdition in einem Zustand ist, in dem sie publizert werden kann, dann generiert folgender Befehl
eine publizierbare Version:

:::{code-block} console
$ hatch run build
:::

Die μEdition generiert dann die Webinhalte in das konfigurierte Ausgabeverzeichnis (Standardmäßig das Verzeichnis
{file}`site`). Der Inhalt kann dann auf eine beliebige Hostinglösung kopiert werden und ist dann öffentlich
Verfügbar.
