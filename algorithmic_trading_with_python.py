# Algorithmic Trading with Python
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

# 1. Fetch closing price data
data = yf.download("AAPL", "2020-01-01", "2025-01-01")["Close"]

# 2. Fit ARIMA model & forecast
model = ARIMA(data, order=(1,1,1)).fit()
forecast = model.forecast(5)

# 3. Generate a simple signal
if forecast.mean() > data[-1]:
    print("Buy signal")
else:
    print("Sell signal")