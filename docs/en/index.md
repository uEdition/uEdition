# μEdition

The process of creating and making available a (critical) digital edition often presents projects with a range of significant
hurdles, particularly around technical knowledge and hosting costs. The μEdition is a framwork that lowers these barriers by
providing a simple tool that supports users in easily building (multi-lingual) digital editions that can then easily be made
available online using free or low-cost hosting solutions.

:::{admonition} Getting Help
:class: tip

The μEdition is still a young project and relies on your feedback to further lower the barriers to its use. Whether this is
adding documentation on how to do things, fixing broken things, or adding extra features, please let us know what is needed
and then we can make it better.

If you have any questions about anything related to the μEdition, please use our GitHub Discussions forum to ask:
[https://github.com/uEdition/uEdition/discussions](https://github.com/uEdition/uEdition/discussions).

If you run into any bugs, then please report these via the GitHub Issues and we can get them fixed:
[https://github.com/uEdition/uEdition/issues](https://github.com/uEdition/uEdition/issues).
:::

## Contents

:::{tableofcontents}
:::

## Quickstart

To quickly get started with the μEdition, follow these steps (assuming you already have Python 3.10 or newer and pipx installed):

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

Your new digital edition will be available at http://localhost:8000.
