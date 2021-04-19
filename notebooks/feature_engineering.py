# %%

import os
import warnings

import pandas as pd

from tools.path_tools import normalize_path

warnings.filterwarnings("ignore")

# %%

BUILD_DIR = normalize_path([os.getcwd(), "..", "build"])
DATA_INPUT_DIR = normalize_path([BUILD_DIR, "data-ingested.csv"])

# %%

data = pd.read_csv(DATA_INPUT_DIR, parse_dates=["datetime"])
data.info()

# %%
