from dataclasses import asdict
from dataclasses import dataclass


@dataclass(slots=True)
class NewsItem:
    """Model standar untuk satu artikel berita."""

    title: str = ""

    url: str = ""

    source: str = ""

    category: str = ""

    published: str = ""

    summary: str = ""

    image: str = ""

    def to_dict(self):
        """Mengubah NewsItem menjadi dictionary."""

        return asdict(self)
