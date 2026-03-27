# First steps with the μEditor

The μEditor is a web-based editor for the μEdition. You don't have to use the μEditor to create a μEdition, as the
μEdition can be edited using any text editor you wish to use. In this tutorial we will use the μEditor to avoid having
to install any further software.

:::{room3b-video} /uedition/tutorial/ueditor/en
:::

## Individual steps

1. Open a new terminal and run the following command to start the μEditor:

   :::{code} console
   $ hatch run edit
   :::

   The μEditor can then be accessed at http://localhost:8080 using your browser.
2. The μEditor has a menubar at the top, which we will use more extensively later. At the right end of that is the
   {guilabel}`Help` menu, via which you can access the μEditor's documentation and report any issues you may run into.
   On the left side is the file browser, via which all files in the μEdition can be accessed. On the right is the main
   area in which the individual files are edited.
3. Use the file browser to explore the μEdition structure.
4. The file {file}`uEdition.yml` contains configuration settings for the μEdition. Select the file in the file browser
   to open it for editing. Add the following content to the end of the file (using your own name and e-mail address
   of course):

   :::{code-block} yaml
   author:
     name: Your name
     email: Your email address
   :::

5. Save the file by clicking on the Save icon in the toolbar or by pressing {kbd}`Ctrl+s` (Mac: {kbd}`Command+s`).
6. The μEdition will automatically detect the change and re-generate all content. As a change in the confiration causes
   the complete μEdition to be regenerated, this can take a bit.
7. After the HTML version has been regenerated automatically, the browser page will also reload automatically to show
   the latest changes. After that happens, you will see that your name is now visible there. The change was successful.
