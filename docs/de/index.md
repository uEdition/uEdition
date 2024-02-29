# μEdition

Das Erstellen einer kritischen, digitalen Edition bringt mit sich eine Reihe signifikanter Hürden, besonders wenn es um
die technischen Anforderungen und Hostingkosten geht. Die μEdition bietet ein Gerüst um diese Hürden zu reduzieren, indem
es ein einfaches Werkzeug anbietet, welches Projekte darin unterstützt einfach (multilinguale) digitale Editionen zu
erstellen, welche dann über gratis oder billige Hostinglösungen online verfügbar gemacht werden können.

:::{admonition} Hilfe und Unterstützung
:class: tip

Die μEdition ist noch ein junges Projekt und benötigt Feedback von Nutzern und Nutzerinnen um die Hürden zur Nutzung
weiter zu reduzieren. Egal ob dies zusätzliche Dokumentation ist, Fehler beheben, oder zusätzliche Funktionalität,
bitte informiert uns und dann können wir die μEdition besser machen.

Für alle Fragen zur μEdition und zu ihrer Nutzung, nutzt bitte unser GitHub Discussions Forum:
https://github.com/uEdition/uEdition/discussions.

Wenn Fehler auftreten, dann bitte diese über unsere GitHub Issues melden und dann können wir sie reparieren:
https://github.com/uEdition/uEdition/issues.
:::

## Inhaltsverzeichnis

:::{tableofcontents}
:::

## Schnellstart

Für einen Schnellstart mit der μEdition, folgens sie diesen Schritten (Python 3.10 oder neuer und pipx müssen bereits installiert sein):

:::{code} console
$ pipx install hatch
$ pipx install copier
$ copier copy https://github.com/uEdition/uEdition-project-template my-edition
🎤 What is the name of your μEdition?
   My Edition
🎤 What is the μEdition author's name?
   A.N. Editor
🎤 What is the μEdition author's address?
   a.n.editor@example.com
🎤 Do you wish to automatically publish your μEdition?
   (Use arrow keys)
 » Disable automatic publishing
   Via GitHub Pages
   Via Read the Docs
🎤 What is the URL of the repository containing your μEdition?
   https://github.com/aneditor/my-edition
🎤 What is the repository branch containing your μEdition?
   main

Copying from template version 0.6.1
    create  .
    create  toc.yml
    create  uEdition.yml
    create  .uEdition.answers
    create  .github
    create  .github/workflows
    create  .github/workflows/pages.yml
    create  .gitignore
    create  pyproject.toml
$ cd my-edition
$ hatch run add-language cy
🎤 What is the language code?
   cy
🎤 What is the name of the language?
   Cymraeg
$ hatch run serve
:::

Die neue, digitale Edition ist dann unter http://localhost:8000 verfügbar.
