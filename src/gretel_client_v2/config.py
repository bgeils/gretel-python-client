import os
from typing import Optional, Type, TypeVar, Union
from pathlib import Path
import json

from gretel_client_v2.rest.configuration import Configuration
from gretel_client_v2.rest.api_client import ApiClient


GRETEL = "gretel"
"""Gretel application name"""

GRETEL_API_KEY = "GRETEL_API_KEY"
"""Env variable to configure Gretel api key."""

GRETEL_ENDPOINT = "GRETEL_ENDPOINT"
"""Env variable name to configure default Gretel endpoint. Defaults
to DEFAULT_GRETEL_ENDPOINT.
"""

GRETEL_CONFIG_FILE = "GRETEL_CONFIG_FILE"
"""Env variable name to override default configuration file location"""

GRETEL_PROJECT = "GRETEL_PROJECT"
"""Env variable name to select default project"""


DEFAULT_GRETEL_ENDPOINT = "https://api-dev.gretel.cloud"
"""Default gretel endpoint. TODO: changeme to prod"""


class GretelClientConfigurationError(Exception):
    ...


T = TypeVar("T")


class _ClientConfig:
    """Holds Gretel client configuration details. This can be instantiated from
    a file or environment.
    """

    endpoint: str
    """Gretel API endpoint."""

    api_key: Optional[str] = None
    """Gretel API key."""

    default_project_name: Optional[str] = None
    """Default Gretel project name."""

    def __init__(
        self,
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        default_project_name: Optional[str] = None,
    ):
        self.endpoint = os.getenv(GRETEL_ENDPOINT) or endpoint or DEFAULT_GRETEL_ENDPOINT
        self.api_key = os.getenv(GRETEL_API_KEY) or api_key
        self.default_project_name = os.getenv(GRETEL_PROJECT) or default_project_name

    @classmethod
    def from_file(cls, file_path: Path) -> "_ClientConfig":
        config = json.loads(file_path.read_bytes())
        return cls.from_dict(config)

    @classmethod
    def from_env(cls) -> "_ClientConfig":
        return cls()

    @classmethod
    def from_dict(cls, source: dict) -> "_ClientConfig":
        return cls(
            **{k: v for k, v in source.items() if k in cls.__annotations__.keys()}
        )

    def get_api_client(self) -> ApiClient:
        configuration = Configuration(
            host=self.endpoint, api_key={"ApiKey": self.api_key}
        )
        return ApiClient(configuration)

    def get_api(self, api_interface: Type[T]) -> T:
        return api_interface(self.get_api_client())

    @property
    def as_dict(self) -> dict:
        return {
            prop: getattr(self, prop)
            for prop in self.__annotations__
            if not prop.startswith("_")
        }

    def __eq__(self, other: "_ClientConfig") -> bool:
        return self.as_dict == other.as_dict

    @property
    def masked(self) -> dict:
        """Returns a masked representation of the config object."""
        c = self.as_dict
        c["api_key"] = "[redacted from output]"
        return c


def _get_config_path() -> Path:
    """Returns the path to the system's Gretel config"""
    from_env = os.getenv(GRETEL_CONFIG_FILE)
    if from_env:
        return Path(from_env)
    return Path().home() / f".{GRETEL}" / "config.json"


def _load_config(config_path: Path = None) -> _ClientConfig:
    """This will load in a Gretel config that can be used for making
    requests to Gretel's API.

    By default this function will look for a config on the local machine. If that
    config doesn't exist, it will fallback to building a config using environment
    variables on the system.

    Args:
        config_path: Path to a local Gretel config. This defaults to
            ``$HOME/.gretel/config.json``.
    """
    if not config_path:
        config_path = _get_config_path()
    if not config_path.exists():
        return _ClientConfig.from_env()
    try:
        return _ClientConfig.from_file(config_path)
    except Exception as ex:
        raise GretelClientConfigurationError(
            f"Could not load config from {config_path}"
        ) from ex


def write_config(config: _ClientConfig, config_path: Union[str, Path] = None) -> Path:
    """Writes a Gretel client config to disk.

    Args:
        config: The client config to write
        config_path: Path to write the config to. If not path is provided, the
            default ``$HOME/.gretel/config.json`` path is used.
    """
    if not config_path:
        config_path = _get_config_path()
    if isinstance(config_path, str):
        config_path = Path(config_path)
    try:
        if not config_path.exists():
            config_path.parent.mkdir(exist_ok=True, parents=True)
            config_path.touch()
        config_path.write_text(json.dumps(config.as_dict, indent=4) + "\n")
        return config_path
    except Exception as ex:
        raise GretelClientConfigurationError(
            f"Could write config to {config_path}"
        ) from ex


_session_client_config = _load_config()  # noqa


def get_session_config() -> _ClientConfig:
    """Return the session's client config"""
    return _session_client_config


def configure_session(config: Union[str, _ClientConfig]):
    """Updates client config for the session

    Args:
        config: The config to update. If the config is a string, this function
            will attempt to parse it as a Gretel URI.
    """
    global _session_client_config
    if isinstance(config, _ClientConfig):
        _session_client_config = config
    if isinstance(config, str):
        raise NotImplementedError("Gretel URIs are not supported yet.")