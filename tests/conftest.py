# -*- coding: utf-8 -*-

import pytest

from configurence import config


@pytest.fixture
def config_cls():
    @config("my_app")
    class Config:
        some_bool: bool

    return Config
