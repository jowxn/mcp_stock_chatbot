MCP Stock Chatbot: Indian Stock Market Information
Features

Stock Information: Retrieve real-time and historical data for Indian stocks (NSE) using yfinance.
Sentiment Analysis: Analyze sentiment of stock-related text using HuggingFace Transformers.
Chatbot Interface: User-friendly Streamlit frontend for interacting with the API.
Deployment: FastAPI backend and Streamlit frontend for scalable deployment.

Setup

Clone and install dependencies
git clone <your_repo_url>
cd mcp_stock_chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Run the FastAPI server
uvicorn app.main:app --reload


Run the Streamlit frontend
streamlit run chatbot.py



API Endpoints
POST /stock_info
Request:
{
  "symbol": "RELIANCE",
  "period": "1d"
}

Response:
{
  "symbol": "RELIANCE.NS",
  "name": "Reliance Industries Limited",
  "current_price": 3000.50,
  "volume": 5000000,
  "high": 3050.75,
  "low": 2950.25,
  "previous_close": 2980.00,
  "market_cap": 20000000000000,
  "period": "1d",
  "last_updated": "2025-07-22 12:35:00"
}

POST /analyze_sentiment
Request:
{
  "texts": ["Reliance stock is booming!", "Tata Motors faces challenges."]
}

Response:
{
  "results": [
    {"label": "POSITIVE", "score": 0.99},
    {"label": "NEGATIVE", "score": 0.98}
  ]
}

Deployment

FastAPI Backend:

Deploy on Render (recommended), Heroku, or AWS.
Example for Render:git push heroku main


Update API_URL in chatbot.py with the deployed URL.


Streamlit Frontend:

Deploy on Streamlit Cloud.
Steps:
Push code to a GitHub repository.
Connect Streamlit Cloud to your GitHub repo.
Select chatbot.py as the main script.
Ensure requirements.txt is included.





Usage

Access the Streamlit app in your browser (e.g., http://localhost:8501).
Enter a stock symbol (e.g., RELIANCE) or text for sentiment analysis.
