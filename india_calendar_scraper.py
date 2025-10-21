import requests
from bs4 import BeautifulSoup
from datetime import datetime

class IndianEconomicCalendarScraper:
    """
    Scraper for Indian economic calendar data
    Focus: RBI policy, GDP, inflation, IIP, and other market-moving events
    """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.base_url = 'https://www.investing.com'

    def scrape_india_calendar(self):
        """
        Scrape Indian economic calendar from Investing.com
        Returns list of Indian economic events
        """
        events = []

        try:
            # Use Investing.com's India economic calendar
            url = f"{self.base_url}/economic-calendar/"

            print(f"Scraping Indian economic calendar from: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find economic events
                event_rows = soup.find_all('tr', {'class': 'js-event-item'})

                for row in event_rows:
                    try:
                        event = self._parse_event(row)

                        # Filter for Indian events only
                        if event and event.get('currency') == 'INR':
                            if event.get('impact') in ['High', 'Medium']:
                                events.append(event)
                    except Exception as e:
                        print(f"Error parsing event row: {e}")
                        continue

                print(f"Found {len(events)} Indian economic events")
            else:
                print(f"Failed to fetch calendar: Status {response.status_code}")

        except Exception as e:
            print(f"Error scraping India calendar: {e}")

        return events

    def _parse_event(self, row):
        """Parse individual event row"""
        try:
            tds = row.find_all('td')
            if len(tds) < 7:
                return None

            # Extract data
            event_time = tds[0].text.strip()
            currency = tds[1].text.strip()
            event_name = tds[3].text.strip()

            # Get impact level
            sentiment_td = tds[2]
            volatility_title = sentiment_td.get('title', '').lower()

            if 'high' in volatility_title:
                impact = 'High'
            elif 'moderate' in volatility_title or 'medium' in volatility_title:
                impact = 'Medium'
            else:
                filled_icons = sentiment_td.find_all('i', class_='grayFullBullishIcon')
                icon_count = len(filled_icons)
                if icon_count >= 3:
                    impact = 'High'
                elif icon_count == 2:
                    impact = 'Medium'
                else:
                    impact = 'Low'

            # Get values
            actual = tds[4].text.strip()
            forecast = tds[5].text.strip()
            previous = tds[6].text.strip()

            # Get datetime
            timestamp = row.get('data-event-datetime', '')
            if timestamp:
                event_datetime = timestamp
            else:
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
                'source': 'Investing.com India',
                'country': 'India'
            }

        except Exception as e:
            print(f"Error parsing event: {e}")
            return None

    def get_major_events(self):
        """
        Get major Indian economic events
        Focus on RBI, GDP, inflation, etc.
        """
        all_events = self.scrape_india_calendar()

        # Filter for high impact
        major_events = [e for e in all_events if e.get('impact') in ['High', 'Medium']]

        print(f"Found {len(major_events)} major Indian economic events")
        return major_events

    def get_rbi_events(self):
        """
        Get RBI-specific events (monetary policy, rate decisions)
        """
        all_events = self.scrape_india_calendar()

        # Filter for RBI events
        rbi_keywords = ['rbi', 'reserve bank', 'repo rate', 'monetary policy', 'mpc']
        rbi_events = []

        for event in all_events:
            event_name = event.get('event_name', '').lower()
            for keyword in rbi_keywords:
                if keyword in event_name:
                    rbi_events.append(event)
                    break

        print(f"Found {len(rbi_events)} RBI events")
        return rbi_events

if __name__ == '__main__':
    # Test the scraper
    scraper = IndianEconomicCalendarScraper()
    events = scraper.get_major_events()

    print("\n=== Major Indian Economic Events ===")
    for event in events[:10]:  # Show first 10
        print(f"{event['event_time']} | {event['event_name']} | Impact: {event['impact']}")
