# μEdition

The μEdition is a micro framwork for quickly building Editions.

[![PyPI - Version](https://img.shields.io/pypi/v/uedition.svg)](https://pypi.org/project/uedition)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/uedition.svg)](https://pypi.org/project/uedition)
[![Test workflow status](https://github.com/uEdition/uEdition/actions/workflows/tests.yml/badge.svg)](https://github.com/uEdition/uEdition/actions/workflows/tests.yml)
[![Test coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/scmmmh/13b76c3c8e59fa624d03918fafde3f2d/raw/coverage.json)](https://github.com/uEdition/uEdition/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/uedition/badge/?version=latest)](https://uedition.readthedocs.io/en/latest/?badge=latest)

-----

**Table of Contents**

- [Quickstart](#quickstart)
- [Documentation](#documentation)
- [License](#license)

## Quickstart

To quickly get started with the μEdition follow these steps:

1. Install [Hatch](https://hatch.pypa.io/latest/install/) for your operating system.
2. Create a new folder for your μEdition.
3. Download the default {download}`https://uedition.readthedocs.io/latest/en_static/pyproject.toml` and move that into
   your new folder.
4. Open a new terminal, change into your new folder and run the following command:

   :::{code-block} console
   hatch run init
   :::

   This creates the configuration file ({file}`uEdition.yml`) and table of contents ({file}`toc.yml`).

5. Then run the following command to add content in a new language:

   :::{code-block} console
   hatch run language add
   :::

   This will ask you a few questions about the new language and then create the required files.

5. Then run the following command to start the writing server:

   :::{code-block} console
   hatch run serve
   :::

## Documentation

Full documentation is available at [https://uedition.readthedocs.io](https://uedition.readthedocs.io).

## License

The μEdition is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
