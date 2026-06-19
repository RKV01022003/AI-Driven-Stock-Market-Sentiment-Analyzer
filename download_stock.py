import yfinance as yf
import sys

ticker = sys.argv[1]   # e.g. 'AAPL'
start_date = sys.argv[2]  # e.g. '2025-01-01'
end_date = sys.argv[3]    # e.g. '2025-09-01'

data = yf.download(ticker, start=start_date, end=end_date)

output_file = f"{ticker}_prices.csv"
data.to_csv(output_file)
print(f"Saved stock price data to {output_file}")
