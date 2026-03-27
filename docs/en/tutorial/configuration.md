# Die μEdition konfigurieren

Die μEdition hat eine riesige Menge an Konfigurationsoptionen, die wir im Tutorial nicht alle ansehen können. Daher
wird in diesem Schritt nur die Konfigurationsoptionen für das Styling ansehen.

:::{room3b-video} /uedition/tutorial/configuration/de
:::

## Einzelschritte

1. Die Datei {file}`uEdition.yml` öffnen.
2. Folgenden Markdownblock an das Ende der Datei anhängen:

   :::{code-block} yaml
   sphinx_config:
     html_static_path:
       - _static
     html_css_files:
       - styling.css
   :::

3. Die Datei speichern.
4. Den Wurzelordner {file}`/` auswählen.
5. Auf den {guilabel}`Create a new Folder` Button klicken.
6. Als Dateinamen {file}`static` eingeben.
7. Auf den {guilabel}`Create` Button klicken oder die {kbd}`Eingabe` Taste drücken.
8. Den neuen Ordern im Dateibrowser auswählen.
9. Dann auf den {guilabel}`Create a new File` Button klicken.
10. Als Dateinamen {file}`styling.css` eingeben.
11. Dann auf den {guilabel}`Create` Button klicken oder die {kbd}`Eingabe` Taste drücken.
12. Die neue Datei im Dateibrowser auswählen.
13. Folgenden CSS Code eingeben

    :::{code-block} css
    [data-tei-mark-rdg] {
        font-style: italic;
    }
    :::
14. Die Datei speichern.
15. Die μEdition wird neu generiert und auf der Seite wo Sie die TEI Annotationen ausprobiert haben, wird jetzt jeder
    Text der als `rdg` annotiert wurde, in Kursivschrift angezeigt.
