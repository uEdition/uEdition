"""Local server that automatically rebuilds on changes."""
from livereload import Server, shell
from os import path
from rich.progress import track
from shutil import copytree, rmtree
from typing import Callable

from ..settings import settings


def rebuild(lang: dict, full: bool = True) -> Callable[[], None]:
    """Create a function that (re-)builds one of the sub-sites."""
    if full:
        build_cmd = shell(f'jupyter-book build --all --path-output {path.join("_build", lang["code"])} {lang["path"]}')
    else:
        build_cmd = shell(f'jupyter-book build --path-output {path.join("_build", lang["code"])} {lang["path"]}')

    def cmd() -> None:
        build_cmd()
        copytree(
            path.join('_build', lang['code'], '_build', 'html'),
            path.join(settings['output'], lang['code']),
            dirs_exist_ok=True
        )
    return cmd


def run() -> None:
    """Run the development server."""
    if path.exists('_build'):
        rmtree('_build')
    full_rebuilds = [rebuild(lang, full=True) for lang in settings['languages']]
    partial_rebuilds = [rebuild(lang, full=False) for lang in settings['languages']]
    for cmd in track(full_rebuilds, 'Fully re-building the site'):
        cmd()
    server = Server()
    for lang, full_cmd, partial_cmd in zip(settings['languages'], full_rebuilds, partial_rebuilds):
        server.watch(path.join(lang['path'], '*.yml'), full_cmd)
        server.watch(path.join(lang['path'], '**', '*.*'), partial_cmd)
    server.watch('uEdition.*', lambda: [cmd() for cmd in full_rebuilds])
    server.serve(root='site', port=8000)
