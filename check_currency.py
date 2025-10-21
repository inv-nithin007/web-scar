#!/usr/bin/env python3
"""
Quick script to check events for a specific currency
Usage: python check_currency.py CAD
"""

import sys
import sqlite3

def check_currency(currency_code):
    """Check events for a specific currency"""
    conn = sqlite3.connect('forex_news.db')
    cursor = conn.cursor()

    # Get events for this currency
    cursor.execute('''
        SELECT event_time, event_name, impact, actual, forecast, previous
        FROM economic_events
        WHERE currency = ?
        ORDER BY event_time
    ''', (currency_code,))

    events = cursor.fetchall()

    print('=' * 80)
    print(f'📊 {currency_code} EVENTS - Market-Moving News')
    print('=' * 80)

    if not events:
        print(f'\nNo events found for {currency_code}')
        print('Available currencies: USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD')
    else:
        for event in events:
            event_time, event_name, impact, actual, forecast, previous = event

            # Show impact with emoji
            impact_emoji = '🔴' if impact == 'High' else '🟡' if impact == 'Medium' else '⚪'

            print(f'\n{impact_emoji} {event_name}')
            print(f'   Time: {event_time}')
            print(f'   Impact: {impact}')

            if actual:
                # Calculate surprise
                try:
                    act_val = float(actual.replace('%', '').replace('B', '').replace('K', '').replace('M', ''))
                    fore_val = float(forecast.replace('%', '').replace('B', '').replace('K', '').replace('M', '')) if forecast else None

                    if fore_val is not None:
                        surprise = act_val - fore_val
                        surprise_emoji = '📈' if surprise > 0 else '📉' if surprise < 0 else '➡️'
                        print(f'   Actual: {actual} {surprise_emoji}')
                    else:
                        print(f'   Actual: {actual}')
                except:
                    print(f'   Actual: {actual}')

            if forecast:
                print(f'   Forecast: {forecast}')
            if previous:
                print(f'   Previous: {previous}')

    print('\n' + '=' * 80)
    print(f'Total {currency_code} events: {len(events)}')
    print('=' * 80)

    conn.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        currency = sys.argv[1].upper()
    else:
        print("Usage: python check_currency.py <CURRENCY>")
        print("Example: python check_currency.py CAD")
        print("\nAvailable currencies: USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD")
        sys.exit(1)

    check_currency(currency)
