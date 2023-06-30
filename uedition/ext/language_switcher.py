# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The Language Switcher extension."""
import json

from importlib.resources import files, as_file
from os import path
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file

from ..settings import settings


def add_language_switcher(app: Sphinx) -> None:
    """Add the language switcher in-line and file JavaScript."""
    app.add_js_file(
        None, body=f"""DOCUMENTATION_OPTIONS.UEDITION = {json.dumps(settings)}"""
    )
    app.add_js_file("language_switcher.js")


def copy_custom_files(app: Sphinx, exc: bool) -> None:
    """Copy the language_switcher.js file from the package."""
    if app.builder.format == "html" and not exc:
        staticdir = path.join(app.builder.outdir, "_static")
        ext_pkg = files("uedition.ext")
        with as_file(ext_pkg / "language_switcher.js") as js_file:
            copy_asset_file(str(js_file), staticdir)


def setup(app: Sphinx) -> None:
    """Set up the Language switcher extension."""
    app.connect("builder-inited", add_language_switcher)
    app.connect("build-finished", copy_custom_files)
