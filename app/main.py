from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.stock_data import get_stock_info
from app.sentiment import analyze_sentiments

app = FastAPI(
    title="MCP Stock Chatbot Server",
    description="REST API for Indian stock market data and sentiment analysis.",
    version="1.0.0"
)

class StockRequest(BaseModel):
    symbol: str
    period: Optional[str] = "1d"

class SentimentRequest(BaseModel):
    texts: List[str]

@app.post("/stock_info")
async def stock_info(request: StockRequest):
    try:
        data = get_stock_info(request.symbol, request.period)
        if data is None:
            raise HTTPException(status_code=404, detail=f"Stock symbol {request.symbol} not found")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stock data: {str(e)}")

@app.post("/analyze_sentiment")
async def analyze(request: SentimentRequest):
    if not request.texts:
        raise HTTPException(status_code=400, detail="No texts provided")
    try:
        results = analyze_sentiments(request.texts)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing sentiments: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Welcome to the MCP Stock Chatbot Server!"}
