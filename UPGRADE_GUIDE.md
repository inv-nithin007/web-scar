# 🚀 SYSTEM UPGRADED! Forex + Indian Stocks

## ✅ What's New

Your scraper has been **upgraded** to collect BOTH:
1. **💱 Forex News** (original system)
2. **🇮🇳 Indian Stock Market News** (NEW!)

Everything is **SEPARATE** - you can run forex only, India only, or both together!

---

## 📊 Indian Stock Market Coverage

### What Gets Collected

**Economic Events:**
- ✅ RBI Monetary Policy & Repo Rate decisions
- ✅ GDP Reports
- ✅ Inflation Data (CPI, WPI)
- ✅ IIP (Industrial Production)
- ✅ Trade Balance
- ✅ SEBI Announcements

**Stock Market News:**
- ✅ Nifty 50 movements
- ✅ Nifty Next 50 news
- ✅ Bank Nifty updates
- ✅ Sensex news
- ✅ IPO listings & announcements
- ✅ Quarterly results & earnings
- ✅ Major stock movements (Reliance, TCS, Infosys, HDFC, etc.)
- ✅ Sector news (Banking, IT, Pharma, Auto)
- ✅ FII/DII activity
- ✅ Mergers & Acquisitions

**News Sources (All Legal):**
- Economic Times Markets & Stocks
- MoneyControl (Latest, Markets, Results)
- LiveMint Markets & Money
- Business Standard Markets
- Hindu Business Line

---

## 🎯 NEW Commands

### INDIAN STOCKS ONLY

**Run scraper once (India):**
```bash
./venv/bin/python scraper_india.py
```

**View Indian stock news:**
```bash
./venv/bin/python view_india.py
```

**Auto-run every 30 minutes (India only):**
```bash
./venv/bin/python scheduler_india.py
```

### FOREX ONLY

**Run scraper once (Forex):**
```bash
./venv/bin/python scraper_forex.py
```

**View Forex news:**
```bash
./venv/bin/python view_news.py
```

**Auto-run every 30 minutes (Forex only):**
```bash
./venv/bin/python scheduler_forex.py
```

### BOTH TOGETHER

**Auto-run both every 30 minutes:**
```bash
./venv/bin/python scheduler_both.py
```

---

## 📂 Database Structure

Everything is stored in **one database** (`forex_news.db`) with **separate tables**:

**Forex Tables:**
- `economic_events` - Forex economic calendar (USD, EUR, CAD, etc.)
- `news_articles` - Forex news from Reuters, Bloomberg, etc.

**Indian Stock Tables:**
- `india_economic_events` - Indian economic calendar (RBI, GDP, etc.)
- `india_stock_news` - Indian stock market news (Nifty, Sensex, etc.)

**Completely separate = No mixing of data!**

---

## 🎮 Interactive Viewers

### View Indian Stock News
```bash
./venv/bin/python view_india.py
```

**Menu Options:**
- [1] High Impact Events Only (RBI, GDP, Major Announcements)
- [2] All Indian Economic Events
- [3] Indian Stock Market News (All)
- [4] Nifty 50 / Sensex Specific News
- [5] Everything (Events + News)

### View Forex News
```bash
./venv/bin/python view_news.py
```

**Menu Options:**
- [1] High Impact Events Only (NFP, Interest Rates, etc.)
- [2] All Economic Events
- [3] Breaking News Articles
- [4] Everything

---

## ✅ Testing Results

### Indian Scraper Test (Just Run!)
```
✓ Collected 70 Indian stock news articles
✓ Sources: Economic Times, MoneyControl, LiveMint, etc.
✓ Time: ~20 seconds
✓ High/Medium impact only
```

**Sample News Found:**
- 🔴 PNB shares: Rs 9,000 crore impact from RBI rules
- 🔴 Gold price hits all-time high on Diwali
- 🟡 Nifty 50 Diwali Muhurat Trading stocks
- 🟡 Share India declares Q2 results
- 🟡 Buyback tax changes impact

### Forex Scraper Test (Already Working)
```
✓ Collected 19 economic events
✓ Collected 19 news articles
✓ Including CAD CPI data you requested
✓ Time: ~19 seconds
```

---

## 🚀 Recommended Usage

### Option 1: Run Separately (More Control)

**For Forex Trading:**
```bash
./venv/bin/python scheduler_forex.py
```

**For Indian Stock Trading:**
```bash
./venv/bin/python scheduler_india.py
```

### Option 2: Run Both Together

**For Both Markets:**
```bash
./venv/bin/python scheduler_both.py
```

This runs both scrapers every 30 minutes.

---

## 📊 What You Get

