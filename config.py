APP_NAME = "News Scraper Portfolio"
APP_VERSION = "0.4.0"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}

HTML_SOURCES = [
    {
        "name": "Antara",
        "url": "https://www.antaranews.com/terkini",
        "enabled": True,
    },
    {
        "name": "Tempo",
        "url": "https://www.tempo.co",
        "enabled": True,
    },
]

RSS_SOURCES = [
    {
        "name": "Antara",
        "url": "https://www.antaranews.com/rss/terkini",
        "enabled": False,
    },
    {
        "name": "Tempo",
        "url": "https://rss.tempo.co/nasional",
        "enabled": False,
    },
]