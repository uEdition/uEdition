# Configuring the μEdition

The μEdition offers a wide range of configuration options, which we cannot all investigate in this part of the tutorial.
We will thus focus on accessing the configuration for styling options.

:::{room3b-video} /uedition/tutorial/configuration/en
:::

## Individual steps

1. Open the file {file}`uEdition.yml`.
2. Add the following Markdown block to the end of the file:

   :::{code-block} yaml
   sphinx_config:
     html_static_path:
       - _static
     html_css_files:
       - styling.css
   :::

3. Save the file.
4. Select the root folder {file}`/` in the file browser.
5. Click on the {guilabel}`Create a new Folder` button.
6. Enter {file}`static` as the new filename.
7. Click on the {guilabel}`Create` button or press the {kbd}`Enter` key.
8. Select the new folder in the file browser.
9. Click on the {guilabel}`Create a new File` button.
10. Enter {file}`styling.css` as the new filename.
11. Click on the {guilabel}`Create` button or press the {kbd}`Enter` key.
12. Select the new file in the file browser.
13. Add the following CSS code into the file:

    :::{code-block} css
    [data-tei-mark-rdg] {
        font-style: italic;
    }
    :::
14. Save the file
15. The μEdition is regenerated and on the page where you tried out the TEI annotations, you will see that the text that
    was annotated as `rdg`, is now shown in italics.
