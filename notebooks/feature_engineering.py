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

invoices = pd.read_csv(DATA_INPUT_DIR, parse_dates=["datetime"])
invoices.info()

# %%

invoices_by_day = (
    invoices.groupby([pd.Grouper(key="datetime", freq="D"), "country"])
    .agg(
        purchases=("invoice", "count"),
        num_invoices=("invoice", pd.Series.nunique),
        num_streams=("stream_id", "count"),
        num_views=("times_viewed", "count"),
        revenue=("price", "sum"),
    )
    .reset_index()
)

invoices_by_day.head()

# %%

countries = sorted(invoices_by_day["country"].unique())

invoices_by_day["country"] = invoices_by_day["country"].apply(
    lambda item: countries.index(item) + 1
)
invoices_by_day.head()

# %%

features = ["purchases", "num_invoices", "num_streams", "num_views", "revenue"]
invoices_by_day.sort_values(["datetime"], inplace=True)
invoices_by_day[features].to_csv(
    normalize_path([BUILD_DIR, "features.csv"]), index=False
)

# %%
