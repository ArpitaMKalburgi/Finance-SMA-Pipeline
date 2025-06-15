📈 Finance SMA Data Pipeline
This is a beginner-friendly hands-on data engineering project that demonstrates how to build a simple data pipeline using Python and Streamlit. 
The pipeline fetches historical stock prices from Yahoo Finance, processes the data by calculating Simple Moving Averages (SMA), and visualizes the results in an interactive dashboard.


Project Overview
- Objective: Build a local data pipeline that collects, processes, stores, and visualizes stock     price data.
- Stock Data Source: Yahoo Finance API (via `yfinance`)
- Processing Logic: Simple Moving Average (SMA-5, SMA-10)
- Visualization Tool: Streamlit (web app)
- Storage: CSV files (for raw and processed data)


Features
- Fetch historical stock price data (e.g., AAPL)
- Store raw data locally in CSV format
- Clean and preprocess the data (handle nulls)
- Calculate 5-day and 10-day SMA
- Save processed data to a new CSV file
- Build an interactive dashboard with:
  - Data table preview
  - Line chart showing Close price vs. SMA-5 and SMA-10


Tech Stack
| Layer            | Tool / Library      |
|------------------|---------------------|
| Language         | Python              |
| API              | `yfinance`          |
| Data Processing  | `pandas`            |
| Visualization    | `Streamlit`         |
| Storage          | CSV (local)         |
| IDE              | VS Code             |

🗂️ Project Structure
Finance-SMA/
├── Finance-SMA.py # Main script (fetch + process + visualize)
├── raw_stock_data.csv # Raw data from yfinance (generated)
├── processed_stock_data.csv # Processed data with SMA (generated)
├── requirements.txt # Dependencies
├── .gitignore # Files to ignore in Git
└── README.md # Project documentation


