# Installation

Die μEdition baut auf einer Reihe von Werkzeugen auf und um die erste μEdition zu erstellen, müssen diese Werkzeuge
installiert werden.

Die μEdition nutzt Python und unterstützt Versionen 3.10 und 3.11 [^python-version]. Bitte
[installieren sie die Python Version für ihr Betriebssystem](https://python.org/downloads).

Für die Erstellung einer μEdition wird ein Werkzeug namens [Copier](https://copier.readthedocs.io/en/stable/) genutzt.
Für die Installation aller weiteren Abhängigkeiten und um die verschiedenen μEdition Funktionen aufzurufen wird
[Hatch](https://hatch.pypa.io) genutzt.

Die einfachste Weise um beide zu installieren ist mittels [pipx](https://pypa.github.io/pipx/), welches
[von hier installiert werden kann](https://pypa.github.io/pipx/installation/). Nach der pipx installation nutzen sie
die folgenden zwei Befehle um Copier und Hatch zu installieren:

:::{code} console
$ pipx install copier
$ pipx install hatch
:::

Um zu überprüfen, dass die Installationen erfolgreich waren, nutzen sie die folgenden Befehle:

:::{code} console
$ copier
$ hatch
:::

Wenn beide Befehle eine Zusammenfassung der verfügbaren Optionen und Befehle für die zwei Werkzeuge anzeigen, dann
sind beide Werkzeuge korrekt installiert.

Um im Team zusammenzuarbeiten und für die GitHub Pages Veröffentlichungsfunktionalität, muss auch das Versionskontrollwerkzeug
[Git](https://git-scm.com/downloads) installiert sein. Eine vollständige Einführung in Git übersteigt den Platz hier,
aber es gibt viele gute Tutorials im Netz und die [offizielle Dokumentation](https://git-scm.com/doc) ist auch hilfreich.

[^python-version]: The μEdition wird mit Python 3.10 and 3.11 getested. Die μEdition funktioniert möglicherweise auch mit
  neueren Python Versionen, ist aber auf diesen noch nicht getestet worden.
