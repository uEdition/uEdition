# Configuring the μEdition

The μEdition and Jupyter Book are highly configurable and in the μEdition both are configured via the {file}`uEdition.yml`
file in the μEdition root. The block below shows the available configuration options that can be used in that file:

:::{code-block} yaml
author:           # The author information consisting of:
  name:           #   The name to display
  email:          #   The e-mail address to use
jb_config:        # Can contain any valid Jupyter Book configuration settings
languages:        # The languages configured for the μEdition. A list, where each item consists of:
- code:           #   The ISO 639-1 two-letter language code
  label:          #   The label to display for this language
  path:           #   The path that contains the language-specific Jupyter Book
output:           # The output directory for the complete μEdition
repository:       # The repository that contains this μEdition, configured via:
  url:            #   The URL to the repository
  branch:         #   The branch containing the μEdition
title:            # The title of the μEdition in all configured languages. Each configured language code must have a key in this mapping:
  en:             #   Mapping from ISO 639-1 language code to the human-readable title
version: '1'      # The version of the μEdition configuration, which must be set to "1"
:::

All elements of this file are optional and working defaults will be substituted.

All elements of the Jupyter Book can be configured via the `jb_config` settings ([see here for a full list](https://jupyterbook.org/en/stable/customize/config.html)).
These values will be used as they are for all configured language-specific Jupyter Books. The only exception to this is
the `title` configuration setting, for which the μEdition will always use the language-specific value configured in the
{file}`uEdition.yml`.
