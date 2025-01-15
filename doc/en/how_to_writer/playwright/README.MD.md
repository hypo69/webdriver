How to use this code block
=========================================================================================

Description
-------------------------
This document explains the custom `Playwright Crawler Module` for browser automation and data scraping. This module provides an implementation of `PlaywrightCrawler` from the `Crawlee` library and allows configuring browser launch parameters, handling requests, and extracting data using the settings defined in the `playwrid.json` file. It provides features like custom options, proxy support, and flexible browser settings.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that the required libraries are installed: `playwright` and `crawlee`. You can install them using pip:
    ```bash
    pip install playwright crawlee
    ```
    Additionally, make sure to install browsers using the command:
        ```bash
        playwright install
        ```
2. **Locate the configuration file**: The module loads its settings from the `playwrid.json` file which should be placed in the `src/webdriver/playwright/` directory.
3.  **Understand Configuration**: The module uses `playwrid.json` to configure various aspects of the browser:
    -  `browser_type`: The browser to use which can be one of these options: `chromium`, `firefox`, or `webkit`.
    - `headless`: To indicate if the browser should run in headless mode or not, defaults to `true`.
    -   `options`: A list of command-line arguments passed to the browser (e.g. `--disable-dev-shm-usage`, `--no-sandbox`, `--disable-gpu`).
    - `user_agent`: The user agent string for browser requests.
    -   `proxy`: Proxy server settings including enabled, server address, username and password.
    -   `viewport`: The dimensions of the browser window including `width` and `height`.
    -   `timeout`: Maximum time to wait for operations (in milliseconds).
    -   `ignore_https_errors`: Indicates whether to ignore HTTPS errors.
4.  **Initialize the `Playwrid` class**: Create an instance of the `Playwrid` class. You can specify parameters such as user-agent, and options during the initialization to override config settings.
     - Example to initialize with default settings from config file: `browser = Playwrid()`
     - Example with custom settings: `browser = Playwrid(options=["--headless"], user_agent='custom_user_agent')`
5.  **Start crawling**: Use the `start` method by passing a URL to initiate the crawler.
    -   Example: `await browser.start('https://www.example.com')`
6. **Access browser data**: You can use different methods to access extracted page data:
     -  Use `current_url` property to get the current URL.
     -  Use `get_page_content` method to extract the HTML content of the current page.
    - Use `get_element_content` method by passing css selector to get the inner HTML content of the first matched element.
   - Use `get_element_value_by_xpath` method by passing an XPath expression to get the text value of first element matching that XPath.
    - Use `click_element` method by passing a CSS selector to click the first matching element.
    -  Use the `execute_locator` method to perform actions on web elements based on a locator configuration.
7.  **Handle exceptions**: The module uses try-except blocks to catch and log errors during execution. Review logs for troubleshooting.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.playwright.playwrid import Playwrid
from playwright.async_api import async_playwright
from types import SimpleNamespace


async def main():
    # Example 1: Initialize Playwright crawler with default settings
    browser = Playwrid()
    await browser.start("https://www.example.com")
    print("Successfully navigated to the URL with default settings.")

    # Example 2: Get HTML content of the page
    html_content = browser.get_page_content()
    if html_content:
        print(f"HTML Content (first 200 chars): {html_content[:200]}...")
    else:
        print("Failed to get HTML content")

    # Example 3: Get content of the h1 element using CSS selector
    element_content = await browser.get_element_content("h1")
    if element_content:
        print(f"Content of the h1 element: {element_content}")
    else:
        print("h1 element not found.")

    # Example 4: Get the value of the element using XPath
    xpath_value = await browser.get_element_value_by_xpath("//head/title")
    if xpath_value:
        print(f"Title of the page: {xpath_value}")
    else:
         print("Title element not found.")

    # Example 5: Click a button by css selector
    await browser.click_element("button")
    print("Clicked button.")

    # Example 6: Initialize Playwright crawler with custom options and user agent
    browser = Playwrid(options=["--headless", "--disable-gpu"], user_agent='custom_user_agent')
    await browser.start("https://www.example.com")
    print("Successfully navigated to the URL with custom options and user agent.")


     # Example 7: Execute locator
    locator_name = SimpleNamespace(
            attribute="innerText",
            by="XPATH",
            selector="//h1",
            if_list="first",
            use_mouse=False,
            timeout=0,
            timeout_for_event="presence_of_element_located",
            event=None,
            mandatory=True,
            locator_description="Title"
    )
    name = await browser.execute_locator(locator_name)
    print(f"Page title: {name}")

    locator_click = {
        "attribute": None,
        "by": "CSS",
        "selector": "button",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "mandatory": True,
        "locator_description": "button"
    }
    await browser.execute_locator(locator_click)



if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Provided a detailed description of the `Playwright Crawler Module`.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for `playwrid.json` config file.
- Added explanations about different methods for page interaction and extraction of the data.
- Improved error handling explanation.
- Added examples of how to set custom user agent and options, use all methods for extracting and interacting with the web page.
-  Added an example of how to execute the locator with `execute_locator` method.