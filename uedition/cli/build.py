# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""Build functionality."""
import json
import subprocess
from copy import deepcopy
from os import makedirs, path
from shutil import copytree, ignore_patterns, rmtree

from yaml import safe_dump, safe_load

from uedition.settings import reload_settings, settings

LANDING_PAGE_TEMPLATE = """\
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
    <p>
      If you are not automatically redirected, then please use one of the links below to access the site in your
      preferred language:
    </p>
    <ul>
      $LANGUAGE_ITEMS
    </ul>
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


def landing_build() -> None:
    """Build the landing page."""
    if not path.exists(settings["output"]["path"]):
        makedirs(settings["output"]["path"], exist_ok=True)
    with open(path.join(settings["output"]["path"], "config.json"), "w") as out_f:
        json.dump(settings, out_f)
    with open(path.join(settings["output"]["path"], "index.html"), "w") as out_f:
        language_items = (f'<li><a href="{lang["path"]}">{lang["label"]}</a></li>' for lang in settings["languages"])
        out_f.write(LANDING_PAGE_TEMPLATE.replace("$LANGUAGE_ITEMS", "\n".join(language_items)))


def toc_build(lang: dict) -> None:
    """Build the language-specific JupyterBook TOC based on the main TOC."""
    with open("toc.yml") as in_f:
        toc = safe_load(in_f)

    def walk(source: dict) -> dict:
        output = {}
        for key, value in source.items():
            if isinstance(value, dict):
                if lang["code"] in value:
                    output[key] = value[lang["code"]]
                elif len(settings["languages"]) > 0 and settings["languages"][0]["code"] in value:
                    output[key] = value[settings["languages"][0]["code"]]
                else:
                    output[key] = ""
            elif isinstance(value, list):
                output[key] = [walk(item) for item in value]
            else:
                output[key] = value
        return output

    with open(path.join(lang["path"], "_toc.yml"), "w") as out_f:
        safe_dump(walk(toc), out_f, encoding="utf-8")


def config_build(lang: dict) -> None:
    """Build the language-specific JupyterBook config based on the main config."""
    config = deepcopy(settings["jb_config"])
    config["author"] = settings["author"]["name"]
    # Set the language-specific title
    if lang["code"] in settings["title"]:
        config["title"] = settings["title"][lang["code"]]
    elif len(settings["languages"]) > 0 and settings["languages"][0]["code"] in settings["title"]:
        config["title"] = settings["title"][settings["languages"][0]["code"]]
    else:
        config["title"] = f"Missing title for {lang['label']}"
    # Set the repository information
    if settings["repository"]["url"] and "repository" not in config:
        config["repository"] = {
            "url": settings["repository"]["url"],
            "path": lang["path"],
            "branch": settings["repository"]["branch"],
        }
        if "html" not in config:
            config["html"] = {}
        if "use_repository_button" not in config["html"]:
            config["html"]["use_repository_button"] = True
    # Set the Sphinx language
    if "sphinx" not in config:
        config["sphinx"] = {}
    if "config" not in config["sphinx"]:
        config["sphinx"]["config"] = {}
    config["sphinx"]["config"]["language"] = lang["code"]
    # Add the uEdition extension
    if "extra_extensions" not in config["sphinx"]:
        config["sphinx"]["extra_extensions"] = []
    if "uedition" not in config["sphinx"]["extra_extensions"]:
        config["sphinx"]["extra_extensions"].append("uedition")

    with open(path.join(lang["path"], "_config.yml"), "w") as out_f:
        safe_dump(config, out_f, encoding="utf-8")


def static_build(lang: dict) -> None:
    """Copy the static files for a single language."""
    if path.exists("static"):
        copytree("static", path.join(lang["path"], "_static"), dirs_exist_ok=True)


def full_build(lang: dict) -> None:
    """Run the full build process for a single language."""
    reload_settings()
    landing_build()
    toc_build(lang)
    config_build(lang)
    static_build(lang)
    subprocess.run(
        [  # noqa: S603, S607
            "jupyter-book",
            "build",
            "--all",
            "--path-output",
            path.join("_build", lang["path"]),
            lang["path"],
        ],
        check=False,
    )
    if settings["output"]["tei"]:
        subprocess.run(
            [  # noqa: S603, S607
                "jupyter-book",
                "build",
                "--all",
                "--path-output",
                path.join("_build", lang["path"]),
                "--builder",
                "custom",
                "--custom-builder",
                "tei",
                lang["path"],
            ],
            check=False,
        )
    copytree(
        path.join("_build", lang["path"], "_build", "html"),
        path.join(settings["output"]["path"], lang["path"]),
        dirs_exist_ok=True,
    )
    if settings["output"]["tei"]:
        copytree(
            path.join("_build", lang["path"], "_build", "tei"),
            path.join(settings["output"]["path"], lang["path"]),
            ignore=ignore_patterns("_sphinx_design_static"),
            dirs_exist_ok=True,
        )


def partial_build(lang: dict) -> None:
    """Run the as-needed build process for a single language."""
    landing_build()
    subprocess.run(
        [  # noqa: S603, S607
            "jupyter-book",
            "build",
            "--path-output",
            path.join("_build", lang["path"]),
            lang["path"],
        ],
        check=False,
    )
    if settings["output"]["tei"]:
        subprocess.run(
            [  # noqa: S603, S607
                "jupyter-book",
                "build",
                "--path-output",
                path.join("_build", lang["path"]),
                "--builder",
                "custom",
                "--custom-builder",
                "tei",
                lang["path"],
            ],
            check=False,
        )
    copytree(
        path.join("_build", lang["path"], "_build", "html"),
        path.join(settings["output"]["path"], lang["path"]),
        dirs_exist_ok=True,
    )
    if settings["output"]["tei"]:
        copytree(
            path.join("_build", lang["path"], "_build", "tei"),
            path.join(settings["output"]["path"], lang["path"]),
            ignore=ignore_patterns("_sphinx_design_static"),
            dirs_exist_ok=True,
        )


def run() -> None:
    """Build the full uEdition."""
    if path.exists(settings["output"]["path"]):
        rmtree(settings["output"]["path"])
    for lang in settings["languages"]:
        full_build(lang)
