# %%

import os
import warnings

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")

# %%

DATA_ROOT_DIR = os.path.abspath(os.path.join("..", "build"))
DATA_INPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-ingested.csv"))
DATA_OUTPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-explored.csv"))

# %%

invoices = pd.read_csv(DATA_INPUT_PATH, parse_dates=["datetime"])
invoices.info()

# %% [markdown]

# # Revenue Analysis

# ## 1. Revenue Over Time
# %%

invoices_by_month = (
    invoices.groupby([pd.Grouper(key="datetime", freq="M")])
    .agg(
        num_invoices=("invoice", "count"),
        revenue_mean=("price", "mean"),
        revenue_std=("price", "std"),
    )
    .reset_index()
)

invoices_by_month.head()

# %%

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(
        name="Invoices",
        x=invoices_by_month["datetime"],
        y=invoices_by_month["num_invoices"],
    ),
    secondary_y=False,
)

fig.add_trace(
    go.Line(
        name="Revenue Mean",
        x=invoices_by_month["datetime"],
        y=invoices_by_month["revenue_mean"],
    ),
    secondary_y=True,
)
fig.add_trace(
    go.Line(
        name="Revenue Std",
        x=invoices_by_month["datetime"],
        y=invoices_by_month["revenue_std"],
    ),
    secondary_y=True,
)
fig.update_layout(title_text="Invoices & Revenue")
fig.update_yaxes(title_text="Num. Invoices", secondary_y=False)
fig.update_yaxes(title_text="Revenue", secondary_y=True)
fig.show()

# %%
