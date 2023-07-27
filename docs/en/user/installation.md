# Installation

The μEdition is built on top of a set of other tools and in order to create our first μEdition, it is necessary to first
install these dependencies.

The μEdition is built in Python and supports version 3.10 and 3.11 [^python-version]. In order to use it, please
[install an appropriate version of Python for your operating system](https://python.org/downloads).

For the initial creation of a new μEdition, the μEdition uses a tool called [Copier](https://copier.readthedocs.io/en/stable/).
To install all required μEdition dependencies and to run the various μEdition tools, [Hatch](https://hatch.pypa.io)
is used.

The easiest way to install both Copier and Hatch is via [pipx](https://pypa.github.io/pipx/), which you can
[install from here](https://pypa.github.io/pipx/installation/). When you have pipx installed, then on the commandline
run the following command to install Copier and Hatch:

:::{code} console
$ pipx install copier
$ pipx install hatch
:::

You can test that your installation has been successful by running

:::{code} console
$ copier
$ hatch
:::

If the two commands show you a summary of the available options and commands, then the core tools are installed correctly.

In order to work collaboratively and for the GitHub Pages publishing functionality to work, you also need to install the
version control system [Git](https://git-scm.com/downloads). Providing you with a full intro to using git exceeds the
space we have here, but there are many good git tutorials out there and there is also the
[official documentation](https://git-scm.com/doc).

[^python-version]: The μEdition is tested using Python 3.10 and 3.11. It may also work on newer Python version,
  it just hasn't been tested on those.
