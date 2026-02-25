# Mit GitHub verbinden

Um Git lokal zu nutzen, ist keine Verbindung mit einem remote Gitserver notwendig. Nur wenn das Service zur Veröffentlichung
oder zum kollaborativen Arbeiten notwendig ist, dann muss das gemacht werden.

:::{room3b-video} /uedition/tutorial/git/remote/de
:::

## Einzelschritte

1. In GitHub einloggen und dort ein neues Repository anlegen.
2. In GitHub entweder
   - unter {menuselection}`Settings --> Developer Settings --> Personal access tokens --> Fine-grained tokens`
     einen neuen Token anlegen und für das neue Repository die Berechtigung `Contents` und `Workflows` zuweisen, mit der Option `Read & Write`.
   - unter {menuselection}`Settings --> SSH and GPG keys` einen SSH Key anlegen

3. Im Terminal den μEditor stoppen.
4. Falls ein Token zur Authentifizierung genutzt wird, dann die HTTPS URL auswählen. Die URL wird so aussehen:
   `https://github.com/BENUTZERNAME/REPOSITORY.git`. Die URL modifizieren und den Token einfügen, damit die URL dann
   dem folgenden Muster folgt: `https://BENUTZERNAME:TOKEN@github.com/BENUTZERNAME/REPOSITORY.git`.
5. Falls ein SSH Key für die Authentifizierung genutzt wird, dann einfach die SSH URL auswählen.
6. Folgenden Befehl ausführen, um die lokale μEdition mit dem GitHub Repository verbinden:

   :::{code-block} console
   $ hatch run uEditor git set-remote
   :::

   Dass Nutzerinterface bittet um die gewünschte URL und dort die URL aus Schritt 4 oder 5 eingeben.

7. Den μEditor wieder starten.
8. In GitHub nachsehen, dass der lokale Inhalt der μEdition jetzt auch remote verfügbar ist.
9. Nach der Verbindung mit GitHub müssen alle Merges in GitHub durchgeführt werden.

:::{note}
Nach dem Verbinden mit GitHub ist es nicht mehr möglich Branches lokal in den Defaultbranch zu mergen.
:::
