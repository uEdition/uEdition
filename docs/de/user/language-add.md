# Eine Sprache hinzufügen

In der μEdition ist Mehrsprachigkeit eine Kernfunktionalität. Das bedeutet, dass selbst wenn die Edition nur in einer
einzigen Sprache veröffentlicht werden soll, diese Sprache trotzdem explizit konfiguriert werden muss.

Um der μEdition eine Sprache hinzuzufügen, führen sie folgenden Befehl aus:

:::{code-block} console
$ hatch run uEdition language add ORDERNAME
:::

Ersetzen sie `ORDNERNAME` mit dem Namen des Orderners in dem die Inhalte in der Sprache gespeichert werden. Der Vorgang
wird ein paar Detailfragen zu der neuen Sprache abfragen und dann ein Inhaltsskelet in dem Ordern erzeugen, welches
dann bereit ist um ediert zu werden.
