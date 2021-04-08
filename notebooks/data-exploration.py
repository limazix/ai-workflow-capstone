# %%

import os
import warnings

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

warnings.filterwarnings("ignore")

# %%

DATA_ROOT_DIR = os.path.abspath(os.path.join("..", "build"))
DATA_INPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-ingested.csv"))
DATA_OUTPUT_PATH = os.path.normpath(os.path.join(DATA_ROOT_DIR, "data-explored.csv"))


# %%

invoices = pd.read_csv(DATA_INPUT_PATH, parse_dates=["datetime"])
invoices.info()

# %%

invoices.set_index("datetime", inplace=True)
invoices.sort_index(inplace=True)
invoices.head(10)

# %% [markdown]

# # Revenue Analysis

# ## 1. Progress Over the Time

# %%

revenue_daily = pd.DataFrame()

for group, feats in invoices.groupby("datetime"):
    revenue_daily = revenue_daily.append(
        {
            "day": group,
            "total": feats["price"].sum(),
            "min": feats["price"].min(),
            "max": feats["price"].max(),
            "std": feats["price"].std(),
        },
        ignore_index=True,
    )

revenue_daily.head()

# %%

fig, ax = plt.subplots()

sns.lineplot(x="day", y="total", data=revenue_daily, ax=ax)

ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.format_ydata = lambda x: "$%1.2f" % x  # format the price.
ax.grid(True)
fig.autofmt_xdate()

plt.show()

# %%
