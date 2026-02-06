# Git initialisieren

# Einzelschritte

1. Im μEditor im Wurzelverzeichnis eine neue Datei mit dem Namen {file}`.env` erstellen.
2. Folgenden Inhalt in die neue Datei hineingeben:

   :::{code-block} text
   UEDITOR__AUTH__PROVIDER=email
   UEDITOR__AUTH__NAME=NAME
   UEDITOR__AUTH__EMAIL=E-MAIL ADDRESSE
   UEDITOR__GIT__DEFAULT_BRANCH=main
   :::

   Dabei `NAME` und ``E-MAIL ADDRESSE` durch den eigenen Namen und E-Mail Addresse ersetzen.
3. Im Terminal in dem Sie `hatch run edit` ausgeführt haben, den μEditor mittels der Tastenkombination {kbd}`Str+c`
   stoppen.
4. Folgenden Befehl ausführen, um das Git Repository zu initialisieren:

   :::{code-block} console
   $ hatch run uEditor git init
   :::

5. Den μEditor mit dem Befehl `hatch run edit` wieder starten.
