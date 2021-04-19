# -*- coding: utf-8 -*-

import os


def normalize_path(parts: list):
    """
    Method used to join and format a given list of a path's parts

    :param parts: List of path's parts
    :type parts: list

    :return: str -- The normalized path
    """
    return os.path.normpath(os.path.join(*parts))


def check_dir(data_dir):
    """
    Method used to validate the given data directory path

    :param data_dir: Absolute path for the data directory
    :type data_dir: str

    :raise: Exception
    """
    if not os.path.isdir(data_dir):
        raise Exception("specified data dir does not exist")
    if not len(os.listdir(data_dir)) > 0:
        raise Exception("specified data dir does not contain any files")
