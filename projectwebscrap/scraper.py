import requests
from bs4 import BeautifulSoup
import re

def scrape_visible_text(url):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        paragraphs = soup.find_all("p")

        text = " ".join(p.get_text() for p in paragraphs)

        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        if len(text) < 200:
            return None

        return text

    except Exception as e:
        print("[SCRAPER ERROR]:", e)
        return None
