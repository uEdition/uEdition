# CLI

## build
The build command is used to build the static html files.

### options
- `fresh_env`: If set to `True`, a fresh environment will be used for the build process. Defaults to `True`.

## serve
The serve command is used to locally build the static html files and serve them using a build in development server.
This is useful for testing and debugging the website locally.

The serve command will always use previously build static html files. If you want a fresh build, use
the build command with the option `--fresh_env=True`.

Do not use this command for production environments.

### options
- `port`: The port to use for the development server. Defaults to `8000`.
- `host`: The host to use for the development server. Defaults to `127.0.0.1`.
