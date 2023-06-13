"""Sphinx extensions for the uEdition."""
from sphinx.application import Sphinx

from . import config, tei


def setup(app: Sphinx):
    """Setup the extensions."""
    config.setup(app)
    tei.setup(app)
