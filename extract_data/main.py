import yfinance as yf
import argparse

parser = argparse.ArgumentParser(description="Download stock data for a given company and date range.")
parser.add_argument("--company", required=True, help="Company ticker symbol")
parser.add_argument("--start", required=True, help="Start year in YYYYformat")
parser.add_argument("--end", required=True, help="End year in YYYY format")
args = parser.parse_args()

company = args.company
start_year = args.start
end_year = args.end

# Downloading the data
df = yf.download(company, start=f"{start_year}-01-01", end=f"{end_year}-12-31", multi_level_index=False)

# Defining the column names
df.reset_index(inplace=True)
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Saving the data to a CSV file
df.to_csv(f"data_{company}_{start_year}-{end_year}.csv", index=False)