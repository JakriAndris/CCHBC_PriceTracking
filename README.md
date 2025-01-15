Price Tracker for Coca-Cola HBC

Overview
--------
This project is a price-tracking system designed for Coca-Cola HBC. It automates the process of scraping and analyzing product prices from various online stores and tracks weekly price trends. The system supports functionality for:

- Extracting and cleaning price data from online stores (Auchan, Tesco, Spar).
- Maintaining a historical record of weekly price shifts.
- Highlighting promotional prices when a product's price drops compared to the previous week.

Features
--------
### Excel Integration:
- Loads and saves data from/to Excel files.
- Updates weekly pricing columns to preserve historical data.

### Web Scraping:
- Uses Selenium to scrape price data from supported online stores.
- Includes custom configurations for each store (URL structure and price element selectors).

### Automated Data Handling:
- Cleans and processes scraped price data.
- Tracks promotions by comparing weekly prices.

### Compatibility:
- Designed for ease of extension to new stores.
- Flexible structure for adapting to various price data formats.

File Descriptions
------------------
**main.py**:  
The main script orchestrating the price tracking workflow, including data loading, processing, and saving.

**data_handling.py**:  
Handles Excel data operations, including loading, saving, shifting weekly price columns, and comparing prices.

**webscraper.py**:  
Contains the web scraper logic for fetching price data from online stores using Selenium.
