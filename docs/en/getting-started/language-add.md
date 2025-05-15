# Adding a Language

The μEdition has multi-language support as a core principle. Thus, even if you are planning to release your edition in
a single language only, you need to explicitly configure this one language.

To add a language to your μEdition, run the following command:

:::{code-block} console
$ hatch run language add
:::

The process will ask you for some detail about the language you are adding and will then create a new folder with the
language's code and creat the basic files there, ready for editing.
