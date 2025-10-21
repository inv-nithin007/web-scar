#!/usr/bin/env python3
"""
Scheduler for Forex News Scraper ONLY
Runs the forex scraper automatically every 30 minutes
"""

import schedule
import time
from datetime import datetime
from scraper_forex import run_scraper as run_forex_scraper

def job():
    """Job to run the forex scraper"""
    print("\n" + "="*60)
    print(f"💱 Forex scrape triggered at {datetime.now()}")
    print("="*60)
    run_forex_scraper()

def main():
    """
    Main scheduler function
    Runs forex scraper every 30 minutes
    """
    print("=" * 60)
    print("💱 FOREX News Scraper - Scheduler Started")
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
