"""
MkDocs Plugin.

https://www.mkdocs.org/
https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/
"""
# standard lib
import logging
import re
import os
import time

# 3rd party
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Page
from mkdocs.exceptions import PluginError

from src.exclude import exclude

from typing import Any, Dict
from collections import OrderedDict

class RequiredFrontmatterPlugin(BasePlugin):
    """
    Mkdocs plugin to require certain frontmatter for documents.

    See https://www.mkdocs.org/user-guide/plugins
    """

    config_scheme = (
        ("required_keys", config_options.Type(list, default=[])),
        ("exclude", config_options.Type(list, default=[])),
        ("enabled", config_options.Type(bool, default=True)),
        ("strict", config_options.Type(bool, default=True)),
    )

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        """
        Determine configuration options.

        The config event is the first event called on build and
        is run immediately after the user configuration is loaded and validated.
        Any alterations to the config should be made here.
        https://www.mkdocs.org/user-guide/plugins/#on_config

        Args:
            config (dict): global configuration object

        Returns:
            dict: global configuration object
        """
        if not self.config.get('enabled'):
            return config
        
        return config

    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        """
        Check if tags in page.meta are included when required by the plugin's configuration.

        The page_markdown event is called after the page's markdown is loaded
        from file and can be used to alter the Markdown source text.
        The meta- data has been stripped off and is available as page.meta
        at this point.

        https://www.mkdocs.org/user-guide/plugins/#on_page_markdown

        Args:
            markdown (str): Markdown source text of page as string
            page: mkdocs.nav.Page instance
            config: global configuration object
            site_navigation: global navigation object

        Returns:
            str: Markdown source text of page as string
        """
        if not self.config.get('enabled'):
            return markdown
        
        # Exclude pages specified in config
        excluded_pages = self.config.get("exclude", [])
        if exclude(page.file.src_path, excluded_pages):
            logging.debug("Excluding page " + page.file.src_path)
            return markdown
        
        for key in self.config.get('required_keys'):
            if key not in page.meta:
                if self.config.get('strict'):
                    raise PluginError(f"The required tag '{key}' is missing on the page.")
                else:
                    logging.warn(f"The required tag '{key}' is missing on the page at {page.file.src_path}.")

        return markdown