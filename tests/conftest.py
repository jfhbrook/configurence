# -*- coding: utf-8 -*-

from typing import Any, Optional

try:
    from typing import Self
except ImportError:
    Self = Any

import pytest

from configurence import BaseConfig
from configurence import config as config_
from configurence import field


class Other:
    def __init__(self: Self, name: str) -> None:
        self.name = name

    def __eq__(self: Self, other: Any) -> bool:
        return isinstance(other, Other) and self.name == other.name


def convert_other(value: str) -> Other:
    return Other(value)


@pytest.fixture
def config_cls(app_name):
    @config_(app_name)
    class Config(BaseConfig):
        some_str: str
        opt_str: Optional[str]
        some_bool: bool
        opt_bool: Optional[bool]
        some_int: int
        opt_int: Optional[int]
        some_float: float
        opt_float: Optional[float]

        some_other: Other = field(
            default_factory=lambda: Other("default"), convert=convert_other
        )

    return Config


@pytest.fixture
def app_name() -> str:
    return "test-app"


@pytest.fixture
def local_filename(app_name) -> str:
    return f"/Users/josh/.config/{app_name}.yaml"


@pytest.fixture
def config(config_cls, local_filename):
    return config_cls(
        file=local_filename,
        some_str="some_str",
        opt_str=None,
        some_bool=True,
        opt_bool=None,
        some_int=1,
        opt_int=None,
        some_float=1.0,
        opt_float=None,
    )
