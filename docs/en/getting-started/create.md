# Creating a μEdition

With all the pre-requisites installed correctly, you are now ready to create your μEdition. Create a new folder
that will contain your μEdition. Then download the {download}`../_static/pyproject.toml` and save it into the
folder you just created.

On the commandline navigate to the folder where you saved the {file}`pyproject.toml` and run the following
command:

:::{code-block} console
$ hatch run init
:::

This will create a virtual python installation with all the software needed by the μEdition and run the initialisation
step, which will create the {file}`uEdition.yml` file, which contains the configuration settings, and the {file}`toc.yml`,
which contains the table of contents.

The next step is to add a language to your μEdition, so that you can start creating some content.
