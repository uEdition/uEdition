#!/usr/bin/env python
from livereload import Server, shell

shell("jupyter-book clean .")()
incremental_build = shell("jupyter-book build docs")
full_build = shell("jupyter-book build docs --all")
full_build()

server = Server()
server.watch("docs/**/*.md", incremental_build)
server.watch("docs/**/*.yml", full_build)
server.watch("docs/_static/*.*", full_build)
server.serve(root="docs/_build/html", port=8000)
