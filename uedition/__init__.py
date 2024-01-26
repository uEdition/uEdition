# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The uEdition toolkit."""
from sphinx.application import Sphinx

from uedition import ext


def setup(app: Sphinx) -> None:
    """Set up the theme and its extensions."""
    ext.setup(app)
