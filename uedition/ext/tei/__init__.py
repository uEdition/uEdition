"""TEI extension for Sphinx."""

from importlib.resources import as_file, files
from os import path

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file

from uedition.ext.tei import parser
from uedition.settings import settings


def add_language_switcher(app: Sphinx) -> None:
    """Add the language switcher in-line and file JavaScript."""
    app.add_js_file("tei_download.js")


def copy_custom_files(app: Sphinx, exc: bool) -> None:  # noqa: FBT001
    """Copy the language_switcher.js file from the package."""
    if app.builder.format == "html" and not exc:
        staticdir = path.join(app.builder.outdir, "_static")
        ext_pkg = files("uedition.ext.tei")
        with as_file(ext_pkg / "tei_download.js") as js_file:
            copy_asset_file(str(js_file), staticdir)


def setup(app: Sphinx) -> None:
    """Set up the TEI Sphinx extension."""
    parser.setup(app)
    if settings["output"]["tei"]:
        app.connect("builder-inited", add_language_switcher)
        app.connect("build-finished", copy_custom_files)
