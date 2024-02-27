# Die μEdition publizieren

Wenn die μEdition in einem Zustand ist, in dem sie publizert werden kann, dann generiert folgender Befehl
eine publizierbare Version:

:::{code-block} console
$ hatch run build
:::

Die μEdition generiert dann die Webinhalte in das konfigurierte Ausgabeverzeichnis (Standardmäßig das Verzeichnis
{file}`site`). Der Inhalt kann dann auf eine beliebige Hostinglösung kopiert werden und ist dann öffentlich
Verfügbar.

## Auf GitHub Pages publizieren

Die μEdition kommt standardmäßig mit Unterstützung um die μEdition über [GitHub Pages](https://pages.github.com/)
zu publizieren. Damit das funktioniert müssen folgende Vorraussetzungen erfüllt werden:

* Die μEdition muss ein Git Repository nutzen.
* Ein Benutzerkonto auf [GitHub](https://www.github.com) muss verfügbar sein.
* Ein Repository muss auf GitHub konfiguriert sein und die μEdition muss in dieses Repository gepushed werden.

Danach in GitHub in dem Repository in den Bereich {guilabel}`Settings` navigieren und dann zu {guilabel}`Pages`.
Auf der {guilabel}`Pages` Seite muss unter der Überschrift {guilabel}`Build and deployment` die {guilabel}`Source`
Auswahl auf "GitHub Actions" gesetzt sein.

Um die μEdition manuell zu publizieren, in GitHub im Respository auf {guilabel}`Actions` navigieren und dort links den
{guilabel}`Publish the site` Workflow auswählen. Dieser Workflow kann manuell getriggered werden. Dazu auf den
{guilabel}`Run workflow` Knopf klicken und dann auf den grünen {guilabel}`Run workflow` Knopf im Popup klicken.
Dies startet den Publikationsvorgang und wenn der Workflow abgeschlossen ist, can die μEdition unter der URL, die
unter {guilabel}`Settings` > {guilabel}`Pages` angezeigt wird, aufgerufen werden.

Der Workflow ist auch so konfiguriert, dass die μEdition automatisch publiziert wird, sobald eine Änderung im
primären Branch erfolgt.
