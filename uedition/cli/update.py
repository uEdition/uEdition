# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition check functionality for validating a μEdition and its files."""
from os import path

from copier import run_update

from uedition.settings import NoConfigError


def run() -> None:
    """Update the μEdition using Copier."""
    if not path.exists("uEdition.yml") and not path.exists("uEdition.yaml"):
        raise NoConfigError()
    run_update(".", answers_file=".uEdition.answers", overwrite=True, skip_answered=True)
