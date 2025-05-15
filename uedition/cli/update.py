# SPDX-FileCopyrightText: 2023-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""The μEdition update functionality."""

from enum import Enum
from os import path

import httpx
import tomlkit
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from rich import print as output

from uedition.cli.base import app
from uedition.settings import NoConfigError


class UpdateVersionOptions(Enum):
    """Option settings for upgrade version selection."""

    RELEASES = "releases"
    PRE_RELEASES = "pre-releases"


@app.command()
def update(allow_versions: UpdateVersionOptions = UpdateVersionOptions.RELEASES.value) -> None:
    """Update the μEdition to the latest version."""
    try:
        if not path.exists("uEdition.yml") and not path.exists("uEdition.yaml") and not path.exists("pyproject.toml"):
            raise NoConfigError()
        with open("pyproject.toml") as in_f:
            pyproject = tomlkit.parse(in_f.read())
        output(":hourglass_flowing_sand: Determining latest version")
        response = httpx.get(
            "https://pypi.org/simple/uedition/", headers={"Accept": "application/vnd.pypi.simple.v1+json"}
        )
        if response.status_code != 200:  # noqa: PLR2004
            output(":cross_mark: Failed to determine the latest version")
            raise Exception("PyPi access error")  # noqa: EM101
        versions = response.json()["versions"]
        versions.reverse()
        target_version = None
        for version in versions:
            if Version(version).is_prerelease and allow_versions == UpdateVersionOptions.PRE_RELEASES:
                target_version = Version(version)
                break
            elif not Version(version).is_prerelease:
                target_version = Version(version)
                break
        if target_version is None:
            raise Exception("No version found to upgrade to")  # noqa: EM101
        target_specifier = SpecifierSet(f">={target_version},<{target_version.major}.{target_version.minor + 1}")
        output(f":hammer: Upgrading to {target_version}")
        if "tool" not in pyproject:
            pyproject["tool"] = tomlkit.table()
        if "hatch" not in pyproject["tool"]:
            pyproject["tool"]["hatch"] = tomlkit.table()
        if "envs" not in pyproject["tool"]["hatch"]:
            pyproject["tool"]["hatch"]["envs"] = tomlkit.table()
        if "default" not in pyproject["tool"]["hatch"]["envs"]:
            pyproject["tool"]["hatch"]["envs"]["default"] = tomlkit.table()
        if "dependencies" not in pyproject["tool"]["hatch"]["envs"]["default"]:
            pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"] = []
        pyproject["tool"]["hatch"]["envs"]["default"]["skip-install"] = True
        # Upgrade the uEdition version
        found_uedition = False
        for idx, dep in enumerate(pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"]):
            dep = dep.lower()  # noqa:PLW2901
            if (
                dep == "uedition"
                or dep.startswith("uedition=")
                or dep.startswith("uedition<")
                or dep.startswith("uedition>")
            ):
                pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"][idx] = f"uedition{target_specifier}"
                found_uedition = True
        if not found_uedition:
            pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"].append(f"uedition{target_specifier}")
        with open("pyproject.toml", "w") as out_f:
            tomlkit.dump(pyproject, out_f)
        output(":checkered_flag: Upgrade complete")
    except Exception as e:
        output(f":cross_mark: Update failed: {e}")
