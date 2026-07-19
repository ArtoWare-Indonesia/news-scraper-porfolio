import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="news-scraper",
        description="News Scraper Portfolio"
    )

    parser.add_argument(
        "--source",
        type=str,
        choices=["antara", "tempo"],
        help="Run only the selected news source."
    )

    parser.add_argument(
        "--format",
        type=str,
        choices=["csv", "json", "xlsx", "all"],
        default="all",
        help="Export format (default: all)."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of articles to export."
    )

    return parser.parse_args()