#!/bin/bash
# Master control script for News Scrapers

clear
echo "========================================"
echo "📊 NEWS SCRAPER CONTROL CENTER"
echo "========================================"
echo ""
echo "What would you like to run?"
echo ""
echo "FOREX:"
echo "  [1] Run Forex scraper once"
echo "  [2] Run Forex scheduler (every 30 min)"
echo "  [3] View Forex news"
echo ""
echo "INDIAN STOCKS:"
echo "  [4] Run Indian scraper once"
echo "  [5] Run Indian scheduler (every 30 min)"
echo "  [6] View Indian stock news"
echo ""
echo "BOTH:"
echo "  [7] Run both scrapers once"
echo "  [8] Run both schedulers (every 30 min)"
echo ""
echo "OTHER:"
echo "  [9] Check database stats"
echo "  [Q] Quit"
echo ""
echo "========================================"
read -p "Enter choice: " choice

case $choice in
  1)
    echo "💱 Running Forex scraper..."
    ./venv/bin/python scraper_forex.py
    ;;
  2)
    echo "💱 Starting Forex scheduler (Press Ctrl+C to stop)..."
    ./venv/bin/python scheduler_forex.py
    ;;
  3)
    ./venv/bin/python view_news.py
    ;;
  4)
    echo "🇮🇳 Running Indian stock scraper..."
    ./venv/bin/python scraper_india.py
    ;;
  5)
    echo "🇮🇳 Starting Indian scheduler (Press Ctrl+C to stop)..."
    ./venv/bin/python scheduler_india.py
    ;;
  6)
    ./venv/bin/python view_india.py
    ;;
  7)
    echo "🌍 Running both scrapers..."
    ./venv/bin/python scraper_forex.py
    echo ""
    echo "---"
    echo ""
    ./venv/bin/python scraper_india.py
    ;;
  8)
    echo "🌍 Starting both schedulers (Press Ctrl+C to stop)..."
    ./venv/bin/python scheduler_both.py
    ;;
  9)
    ./venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('forex_news.db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(*) FROM economic_events')
forex_events = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM news_articles')
forex_news = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM india_economic_events')
india_events = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM india_stock_news')
india_news = cursor.fetchone()[0]

print('')
print('=' * 50)
print('📊 DATABASE STATISTICS')
print('=' * 50)
print('')
print('💱 FOREX:')
print(f'  Economic Events: {forex_events}')
print(f'  News Articles: {forex_news}')
print(f'  Subtotal: {forex_events + forex_news}')
print('')
print('🇮🇳 INDIAN STOCKS:')
print(f'  Economic Events: {india_events}')
print(f'  News Articles: {india_news}')
print(f'  Subtotal: {india_events + india_news}')
print('')
print('=' * 50)
print(f'📈 TOTAL ITEMS: {forex_events + forex_news + india_events + india_news}')
print('=' * 50)
print('')

conn.close()
"
    ;;
  q|Q)
    echo "Goodbye!"
    exit 0
    ;;
  *)
    echo "Invalid choice!"
    ;;
esac

echo ""
echo "========================================"
echo "Run './run_scraper.sh' again for menu"
echo "========================================"
