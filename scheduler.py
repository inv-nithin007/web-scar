#!/usr/bin/env python3
"""
Scheduler for Forex News Scraper
Runs the scraper automatically every 30 minutes
"""

import schedule
import time
from datetime import datetime
from scraper import run_scraper

def job():
    """Job to run the scraper"""
    print("\n" + "="*60)
    print(f"🤖 Scheduled scrape triggered at {datetime.now()}")
    print("="*60)
    run_scraper()

def main():
    """
    Main scheduler function
    Runs scraper every 30 minutes
    """
    print("=" * 60)
    print("Forex News Scraper - Scheduler Started")
    print("=" * 60)
    print("⏰ Schedule: Every 30 minutes")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 60)

    # Run once immediately
    print("\n🚀 Running initial scrape...")
    job()

    # Schedule to run every 30 minutes
    schedule.every(30).minutes.do(job)

    # Alternative schedules (uncomment the one you want):
    # schedule.every(1).hour.do(job)  # Every 1 hour
    # schedule.every(15).minutes.do(job)  # Every 15 minutes
    # schedule.every(5).minutes.do(job)  # Every 5 minutes

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
