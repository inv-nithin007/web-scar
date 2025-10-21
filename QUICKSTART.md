# Quick Start Guide - Forex News Scraper

## Installation (First Time Setup)

### Step 1: Install Python packages
```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Run Once (Manual)
```bash
python scraper.py
```
This will scrape all sources once and store data in the database.

### Option 2: Auto-Run Every 30 Minutes (Recommended)
```bash
python scheduler.py
```
This will:
- Run the scraper immediately
- Then run automatically every 30 minutes
- Keep running until you press Ctrl+C

### Option 3: View Collected News
```bash
python view_news.py
```
Interactive menu to view:
- High impact events only
- All economic events
- Breaking news articles

## What Gets Collected?

### Economic Events
- Non-Farm Payrolls (NFP)
- GDP Reports
- Interest Rate Decisions
- Inflation Data (CPI, PPI)
- Employment Data
- Central Bank Announcements

### News Articles
- Breaking forex market news
- Central bank policy updates
- Major economic developments
- Market-moving headlines

## Legal Sources

All data is collected from **public, legal sources**:
- ✅ Investing.com Economic Calendar (public)
- ✅ Reuters RSS Feeds (public)
- ✅ Bloomberg RSS Feeds (public)
- ✅ ForexLive RSS (public)
- ✅ FXStreet RSS (public)
- ✅ DailyFX RSS (public)

## Database

All news is stored in: `forex_news.db` (SQLite database)

## Customization

### Change Scraping Frequency

Edit `scheduler.py` line 36:
```python
# Every 30 minutes (default)
schedule.every(30).minutes.do(job)

# Or choose one of these:
schedule.every(1).hour.do(job)      # Every hour
schedule.every(15).minutes.do(job)  # Every 15 minutes
schedule.every(5).minutes.do(job)   # Every 5 minutes
```

### Focus on Specific Currencies

Edit `economic_calendar_scraper.py` line 118:
```python
major_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD']
```

## Troubleshooting

### No data collected?
- Check your internet connection
- Some websites may block requests - wait a few minutes and try again
- Run with verbose output: `python scraper.py`

### Database errors?
- Delete `forex_news.db` and run scraper again to recreate it

## Tips

1. **Run scheduler in background** (Linux/Mac):
   ```bash
   nohup python scheduler.py > scraper.log 2>&1 &
   ```

2. **View real-time logs**:
   ```bash
   tail -f scraper.log
   ```

3. **Stop background process**:
   ```bash
   ps aux | grep scheduler.py
   kill <process_id>
   ```

## Next Steps

Once you have data collected, you can:
- Export to CSV/Excel for analysis
- Create alerts for specific events
- Build a trading strategy based on news
- Integrate with trading platforms

---

**Need help?** Check the README.md for more details.
