# Getting Started with Your Forex News Scraper

## ✅ Setup Complete!

Your forex news scraper is ready to use. Here's everything you need to know:

## 📁 What Was Created

```
forex-news-scraper/
├── scraper.py                      # Main scraper (run this!)
├── scheduler.py                    # Auto-run every 30 minutes
├── view_news.py                    # View collected news
├── database.py                     # Database handler
├── economic_calendar_scraper.py    # Economic events scraper
├── news_scraper.py                 # RSS news scraper
├── run.sh                          # Easy startup script
├── requirements.txt                # Python dependencies
├── README.md                       # Full documentation
├── QUICKSTART.md                   # Quick reference
└── venv/                           # Virtual environment (already set up!)
```

## 🚀 Quick Start (3 Steps)

### Step 1: Run the scraper once to test
```bash
./venv/bin/python scraper.py
```

This will:
- ✅ Collect economic calendar events (NFP, GDP, Interest Rates, etc.)
- ✅ Collect breaking forex news from Reuters, Bloomberg, etc.
- ✅ Store everything in `forex_news.db` database
- ✅ Take about 10-30 seconds to complete

### Step 2: View the collected news
```bash
./venv/bin/python view_news.py
```

Choose what to view:
- Option 1: High impact events only (most important!)
- Option 2: All economic events
- Option 3: Breaking news articles
- Option 4: Everything

### Step 3: Run automatically every 30 minutes
```bash
./venv/bin/python scheduler.py
```

This will:
- Run the scraper immediately
- Then run every 30 minutes automatically
- Keep running until you press Ctrl+C

## 🎯 What News Gets Collected?

### High Impact Economic Events
- ✅ Non-Farm Payrolls (NFP)
- ✅ GDP Reports
- ✅ Interest Rate Decisions
- ✅ Inflation Data (CPI, PPI)
- ✅ Employment Reports
- ✅ Central Bank Announcements (Fed, ECB, BoJ, BoE)
- ✅ FOMC Meetings

### Breaking News Sources
- ✅ Reuters Business & Markets
- ✅ Bloomberg Markets
- ✅ ForexLive
- ✅ FXStreet
- ✅ DailyFX

### Major Currency Pairs
- USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD

## ⚖️ Legal & Ethical

All sources used are:
- ✅ **Publicly available** (no login required)
- ✅ **Legal to access** (RSS feeds and public calendars)
- ✅ **Respectful** (rate-limited, polite scraping)

## 💡 Tips for Success

### 1. Start Small
Run the scraper once manually to see how it works before scheduling.

### 2. Check Data Regularly
```bash
./venv/bin/python view_news.py
```

### 3. Run in Background (Optional)
For Linux/Mac, to keep it running even after closing terminal:
```bash
nohup ./venv/bin/python scheduler.py > scraper.log 2>&1 &
```

View logs:
```bash
tail -f scraper.log
```

Stop background process:
```bash
ps aux | grep scheduler
kill <process_id>
```

### 4. Customize Frequency
Edit `scheduler.py` line 36 to change timing:
- Every 30 minutes (default): `schedule.every(30).minutes.do(job)`
- Every hour: `schedule.every(1).hour.do(job)`
- Every 15 minutes: `schedule.every(15).minutes.do(job)`

### 5. Filter Currencies
Edit `economic_calendar_scraper.py` line 118 to focus on specific currencies:
```python
major_currencies = ['USD', 'EUR']  # Only USD and EUR
```

## 🐛 Troubleshooting

### "No module named 'requests'"
You need to activate virtual environment first:
```bash
./venv/bin/python scraper.py
```
NOT just `python scraper.py`

### "No data collected"
- Check your internet connection
- Some websites may temporarily block requests
- Wait 5 minutes and try again
- Company firewall may block some sites

### "Permission denied"
Run:
```bash
chmod +x run.sh scraper.py scheduler.py view_news.py
```

### Company PC Restrictions
If certain websites are blocked:
1. The scraper will skip blocked sources
2. You'll still get data from accessible sources
3. Check which sites are blocked and remove them from `news_scraper.py`

## 📊 Understanding the Data

### Impact Levels
- 🔴 **High**: Major market movers (NFP, Interest Rates, GDP)
- 🟡 **Medium**: Moderate impact (PMI, Retail Sales)
- ⚪ **Low**: Minor impact (usually filtered out)

### Event Fields
- **Event Time**: When the data is released
- **Currency**: Which currency pair is affected
- **Event Name**: What is being announced
- **Actual**: The actual number released
- **Forecast**: What analysts predicted
- **Previous**: Last period's value

### Trading Logic
- If Actual > Forecast = Usually currency strengthens
- If Actual < Forecast = Usually currency weakens
- Bigger difference = Bigger market move

## 🎓 Next Steps

Once you have data collecting:

1. **Build Alerts**: Send yourself notifications for high-impact events
2. **Backtest Strategies**: Use historical data to test trading ideas
3. **Create Dashboard**: Build a web interface to view news
4. **Automate Trading**: Connect to trading platform (advanced)
5. **Export Data**: Use pandas to export to Excel/CSV for analysis

## 📚 Additional Resources

- `README.md` - Full documentation
- `QUICKSTART.md` - Command reference
- Database location: `forex_news.db`

## ⚠️ Important Notes

1. **Not Financial Advice**: This is a data collection tool only
2. **Test First**: Always test manually before automating
3. **Respect Sources**: Don't hammer websites with requests
4. **Company Policy**: Check if your company allows web scraping
5. **Market Hours**: News is most frequent during market hours

---

## Ready? Let's Start!

```bash
# Test the installation
./venv/bin/python -c "import requests; print('✅ Ready to go!')"

# Run the scraper once
./venv/bin/python scraper.py

# View the news
./venv/bin/python view_news.py

# Start automatic collection
./venv/bin/python scheduler.py
```

**Happy scraping! 📈**
