#!/usr/bin/env python3
"""
Scheduler for Indian Stock Market Scraper ONLY
Runs the Indian stock scraper automatically every 30 minutes
"""

import schedule
import time
from datetime import datetime
from scraper_india import run_india_scraper

def job():
    """Job to run the Indian stock scraper"""
    print("\n" + "="*60)
    print(f"🇮🇳 Indian stock scrape triggered at {datetime.now()}")
    print("="*60)
    run_india_scraper()

def main():
    """
    Main scheduler function
    Runs Indian stock scraper every 30 minutes
    """
    print("=" * 60)
    print("🇮🇳 INDIAN STOCK News Scraper - Scheduler Started")
    print("=" * 60)
    print("⏰ Schedule: Every 30 minutes")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 60)

    # Run once immediately
    print("\n🚀 Running initial scrape...")
    job()

    # Schedule to run every 30 minutes
    schedule.every(30).minutes.do(job)

    print(f"\n⏰ Next run scheduled in 30 minutes")

    # Keep running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Scheduler stopped by user")
        print("Goodbye!")
