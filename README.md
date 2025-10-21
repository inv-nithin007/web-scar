# Forex News Scraper Bot

A Python-based web scraper that collects market-moving forex news from legal, public sources.

## Features
- Scrapes economic calendar events (NFP, GDP, Interest Rates, etc.)
- Collects breaking news from major financial sources
- Stores data in SQLite database
- Runs automatically every 30 minutes
- Filters for high-impact news only

## Legal Sources
- Forex Factory (Economic Calendar)
- Reuters RSS Feed
- Investing.com Economic Calendar
- Bloomberg RSS Feed

## Installation

### For Company PCs (Recommended)
If you're on a company PC, use a virtual environment to avoid permission issues:

```bash
# Create virtual environment (one-time setup)
python3 -m venv venv

# Install dependencies
./venv/bin/pip install -r requirements.txt
```

### For Personal PCs
```bash
pip install -r requirements.txt
```

## Usage

### If using virtual environment (company PC):
```bash
# Run once to collect news
./venv/bin/python scraper.py

# Run with scheduler (every 30 minutes)
./venv/bin/python scheduler.py

# View collected news
./venv/bin/python view_news.py
```

### If installed globally:
```bash
# Run once to collect news
python scraper.py

# Run with scheduler (every 30 minutes)
python scheduler.py

# View collected news
python view_news.py
```

## Database
All news is stored in `forex_news.db` SQLite database.
