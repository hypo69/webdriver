How to use this code block
=========================================================================================

Description
-------------------------
This document explains the `Crawlee Python Module` which provides a custom implementation of the `PlaywrightCrawler` from the Crawlee library. It allows you to configure browser launch parameters, handle web page requests, extract data, and handle errors, using settings configured via the `crawlee_python.json` file.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that `playwright` and `crawlee` are installed. You can install them using pip:
    ```bash
    pip install playwright crawlee
    ```
    Additionally, make sure to install browsers using the command:
        ```bash
        playwright install
        ```
2.  **Locate the configuration file**: The module reads its configuration from the `crawlee_python.json` file which should be placed in `src/webdriver/crawlee_python/`.
3.  **Understand the configuration**: The `crawlee_python.json` file contains the settings for the crawler:
    -   `max_requests`: Maximum number of requests to be performed during crawling.
    -   `headless`: A boolean to run browser in headless mode (without GUI).
    -   `browser_type`: The browser type: `chromium`, `firefox` or `webkit`.
    -   `options`: List of command line arguments passed to browser.
    -   `user_agent`: The user agent string for the requests.
    -   `proxy`: Configuration for proxy server (enabled, server, username, password).
    -   `viewport`: Width and height of the viewport.
    -   `timeout`: Maximum waiting time for operations in milliseconds.
    -   `ignore_https_errors`: Boolean to indicate if to ignore HTTPS errors.
4.  **Import and initialize the `CrawleePython` class**: Import the `CrawleePython` class from `src.webdriver.crawlee_python` and initialize it by creating an instance and passing optional parameters like `max_requests`, `headless`, `browser_type` and `options`.
     -   Example: `crawler = CrawleePython()` or `crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=["--disable-gpu"])`
    - The configuration is loaded from `crawlee_python.json` file during initialization.
5.  **Use the `run` method**: The `run` method allows you to set up the crawler, execute the crawling using provided list of URLs, export data to `results.json` file, and log the extracted data, and handles the potential exceptions.
    -   Example: `await crawler.run(['https://example.com'])`
6.  **Access extracted data:** You can access data directly using the method `get_data`.
    - Example: `data = await crawler.get_data()`
7.  **Customize browser settings**: The `CrawleePython` class uses settings loaded from `crawlee_python.json` for initial configuration, but allows for passing custom options during initialization as well.
8.  **Handle exceptions**: The module includes try-except blocks to catch and log errors during various operations using `logger` from `src.logger`. Check the logs to handle any issues.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.crawlee_python.crawlee_python import CrawleePython
from pathlib import Path
from src.utils.jjson import j_loads_ns


async def main():
    # Example 1: Load settings from the config file
    config_path = Path('src/webdriver/crawlee_python/crawlee_python.json')
    config = j_loads_ns(config_path)
    if config:
        print("Configuration loaded successfully")
    else:
        print("Failed to load configuration file")
        return

    # Example 2: Initialize and run the crawler with settings loaded from the config file
    crawler = CrawleePython(max_requests=config.max_requests, headless=config.headless, browser_type=config.browser_type, options=config.options)
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with default settings loaded from config.")

    # Example 3: Initialize and run the crawler with custom settings
    crawler = CrawleePython(max_requests=5, headless=True, browser_type='chromium', options=["--disable-gpu"])
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with custom settings.")


    # Example 4: Run crawler and export data to a results.json file and get the data
    crawler = CrawleePython(max_requests=3, browser_type='firefox', headless=True)
    await crawler.run(['https://www.example.com'])
    data = await crawler.get_data()
    if data:
        print(f"Data extracted with {len(data)} items.")
    else:
       print("No data was returned from crawler")



if __name__ == "__main__":
    asyncio.run(main())

```
```

## Changes
- Provided a detailed description of the `Crawlee Python Module` and its functionality.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for each method and its functionality, including configuration details from `crawlee_python.json`.
- Added detailed steps on how to use the `run` and `get_data` methods.
- Added a usage example with loading the config from JSON.
- Improved explanations for the setup process, data handling and usage of the logging functionality.