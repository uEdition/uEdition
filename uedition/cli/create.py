# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The uEdition check functionality for validating a uEdition and its files."""
from copier import run_copy


def run(path: str) -> None:
    """Create a new μEdition using Copier."""
    run_copy("gh:uEdition/uEdition-project-template", path)
