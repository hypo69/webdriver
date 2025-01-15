How to use this code block
=========================================================================================

Description
-------------------------
This document describes the Crawlee Python module, which provides a custom implementation of `PlaywrightCrawler` from the Crawlee library. It enables you to configure browser settings, manage requests, and extract data from web pages using settings specified in a `crawlee_python.json` file. It is designed to streamline web automation and data extraction tasks.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure you have the required libraries installed: `playwright` and `crawlee`. Use pip to install them:
    ```bash
    pip install playwright crawlee
    ```
   Also, make sure to install the browsers using the command:
        ```bash
        playwright install
        ```
2.  **Locate the configuration file**: The module reads its settings from the `crawlee_python.json` file. This file should be located in the `src/webdriver/crawlee_python` directory.
3.  **Understand the configuration**: The `crawlee_python.json` file includes configuration options for the crawler, such as:
    -   `max_requests`: The maximum number of requests the crawler should make.
    -   `headless`: A boolean value to run the browser in headless mode.
    -   `browser_type`: Type of browser to use (`chromium`, `firefox`, `webkit`).
    -   `options`: A list of command-line arguments passed to the browser, example: `--disable-dev-shm-usage` or `--no-sandbox`.
    -  `user_agent`: The user agent string to use for requests.
    -   `proxy`: Configuration for proxy server settings (enabled, server, username, password).
    -   `viewport`: Settings for the browser window size (`width` and `height`).
    -   `timeout`: Timeout for operations in milliseconds.
    -   `ignore_https_errors`: A boolean value to ignore HTTPS errors.
4.  **Initialize the `CrawleePython` class**: Create an instance of the `CrawleePython` class, passing optional parameters or using default values from `crawlee_python.json` configuration file.
    - Example: `crawler = CrawleePython()` to use all default parameters from config.
    - Example with custom parameters: `crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=['--disable-gpu'])`
5. **Use the `run` method**: Call the `run` method, passing a list of URLs to start crawling. This method sets up the crawler, executes it, exports the data into a `results.json` file located in the `/tmp` directory of the project and logs the results, as well as handles exceptions that may occur during the process.
   - Example: `await crawler.run(['https://www.example.com', 'https://www.example2.com'])`
6.  **Access extracted data**: After running the crawler, you can get the extracted data by calling the `get_data` method, which returns a dictionary.
    - Example: `data = await crawler.get_data()`
7.  **Customize browser settings**: The module allows for specifying custom browser settings, such as user-agent or proxy settings. These can be configured in `crawlee_python.json` or can be passed as arguments to the `CrawleePython` constructor to override the config settings.
8.  **Handle exceptions**: The module logs errors and warnings using the `logger` from `src.logger`. Check the logs for debugging.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.crawlee_python.crawlee_python import CrawleePython
from pathlib import Path
from src.utils.jjson import j_loads_ns


async def main():
    # Example 1: Load settings from configuration file
    config_path = Path('src/webdriver/crawlee_python/crawlee_python.json')
    config = j_loads_ns(config_path)
    if config:
        print("Configuration loaded successfully")
    else:
       print("Failed to load configuration from crawlee_python.json")
       return

    # Example 2: Initialize and run the crawler with settings from config
    crawler = CrawleePython(max_requests=config.max_requests, headless=config.headless, browser_type=config.browser_type, options=config.options)
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with settings from the configuration file.")

    # Example 3: Initialize and run crawler with custom settings
    crawler = CrawleePython(max_requests=5, headless=True, browser_type='chromium', options=["--disable-gpu"])
    await crawler.run(['https://www.example.com'])
    print("Crawler ran with custom settings.")

    # Example 4: Run the crawler and get the results
    crawler = CrawleePython(max_requests=3, browser_type='firefox', headless=True)
    await crawler.run(['https://www.example.com'])
    data = await crawler.get_data()
    if data:
        print(f"Data extracted with {len(data)} items")
    else:
        print("No data was returned from crawler")


if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Provided a detailed description of the `Crawlee Python Module`.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for all configuration options from the `crawlee_python.json` file.
- Improved explanation of the crawling, exporting and data extraction process.
- Added examples showing how to run the crawler with settings from file and with custom settings.
- Updated example to include the data access after execution of the crawler.