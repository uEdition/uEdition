# Die μEdition konfigurieren

Die μEdition und Sphinx sind sehr konfigurable. Sowohl die μEdition, wie auch die Sphinx Funktionalität
werden über die {file}`uEdition.yml` (im Wurzelverzeichnis der μEdition) konfiguriert. Der folgende Block zeigt alle
verfügbaren Konfigurationsoptionen:

:::{code-block} yaml
author:           # Die Autor:innen:information bestehend aus
  name:           #   Dem Autor:in:namen
  email:          #   Der E-Mailaddresse der/des Autor:in:s
languages:        # Die in der μEdition konfigurierten Sprachen. Eine List, in der jeder Eintrag aus folgenden Teilen besteht:
  - code:         #   Der ISO 639-1 zweistellige Sprachcode
    label:        #   Der Text der in der Ausgabe für die Sprache angezeigt wird
    path:         #   Der Dateipfad in dem das sprachspezifische Jupyter Book abgelegt ist
output:           # Das Ausgabeverzeichnis für die komplette μEdition
repository:       # Das Git Repository für diese μEdition:
  url:            #   Die URL für das Repository
title:            # Der Titel der μEdition in allen konfigurierten Sprachen. Jede konfigurierte Sprache muss vorkommen.
  en:             #   Abbildung vom ISO 639-1 Sprachcode auf den natürlichsprachlichen Titel
version: '2'      # Die Version der μEdition Konfigurationsdatei. Muss auf "2" gesetzt sein.
sphinx_config:    # Enthält alle zusätzlichen Sphinx Konfigurationseinträge
:::

Alle Konfigurationselement der Datei sind optional und nicht angegebene Werte werden durch funktionierende Standardwerte
ersetzt.

Alle Sphinx Einstellungen können über den `sphinx_config` Eintrag konfiguriert werden. Alle Sphinxeinstellungen welche über
den `sphinx_config` Schlüssel konfiguriert werden, werden für alle Sprachen genutzt. Die einzige Ausnahme ist die `title`
Einstellung, für welche die μEdition immer den Titel der spezifischen Sprache nutzt.
