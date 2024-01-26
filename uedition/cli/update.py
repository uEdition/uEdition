# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition check functionality for validating a μEdition and its files."""
from copier import run_update


def run() -> None:
    """Update the μEdition using Copier."""
    run_update(".", answers_file=".uEdition.answers", overwrite=True, skip_answered=True)
