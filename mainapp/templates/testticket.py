from yahoo_fin.stock_info import get_live_price

# List of tickers to test
tickers = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "META", "NVDA", "TSLA", "PEP", "AVGO",
    "COST", "CSCO", "ADBE", "TXN", "QCOM", "AMGN", "INTC", "HON", "AMD", "SBUX",
    "MDLZ", "AMAT", "INTU", "BKNG", "ADI", "LRCX", "GILD", "FISV", "ADP", "MU",
    "ISRG", "REGN", "VRTX", "MRNA", "ASML", "LULU", "JD", "ZM", "DOCU", "SNPS",
    "ILMN", "WDAY", "NXPI", "MAR", "CTSH", "ATVI", "EBAY", "EXC", "CSX", "KDP",
    "ORLY", "MNST", "CTAS", "ROST", "PAYX", "PCAR", "XLNX", "SWKS", "MELI", "TEAM",
    "BIDU", "NTES", "VRSK", "CHTR", "FAST", "DLTR", "WBA", "LBTYA", "LBTYK", "UAL",
    "EXPE", "IDXX", "SIRI", "ZBRA", "ABNB", "DOCU", "CRWD", "PANW", "SPGI", "TSCO",
    "FICO", "RGEN", "EPAM", "MTCH"
]

# Function to test each ticker
def test_tickers(ticker_list):
    valid_tickers = []
    invalid_tickers = []
    for ticker in ticker_list:
        try:
            price = get_live_price(ticker)
            print(f"✅ {ticker}: {price}")
            valid_tickers.append(ticker)
        except Exception as e:
            print(f"❌ {ticker}: Failed ({e})")
            invalid_tickers.append(ticker)
    return valid_tickers, invalid_tickers

# Run the test
valid, invalid = test_tickers(tickers)

# Print results
print("\nSummary:")
print(f"Valid tickers ({len(valid)}): {valid}")
print(f"Invalid tickers ({len(invalid)}): {invalid}")
