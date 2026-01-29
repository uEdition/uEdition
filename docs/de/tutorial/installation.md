# Installation

Die μEdition ist in der Python Programmiersprache implementiert, und benötigt eine auf ihrem Computer installierte,
aktuelle Python Version um zu funktionieren. Die aktuellste Version für ihr Betriebsystem können sie unter
[https://www.python.org/downloads](https://www.python.org/downloads) finden. Folgen sie den Anweisungen für ihr
Betriebssystem, um Python zu installieren.

Wenn sie Python bereits installiert haben, dann können sie einfach die bereits installierte Version nutzen. Die μEdition
ist mit allen zur Zeit unterstützten Versionen kompatibel[^python-version]. Sie sollte in den meisten Fällen auch mit
älteren Versionen kompatibel sein, aber das kann nicht garantiert werden. Falls ihre Python Version veraltert ist, ist
jetzt ein guter Moment um zu aktualisieren.

Die μEdition nutzt eine Reihe an existierenden Softwarekomponenten. Um die Installation dieser zu vereinfachen, nutzt die
μEdition [Hatch](https://hatch.pypa.io/latest/install/) um die Softwareumgebung zu verwalten. Folgen sie bitte den
Installationsschritten unter [https://hatch.pypa.io/latest/install/](https://hatch.pypa.io/latest/install/), um Hatch
für ihr Betriebssystem zu installieren.

Bevor wir die μEdition erstellen, ist es sinnvoll zuerst zu testen, dass die Softwareinstallationen erfolgreich waren.
Um zu testen, dass Python korrekt installiert ist, öffnen sie ein Terminal und führen sie folgenden Befehl aus[^no-prompt]:

:::{code-block} console
$ python --version
:::

Wenn dies die installierte Python Version ausgibt, dann ist Python korrekt installiert. Als nächstes führen sie folgenden
Befehl aus, um die Hatch Installation zu testen:

:::{code-block} console
$ hatch --version
:::

Wenn dies die Hatch Version ausgibt, dann ist Hatch auch erfolgreich installiert worden.

Falls eine oder beider der Installationen fehlgeschlagen sind, dann konsultieren sie bitte die Dokumentation der jeweiligen
Software. Aufgrund der großen Breite an Systemkonfigurationen können wir keinen nützlichen Support für derartige Probleme
bieten.

[^python-version]: Die aktuell unterstützten Python versionen [finden sie hier](https://devguide.python.org/versions/)
[^no-prompt]: Das `$` Zeichen darf nicht in das Terminal kopiert werden. Das `$` Zeichen ist nur da, um anzuzeigen, dass
  der Rest der Zeile ein Befehl ist, der im Terminal ausgeführt werden muss.
