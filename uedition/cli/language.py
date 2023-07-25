# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition language functionality for managing languages used in the μEdition."""
import os

from copier import run_copy, run_update
from yaml import dump, safe_load


def add(path: str) -> None:
    """Add a language to the μEdition using Copier."""
    run_copy("gh:uEdition/uEdition-language-template", path, data={"path": path})
    with open(os.path.join(path, ".uEdition.answers")) as in_f:
        answers = safe_load(in_f)
    with open("uEdition.yml") as in_f:
        config = safe_load(in_f)
    found = False
    if "languages" in config:
        for lang in config["languages"]:
            if lang["code"] == answers["code"]:
                lang["label"] = answers["label"]
                lang["path"] = path
                found = True
    else:
        config["languages"] = []
    if not found:
        config["languages"].append({"code": answers["code"], "label": answers["label"], "path": path})
    with open("uEdition.yml", "w") as out_f:
        dump(config, out_f)


def update(path: str) -> None:
    """Update a language to the latest template."""
    run_update(path, answers_file=".uEdition.answers", overwrite=True, data={"path": path})
    with open(os.path.join(path, ".uEdition.answers")) as in_f:
        answers = safe_load(in_f)
    with open("uEdition.yml") as in_f:
        config = safe_load(in_f)
    found = False
    if "languages" in config:
        for lang in config["languages"]:
            if lang["code"] == answers["code"]:
                lang["label"] = answers["label"]
                lang["path"] = path
                found = True
    else:
        config["languages"] = []
    if not found:
        config["languages"].append({"code": answers["code"], "label": answers["label"], "path": path})
    with open("uEdition.yml", "w") as out_f:
        dump(config, out_f)