### Forex News (Unchanged)
- ✅ 19 economic events (CAD CPI, USD data, etc.)
- ✅ 19 news articles (Bloomberg, ForexLive, etc.)
- ✅ Major currencies: USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD

### Indian Stock News (NEW!)
- ✅ 70 stock news articles
- ✅ Nifty 50, Sensex, Bank Nifty coverage
- ✅ RBI policy, GDP, inflation events
- ✅ IPO, results, earnings announcements
- ✅ FII/DII activity tracking

---

## 💡 Usage Examples

### Morning Routine (India Trading)
```bash
# Check overnight Indian stock news
./venv/bin/python view_india.py

# Choose option 4 for Nifty-specific news
# Choose option 1 for high-impact events
```

### Before Trading CAD (Forex)
```bash
# Check CAD events
./venv/bin/python check_currency.py CAD
```

### All-Day Monitoring (Both Markets)
```bash
# Start both scrapers
./venv/bin/python scheduler_both.py

# Let it run in background
# Collects news every 30 minutes
```

---

## 🎯 Quick Command Reference

| Task | Command |
|------|---------|
| **Scrape India once** | `./venv/bin/python scraper_india.py` |
| **Scrape Forex once** | `./venv/bin/python scraper_forex.py` |
| **View India news** | `./venv/bin/python view_india.py` |
| **View Forex news** | `./venv/bin/python view_news.py` |
| **Auto-run India** | `./venv/bin/python scheduler_india.py` |
| **Auto-run Forex** | `./venv/bin/python scheduler_forex.py` |
| **Auto-run Both** | `./venv/bin/python scheduler_both.py` |
| **Check CAD events** | `./venv/bin/python check_currency.py CAD` |

---

## 📁 New Files Created

**Indian Stock Scrapers:**
- `india_news_scraper.py` - Scrapes Indian stock news
- `india_calendar_scraper.py` - Scrapes Indian economic calendar
- `scraper_india.py` - Main Indian scraper command
- `view_india.py` - Indian news viewer

**Forex Files (Renamed):**
- `scraper_forex.py` - Main Forex scraper (was `scraper.py`)
- `scheduler_forex.py` - Forex-only scheduler

**Combined:**
- `scheduler_both.py` - Runs both systems

**Database:**
- `database.py` - Updated with Indian stock tables

---

## ⚡ Performance

**Indian Scraper:**
- Time: ~20 seconds
- Sources: 9 Indian news sites
- Articles: 70+ per run (high/medium impact only)

**Forex Scraper:**
- Time: ~19 seconds
- Sources: 6 forex news sites + economic calendar
- Articles: 20-40 per run

**Both Together:**
- Time: ~40 seconds total
- Perfect for 30-minute intervals

---

## 🎓 Next Steps

### 1. Test Indian Scraper
```bash
./venv/bin/python scraper_india.py
./venv/bin/python view_india.py
```

### 2. Test Forex Scraper (Already Working)
```bash
./venv/bin/python scraper_forex.py
./venv/bin/python view_news.py
```

### 3. Choose Your Automation

**Trading Indian stocks only?**
```bash
./venv/bin/python scheduler_india.py
```

**Trading Forex only?**
```bash
./venv/bin/python scheduler_forex.py
```

**Trading both?**
```bash
./venv/bin/python scheduler_both.py
```

---

## 📊 Database Stats

Check what you've collected:
```bash
./venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('forex_news.db')
cursor = conn.cursor()

# Forex
cursor.execute('SELECT COUNT(*) FROM economic_events')
forex_events = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM news_articles')
forex_news = cursor.fetchone()[0]

# India
cursor.execute('SELECT COUNT(*) FROM india_economic_events')
india_events = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM india_stock_news')
india_news = cursor.fetchone()[0]

print('📊 Database Summary:')
print(f'  Forex Events: {forex_events}')
print(f'  Forex News: {forex_news}')
print(f'  India Events: {india_events}')
print(f'  India News: {india_news}')
print(f'  Total Items: {forex_events + forex_news + india_events + india_news}')

conn.close()
"
```

---

## ✅ Summary

**BEFORE:** Forex news only
**NOW:** Forex + Indian stocks (separate systems)

**Separate Commands:**
- ✅ `scraper_forex.py` for Forex
- ✅ `scraper_india.py` for Indian stocks
- ✅ `scheduler_both.py` for both together

**Separate Viewers:**
- ✅ `view_news.py` for Forex
- ✅ `view_india.py` for Indian stocks

**Separate Database Tables:**
- ✅ No mixing of data
- ✅ Easy to query each market separately

**Everything working and tested!** 🎉

---

**Ready to start? Try the Indian scraper:**
```bash
./venv/bin/python scraper_india.py
./venv/bin/python view_india.py
```
