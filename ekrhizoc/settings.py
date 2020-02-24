import sys
from os import getenv
from pathlib import Path
from typing import Any, Set


class EkrhizocSetting:
    def __init__(
        self,
        field: str,
        datatype: type,
        default_value: Any,
        env_var_alias: str = None,
        description: str = None,
    ):
        self.field = field
        self.datatype = datatype
        self.default_value = default_value
        self.env_var_alias = env_var_alias
        self.description = description
        self._name = "_".join(("E6C", self.field.upper()))

    def __invert__(self):
        """
        Access the setting value by using the invert ~
        e.g. ~EkrhizocSetting == EkrhizocSetting.value
        """
        return self.value

    @property
    def name(self):
        return self._name

    @property
    def env_var(self):
        return getenv(
            self._name,
            getenv(self.env_var_alias, None) if self.env_var_alias else None,
        )

    @property
    def value(self):
        if self.env_var:
            return self.datatype(self.env_var)
        return self.default_value


LOG_LEVEL = EkrhizocSetting(
    field="log_level",
    datatype=str,
    default_value="INFO",
    description="Level of logging",
)

LOG_DIR = EkrhizocSetting(
    field="log_dir",
    datatype=str,
    default_value="",
    description="Directory to save logs",
)

BIN_DIR = EkrhizocSetting(
    field="bin_dir",
    datatype=str,
    default_value="bin",
    description="Directory to save any output (bin)",
)

IGNORE_FILETYPES = EkrhizocSetting(
    field="ignore_filetypes",
    datatype=str,
    default_value=".png,.pdf,.txt,.doc,.jpg,.gif",
    description='File types of websites to ignore (e.g. ".filetype1,.filetype2")',
)

URL_REQUEST_TIMER = EkrhizocSetting(
    field="url_request_timer",
    datatype=float,
    default_value=0.1,
    description="Time to wait per request (not to populate server with multiple requests)",
)

MAX_URLS = EkrhizocSetting(
    field="max_urls",
    datatype=int,
    default_value=10000,
    description="The maximum number of urls to fetch/crawl",
)

MAX_URL_LENGTH = EkrhizocSetting(
    field="max_url_length",
    datatype=int,
    default_value=300,
    description="The maximum length (character count) of a url to fetch/crawl",
)
