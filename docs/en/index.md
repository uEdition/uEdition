# μEdition

The process of creating and making available a (critical) digital edition often presents projects with a range of significant
hurdles, particularly around technical knowledge and hosting costs. The μEdition is a framwork that lowers these barriers by
providing a simple tool that supports users in easily building (multi-lingual) digital editions that can then easily be made
available online using free or low-cost hosting solutions.

## Contents

:::{tableofcontents}
:::

## Quickstart

To quickly get started with the μEdition, follow these steps (assuming you already have Python 3.10 or newer installed):

:::{code} console
$ pipx install hatch copier
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

Copying from template version 0.1.0
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
$ hatch run uEdition language add cy
🎤 What is the language code?
   cy
🎤 What is the name of the language?
   Cymraeg
$ hatch run serve
:::

Your new digital edition will be available at http://localhost:8000.
