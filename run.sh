#!/bin/bash
# Simple startup script for Forex News Scraper

echo "========================================"
echo "Forex News Scraper"
echo "========================================"
echo ""
echo "What would you like to do?"
echo "  [1] Run scraper once"
echo "  [2] Run scheduler (every 30 minutes)"
echo "  [3] View collected news"
echo "  [4] Test installation"
echo "========================================"
read -p "Enter choice: " choice

case $choice in
  1)
    echo "Running scraper..."
    ./venv/bin/python scraper.py
    ;;
  2)
    echo "Starting scheduler (Press Ctrl+C to stop)..."
    ./venv/bin/python scheduler.py
    ;;
  3)
    ./venv/bin/python view_news.py
    ;;
  4)
    echo "Testing installation..."
    ./venv/bin/python -c "import requests, bs4, feedparser, schedule; print('✓ All packages installed successfully!')"
    echo "✓ Installation test passed!"
    ;;
  *)
    echo "Invalid choice"
    ;;
esac
