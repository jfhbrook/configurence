# -*- coding: utf-8 -*-


def test_default_file(local_config, local_filename) -> None:
    assert local_config.file == local_filename


def test_default_global_file(global_config, global_filename) -> None:
    assert global_config.file == global_filename
