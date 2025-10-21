import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

class IndianStockNewsScraper:
    """
    Scraper for Indian stock market news from legal RSS feeds
    Focus: Nifty 50, Nifty Next 50, and market-moving events
    """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Public RSS feeds for Indian stock market (all legal and free)
        self.rss_feeds = {
            'Economic Times Markets': 'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms',
            'Economic Times Stocks': 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms',
            'MoneyControl Latest': 'https://www.moneycontrol.com/rss/latestnews.xml',
            'MoneyControl Markets': 'https://www.moneycontrol.com/rss/marketreports.xml',
            'MoneyControl Results': 'https://www.moneycontrol.com/rss/results.xml',
            'LiveMint Markets': 'https://www.livemint.com/rss/markets',
            'LiveMint Money': 'https://www.livemint.com/rss/money',
            'Business Standard Markets': 'https://www.business-standard.com/rss/markets-106.rss',
            'Hindu Business Line': 'https://www.thehindubusinessline.com/markets/stock-markets/feeder/default.rss',
        }

        # Keywords for Indian stock market news
        self.stock_keywords = [
            # Indices
            'nifty', 'sensex', 'nifty 50', 'nifty next 50', 'bank nifty', 'nifty bank',
            'nifty midcap', 'nifty smallcap', 'bse', 'nse',

            # Economic indicators
            'rbi', 'reserve bank', 'monetary policy', 'repo rate', 'interest rate',
            'inflation', 'cpi', 'wpi', 'iip', 'gdp', 'fiscal deficit',
            'budget', 'sebi', 'taxation', 'gst',

            # Market events
            'ipo', 'listing', 'results', 'earnings', 'dividend', 'buyback',
            'merger', 'acquisition', 'stake sale', 'fii', 'dii',
            'foreign institutional', 'domestic institutional',

            # Sectors
            'banking sector', 'it sector', 'pharma sector', 'auto sector',
            'real estate', 'infrastructure', 'metal stocks',

            # Major stocks (Nifty 50 companies)
            'reliance', 'tcs', 'infosys', 'hdfc bank', 'icici bank',
            'state bank', 'bharti airtel', 'itc', 'wipro', 'hcl tech',
            'asian paints', 'bajaj', 'maruti', 'titan', 'adani',

            # Market moves
            'rally', 'crash', 'correction', 'bull market', 'bear market',
            'circuit breaker', 'upper circuit', 'lower circuit',
            'market crash', 'market surge', 'all-time high', 'record high',
        ]

    def scrape_rss_feed(self, feed_name, feed_url):
        """
        Scrape a single RSS feed for Indian stock news
        Returns list of articles
        """
        articles = []

        try:
            print(f"Scraping {feed_name}...")
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:30]:  # Get latest 30 articles
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

                    # Check if article is stock market related
                    if self._is_stock_related(title, summary):
                        # Determine impact/category
                        category = self._categorize_news(title, summary)

                        articles.append({
                            'title': title,
                            'summary': summary,
                            'url': url,
                            'published_at': published_at,
                            'source': feed_name,
                            'category': category
                        })

                except Exception as e:
                    print(f"Error parsing entry: {e}")
                    continue

            print(f"Found {len(articles)} stock-related articles from {feed_name}")

        except Exception as e:
            print(f"Error scraping {feed_name}: {e}")

        return articles

    def _is_stock_related(self, title, summary):
        """
        Check if article is related to Indian stock market
        """
        text = (title + ' ' + summary).lower()

        for keyword in self.stock_keywords:
            if keyword in text:
                return True

        return False

    def _categorize_news(self, title, summary):
        """
        Categorize news as High, Medium, or Low impact
        """
        text = (title + ' ' + summary).lower()

        # High impact indicators
        high_impact_keywords = [
            'rbi', 'monetary policy', 'repo rate', 'budget', 'gdp',
            'crash', 'surge', 'all-time high', 'record high',
            'circuit breaker', 'sebi action', 'major announcement',
            'emergency', 'crisis', 'ban', 'regulation'
        ]

        # Medium impact indicators
        medium_impact_keywords = [
            'nifty', 'sensex', 'results', 'earnings', 'dividend',
            'ipo', 'listing', 'merger', 'acquisition', 'fii', 'dii',
            'inflation', 'q1', 'q2', 'q3', 'q4', 'quarterly'
        ]

        for keyword in high_impact_keywords:
            if keyword in text:
                return 'High'

        for keyword in medium_impact_keywords:
            if keyword in text:
                return 'Medium'

        return 'Low'

    def scrape_all_feeds(self):
        """
        Scrape all Indian stock RSS feeds
        Returns all stock-related articles
        """
        all_articles = []

        for feed_name, feed_url in self.rss_feeds.items():
            articles = self.scrape_rss_feed(feed_name, feed_url)
            all_articles.extend(articles)
            time.sleep(1)  # Be polite to servers

        print(f"\nTotal Indian stock articles collected: {len(all_articles)}")
        return all_articles

    def get_high_impact_news(self):
        """
        Get only high and medium impact news
        """
        all_articles = self.scrape_all_feeds()

        # Filter for high and medium impact only
        important_news = [a for a in all_articles if a.get('category') in ['High', 'Medium']]

        print(f"High/Medium impact news: {len(important_news)} articles")
        return important_news

    def get_nifty_news(self):
        """
        Get Nifty 50 / Nifty Next 50 specific news
        """
        all_articles = self.scrape_all_feeds()

        # Filter for Nifty-specific news
        nifty_keywords = ['nifty 50', 'nifty', 'nifty next 50', 'nifty bank', 'bank nifty']
        nifty_news = []

        for article in all_articles:
            text = (article['title'] + ' ' + article.get('summary', '')).lower()
            for keyword in nifty_keywords:
                if keyword in text:
                    nifty_news.append(article)
                    break

        print(f"Nifty-specific news: {len(nifty_news)} articles")
        return nifty_news

if __name__ == '__main__':
    # Test the scraper
    scraper = IndianStockNewsScraper()
    news = scraper.get_high_impact_news()

    print("\n=== Latest Indian Stock Market News ===")
    for article in news[:10]:  # Show first 10
        print(f"\n[{article['source']}] {article['title']}")
        print(f"Category: {article['category']}")
        print(f"Published: {article['published_at']}")
        print(f"URL: {article['url'][:70]}...")
