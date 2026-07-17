# News Scraper Portfolio

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-v0.4.0-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)

A modular Python news scraper framework built as a freelance portfolio project.

The project demonstrates how to build reusable, maintainable, and extensible web scrapers using modern Python architecture. Currently it supports HTML news scraping with a reusable scraping framework and standardized data model.

---

## Features

- Modular HTML scraper framework
- Reusable `BaseScraper`
- Automatic HTTP retry using `requests.Session`
- BeautifulSoup HTML parsing
- Centralized `ScraperManager`
- Standardized `NewsItem` data model
- CSV export
- Excel export (.xlsx)
- JSON export
- Configurable scraper registry
- Logging
- Lightweight (no pandas dependency)
- Compatible with Windows and Linux (antiX)
- Improved logging
- Execution time measurement
- Scraping summary
- Exported file reporting

---

## Current Supported Sources

### HTML

| Source | Status |
|---------|--------|
| Antara | ✅ |
| Tempo | ✅ |

### RSS

The RSS scraping engine from v0.2.x is still available in the project and will be integrated into the new `ScraperManager` architecture in a future release.

---

# Architecture

```
                    main.py
                        │
                        ▼
               ScraperManager
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   AntaraScraper               TempoScraper
          │                           │
          └─────────────┬─────────────┘
                        ▼
                  BaseScraper
                        │
             fetch() → parse()
                        │
                        ▼
                   NewsItem
                        │
                        ▼
                    Exporter
                        │
      ┌───────────┬────────────┬───────────┐
      ▼           ▼            ▼
   news.csv    news.json    news.xlsx
```

---

## Project Structure

```
news-scraper-portfolio/
│
├── config.py
├── main.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   └── news.py
│
├── scrapers/
│   ├── __init__.py
│   ├── base.py
│   ├── manager.py
│   ├── antara.py
│   └── tempo.py
│
├── utils/
│   ├── exporter.py
│   └── logger.py
│
├── docs/
│   └── images/
│       ├── news.csv.png
│       ├── news.xlsx.png
│       └── news.json.png
│
├── output/
│   ├── news.csv
│   ├── news.xlsx
│   └── news.json
│
├── test_antara.py
├── test_tempo.py
├── test_manager.py
└── test_newsitem.py
```

---

## Tech Stack

- Python 3
- Requests
- BeautifulSoup4
- urllib3
- openpyxl

---

## Requirements

- Python 3.13+
- pip
- Virtual Environment (recommended)

Main dependencies:

- requests
- beautifulsoup4
- lxml
- feedparser
- openpyxl

---

## Installation

```bash
git clone <repository-url>

cd news-scraper-porfolio

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```
## 💻 Running the Project
============================================================
News Scraper Portfolio v0.5.0
============================================================

Starting news scraping...

Running AntaraScraper (Antara)
[SUCCESS] Antara collected 15 article(s) in 1.18 seconds

Running TempoScraper (Tempo)
[SUCCESS] Tempo collected 20 article(s) in 0.92 seconds

============================================================
SCRAPING SUMMARY
============================================================
Version          : 0.5.0
Successful       : 2
Failed           : 0
Total articles   : 35

Articles by source
  Antara         : 15
  Tempo          : 20

Exported files
  output/news_20260716_101530.csv
  output/news_20260716_101530.json
  output/news_20260716_101530.xlsx

Elapsed time     : 2.10 seconds
============================================================

---

## Usage

Run all registered scrapers:

```bash
python main.py
```

Example output:

```
Starting news scraping...

Running AntaraScraper
Running TempoScraper

Scraping completed successfully!

Total articles: 108

Files saved in output/
```
## 📸 Output Preview

### CSV Output
![CSV Output](docs/images/output-csv.png)

### Excel Output
![Excel Output](docs/images/output-excel.png)

### JSON Output
![JSON Output](docs/images/output-json.png)
---

## Output

Generated files are stored in the `output/` directory.

```
output/
├── news_20260716_101530.csv
├── news_20260716_101530.json
└── news_20260716_101530.xlsx

```

---

## Development

Run individual scraper tests:

```bash
python test_antara.py
```

```bash
python test_tempo.py
```

Run all scrapers:

```bash
python test_manager.py
```

Test the data model:

```bash
python test_newsitem.py
```

---

## Design Principles

This project follows several software engineering principles:

- Modular architecture
- Template Method Pattern
- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Reusable components
- Standardized data model

---

## Roadmap

### v0.5.0
- Improved logging
- Documentation
- Initial unit tests
- CLI (--source, --format, --limit)

### v0.6.0
- Kompas scraper
- CNBC Indonesia scraper
- Detik scraper
- Parallel scraping
- YAML/JSON configuration
- Date/category filtering

### v1.0.0
- Stable API
- Plugin-based scraper system
- GitHub Actions
- Complete documentation

---

## License

This project is intended for educational purposes and freelance portfolio demonstrations.

Please respect each website's Terms of Service and robots.txt when scraping.
