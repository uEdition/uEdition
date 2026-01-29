# Installation

Die μEdition ist in der Python Programmiersprache implementiert, und benötigt eine auf ihrem Computer installierte,
aktuelle Python Version. Die aktuellste Version führ ihr Betriebsystem können sie unter
[https://www.python.org/downloads](https://www.python.org/downloads) finden. Folgen sie den Anweisungen für ihr
Betriebssystem, um Python zu installieren.

If you already have a version of Python installed on your system, then you can just use that. The μEdition supports all
versions of Python that are currently supported[^python-version]. It is likely that it will also work on older versions,
but this cannot be guaranteed, so if you have a Python version that is out of date, now is a good time to update that.

The μEdition uses a number of existing libraries to provide you with the full functionality. To simplify the process of
installing these dependencies, the μEdition uses [Hatch](https://hatch.pypa.io/latest/install/) to manage the environment
that the μEdition is installed into. Follow the instructions on [https://hatch.pypa.io/latest/install/](https://hatch.pypa.io/latest/install/)
to install Hatch for your operating system.

Before we move on to actually creating your μEdition, it is a good idea to test that the installations were successful.
To test that Python is correctly installed, open a terminal and then run the following command[^no-prompt]:

:::{code-block} console
$ python --version
:::

If this shows the installed Python version, then the Python installation was successful. Next, run the following command
to test that Hatch was correctly installed:

:::{code-block} console
$ hatch --version
:::

If this outputs a list of commands that Hatch provides, then Hatch has also been successfully installed.

If either of the two installations did not work correctly, then please check the respective software's documentation and
support forum. Unfortunately the variety of systems out there means that we cannot provide useful support for these issues.

[^python-version]: See here for the current [Python version support status](https://devguide.python.org/versions/)
[^no-prompt]: Do not include the `$` when running the command. The `$` just indicates that the rest of the line is to
  be entered as a command on the commandline.
