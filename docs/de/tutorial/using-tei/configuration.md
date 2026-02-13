# TEI konfigurieren

Im Gegensatz zum Rest der μEdition müssen sowohl die μEdition und der μEditor konfiguriert werden, bevor die TEI
Funktionalität genutzt werden kann.

## Einzelschritte

1. Die {file}`uEdition.yml` Datei öffnen und folgenden Code unter dem `sphinx_config` Schlüssel einfügen:

   :::{code-block} yaml
   tei:
     blocks:
       - name: paragraph
         selector: tei:p
         tag: p
       - name: heading1
         selector: tei:head[@type="level-1"]
         tag: h3
       - name: heading2
         selector: tei:head[@type="level-2"]
         tag: h4
     marks:
       - name: reading
         selector: tei:rdg
         attributes:
           - name: wit
             type: text
     sections:
       - name: metadata
         type: metadata
         selector: /tei:TEI/tei:teiHeader
         fields:
           - title: Author
             type: single
             selector: tei:fileDesc/tei:titleStmt/tei:author/tei:persName/text()
       - name: bodytext
         title: Main text
         type: text
         selector: /tei:TEI/tei:text/tei:body
   :::

   Dies konfiguriert TEI in der μEdition mit drei Blöcken (`blocks`: Absatz, Überschrift Ebene 1, Überschrift Ebene 2)
   und einer Auszeichnung (`marks`: Reading). Die TEI Dateien bestehen dabei aus einem Metadaten Block (`type: metadata`)
   und einem Haupttext Block (`type: text`).

   Wenn der μEditor nicht genutzt wird, dann ist das die einzige Konfiguration, die für die Nutzung von TEI in der
   μEdition notwendig ist.

2. Im Wurzelverzeichnis eine neue Datei {file}`uEditor.yml` erstellen. Diese wird die Konfiguration des μEditors enthalten.
   Folgenden Inhalt in die Datei einfügen:

   :::{code-block} yaml
   ui:
     css_files:
       - static/overrides.css
       - static/editor.css
   tei:
     sections:
       - name: metadaten
         title: Metadaten
         type: metadata
         selector: /tei:TEI/tei:teiHeader
       - name: bodytext
         title: Main text
         type: text
         selector: /tei:TEI/tei:text/tei:body
         sidebar:
           - title: Blöcke
             type: toolbar
             items:
               - type: set-block
                 block: heading1
                 title: Überschrift, Ebene 1
                 icon: M3,4H5V10H9V4H11V18H9V12H5V18H3V4M14,18V16H16V6.31L13.5,7.75V5.44L16,4H18V16H20V18H14Z
               - type: set-block
                 block: heading2
                 title: Überschrift, Ebene 2
                 icon: M3,4H5V10H9V4H11V18H9V12H5V18H3V4M21,18H15A2,2 0 0,1 13,16C13,15.47 13.2,15 13.54,14.64L18.41,9.41C18.78,9.05 19,8.55 19,8A2,2 0 0,0 17,6A2,2 0 0,0 15,8H13A4,4 0 0,1 17,4A4,4 0 0,1 21,8C21,9.1 20.55,10.1 19.83,10.83L15,16H21V18Z
               - type: set-block
                 block: paragraph
                 title: Absatz
                 icon: M4,5H20V7H4V5M4,9H20V11H4V9M4,13H20V15H4V13M4,17H14V19H4V17Z
           - title: Auszeichnungen
             type: toolbar
             items:
               - type: toggle-mark
                 mark: reading
                 title: Reading
                 icon: M9.6,14L12,7.7L14.4,14M11,5L5.5,19H7.7L8.8,16H15L16.1,19H18.3L13,5H11Z
           - title: Quellenkürzel
             type: form
             condition:
               node: reading
             items:
               - type: input-mark-attribute
                 mark: reading
                 name: wit
                 title: Quellenkürzel
   :::

    Der `ui` Schlüssel erlaubt uns zusätzliche CSS Dateien in den μEditor einzubinden.
    Der `tei` Schlüssel enhätlt die TEI Konfiguration. Es werden darin die gleichen Textstrukturen definiert,
    wie in der {file}`uEdition.yml`. Der Zusatz ist, dass im Haupttext der `sidebar` Schlüssel genutzt wird,
    um die Seitenliste mit den Auszeichnungseinstellungen so angezeigt wird, wie für den TEI Text gewünscht.

3. Der letzte Schritt ist, im {file}`static` Dateiordner eine neue Datei {file}`editor.css` anzulegen und dort
   folgenden Inhalt hineinzukopieren:

   :::{code-block} css
   .tiptap p {
     font-size: 1em;
     line-height: 1.15rem;
     margin-bottom: 1.15rem;
   }

   .tiptap h3 {
     font-size: 1.75em;
     line-height: 1.15rem;
     margin: 2.75rem 0 1.05rem;
   }

   .tiptap h4 {
     font-size: 1.5em;
     line-height: 1.15rem;
     margin: 2.75rem 0 1.05rem;
   }
   :::

   Dies kopiert nur den Standardstil für die Überschriften aus der μEdition und ist dazu da, dass der Text im
   μEditor gleich aussieht, wie in der μEdition.
