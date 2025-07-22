from transformers import pipeline

# Load the sentiment analysis pipeline once at import
try:
    analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    raise RuntimeError(f"Failed to load sentiment analysis model: {str(e)}")

def analyze_sentiments(texts: list) -> list:
    """
    Analyze sentiment for a list of texts.
    Returns list of dicts: [{"label": ..., "score": ...}, ...]
    """
    if not texts:
        return []
    try:
        results = analyzer(texts)
        return results
    except Exception as e:
        raise RuntimeError(f"Error during sentiment analysis: {str(e)}")
