# -*- coding: utf-8 -*-

import pytest

from configurence import config as config_


@pytest.fixture
def config_cls():
    @config_
    class Config:
        some_bool: bool

    return Config


@pytest.fixture
def app_name() -> str:
    return "my-app"


@pytest.fixture
def local_filename() -> str:
    return "/Users/josh/.config/my-app.yaml"


@pytest.fixture
def config(config_cls, app_name, local_filename):
    return config_cls(name=app_name, _file=local_filename, some_bool=True)
