# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Build functionality."""
import json
import subprocess

from os import path, makedirs
from shutil import rmtree, copytree
from yaml import safe_load, safe_dump

from ..settings import settings


def landing_build() -> None:
    """Build the landing page."""
    if not path.exists(settings["output"]):
        makedirs(settings["output"], exist_ok=True)
    with open(path.join(settings["output"], "config.json"), "w") as out_f:
        json.dump(settings, out_f)
    with open(path.join(settings["output"], "index.html"), "w") as out_f:
        out_f.write(
            """\
<!DOCTYPE html>
<html>
  <head>
    <meta name="charset" value="utf-8">
    <title>Redirecting... Please wait...</title>
  </head>
  <body>
    <h1>You are being redirected. Please wait.</h1>
    <p>
      We are checking if there is a site in your preferred language and will redirect you to that, if possible.
      Otherwise we will redirect you to the default language site.
    </p>
    <script>
      async function redirect() {
        const response = await fetch('config.json');
        if (response.status !== 200) {
          return;
        }
        const config = await response.json()
        let found = false;
        for (let code of navigator.languages) {
          if (code.indexOf('-') > 0) {
            code = code.substring(0, code.indexOf('-'));
          }
          for (const configLanguage of config.languages) {
            if (code === configLanguage.code) {
              window.location = window.location.href + configLanguage.path;
              found = true;
              break
            }
          }
          if (found) {
            break
          }
        }
        if (!found) {
          window.location = window.location.href + config.languages[0].path;
        }
      }
      redirect();
    </script>
  </body>
</html>
"""
        )


def toc_build(lang: dict) -> None:
    """Build the language-specific TOC based on the main TOC."""
    with open("toc.yml") as in_f:
        toc = safe_load(in_f)

    def walk(input: dict) -> dict:
        output = {}
        for key, value in input.items():
            if isinstance(value, dict):
                if lang["code"] in value:
                    output[key] = value[lang["code"]]
                elif settings["languages"][0]["code"] in value:
                    output[key] = value[settings["languages"][0]["code"]]
                else:
                    output[key] = ""
            elif isinstance(value, list):
                output[key] = [walk(item) for item in value]
            else:
                output[key] = value
        return output

    with open(path.join(lang["path"], "_toc.yml"), "w") as out_f:
        safe_dump(walk(toc), out_f)


def full_build(lang: dict) -> None:
    """Run the full build process for a single language."""
    landing_build()
    toc_build(lang)
    subprocess.run(
        [
            "jupyter-book",
            "build",
            "--all",
            "--path-output",
            path.join("_build", lang["code"]),
            lang["path"],
        ]
    )
    copytree(
        path.join("_build", lang["code"], "_build", "html"),
        path.join(settings["output"], lang["code"]),
        dirs_exist_ok=True,
    )


def partial_build(lang: dict) -> None:
    """Run the as-needed build process for a single language."""
    landing_build()
    subprocess.run(
        [
            "jupyter-book",
            "build",
            "--path-output",
            path.join("_build", lang["code"]),
            lang["path"],
        ]
    )
    copytree(
        path.join("_build", lang["code"], "_build", "html"),
        path.join(settings["output"], lang["code"]),
        dirs_exist_ok=True,
    )


def run() -> None:
    """Build the full uEdition."""
    if path.exists(settings["output"]):
        rmtree(settings["output"])
    for lang in settings["languages"]:
        full_build(lang)
