import csv
import json
from datetime import datetime
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

        # Timestamp dibuat sekali agar semua file memiliki nama yang sama
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def export_csv(self, articles, filename=None):
        """Export articles to CSV."""

        if not articles:
            return

        if filename is None:
            filename = f"news_{self.timestamp}.csv"

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

    def export_json(self, articles, filename=None):
        """Export articles to JSON."""

        if filename is None:
            filename = f"news_{self.timestamp}.json"

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

    def export_excel(self, articles, filename=None):
        """Export articles to Excel."""

        if not articles:
            return

        if filename is None:
            filename = f"news_{self.timestamp}.xlsx"

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
        """Export to all supported formats."""

        if not articles:
            return

        self.export_csv(articles)
        self.export_json(articles)
        self.export_excel(articles)