import yfinance as yf

data = yf.download("SPY", start="2017-01-01", end="2019-01-01")
data.to_csv('example.csv')