# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The uEdition check functionality for validating a uEdition and its files."""
from copier import run_update


def run() -> None:
    """Update the μEdition using Copier."""
    run_update(".", overwrite=True)
