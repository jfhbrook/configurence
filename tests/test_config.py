# -*- coding: utf-8 -*-

from typing import Any

import pytest


@pytest.mark.parametrize("name", ["some_bool"])
def test_get(config, name: str) -> None:
    assert config.get(name) == getattr(config, name)


def test_get_unknown(config) -> None:
    with pytest.raises(ValueError):
        config.get("pony")


@pytest.mark.parametrize(
    "name,value,expected",
    [
        ("some_bool", "true", True),
        ("some_bool", "false", False),
    ],
)
def test_set(config, name: str, value: str, expected: Any) -> None:
    config.set(name, value)
    assert config.get(name) == expected


@pytest.mark.parametrize(
    "name,value",
    [],
)
def test_set_value_error(config, name: str, value: str) -> None:
    with pytest.raises(ValueError):
        config.set(name, value)


def test_set_unknown(config) -> None:
    with pytest.raises(ValueError):
        config.set("pony", "pony")


@pytest.mark.parametrize("name", [])
def test_unset(config, name: str) -> None:
    config.unset(name)
    assert config.get(name) is None


@pytest.mark.parametrize("name", [])
def test_unset_required(config, name: str) -> None:
    with pytest.raises(ValueError):
        config.unset(name)


def test_repr(config, snapshot) -> None:
    assert repr(config) == snapshot
