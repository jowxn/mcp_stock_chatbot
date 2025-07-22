import yfinance as yf
from datetime import datetime

def get_stock_info(symbol: str, period: str = "1d"):
    """
    Fetch stock data for the given symbol and period.
    Returns dict with price, volume, and other info.
    """
    try:
        # Ensure symbol ends with .NS for NSE stocks
        if not symbol.endswith(".NS"):
            symbol = f"{symbol}.NS"
        
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None
        
        # Get latest data
        
        latest = hist.iloc[-1]
        info = stock.info
        
        return {
            "symbol": symbol,
            "name": info.get("longName", "N/A"),
            "current_price": round(latest["Close"], 2),
            "volume": int(latest["Volume"]),
            "high": round(latest["High"], 2),
            "low": round(latest["Low"], 2),
            "previous_close": round(info.get("previousClose", latest["Close"]), 2),
            "market_cap": info.get("marketCap", "N/A"),
            "period": period,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        raise RuntimeError(f"Error fetching stock data for {symbol}: {str(e)}")
