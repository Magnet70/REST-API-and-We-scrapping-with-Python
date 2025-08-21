Stock Price & Revenue Visualization

This project retrieves, cleans, and visualizes historical stock price and revenue data for Tesla (TSLA) and GameStop (GME) using Python. It leverages data scraping, cleaning, and interactive charting to provide insightful visualizations.


---

Features

Fetches historical stock data using investpy.

Scrapes revenue data from HTML tables using BeautifulSoup.

Cleans financial data by removing special characters and converting to numeric formats.

Plots interactive charts with Plotly, combining stock prices and revenues.

Exports interactive graphs as HTML files for easy sharing and offline viewing.

Designed to work on Android Python environments (e.g., Pydroid).



---

Technologies Used

Python 3.x

investpy

BeautifulSoup

pandas

plotly

requests and re for web scraping and regex



---

How It Works

1. Data Collection

Stock data is fetched via investpy.get_stock_historical_data().

Revenue data is scraped from provided URLs using BeautifulSoup.



2. Data Cleaning

Removes currency symbols and commas using regex.

Converts revenue values to numeric and removes empty rows.



3. Visualization

Creates two-panel interactive charts:

Stock price over time.

Revenue over time.


Saves the output as an HTML file (gme_stock.html or similar).





---

Usage

1. Install dependencies:

pip install pandas plotly investpy beautifulsoup4 requests


2. Run the script in your Python environment (works on Android too).


3. The generated graph will be saved as an HTML file. Open it in your browser to explore interactively.




---

Example Output

Tesla stock prices and revenues plotted from 1900 to 2025.

GameStop historical trends displayed interactively.



---

Future Improvements

Add support for more stocks dynamically.

Automate data updates via APIs.

Enhance UI with filters and range selectors.
