# Publishing the μEdition

Publishing the μEdition is the last core step in this tutorial. The two other aspects of using Git and TEI are
optional and are not needed for the core usage of the μEdition.

:::{room3b-video} /uedition/tutorial/publishing/en
:::

## Individual steps

1. In the terminal where you are running the μEdition server, press {kbd}`Ctrl+c` to stop the server.
2. Then run the following command to generate the μEdition for publication:

   :::{code-block} console
   $ hatch run build
   :::

3. In the file explorer of your operating system (not in the μEditor) go to the folder with your μEdition and
   there you will find a folder {file}`site`. This contains the generated μEdition. The files in this folder
   can now be uploaded to any web-hosting platform in order to publish the μEdition.
4. You can try opening the {file}`index.html` in the {file}`site/en` folder directly in the browser, in order
   to see that it has generated correctly.
