# Writing Content

The μEdition uses [Sphinx](https://www.sphinx-doc.org) as its underlying technology for turning your text into a
publishable website. Each language in the μEdition is a separate Sphinx document and the μEdition provides the glue that
merges the individual outputs together into a single site. It also automatically loads and configures
[MyST](https://myst-parser.readthedocs.io/en/latest/) to allow you to write content in Markdown.

## Structuring the μEdition

The structure of the μEdition is defined via its table of contents, which is configured in the {file}`toc.yml` file
in the μEdition root folder. The {file}`toc.yml` file uses the same format as
[defined by the Jupyter Book project](https://jupyterbook.org/en/stable/structure/toc.html) and the initial
{file}`toc.yml` looks like this:

:::{code-block} yaml
format: jb-book
root: index
:::

The important part here is the `root: index` setting, which says that any file called {file}`index` will be used
as the starting page for the output. If you look in the folder of your first language, you will see that it contains
a {file}`index.md` file and it is the contents of this file that will be the first page of your μEdition.

To add pages to your μEdition, you need to organise the content into chapters. For example, to add two chapters
"guidelines" and "contact", update the {file}`toc.yml` to look like this:

:::{code-block} yaml
format: jb-book
root: index
chapters:
  - file: guidelines
  - file: contact
:::

Then create the two files {file}`guidelines.md` and {file}`contact.md` in the language folder and add some content
into them. Make sure that the filename you provide for the `file:` entry is the relative path from the language
folder to the file.

Read the [Jupyter Book TOC documentation](https://jupyterbook.org/en/stable/structure/toc.html) for details on how
to create more complex structures.

By default each TOC entry's title is the title in the document. However, this can be overriden by providing a `caption`
or `title`. The μEdition extends this format by allowing you to provide separate titles for each language:

:::{code-block} yaml
format: jb-book
root: index
parts:
  - caption:
      en: Name of Part 1
      de: Name von Teil 1
    chapters:
    - title:
        en: Chapter 1
        de: Chapter 2
      file: path/to/part1/chapter1
    - file: path/to/part1/chapter2
:::

## Writing text content

Markedly Structured Text is the primary format for writing text content. A good overview over the core functionality can be found
[here](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html) and extensions defined by the JupyterBook,
which are [documented here](https://jupyterbook.org/en/stable/content/index.html) are available and include useful things like
glossaries, indices, citations, footnotes, plus elements for structuring the layout of the page and its content.

## Local server

While writing it can be helpful to see what the result will look like. To simplify this, the μEdition provides a built-in
web-server that automatically re-generates your μEdition when you edit the content. To start this server, run the
following command:

:::{code-block} console
$ hatch run serve
:::

This will build your μEdition and then make it available at http://localhost:8000. When you make changes to the content,
the μEdition will automatically re-build your μEdition and automatically reload the view in the browser.
