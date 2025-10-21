import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

class ForexNewsScraper:
    """
    Scraper for forex and financial news from legal RSS feeds
    """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Public RSS feeds (all legal and free to access)
        self.rss_feeds = {
            'Reuters Markets': 'https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best',
            'Reuters Business': 'http://feeds.reuters.com/reuters/businessNews',
            'Bloomberg Markets': 'https://feeds.bloomberg.com/markets/news.rss',
            'ForexLive': 'https://www.forexlive.com/feed/news',
            'FXStreet': 'https://www.fxstreet.com/feeds/news',
            'DailyFX': 'https://www.dailyfx.com/feeds/market-news',
        }

        # Keywords that indicate market-moving news
        self.forex_keywords = [
            'federal reserve', 'fed', 'interest rate', 'inflation', 'cpi', 'ppi',
            'nfp', 'employment', 'gdp', 'central bank', 'ecb', 'boj', 'bank of england',
            'dollar', 'euro', 'pound', 'yen', 'currency', 'forex', 'fx',
            'fomc', 'monetary policy', 'rate decision', 'unemployment',
            'trade war', 'tariff', 'geopolitical', 'oil price', 'gold price'
        ]

    def scrape_rss_feed(self, feed_name, feed_url):
        """
        Scrape a single RSS feed
        Returns list of articles
        """
        articles = []

        try:
            print(f"Scraping {feed_name}...")
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:20]:  # Get latest 20 articles
                try:
                    title = entry.get('title', '')
                    summary = entry.get('summary', entry.get('description', ''))
                    url = entry.get('link', '')
                    published = entry.get('published', entry.get('updated', ''))

                    # Convert published date
                    try:
                        if published:
                            pub_date = datetime(*entry.published_parsed[:6])
                            published_at = pub_date.isoformat()
                        else:
                            published_at = datetime.now().isoformat()
                    except:
                        published_at = datetime.now().isoformat()

                    # Check if article is forex-related
                    if self._is_forex_related(title, summary):
                        articles.append({
                            'title': title,
                            'summary': summary,
                            'url': url,
                            'published_at': published_at,
                            'source': feed_name,
                            'category': 'forex'
                        })

                except Exception as e:
                    print(f"Error parsing entry: {e}")
                    continue

            print(f"Found {len(articles)} forex-related articles from {feed_name}")

        except Exception as e:
            print(f"Error scraping {feed_name}: {e}")

        return articles

    def _is_forex_related(self, title, summary):
        """
        Check if article is related to forex/market-moving news
        """
        text = (title + ' ' + summary).lower()

        for keyword in self.forex_keywords:
            if keyword in text:
                return True

        return False

    def scrape_all_feeds(self):
        """
        Scrape all RSS feeds
        Returns all forex-related articles
        """
        all_articles = []

        for feed_name, feed_url in self.rss_feeds.items():
            articles = self.scrape_rss_feed(feed_name, feed_url)
            all_articles.extend(articles)
            time.sleep(1)  # Be polite to servers

        print(f"\nTotal articles collected: {len(all_articles)}")
        return all_articles

    def get_breaking_news(self):
        """
        Get only the most recent breaking news (last 24 hours)
        """
        all_articles = self.scrape_all_feeds()

        # Filter for recent news (last 24 hours)
        recent_articles = []
        now = datetime.now()

        for article in all_articles:
            try:
                pub_date = datetime.fromisoformat(article['published_at'])
                hours_old = (now - pub_date).total_seconds() / 3600

                if hours_old <= 24:
                    recent_articles.append(article)
            except:
                # If we can't parse date, include it anyway
                recent_articles.append(article)

        print(f"Breaking news (last 24h): {len(recent_articles)} articles")
        return recent_articles

if __name__ == '__main__':
    # Test the scraper
    scraper = ForexNewsScraper()
    news = scraper.get_breaking_news()

    print("\n=== Latest Forex News ===")
    for article in news[:10]:  # Show first 10
        print(f"\n[{article['source']}] {article['title']}")
        print(f"Published: {article['published_at']}")
        print(f"URL: {article['url']}")
