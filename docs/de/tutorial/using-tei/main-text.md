# Haupttext bearbeiten

## Einzelschritte

1. Im TEI Editor den {guilabel}`Main text` Reiter auswählen.
2. In den Bereich unter dem Reiter klicken.
3. Gewünschten Text eingeben.
4. Rechts, über die Auszeichnungsmöglichkeiten den Text auszeichnen.
5. Auf den Speichern Icon klicken oder die Tastenkombination {kbd}`Strg+s` (Mac: {kbd:`Command+s`}) drücken.
6. Die Datei {file}`static/styling.css` öffnen und bearbeiten, damit sie wie folgt aussieht:

    :::{code-block} css
    [data-tei-mark-rdg], [data-tei-mark-reading] {
        font-style: italic;
    }
    :::
