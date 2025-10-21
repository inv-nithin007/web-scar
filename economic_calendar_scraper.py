import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

class EconomicCalendarScraper:
    """
    Scraper for economic calendar data
    Uses Investing.com's public economic calendar
    """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.base_url = 'https://www.investing.com'

    def scrape_investing_calendar(self):
        """
        Scrape economic calendar from Investing.com
        Returns list of economic events
        """
        events = []

        try:
            # Use Investing.com's economic calendar API (public endpoint)
            url = f"{self.base_url}/economic-calendar/"

            print(f"Scraping economic calendar from: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find economic events in the calendar
                event_rows = soup.find_all('tr', {'class': 'js-event-item'})

                for row in event_rows:
                    try:
                        # Extract event data
                        event = self._parse_investing_event(row)
                        if event and event.get('impact') in ['High', 'Medium']:
                            events.append(event)
                    except Exception as e:
                        print(f"Error parsing event row: {e}")
                        continue

                print(f"Found {len(events)} high/medium impact events")
            else:
                print(f"Failed to fetch calendar: Status {response.status_code}")

        except Exception as e:
            print(f"Error scraping Investing.com calendar: {e}")

        return events

    def _parse_investing_event(self, row):
        """Parse individual event row from Investing.com"""
        try:
            tds = row.find_all('td')
            if len(tds) < 7:
                return None

            # TD structure: [0]=time, [1]=currency, [2]=sentiment, [3]=event, [4]=actual, [5]=forecast, [6]=previous
            event_time = tds[0].text.strip()
            currency = tds[1].text.strip()
            event_name = tds[3].text.strip()

            # Get impact level from title attribute and icon count
            sentiment_td = tds[2]
            volatility_title = sentiment_td.get('title', '').lower()

            if 'high' in volatility_title:
                impact = 'High'
            elif 'moderate' in volatility_title or 'medium' in volatility_title:
                impact = 'Medium'
            else:
                # Also check by counting filled icons
                filled_icons = sentiment_td.find_all('i', class_='grayFullBullishIcon')
                icon_count = len(filled_icons)
                if icon_count >= 3:
                    impact = 'High'
                elif icon_count == 2:
                    impact = 'Medium'
                else:
                    impact = 'Low'

            # Get actual, forecast, previous values
            actual = tds[4].text.strip()
            forecast = tds[5].text.strip()
            previous = tds[6].text.strip()

            # Get event datetime
            timestamp = row.get('data-event-datetime', '')

            if timestamp:
                event_datetime = timestamp
            else:
                # Use today's date + time
                today = datetime.now().strftime('%Y-%m-%d')
                event_datetime = f"{today} {event_time}"

            return {
                'event_time': event_datetime,
                'currency': currency,
                'event_name': event_name,
                'impact': impact,
                'actual': actual,
                'forecast': forecast,
                'previous': previous,
                'source': 'Investing.com'
            }

        except Exception as e:
            print(f"Error parsing event: {e}")
            return None

    def get_major_market_events(self):
        """
        Get major market-moving events
        Focuses on high and medium impact news
        """
        all_events = self.scrape_investing_calendar()

        # Filter for high and medium impact
        major_events = [e for e in all_events if e.get('impact') in ['High', 'Medium']]

        # Filter for major currencies
        major_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUD', 'NZD']
        major_events = [e for e in major_events if e.get('currency') in major_currencies]

        print(f"Found {len(major_events)} major market-moving events (High + Medium impact)")
        return major_events

if __name__ == '__main__':
    # Test the scraper
    scraper = EconomicCalendarScraper()
    events = scraper.get_major_market_events()

    print("\n=== Major Market Events ===")
    for event in events[:10]:  # Show first 10
        print(f"{event['event_time']} | {event['currency']} | {event['event_name']} | Impact: {event['impact']}")
