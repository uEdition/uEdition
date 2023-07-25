# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Sphinx extensions for the uEdition."""
from sphinx.application import Sphinx

from uedition.ext import config, language_switcher, tei


def setup(app: Sphinx) -> None:
    """Run the setup process for the extensions."""
    config.setup(app)
    tei.setup(app)
    language_switcher.setup(app)
