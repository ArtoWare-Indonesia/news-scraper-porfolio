import csv
import json
from pathlib import Path

from openpyxl import Workbook


class Exporter:
    """Export scraped articles to various formats."""

    FIELDS = [
        "title",
        "url",
        "source",
        "category",
        "published",
        "summary",
        "image",
    ]

    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_csv(self, articles, filename="news.csv"):
        if not articles:
            return

        filepath = self.output_dir / filename

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8-sig",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=self.FIELDS,
                extrasaction="ignore",
            )

            writer.writeheader()

            for article in articles:
                writer.writerow(article)

    def export_json(self, articles, filename="news.json"):
        filepath = self.output_dir / filename

        with open(
            filepath,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                articles,
                file,
                ensure_ascii=False,
                indent=4,
            )

    def export_excel(self, articles, filename="news.xlsx"):
        if not articles:
            return

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "News"

        sheet.append(self.FIELDS)

        for article in articles:
            sheet.append([
                article.get(field, "")
                for field in self.FIELDS
            ])

        filepath = self.output_dir / filename

        workbook.save(filepath)

    def export_all(self, articles):
        self.export_csv(articles)
        self.export_json(articles)
        self.export_excel(articles)
