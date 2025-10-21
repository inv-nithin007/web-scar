#!/usr/bin/env python3
"""
Main Forex News Scraper
Collects market-moving news from multiple sources and stores in database
"""

from database import ForexNewsDB
from economic_calendar_scraper import EconomicCalendarScraper
from news_scraper import ForexNewsScraper
from datetime import datetime

def run_scraper():
    """
    Main function to run all scrapers
    """
    print("=" * 60)
    print(f"Forex News Scraper Started at {datetime.now()}")
    print("=" * 60)

    # Initialize database
    db = ForexNewsDB()

    # 1. Scrape Economic Calendar
    print("\n[1/2] Scraping Economic Calendar...")
    print("-" * 60)
    calendar_scraper = EconomicCalendarScraper()

    try:
        events = calendar_scraper.get_major_market_events()

        # Store events in database
        event_count = 0
        for event in events:
            if db.insert_economic_event(event):
                event_count += 1

        print(f"✓ Stored {event_count} economic events in database")
    except Exception as e:
        print(f"✗ Error scraping calendar: {e}")

    # 2. Scrape News Articles
    print("\n[2/2] Scraping Breaking News...")
    print("-" * 60)
    news_scraper = ForexNewsScraper()

    try:
        articles = news_scraper.get_breaking_news()

        # Store articles in database
        article_count = 0
        for article in articles:
            if db.insert_news_article(article):
                article_count += 1

        print(f"✓ Stored {article_count} news articles in database")
    except Exception as e:
        print(f"✗ Error scraping news: {e}")

    print("\n" + "=" * 60)
    print(f"Scraping completed at {datetime.now()}")
    print("=" * 60)

    # Show summary with better breakdown
    print("\n📊 Database Summary:")

    # Get impact breakdown
    import sqlite3
    conn = sqlite3.connect('forex_news.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM economic_events WHERE impact = 'High'")
    high_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM economic_events WHERE impact = 'Medium'")
    medium_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM news_articles")
    news_count = cursor.fetchone()[0]

    conn.close()

    print(f"  Economic Events:")
    print(f"    🔴 High impact: {high_count}")
    print(f"    🟡 Medium impact: {medium_count}")
    print(f"  📰 News articles: {news_count}")
    print(f"\nDatabase: forex_news.db")
    print("Run 'python view_news.py' to view collected data\n")

if __name__ == '__main__':
    run_scraper()
