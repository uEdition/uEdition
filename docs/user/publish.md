# Publishing the μEdition

When you have your μEdition in a state that you want to publish it, then run the following command to generate the
publishable version:

:::{code-block} console
$ hatch run publish
:::

The μEdition will build the site into the configured output folder, which by default is {file}`site`. You can then
copy the content of this folder to your chosen hosting solution.

## Publishing to GitHub Pages

The μEdition comes with built-in support for publishing your μEdition via [GitHub Pages](https://pages.github.com/).
To do this, you need to have

* The μEdition set up to use git.
* An account on [GitHub](https://www.github.com).
* A repository set up on GitHub and the μEdition pushed to that repository

Then on GitHub in your repository navigate to {guilabel}`Settings` and then {guilabel}`Pages`. On the {guilabel}`Pages`
page ensure that under the {guilabel}`Build and deployment` heading, the {guilabel}`Source` dropdown is set to
"GitHub Actions".

To run the build manually, on GitHub navigate to {guilabel}`Actions` in your repository and then select the
{guilabel}`Publish the site` workflow on the left. This workflow can be triggered manually. Click on the
{guilabel}`Run workflow` button and then on the green {guilabel}`Run workflow` button in the popup. This will start
the build and deployment process and when the workflow is completed, you can access your μEdition at the URL that
is shown at the top of the {guilabel}`Settings` > {guilabel}`Pages` page.

The workflow is also set to automatically rebuild and deploy the μEdition whenever you push a change to the main
branch.
