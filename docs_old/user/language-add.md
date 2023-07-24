# Adding a Language

The μEdition has multi-language support as a core principle. Thus, even if you are planning to release your edition in
a single language only, you need to explicitly configure this one language.

To add a language to your μEdition, run the following command:

:::{code-block} console
$ hatch run uEdition language add FOLDER_NAME
:::

Replace `FOLDER_NAME` with the name of the folder that the μEdition content for that language is to be placed in. The
process will ask you for some detail about the language you are adding and will then create skeleton in the folder,
which is then ready for editing.
