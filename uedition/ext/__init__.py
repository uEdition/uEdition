"""Sphinx extensions for the uEdition."""
from sphinx.application import Sphinx

from . import config, tei, language_switcher


def setup(app: Sphinx) -> None:
    """Run the setup process for the extensions."""
    config.setup(app)
    tei.setup(app)
    language_switcher.setup(app)
