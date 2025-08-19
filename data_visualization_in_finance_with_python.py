import pandas as pd
import plotly.express as px

df = pd.read_csv("portfolio_returns.csv", parse_dates=["date"])
fig = px.line(df, x="date", y="cumulative_return",
              title="Cumulative Portfolio Return",
              labels={"cumulative_return": "Return"})

fig.update_layout(template="plotly_dark")
fig.show()