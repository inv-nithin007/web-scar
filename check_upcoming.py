#!/usr/bin/env python3
"""
Check upcoming forex and Indian stock events
Shows only events that haven't happened yet
"""

import sqlite3
from datetime import datetime

def check_upcoming_forex():
    """Check upcoming forex events"""
    conn = sqlite3.connect('forex_news.db')
    cursor = conn.cursor()

    now = datetime.now()
    current_hour = now.hour

    cursor.execute('''
        SELECT event_time, currency, event_name, impact, forecast, previous
        FROM economic_events
        ORDER BY event_time
    ''')

    events = cursor.fetchall()

    print("=" * 80)
    print("⏰ UPCOMING FOREX EVENTS TODAY")
    print("=" * 80)

    upcoming_count = 0
    for event_time, currency, event_name, impact, forecast, previous in events:
        # Extract hour
        try:
            if ' ' in event_time:
                time_str = event_time.split()[1]
            else:
                time_str = event_time

            event_hour = int(time_str.split(':')[0])

            # Only show upcoming events
            if event_hour >= current_hour:
                icon = '🔴' if impact == 'High' else '🟡' if impact == 'Medium' else '⚪'

                print(f"\n{icon} {time_str} | {currency} | {event_name}")
                print(f"   Impact: {impact}")
                if forecast:
                    print(f"   Forecast: {forecast} | Previous: {previous}")

                upcoming_count += 1
        except:
            continue

    if upcoming_count == 0:
        print("\n✅ All events for today have passed!")
        print("Next events will be tomorrow.")
    else:
        print(f"\n{'=' * 80}")
        print(f"Found {upcoming_count} upcoming events")
        print("=" * 80)

    conn.close()

def check_upcoming_india():
    """Check upcoming Indian stock news"""
    conn = sqlite3.connect('forex_news.db')
    cursor = conn.cursor()

    # Get recent Indian stock news (since India doesn't have timed events like forex)
    cursor.execute('''
        SELECT title, category, source, published_at
        FROM india_stock_news
        ORDER BY published_at DESC
        LIMIT 10
    ''')

    news = cursor.fetchall()

    print("\n" + "=" * 80)
    print("📰 LATEST INDIAN STOCK NEWS")
    print("=" * 80)

    for title, category, source, published_at in news:
        icon = '🔴' if category == 'High' else '🟡' if category == 'Medium' else '⚪'

        pub_time = published_at.split('T')[1][:5] if 'T' in published_at else ''

        print(f"\n{icon} [{source}] {title[:60]}")
        print(f"   Published: {pub_time} | Impact: {category}")

    conn.close()

if __name__ == '__main__':
    import sys

    print(f"\n🕐 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'india':
        check_upcoming_india()
    elif len(sys.argv) > 1 and sys.argv[1].lower() == 'forex':
        check_upcoming_forex()
    else:
        # Show both
        check_upcoming_forex()
        check_upcoming_india()

    print("\n")
