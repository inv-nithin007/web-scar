#!/usr/bin/env python3
"""
News Viewer - Display collected forex news
"""

from database import ForexNewsDB
from datetime import datetime
import sys

def display_economic_events(limit=20):
    """Display recent economic events"""
    db = ForexNewsDB()
    events = db.get_recent_events(limit)

    print("\n" + "=" * 80)
    print("📅 ECONOMIC CALENDAR - HIGH IMPACT EVENTS")
    print("=" * 80)

    if not events:
        print("No events found. Run the scraper first: python scraper.py")
        return

    for event in events:
        event_id, event_time, currency, event_name, impact, actual, forecast, previous, source, scraped_at = event

        print(f"\n{'='*80}")
        print(f"🕐 Time: {event_time}")
        print(f"💱 Currency: {currency}")
        print(f"📊 Event: {event_name}")
        print(f"⚡ Impact: {impact}")

        if actual:
            print(f"   Actual: {actual}")
        if forecast:
            print(f"   Forecast: {forecast}")
        if previous:
            print(f"   Previous: {previous}")

        print(f"   Source: {source}")

def display_high_impact_only(limit=15):
    """Display only high impact events"""
    db = ForexNewsDB()
    events = db.get_high_impact_events(limit)

    print("\n" + "=" * 80)
    print("⚡ HIGH IMPACT EVENTS ONLY - MAJOR MARKET MOVERS")
    print("=" * 80)

    if not events:
        print("No high impact events found.")
        return

    for event in events:
        event_id, event_time, currency, event_name, impact, actual, forecast, previous, source, scraped_at = event

        print(f"\n🔴 {currency} | {event_name}")
        print(f"   Time: {event_time}")
        if actual:
            print(f"   Actual: {actual} | Forecast: {forecast} | Previous: {previous}")
        else:
            print(f"   Forecast: {forecast} | Previous: {previous}")

def display_news_articles(limit=20):
    """Display recent news articles"""
    db = ForexNewsDB()
    articles = db.get_recent_news(limit)

    print("\n" + "=" * 80)
    print("📰 BREAKING FOREX NEWS")
    print("=" * 80)

    if not articles:
        print("No articles found. Run the scraper first: python scraper.py")
        return

    for article in articles:
        article_id, title, summary, url, published_at, source, category, scraped_at = article

        print(f"\n{'='*80}")
        print(f"📌 {title}")
        print(f"🗓  Published: {published_at}")
        print(f"📡 Source: {source}")
        if summary:
            # Truncate summary to 200 chars
            summary_short = summary[:200] + "..." if len(summary) > 200 else summary
            print(f"📝 {summary_short}")
        print(f"🔗 {url}")

def display_menu():
    """Display interactive menu"""
    print("\n" + "=" * 80)
    print("FOREX NEWS SCRAPER - VIEWER")
    print("=" * 80)
    print("\nSelect what you want to view:")
    print("  [1] High Impact Events Only (Major Market Movers)")
    print("  [2] All Economic Events")
    print("  [3] Breaking News Articles")
    print("  [4] Everything (Events + News)")
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
        display_high_impact_only()
    elif choice == '2':
        display_economic_events()
    elif choice == '3':
        display_news_articles()
    elif choice == '4':
        display_high_impact_only()
        display_news_articles()
    elif choice.lower() == 'q':
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")

    print("\n" + "=" * 80)
    print("To run scraper: python scraper.py")
    print("To auto-run every 30min: python scheduler.py")
    print("=" * 80 + "\n")

if __name__ == '__main__':
    main()
