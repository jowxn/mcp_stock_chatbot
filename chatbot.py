import streamlit as st
import requests
import json

# FastAPI server URL (update with deployed URL after deployment)
API_URL = "http://localhost:8000"

st.set_page_config(page_title="Indian Stock Market Chatbot", page_icon="📈")

st.title("Indian Stock Market Chatbot")
st.write("Ask about Indian stock prices or analyze stock-related sentiments!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Enter a stock symbol (e.g., RELIANCE) or text for sentiment analysis:")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            if prompt.upper().replace(".NS", "").isalpha():
                # Treat as stock symbol query
                response = requests.post(f"{API_URL}/stock_info", json={"symbol": prompt.upper()})
                if response.status_code == 200:
                    data = response.json()
                    response_text = (
                        f"**{data['name']} ({data['symbol']})**\n"
                        f"- Current Price: ₹{data['current_price']}\n"
                        f"- Previous Close: ₹{data['previous_close']}\n"
                        f"- High: ₹{data['high']}\n"
                        f"- Low: ₹{data['low']}\n"
                        f"- Volume: {data['volume']:,}\n"
                        f"- Market Cap: {data['market_cap']}\n"
                        f"- Last Updated: {data['last_updated']}"
                    )
                else:
                    response_text = f"Error: Could not fetch data for {prompt} (Status: {response.status_code})"
            else:
                # Treat as sentiment analysis
                response = requests.post(f"{API_URL}/analyze_sentiment", json={"texts": [prompt]})
                if response.status_code == 200:
                    result = response.json()["results"][0]
                    response_text = (
                        f"**Sentiment Analysislds: {result['label']} (Confidence: {result['score']:.2%})"
                    )
                else:
                    response_text = f"Error: Sentiment analysis failed (Status: {response.status_code})"
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except requests.RequestException as e:
            error_msg = f"Failed to connect to the server: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
