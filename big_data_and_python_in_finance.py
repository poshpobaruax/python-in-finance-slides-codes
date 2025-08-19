# Big Data and Python in Finance

import dask.dataframe as dd

# 1. Read all trade files in one go
df = dd.read_csv("trades_2025-*.csv")

# 2. Compute the average trade price for each stock symbol
avg_price = df.groupby("symbol")["price"].mean().compute()

print(avg_price)