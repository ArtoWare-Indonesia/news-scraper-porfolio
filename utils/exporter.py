from pathlib import Path
import pandas as pd


class Exporter:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def to_csv(self, data, filename="news.csv"):
        df = pd.DataFrame(data)
        filepath = self.output_dir / filename
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        return filepath

    def to_excel(self, data, filename="news.xlsx"):
        df = pd.DataFrame(data)
        filepath = self.output_dir / filename
        df.to_excel(filepath, index=False)
        return filepath

    def to_json(self, data, filename="news.json"):
        df = pd.DataFrame(data)
        filepath = self.output_dir / filename
        df.to_json(
            filepath,
            orient="records",
            force_ascii=False,
            indent=4
        )
        return filepath