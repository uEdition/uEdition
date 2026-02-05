# Erste Schritte im μEditor

Der μEditor ist ein web-basierter Editor für die μEdition. Der μEditor muss nicht genutzt werden. Die μEdition kann
auch mit einem beliebigen anderen Texteditor bearbeitet werden. Im Tutorial nutzen wir den μEditor, damit keine
weitere Software installiert werden muss.

:::{room3b-video} /uedition/tutorial/ueditor/de
:::

## Einzelschritte

1. Ein neues Terminal öffnen und dann folgenden Befehl im Terminal ausführen, um den μEditor zu starten:

   :::{code} console
   $ hatch run edit
   :::

   Der μEditor kann dann unter http://localhost:8080 im Browser aufgerufen werden.
2. Der μEditor hat am oberen Rand eine Menüzeile, die wir später im Tutorial im Detail nutzen werden, und die am rechten
   Ende das Hilfemenü hat, über die die μEditorhilfe aufgerufen werden kann und auch Fehler gemeldet werden können.
   Links hat der μEditor den Dateibrowser, über den alle Dateien in der μEdition aufgerufen werden können. Rechts, im
   Hauptbereich können die Dateien dann bearbeitet werden.
3. Navigieren sie jetzt ein bischen links im Dateibrowser und erkunden sie die Grundstruktur einer μEdition.
4. Die Datei {file}`uEdition.yml` enthält die Konfigurationseinstellungen für die μEdition. Wählen sie die Datei im
   Dateibrowser aus, damit sie im Editorbereich zum Bearbeiten geöffnet wird. Fügen sie dann am Ende der Datei folgenden
   Block ein (natürlich den eigenen Namen und Emailaddresse nutzen):

   :::{code-block} yaml
   author:
     name: Ihr Name
     email: Ihre Email Addresse
   :::

5. Speichern sie die Datei indem sie auf den Speichern Icon links oben in der Toolbar klicken oder indem sie das
   Tastaturkürzel {kbd}`Strg+s` (Mac: {kbd}`Command+s`) drücken.
6. Die μEdition bemerkt die Änderung automatisch und generiert alle Inhalte neu. Eine Änderung der Konfigurationsdateien
   führt zu einer kompletten Neugenerierung, dies kann ein bischen dauern.
7. Wenn die Inhalte neu generiert wurden, wird die μEdition im Browser automatisch aktualisiert und sie können am unteren
   Rand sehen, dass dort jetzt "Durch Ihr Name" steht. Die Änderung war erfolgreich
