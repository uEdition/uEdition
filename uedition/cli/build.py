"""Build functionality."""
import subprocess

from os import path
from shutil import rmtree, copytree

from ..settings import settings


def full_build(lang: dict) -> None:
    """Run the full build process for a single language."""
    subprocess.run(['jupyter-book', 'build', '--all', '--path-output', path.join('_build', lang['code']), lang['path']])
    copytree(
        path.join('_build', lang['code'], '_build', 'html'),
        path.join(settings['output'], lang['code']),
        dirs_exist_ok=True
    )


def partial_build(lang: dict) -> None:
    """Run the as-needed build process for a single language."""
    subprocess.run(['jupyter-book', 'build', '--path-output', path.join('_build', lang['code']), lang['path']])
    copytree(
        path.join('_build', lang['code'], '_build', 'html'),
        path.join(settings['output'], lang['code']),
        dirs_exist_ok=True
    )


def run() -> None:
    """Build the full uEdition."""
    if path.exists(settings['output']):
        rmtree(settings['output'])
    for lang in settings['languages']:
        full_build(lang)
