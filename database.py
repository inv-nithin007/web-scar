import sqlite3
from datetime import datetime

class ForexNewsDB:
    def __init__(self, db_name='forex_news.db'):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create economic events table (Forex)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS economic_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_time TEXT NOT NULL,
                currency TEXT NOT NULL,
                event_name TEXT NOT NULL,
                impact TEXT,
                actual TEXT,
                forecast TEXT,
                previous TEXT,
                source TEXT,
                scraped_at TEXT,
                UNIQUE(event_time, currency, event_name)
            )
        ''')

        # Create news articles table (Forex)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news_articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                summary TEXT,
                url TEXT UNIQUE,
                published_at TEXT,
                source TEXT,
                category TEXT,
                scraped_at TEXT
            )
        ''')

        # Create Indian economic events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS india_economic_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_time TEXT NOT NULL,
                event_name TEXT NOT NULL,
                impact TEXT,
                actual TEXT,
                forecast TEXT,
                previous TEXT,
                source TEXT,
                country TEXT,
                scraped_at TEXT,
                UNIQUE(event_time, event_name)
            )
        ''')

        # Create Indian stock news table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS india_stock_news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                summary TEXT,
                url TEXT UNIQUE,
                published_at TEXT,
                source TEXT,
                category TEXT,
                scraped_at TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def insert_economic_event(self, event_data):
        """Insert economic event into database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT OR IGNORE INTO economic_events
                (event_time, currency, event_name, impact, actual, forecast, previous, source, scraped_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event_data.get('event_time'),
                event_data.get('currency'),
                event_data.get('event_name'),
                event_data.get('impact'),
                event_data.get('actual'),
                event_data.get('forecast'),
                event_data.get('previous'),
                event_data.get('source'),
                datetime.now().isoformat()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting event: {e}")
            return False
        finally:
            conn.close()

    def insert_news_article(self, article_data):
        """Insert news article into database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT OR IGNORE INTO news_articles
                (title, summary, url, published_at, source, category, scraped_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                article_data.get('title'),
                article_data.get('summary'),
                article_data.get('url'),
                article_data.get('published_at'),
                article_data.get('source'),
                article_data.get('category'),
                datetime.now().isoformat()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting article: {e}")
            return False
        finally:
            conn.close()

    def get_recent_events(self, limit=50):
        """Get recent economic events"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM economic_events
            ORDER BY event_time DESC
            LIMIT ?
        ''', (limit,))

        events = cursor.fetchall()
        conn.close()
        return events

    def get_recent_news(self, limit=50):
        """Get recent news articles"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM news_articles
            ORDER BY published_at DESC
            LIMIT ?
        ''', (limit,))

        articles = cursor.fetchall()
        conn.close()
        return articles

    def get_high_impact_events(self, limit=20):
        """Get high impact events only"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM economic_events
            WHERE impact = 'High'
            ORDER BY event_time DESC
            LIMIT ?
        ''', (limit,))

        events = cursor.fetchall()
        conn.close()
        return events

    # Indian Stock Market Methods

    def insert_india_event(self, event_data):
        """Insert Indian economic event into database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT OR IGNORE INTO india_economic_events
                (event_time, event_name, impact, actual, forecast, previous, source, country, scraped_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event_data.get('event_time'),
                event_data.get('event_name'),
                event_data.get('impact'),
                event_data.get('actual'),
                event_data.get('forecast'),
                event_data.get('previous'),
                event_data.get('source'),
                event_data.get('country', 'India'),
                datetime.now().isoformat()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting India event: {e}")
            return False
        finally:
            conn.close()

    def insert_india_news(self, article_data):
        """Insert Indian stock news article into database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT OR IGNORE INTO india_stock_news
                (title, summary, url, published_at, source, category, scraped_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                article_data.get('title'),
                article_data.get('summary'),
                article_data.get('url'),
                article_data.get('published_at'),
                article_data.get('source'),
                article_data.get('category'),
                datetime.now().isoformat()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting India news: {e}")
            return False
        finally:
            conn.close()

    def get_recent_india_events(self, limit=50):
        """Get recent Indian economic events"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM india_economic_events
            ORDER BY event_time DESC
            LIMIT ?
        ''', (limit,))

        events = cursor.fetchall()
        conn.close()
        return events

    def get_recent_india_news(self, limit=50):
        """Get recent Indian stock news"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM india_stock_news
            ORDER BY published_at DESC
            LIMIT ?
        ''', (limit,))

        news = cursor.fetchall()
        conn.close()
        return news

    def get_high_impact_india_events(self, limit=20):
        """Get high impact Indian events only"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM india_economic_events
            WHERE impact = 'High'
            ORDER BY event_time DESC
            LIMIT ?
        ''', (limit,))

        events = cursor.fetchall()
        conn.close()
        return events
