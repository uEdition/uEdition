# Adding a new page

The following steps will take you through the process of adding a new page to the μEdition. Later you will repeat these
steps to grow your μEdition.

:::{room3b-video} /uedition/tutorial/new-page/en
:::

## Individual steps

1. In the file browser select the folder in which you want to create the new file.
2. Then click on the {guilabel}`Create a new File` button.
3. Enter the filename for the new file. As the μEdition aims for publication on the web, it is recommended not to use
   spaces or special characters in the filename. The exception to this are `-` and `_`, which are generally used to
   replace spaces. To create a new Markdown file, it must have the {file}`.md` extension.
4. Next click on the {guilabel}`Create` button or press the {kbd}`Enter` key.
5. Select the new file in the file browser.
6. Give the new file a title (in Markdown a first-level heading)

   :::{code-block} markdown
   # About the μEdition
   :::
7. Save the change
8. In the file browser select the {file}`toc.yml` file. Initially the file will have the following content:

   :::{code-block} yaml
   format: jb-book
   root: index
   :::

   The first line defines the format of the file. In this case we have `jb-book`, which defines a structure of
   `Parts` -> `Chapters` -> `Sections`. You can find further documentation for this here:
   [https://sphinx-external-toc.readthedocs.io/en/latest/intro.html](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html).

   The second line defines the filename of the landing page, in this case {file}`index.md`.

   :::{important}
   The {file}`toc.yml` is in the root folder of the μEdition. The {file}`_toc.yml` files in the individual language
   folders will automatically be overwritten with the content of the {file}`toc.yml`, so do not make any changes in
   those files.
   :::
9. To add the new page to the μEdition, the following needs to be added to the {file}`toc.yml`:

   :::{code-block} yaml
   chapters:
     - file: FILENAME
   :::

   You need to replace `FILENAME` with the name of the new file **without the extension**. The path to the file
   is relative to the language folder, not relative to the root folder of the μEdition.
10. Save the file
11. The μEdition is automatically regenerated and the new file will appear in it.

:::{note}
If the new file does not appear, check the terminal for error messages. Generally the most common cause is a typo in
the filenames.
:::
