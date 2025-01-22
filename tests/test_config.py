# -*- coding: utf-8 -*-


def test_simple(config_cls) -> None:
    """Test that config can be constructed"""
    config_cls(name="my_app", some_bool=True, _file="/etc/my_app.yaml")
