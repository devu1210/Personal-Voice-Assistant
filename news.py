import requests
from config import NEWS_API_KEY


def get_news(limit=5):
    if not NEWS_API_KEY:
        return []

    url = (
        f"https://newsapi.org/v2/everything"
        f"?q=India"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize={limit}"
        f"&apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    data = response.json()

    return data.get("articles", [])