# -*- coding: utf-8 -*-


def test_default_file(local_config, local_filename) -> None:
    assert local_config.file == local_filename
