# Configuring the μEdition

The μEdition is highly configurable via the {file}`uEdition.yml` file in the μEdition's root folder. The block below
shows the available configuration options that can be used in that file:

:::{code-block} yaml
author:           # The author information consisting of:
  name:           #   The name to display
  email:          #   The e-mail address to use
languages:        # The languages configured for the μEdition. A list, where each item consists of:
- code:           #   The ISO 639-1 two-letter language code
  label:          #   The label to display for this language
  path:           #   The path that contains the language-specific Jupyter Book
output:           # The output directory for the complete μEdition
repository:       # The repository that contains this μEdition, configured via:
  url:            #   The URL to the repository
title:            # The title of the μEdition in all configured languages. Each configured language code must have a key in this mapping:
  en:             #   Mapping from ISO 639-1 language code to the human-readable title
version: '2'      # The version of the μEdition configuration, which must be set to "2"
sphinx_config:    # Can contain any valid Sphinx configuration settings
:::

All elements of this file are optional and working defaults will be substituted.

The underlying Spinx document engine can be configured via the `sphinx_config` settings. Any configuration settings set
in the `sphinx_config` element will be used for all languages. The only exception to this is the `title` configuration
setting, for which the μEdition will always use the language-specific value configured under the `title` key.
