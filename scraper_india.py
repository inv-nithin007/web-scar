#!/usr/bin/env python3
"""
Indian Stock Market Scraper
Collects Nifty 50, Nifty Next 50, and major market-moving news for Indian stocks
"""

from database import ForexNewsDB
from india_calendar_scraper import IndianEconomicCalendarScraper
from india_news_scraper import IndianStockNewsScraper
from datetime import datetime

def run_india_scraper():
    """
    Main function to run Indian stock market scrapers
    """
    print("=" * 60)
    print(f"🇮🇳 Indian Stock Market Scraper Started at {datetime.now()}")
    print("=" * 60)

    # Initialize database
    db = ForexNewsDB()

    # 1. Scrape Indian Economic Calendar
    print("\n[1/2] Scraping Indian Economic Calendar...")
    print("-" * 60)
    calendar_scraper = IndianEconomicCalendarScraper()

    try:
        events = calendar_scraper.get_major_events()

        # Store events in database
        event_count = 0
        for event in events:
            if db.insert_india_event(event):
                event_count += 1

        print(f"✓ Stored {event_count} Indian economic events in database")
    except Exception as e:
        print(f"✗ Error scraping Indian calendar: {e}")

    # 2. Scrape Indian Stock News
    print("\n[2/2] Scraping Indian Stock Market News...")
    print("-" * 60)
    news_scraper = IndianStockNewsScraper()

    try:
        articles = news_scraper.get_high_impact_news()

        # Store articles in database
        article_count = 0
        for article in articles:
            if db.insert_india_news(article):
                article_count += 1

        print(f"✓ Stored {article_count} Indian stock news articles in database")
    except Exception as e:
        print(f"✗ Error scraping Indian news: {e}")

    print("\n" + "=" * 60)
    print(f"Scraping completed at {datetime.now()}")
    print("=" * 60)

    # Show summary with better breakdown
    print("\n📊 Database Summary:")

    # Get impact breakdown
    import sqlite3
    conn = sqlite3.connect('forex_news.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM india_economic_events WHERE impact = 'High'")
    high_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM india_economic_events WHERE impact = 'Medium'")
    medium_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM india_stock_news WHERE category = 'High'")
    high_news = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM india_stock_news WHERE category = 'Medium'")
    medium_news = cursor.fetchone()[0]

    conn.close()

    print(f"  Economic Events:")
    print(f"    🔴 High impact: {high_events}")
    print(f"    🟡 Medium impact: {medium_events}")
    print(f"  Stock Market News:")
    print(f"    🔴 High impact: {high_news}")
    print(f"    🟡 Medium impact: {medium_news}")
    print(f"\nDatabase: forex_news.db (india_economic_events & india_stock_news tables)")
    print("Run 'python view_india.py' to view collected Indian stock data\n")

if __name__ == '__main__':
    run_india_scraper()
