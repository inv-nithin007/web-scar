#!/usr/bin/env python3
"""
Combined Scheduler for Forex and Indian Stock News Scrapers
Runs both scrapers automatically every 30 minutes
"""

import schedule
import time
from datetime import datetime
from scraper_forex import run_scraper as run_forex_scraper
from scraper_india import run_india_scraper

def job_forex():
    """Job to run the forex scraper"""
    print("\n" + "="*60)
    print(f"💱 Forex scrape triggered at {datetime.now()}")
    print("="*60)
    run_forex_scraper()

def job_india():
    """Job to run the Indian stock scraper"""
    print("\n" + "="*60)
    print(f"🇮🇳 Indian stock scrape triggered at {datetime.now()}")
    print("="*60)
    run_india_scraper()

def job_both():
    """Job to run both scrapers"""
    print("\n" + "="*80)
    print(f"🌍 Combined scrape triggered at {datetime.now()}")
    print("="*80)

    # Run forex first
    job_forex()

    # Small delay
    time.sleep(5)

    # Run India
    job_india()

def main():
    """
    Main scheduler function
    Runs both scrapers every 30 minutes
    """
    print("=" * 80)
    print("📊 COMBINED NEWS SCRAPER - Scheduler Started")
    print("=" * 80)
    print("⏰ Schedule: Every 30 minutes")
    print("📰 Collecting: Forex News + Indian Stock News")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 80)

    # Run once immediately
    print("\n🚀 Running initial scrape...")
    job_both()

    # Schedule to run every 30 minutes
    schedule.every(30).minutes.do(job_both)

    # Alternative schedules (uncomment the one you want):
    # schedule.every(1).hour.do(job_both)  # Every 1 hour
    # schedule.every(15).minutes.do(job_both)  # Every 15 minutes

    # Or run them separately at different times:
    # schedule.every(30).minutes.do(job_forex)  # Forex every 30 min
    # schedule.every(30).minutes.do(job_india)  # India every 30 min

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
