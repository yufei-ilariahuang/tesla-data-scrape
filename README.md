# Tesla Location Dataset Scraper

This Python script scrapes information about Tesla locations from the Tesla website and writes it to a JSON file.

## Requirements
- Python 3.x
- Selenium
- Chrome WebDriver

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
2. Install Selenium using pip:
   ```
   pip install selenium
   ```
3. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system PATH.

## Usage
1. Clone this repository:
   ```
   git clone [https://github.com/yufei-ilariahuang/tesla-data-scrape.git]
   ```
2. Navigate to the project directory:
   ```
   cd scrap
   ```
3. Run the script:
   ```
   python scrape.py
   ```
4. The script will scrape Tesla location information from the Tesla website and store it in a file named `tesla_location_dataset.json` in the project directory.

## Description
- The script uses Selenium to automate web browsing and extract information from the Tesla website.
- It consists of three main functions:
  - `scrape_tesla_infos`: Scrapes information about Tesla locations from a given webpage.
  - `scrape_tesla_locations`: Scrapes links to Tesla location pages from the main Tesla locations page.
  - `scrape_and_write_to_json`: Integrates the above two functions to scrape information from all Tesla location pages and write it to a JSON file.
- The script handles cases where elements are not found on the webpage and continues scraping other elements.
- The scraped information includes location titles, URLs, addresses, and postal codes.

## Note
- Ensure that you have the necessary permissions to scrape data from the Tesla website.
- Use this script responsibly and avoid excessive scraping to prevent overloading the Tesla website servers.
- This script is provided as-is, without any warranties or guarantees.
