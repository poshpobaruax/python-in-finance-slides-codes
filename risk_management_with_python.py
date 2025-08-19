import pandas as pd, plotly.express as px

# 1. Load returns
df = pd.read_csv("returns.csv", index_col=0, parse_dates=True)

# 2. Rolling 95% VaR over 60 days
rolling_var = df['Portfolio'].rolling(60).quantile(0.05)

# 3. Simulate a 10% market crash
stressed = df * 0.90
crash_var = stressed['Portfolio'].quantile(0.05)

# 4. Plot both
fig = px.line(rolling_var, title='60-Day Rolling 95% VaR')
fig.add_scatter(x=rolling_var.index, y=[crash_var]*len(rolling_var),
                name="10% Shock VaR", line=dict(dash="dash"))

fig.show()