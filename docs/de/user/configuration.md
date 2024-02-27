# Die μEdition konfigurieren

Die μEdition und Jupyter Book sind sehr konfigurable. Sowohl die μEdition, wie auch die Jupyter Book Funktionalität
werden über die {file}`uEdition.yml` (im Wurzelverzeichnis der μEdition) konfiguriert. Der folgende Block zeigt alle
verfügbaren Konfigurationsoptionen:

:::{code-block} yaml
author:           # Die Autor:innen:information bestehend aus
  name:           #   Dem Autor:in:namen
  email:          #   Der E-Mailaddresse der/des Autor:in:s
jb_config:        # Enthält alle gültigen Jupyter Book Konfigurationseinträge
languages:        # Die in der μEdition konfigurierten Sprachen. Eine List, in der jeder Eintrag aus folgenden Teilen besteht:
- code:           #   Der ISO 639-1 zweistellige Sprachcode
  label:          #   Der Text der in der Ausgabe für die Sprache angezeigt wird
  path:           #   Der Dateipfad in dem das sprachspezifische Jupyter Book abgelegt ist
output:           # Das Ausgabeverzeichnis für die komplette μEdition
repository:       # Das Git Repository für diese μEdition:
  url:            #   Die URL für das Repository
  branch:         #   Der Repositoryzweig in der μEdition
title:            # Der Titel der μEdition in allen konfigurierten Sprachen. Jede konfigurierte Sprache muss vorkommen.
  en:             #   Abbildung vom ISO 639-1 Sprachcode auf den natürlichsprachlichen Titel
version: '1'      # Die Version der μEdition Konfigurationsdatei. Muss auf "1" gesetzt sein.
:::

Alle Konfigurationselement der Datei sind optional und nicht angegebene Werte werden durch funktionierende Standardwerte
ersetzt.

Alle Element des Jupyter Book können über den `jb_config` Eintrag konfiguriert werden
([eine vollständige Liste findet sich hier](https://jupyterbook.org/en/stable/customize/config.html)).
Die hier angebenen Einstellungen werden für alle sprachspezifischen Jupyter Books genutzt. Die Ausnahme ist die `titel`
Einstellung, für die der Text für die jeweilige Sprache genutzt wird.
