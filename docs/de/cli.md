# CLI

## build
Dieser Befehl baut die statischen HTML-Dateien.

### options
- `fresh_env`: Wenn `True` wird eine neue Umgebung für den Buildvorgang verwendet. Default ist `True`.

## serve
Der serve Befehl baut die statischen HTML-Dateien und stellt diese über einen development Server bereit.
Dies ist nützlich für das Testen und Debuggen der Website.

Der serve Befehl wird immer bereits gebaute statischen HTML-Dateien verwenden. Um einen frischen Build zu
erzeugen kann der Befehl build mit der Options `--fresh_env=True`verwendet werden.

Der development Server ist nicht für den produktiven Einsatz geeignet.

### options
- `port`: Der Port für den Server. Default ist `8000`.
- `host`: Die Host IP auf der der Server läuft. Default ist `127.0.0.1`.
