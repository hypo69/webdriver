How to use this code block
=========================================================================================

Description
-------------------------
The `crawlee_python.py` module provides a custom implementation of a web crawler using the `Crawlee` library and `Playwright`. This module allows you to configure browser settings, manage requests, and extract data from web pages. It offers a flexible framework for web scraping and data extraction tasks.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that you have `crawlee`, `playwright`, and other necessary libraries installed. You can install them using pip:
    ```bash
    pip install crawlee playwright
    ```
    Additionally, install the `fake_useragent` library:
     ```bash
    pip install fake_useragent
    ```
2.  **Import necessary modules**: The module imports modules from `pathlib`, `typing`, `asyncio`, `crawlee`, and internal modules such as `gs`, `logger`, and `j_loads_ns`. Ensure these modules are available in your project.
3.  **Initialize the `CrawleePython` class**: Create an instance of the `CrawleePython` class, passing required parameters like `max_requests`, `headless`, `browser_type` and `options` for customization.
    -   `max_requests`:  Maximum number of requests to perform during the crawl. Defaults to 5.
    -   `headless`: Whether to run the browser in headless mode (without a UI). Defaults to `False`.
    -   `browser_type`: The type of browser to use ('chromium', 'firefox', 'webkit'). Defaults to `'firefox'`.
    -   `options`: A list of custom command line options to pass to the browser during initialization.
   - Example: `crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=["--disable-gpu"])`
4.  **Set up the crawler**: Call the `setup_crawler` method. This method sets up the `PlaywrightCrawler` instance, defining a default request handler for processing web pages.
    - Inside the request handler:
        - Log the URL of the current request.
        - Enqueue links found on the page to continue the crawl.
        - Extract data from the page, including the URL, title, and content (truncated to 100 characters)
        - Push the extracted data to the dataset.
5.  **Run the crawler**: Call the `run_crawler` method, passing a list of URLs to begin the crawl.
    -   Example: `await crawler.run_crawler(['https://www.example.com', 'https://www.example2.com'])`
6.  **Export data**: After the crawl completes, call the `export_data` method with the file path to export the entire dataset to a JSON file.
    - Example: `await crawler.export_data('results.json')`
7.  **Get the data**: Use the `get_data` method to retrieve extracted data from the crawler.
    - Example: `data = await crawler.get_data()`
8.  **Use the `run` method**: This method encapsulates all steps: set up the crawler, run the crawler with the URLs, export the data, and log the results. It also catches and logs errors during the crawl.
    - Example: `await crawler.run(['https://example.com'])`

Usage example
-------------------------
```python
import asyncio
from src.webdriver.crawlee_python.crawlee_python import CrawleePython
from pathlib import Path

async def main():
    # Example 1: Initialize and run the crawler with default settings
    crawler = CrawleePython()
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with default settings.")


    # Example 2: Initialize and run the crawler with custom settings
    crawler = CrawleePython(max_requests=5, headless=True, browser_type='chromium', options=['--disable-gpu'])
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with custom settings.")


    # Example 3: Run a crawler and export data to json file.
    crawler = CrawleePython(max_requests=3, browser_type='firefox', headless=True)
    await crawler.run(['https://www.example.com'])

    # Example 4: Get the data from crawler after execution
    data = await crawler.get_data()
    if data:
        print(f"Data extracted with {len(data)} items")
    else:
       print("No data returned from crawler")

if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Provided a detailed description of the `crawlee_python.py` module and its functionalities.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added clear instructions for each method and its functionality.
- Added examples for different scenarios such as custom settings, exporting data, and retrieving extracted data.
- Improved explanations for using the `run` method.
- Corrected a small typo in the usage example.