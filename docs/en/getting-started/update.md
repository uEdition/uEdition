# Updating the μEdition

Work on the μEdition is ongoing and in order to ensure you benefit from the latest improvements, it is useful to update
the μEdition.

:::{warning}
Before updating the μEdition, make sure that you have a backup of the current state of the μEdition. The update process
is tested extensively, but there is always the possibility of an unknown bug and having a backup ensure you can easily
recover from this.
:::

Updating the μEdition is a two-step process. First run

:::{code-block} console
$ hatch run update
:::

This will update the configured version of the μEdition to the latest release. Then run

:::{code-block} console
$ hatch run migrate
:::

This will install the updated version of the μEdition and also apply any required configuration changes.

You are now ready to continue working with the latest version of the μEdition.
