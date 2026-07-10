from models import NewsItem

item = NewsItem(
    title="Contoh Berita",
    url="https://example.com",
    source="Example",
)

print(item)

print()

print(item.to_dict())
