import yfinance as yf
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def download_ticker(ticker, start="2000-01-01", end=None, interval="1d", save_name=None):
    print(f"Downloading {ticker} ...")
    df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
    if df.empty:
        raise RuntimeError(f"No data for {ticker} (empty dataframe).")
    df.index = pd.to_datetime(df.index)
    save_name = save_name or ticker.replace("^","").replace("/","_") + ".csv"
    outpath = DATA_DIR / save_name
    df.to_csv(outpath)
    print(f"Saved {outpath} rows={len(df)}")
    return df

if __name__ == "__main__":

    sp = download_ticker("^GSPC", start="2000-01-01", save_name="sp500_daily.csv")
    vix = download_ticker("^VIX", start="2000-01-01", save_name="vix_daily.csv")

    try:
        nifty = download_ticker("^NSEI", start="2000-01-01", save_name="nifty_daily.csv")
    except Exception as e:
        print("NIFTY download failed (yfinance issues). Use NSE official CSV if needed.", e)
