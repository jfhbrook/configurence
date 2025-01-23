# -*- coding: utf-8 -*-


def test_default_file(config, local_filename) -> None:
    assert config.file == local_filename
