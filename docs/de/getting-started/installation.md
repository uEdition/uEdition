# Installation

Die μEdition nutzt Python und unterstützt alle aktuell unterstützten Versionen[^python-version]. Bitte
[installieren sie die Python Version für ihr Betriebssystem](https://python.org/downloads).

Die μEdition nutzt [Hatch](https://hatch.pypa.io) um die Python Packete der μEdition zu verwalten. Bitte installieren
sie die aktuellste Version für ihr Betriebssystem.

Um zu Testen ob Python und Hatch korrekt installiert wurden, führen sie die folgenden zwei Befehle auf der Kommandozeile
aus[^kein-prompt]:

:::{code} console
$ python --version
$ hatch
:::

Wenn dies die aktuell installierte Python Version und eine Liste von Hatch Befehlen anzeigt, dann war die Installation
erfolgreich.

Um im Team zusammenzuarbeiten und für die GitHub Pages Veröffentlichungsfunktionalität, muss auch das Versionskontrollwerkzeug
[Git](https://git-scm.com/downloads) installiert sein. Eine vollständige Einführung in Git übersteigt den Platz hier,
aber es gibt viele gute Tutorials im Netz und die [offizielle Dokumentation](https://git-scm.com/doc) ist auch hilfreich.

[^python-version]: Hier finden sie die [aktuell unterstützten Python Versionen](https://devguide.python.org/versions/)
[^kein-prompt]: Das `$` Zeichen darf nicht eingegeben werden, wenn der Befehl ausgeführt wird. Das `$` wird nur genutzt um
  hier anzuzeigen, dass es sich um ein Befehl und nicht um ein Programmergebnis handelt.
