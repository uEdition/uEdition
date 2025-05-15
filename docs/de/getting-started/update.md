# Die μEdition aktualisieren

Die μEdition wird kontinuierlich weiterentwickelt und um sicherzustellen, dass sie von den neuesten Verbesserungen
profitieren, sollte die μEdition regelmäßig aktualisiert werden.

:::{warning}
Bevor sie die μEdition aktualisieren, legen sie unbedingt ein Backup des aktuellen Zustands ihrer μEdition an. Der
Aktualisierungsvorgang ist ausführlich getestet, aber es besteht immer die Möglichkeit einen unbekannten Fehlers
und ein Backup stellt sicher, dass eine derartige Situation kein Problem darstellt.
:::

Die Aktualisierung der μEdition besteht aus zwei Schritten. Führen sie zuerst folgenden Befehl aus

:::{code-block} console
$ hatch run update
:::

Dies aktualisiert die konfigurierte μEditionsversion auf die neueste Version. Dann führen sie Folgenden Befehl aus

:::{code-block} console
$ hatch run migrate
:::

Dies installiert die aktuelle Version der μEdition Software und führt auch alle notwendigen Konfigurationsänderungen aus.

Danach können sie jetzt mit der aktuellsten Version der μEdition weiterarbeiten.
