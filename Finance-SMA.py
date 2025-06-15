# Step 1: Fetching data using API
import yfinance as yf
import pandas as pd
import streamlit as st

def fetch_stock_data(symbol='AAPL', start='2023-01-01', end='2023-12-31'):
    df = yf.download(symbol, start=start, end=end)
    df.to_csv("raw_stock_data.csv")
    print("Data saved to csv file")
    return df

df = fetch_stock_data()

# Step 2: Process the data
print("Any nulls in raw data?", df.isnull().values.any())
print(df.head())
print(df.describe())

def calculate_sma(input_file='raw_stock_data.csv'):
    df = pd.read_csv(input_file)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df.dropna(subset=['Close'], inplace=True)
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df.to_csv("processed_stock_data.csv", index=False)
    print("Processed and saved to processed_stock_data.csv")

calculate_sma()

# Step 3: Visualize using Streamlit
st.title("📈 Stock Price with SMA (Simple Moving Average)")

# Reload processed data
try:
    df_processed = pd.read_csv("processed_stock_data.csv")

    st.write("### Preview of Processed Data")
    st.dataframe(df_processed.tail())

    if all(col in df_processed.columns for col in ['Close', 'SMA_5', 'SMA_10']):
        st.line_chart(df_processed[['Close', 'SMA_5', 'SMA_10']])
    else:
        st.warning("Missing SMA columns. Check processing step.")

except FileNotFoundError:
    st.error("Processed file not found. Run the pipeline again.")
