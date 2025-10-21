# Forex News Scraper - Usage Guide

## ✅ Your Scraper is Working!

**Current Status:**
- ✅ 19 Economic Events collected
- ✅ 19 Breaking News Articles
- ✅ All CAD CPI events captured
- ✅ Speed: ~19 seconds per run

---

## 📊 Quick Commands

### 1. Run Scraper Once
```bash
./venv/bin/python scraper.py
```
Collects all current news and stores in database (~20 seconds)

### 2. Run Every 30 Minutes (Auto)
```bash
./venv/bin/python scheduler.py
```
Keeps running and scrapes every 30 minutes. Press Ctrl+C to stop.

### 3. View All News
```bash
./venv/bin/python view_news.py
```
Interactive menu:
- [1] High Impact Events Only
- [2] All Economic Events
- [3] Breaking News Articles
- [4] Everything

### 4. Check Specific Currency
```bash
./venv/bin/python check_currency.py CAD
./venv/bin/python check_currency.py USD
./venv/bin/python check_currency.py EUR
```
Shows events for specific currency with impact indicators.

---

## 🎯 What You're Collecting

### Economic Events (19 today)
✅ CAD CPI (MoM, YoY, Core) - **Your request!**
✅ USD Business Inventories, Leading Index
✅ JPY Trade Balance, Exports
✅ EUR/GBP Central Bank Speeches (ECB, BoE, Fed)

### Breaking News (19 articles)
✅ Bloomberg Markets - Major financial news
✅ ForexLive - Real-time forex updates
✅ Reuters - Business & Markets (when available)
✅ FXStreet - Forex analysis (when available)

---

## 📈 Impact Indicators

- 🔴 **High** = 3 icons = Major market movers (NFP, Interest Rates, GDP)
- 🟡 **Medium** = 2 icons = Moderate impact (CPI, Employment, PMI)
- ⚪ **Low** = 1 icon = Minor impact (filtered out)

**Your CAD CPI events = Medium (🟡) = Still important for CAD pairs!**

---

## 💡 Typical Workflow

### Morning Routine
```bash
# Check what happened overnight
./venv/bin/python view_news.py

# Choose option 1 to see high-impact events
# Choose option 3 to see breaking news
```

### All-Day Monitoring
```bash
# Start the scheduler
./venv/bin/python scheduler.py

# Let it run in background
# It will collect news every 30 minutes automatically
```

### Before Trading CAD
```bash
# Quick check CAD events
./venv/bin/python check_currency.py CAD
```

---

## 🔧 Customization

### Change Scraping Frequency
Edit `scheduler.py` line 36:

```python
# Current: Every 30 minutes
schedule.every(30).minutes.do(job)

# Options:
schedule.every(15).minutes.do(job)  # Every 15 minutes
schedule.every(1).hour.do(job)      # Every hour
schedule.every(5).minutes.do(job)   # Every 5 minutes (fast!)
```

### Focus on Specific Currencies
Edit `economic_calendar_scraper.py` line 129:

```python
# Current: All major currencies
major_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD']

# Example: Focus on USD and CAD only
major_currencies = ['USD', 'CAD']
```

### Add More News Keywords
Edit `news_scraper.py` line 21:

```python
self.forex_keywords = [
    'federal reserve', 'fed', 'interest rate', 'inflation', 'cpi',
    # Add your own keywords here
    'tariff', 'trade deal', 'oil price', 'gold',
]
```

---

## 📊 Database Queries

### Check Database Stats
```bash
./venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('forex_news.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM economic_events')
events = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM news_articles')
articles = cursor.fetchone()[0]
print(f'Events: {events}, Articles: {articles}')
conn.close()
"
```

### Export to CSV (for Excel)
```bash
./venv/bin/python -c "
import sqlite3
import pandas as pd

conn = sqlite3.connect('forex_news.db')

# Export events
df_events = pd.read_sql_query('SELECT * FROM economic_events', conn)
df_events.to_csv('events.csv', index=False)

# Export news
df_news = pd.read_sql_query('SELECT * FROM news_articles', conn)
df_news.to_csv('news.csv', index=False)

print('Exported to events.csv and news.csv')
conn.close()
"
```

---

## ⚡ Performance

**Speed:**
- Single scrape: 15-20 seconds
- Memory usage: ~50MB
- CPU usage: Low
- Perfect for company PC

**Frequency Options:**
- ✅ Every 30 minutes = 48 runs/day
- ✅ Every 15 minutes = 96 runs/day
- ✅ Every 5 minutes = 288 runs/day
- ⚠️ Every 1 minute = May trigger rate limits

**Recommended:** 30 minutes for normal trading, 15 minutes for active trading

---

## 🛑 Stopping the Scheduler

If running in terminal:
```bash
# Press Ctrl+C
```

If running in background:
```bash
# Find the process
ps aux | grep scheduler.py

# Kill it
kill <process_id>
```

---

## 🐛 Troubleshooting

### "No events found"
- Check internet connection
- Some websites may be blocked by company firewall
- The scraper will skip blocked sources and continue

### "0 high impact events"
- The database query shows only "High" impact
- Your data includes "Medium" impact (CAD CPI)
- Use `view_news.py` option 2 to see all events

### "Permission denied"
- Make sure to use `./venv/bin/python` not just `python`
- Run: `chmod +x *.py *.sh`

---

## 📚 Files Reference

**Core Scripts:**
- `scraper.py` - Main scraper
- `scheduler.py` - Auto-run every 30 minutes
- `view_news.py` - Interactive news viewer
- `check_currency.py` - Quick currency checker

**Data:**
- `forex_news.db` - SQLite database (all your data)

**Docs:**
- `GETTING_STARTED.md` - Detailed setup guide
- `QUICKSTART.md` - Command reference
- `README.md` - Project overview
- `USAGE_GUIDE.md` - This file!

---

## 🎓 Next Level

Once you're comfortable, you can:

1. **Create Alerts**
   - Send email/SMS when high-impact news drops
   - Alert when actual ≠ forecast

2. **Build Dashboard**
   - Web interface to view news
   - Charts and graphs

3. **Integrate with Trading**
   - Connect to MetaTrader, TradingView
   - Auto-execute trades based on news

4. **Machine Learning**
   - Predict market moves from news
   - Sentiment analysis

---

## ✅ Your Setup is Complete!

**What you have:**
- ✅ Working scraper (tested)
- ✅ Automatic scheduler
- ✅ Interactive viewer
- ✅ Currency checker
- ✅ CAD CPI events captured

**What to do now:**
```bash
# Start collecting news automatically
./venv/bin/python scheduler.py
```

**Let it run and check periodically:**
```bash
./venv/bin/python view_news.py
```

---

**Questions? Check the other docs or run `./venv/bin/python view_news.py` to see your data!**
