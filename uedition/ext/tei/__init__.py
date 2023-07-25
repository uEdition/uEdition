"""TEI extension for Sphinx."""
from sphinx.application import Sphinx

from uedition.ext.tei import parser


def setup(app: Sphinx) -> None:
    """Set up the TEI Sphinx extension."""
    parser.setup(app)
