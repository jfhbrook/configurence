# -*- coding: utf-8 -*-

from typing import Optional

import pytest

from configurence import config as config_


@pytest.fixture
def config_cls():
    @config_
    class Config:
        some_str: str
        opt_str: Optional[str]
        some_bool: bool
        opt_bool: Optional[bool]
        some_int: int
        opt_int: Optional[int]
        some_float: float
        opt_float: Optional[float]

    return Config


@pytest.fixture
def app_name() -> str:
    return "my-app"


@pytest.fixture
def local_filename() -> str:
    return "/Users/josh/.config/my-app.yaml"


@pytest.fixture
def config(config_cls, app_name, local_filename):
    return config_cls(
        name=app_name,
        _file=local_filename,
        some_str="some_str",
        opt_str=None,
        some_bool=True,
        opt_bool=None,
        some_int=1,
        opt_int=None,
        some_float=1.0,
        opt_float=None,
    )
