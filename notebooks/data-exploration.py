#%%

import os
import warnings

import pandas as pd

warnings.filterwarnings("ignore")

# %%

DATA_ROOT_DIR = os.path.abspath(os.path.join("..", "build"))
DATA_INPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-ingested.csv"))
DATA_OUTPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-explored.csv"))

# %%

data = pd.read_csv(DATA_INPUT_PATH, parse_dates=["datetime"])
data.info()

# %%
