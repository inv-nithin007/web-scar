#!/usr/bin/env python3
"""
Indian Stock News Viewer - Display collected Indian stock market data
"""

from database import ForexNewsDB
from datetime import datetime
import sys

def display_india_events(limit=20):
    """Display recent Indian economic events"""
    db = ForexNewsDB()
    events = db.get_recent_india_events(limit)

    print("\n" + "=" * 80)
    print("📅 INDIAN ECONOMIC CALENDAR - MARKET-MOVING EVENTS")
    print("=" * 80)

    if not events:
        print("No Indian events found. Run the scraper first: python scraper_india.py")
        return

    for event in events:
        event_id, event_time, event_name, impact, actual, forecast, previous, source, country, scraped_at = event

        print(f"\n{'='*80}")
        print(f"🕐 Time: {event_time}")
        print(f"📊 Event: {event_name}")
        print(f"⚡ Impact: {impact}")

        if actual:
            print(f"   Actual: {actual}")
        if forecast:
            print(f"   Forecast: {forecast}")
        if previous:
            print(f"   Previous: {previous}")

        print(f"   Source: {source}")

def display_high_impact_events(limit=15):
    """Display only high impact Indian events"""
    db = ForexNewsDB()
    events = db.get_high_impact_india_events(limit)

    print("\n" + "=" * 80)
    print("⚡ HIGH IMPACT INDIAN EVENTS - MAJOR MARKET MOVERS")
    print("=" * 80)

    if not events:
        print("No high impact events found.")
        return

    for event in events:
        event_id, event_time, event_name, impact, actual, forecast, previous, source, country, scraped_at = event

        print(f"\n🔴 {event_name}")
        print(f"   Time: {event_time}")
        if actual:
            print(f"   Actual: {actual} | Forecast: {forecast} | Previous: {previous}")
        else:
            print(f"   Forecast: {forecast} | Previous: {previous}")

def display_india_news(limit=20):
    """Display recent Indian stock news"""
    db = ForexNewsDB()
    articles = db.get_recent_india_news(limit)

    print("\n" + "=" * 80)
    print("📰 INDIAN STOCK MARKET NEWS - NIFTY 50 & MORE")
    print("=" * 80)

    if not articles:
        print("No Indian stock news found. Run the scraper first: python scraper_india.py")
        return

    for article in articles:
        article_id, title, summary, url, published_at, source, category, scraped_at = article

        # Impact indicator
        if category == 'High':
            indicator = '🔴'
        elif category == 'Medium':
            indicator = '🟡'
        else:
            indicator = '⚪'

        print(f"\n{'='*80}")
        print(f"{indicator} {title}")
        print(f"📅 Published: {published_at}")
        print(f"📡 Source: {source}")
        print(f"⚡ Impact: {category}")
        if summary:
            summary_short = summary[:200] + "..." if len(summary) > 200 else summary
            print(f"📝 {summary_short}")
        print(f"🔗 {url}")

def display_nifty_news(limit=15):
    """Display Nifty 50 / Nifty Next 50 specific news"""
    db = ForexNewsDB()
    all_news = db.get_recent_india_news(100)

    # Filter for Nifty-specific news
    nifty_keywords = ['nifty 50', 'nifty', 'nifty next 50', 'nifty bank', 'bank nifty', 'sensex']
    nifty_news = []

    for article in all_news:
        article_id, title, summary, url, published_at, source, category, scraped_at = article
        text = (title + ' ' + (summary or '')).lower()

        for keyword in nifty_keywords:
            if keyword in text:
                nifty_news.append(article)
                break

    print("\n" + "=" * 80)
    print("📈 NIFTY 50 / SENSEX SPECIFIC NEWS")
    print("=" * 80)

    if not nifty_news:
        print("No Nifty-specific news found.")
        return

    for article in nifty_news[:limit]:
        article_id, title, summary, url, published_at, source, category, scraped_at = article

        if category == 'High':
            indicator = '🔴'
        elif category == 'Medium':
            indicator = '🟡'
        else:
            indicator = '⚪'

        print(f"\n{indicator} [{source}] {title}")
        print(f"   Published: {published_at} | Impact: {category}")
        print(f"   {url[:70]}...")

def display_menu():
    """Display interactive menu"""
    print("\n" + "=" * 80)
    print("🇮🇳 INDIAN STOCK MARKET NEWS VIEWER")
    print("=" * 80)
    print("\nSelect what you want to view:")
    print("  [1] High Impact Events Only (RBI, GDP, Major Announcements)")
    print("  [2] All Indian Economic Events")
    print("  [3] Indian Stock Market News (All)")
    print("  [4] Nifty 50 / Sensex Specific News")
    print("  [5] Everything (Events + News)")
    print("  [Q] Quit")
    print("=" * 80)

def main():
    """Main viewer function"""

    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

    if choice == '1':
        display_high_impact_events()
    elif choice == '2':
        display_india_events()
    elif choice == '3':
        display_india_news()
    elif choice == '4':
        display_nifty_news()
    elif choice == '5':
        display_high_impact_events()
        display_india_news()
    elif choice.lower() == 'q':
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")

    print("\n" + "=" * 80)
    print("To run Indian scraper: python scraper_india.py")
    print("To run Forex scraper: python scraper_forex.py")
    print("To auto-run both: python scheduler.py")
    print("=" * 80 + "\n")

if __name__ == '__main__':
    main()
