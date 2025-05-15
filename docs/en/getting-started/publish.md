# Publishing the μEdition

When you have your μEdition in a state that you want to publish it, then run the following command to generate the
publishable version:

:::{code-block} console
$ hatch run build
:::

The μEdition will build the site into the configured output folder, which by default is {file}`site`. You can then
copy the content of this folder to your chosen hosting solution.
