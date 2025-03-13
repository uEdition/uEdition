# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""
uEdition configuration handling.

This module handles reading the uEdition-specific configuration settings, validating them and
adding any required default values.
"""

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging

from uedition.ext.settings import TEISettings

logger = logging.getLogger(__name__)


def validate_config(app: Sphinx, config: Config) -> None:  # noqa: ARG001
    """Validate the configuration and add any default values."""
    if config.tei:
        config.tei = TEISettings(**config.tei).model_dump()
    else:
        config.tei = {"blocks": [], "marks": "", "sections": []}


def setup(app: Sphinx) -> None:
    """Set up the Sphinx configuration handling for the uEdition."""
    app.add_config_value("tei", default=None, rebuild="html", types=[dict])
    app.connect("config-inited", validate_config)
