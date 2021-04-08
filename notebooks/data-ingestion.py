# %%

import os
import warnings

import pandas as pd

warnings.filterwarnings("ignore")

# %%

DATA_ROOT_DIR = os.path.abspath(os.path.join("..", "data"))
DATA_TRAIN_DIR = os.path.normpath(os.path.join(DATA_ROOT_DIR, "cs-train"))
DATA_OUTPUT_DIR = os.path.normpath(os.path.join("..", "build"))

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


def parse_column_names(df):
    """
    Method used to parse the column names

    :param df: Original data frame
    :type df: pd.DataFrame

    :return: pd.DataFrame -- Formatted data frame
    """
    cols = set(df.columns.tolist())
    if "StreamID" in cols:
        df.rename(columns={"StreamID": "stream_id"}, inplace=True)
    if "TimesViewed" in cols:
        df.rename(columns={"TimesViewed": "times_viewed"}, inplace=True)
    if "total_price" in cols:
        df.rename(columns={"total_price": "price"}, inplace=True)

    return df


def create_datetime_column(df):
    """
    Method used to create a datetime column combining year, month and day in each row

    :param df: Base data frame object
    :type df: pd.DataFrame

    :return: pd.DateFrame -- Data object with a new column datetime
    """
    df["datetime"] = pd.to_datetime(df[["year", "month", "day"]])
    return df.drop(["year", "month", "day"], axis=1)


def read_data_file(data_file_path):
    """
    Method used to read a data file located on the given path

    :param data_file_path: Data file full path
    :type data_file_path: str

    :return: pd.DataFrame -- Data load to a dataframe object
    """
    df = pd.read_json(data_file_path)
    df = parse_column_names(df)
    return create_datetime_column(df)


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

    data = pd.concat(data, sort=True)
    data.sort_values(by="datetime", inplace=True)
    return data.reset_index(drop=True)


# %%

data = fetch_data(DATA_TRAIN_DIR)
data.to_csv(os.path.join(DATA_OUTPUT_DIR, "data-ingested.csv"), index=False)

# %%
