# Installation

The μEdition is built in Python and supports all Python versions that are currently supported[^python-version]. In
order to use it, please [install an appropriate version of Python for your operating system](https://python.org/downloads).

The μEdition uses [Hatch](https://hatch.pypa.io/latest/install/) to manage the Python packages that build your
μEdition. Please install the latest version for your operating system.

You can test that the installation was successful by running the following command on the commandline[^no-prompt]:

:::{code-block} console
$ python --version
$ hatch
:::

If this shows the installed Python version and a list of commands that hatch provides, then the installation was successful.

In order to work collaboratively and for the GitHub Pages publishing functionality to work, you also need to install the
version control system [Git](https://git-scm.com/downloads). This is optional and not necessary if you are just working
on your own. Providing you with a full intro to using git exceeds the space we have here, but there are many good git
tutorials out there and there is also the [official documentation](https://git-scm.com/doc).

[^python-version]: See here for the current [Python version support status](https://devguide.python.org/versions/)
[^no-prompt]: Do not include the `$` when running the command. The `$` just indicates that the rest of the line is to
  be entered as a command on the commandline.
