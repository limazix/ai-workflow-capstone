# %%
%reload_ext autoreload
%autoreload 2

import os
import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('..')

import pandas as pd
import numpy as np

import tools
import importlib
importlib.reload(tools)

# %%
DATA_ROOT_DIR = os.path.abspath(os.path.join('..', 'data'))
DATA_TRAIN_DIR = os.path.normpath(os.path.join(DATA_ROOT_DIR, 'cs-train'))

print(DATA_TRAIN_DIR)
# %%


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


def read_data_file(data_file_path):
    """
    Method used to read a data file located on the given path

    :param data_file_path: Data file full path
    :type data_file_path: str

    :return: pd.DataFrame -- Data load to a dataframe object
    """
    return pd.read_json(data_file_path)


def fetch_data(data_dir):
    """
    Method used to read data from json files and add it to a dataframe

    :param data_dir: Absolute path for the data directory
    :type data_dir: str

    :return: pd.DataFrame -- Data load on a pandas DataFrame
    """
    check_dir(data_dir)

    data = list()
    for data_file in os.listdir(data_dir):
        data_file_path = normalize_path([data_dir, data_file])
        data.append(read_data_file(data_file_path))


fetch_data(DATA_TRAIN_DIR)
# %%
