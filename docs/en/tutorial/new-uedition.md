# Creating a μEdition

Now that the fundamental components are installed, the following video covers the steps for creating a new μEdition:

:::{room3b-video} /uedition/tutorial/installation/en
:::

# Individual steps

1. Download the {download}`../_static/pyproject.toml` file.
2. Create a new folder for the new μEdition.
3. Move the downloaded {file}`pyproject.toml` file into the new folder.
4. Create a terminal in the new folder.
5. Run the following command to initialise the new μEdition:

   :::{code-block} console
   $ hatch run init
   :::

   Depending on circumstances this can take a few minutes.

6. Run the following command to add a language to the μEdition (every μEdition requires at least one language):

   :::{code-block} console
   $ hatch run language add
   :::

   Running the command will ask you for three pieces of information:
   - **Language code**: ISO language code for the language. This will be used for the folder name containing the
     language-specific μEdition content.
   - **Language name**: The name of the new language. This is used for the language-witching functionality of the μEdition.
   - **Title**: The title of the μEdition in the new language.

7. Run the following command to build the HTML version of the μEdition:

   :::{code-block} console
   $ hatch run serve
   :::

   This starts a small, local webserver and the HTML version of the μEdition can then be accessed via the following
   URL: [http://localhost:8000](http://localhost:8000). The start can take a few seconds. Please be patient :-).

After the last step you should be able to see the μEdition in the browser. If that works, then you are ready for the
next steps. If the μEdition does not load in the browser, then there will be an error message shown in the terminal.
Fix this and then the μEdition will load.

:::{note}
To stop the webserver, switch into the terminal and press {kdb}`Ctrl+c`.

Before continuing with the μEdition, you will then have to restart the webserver by running `hatch run serve` again.
:::
