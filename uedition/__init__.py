# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The uEdition toolkit."""

from sphinx.application import Sphinx

from uedition import ext


def setup(app: Sphinx) -> None:
    """Set up the theme and its extensions."""
    for dependency in ("myst_parser", "sphinx_external_toc"):
        app.setup_extension(dependency)
    ext.setup(app)
