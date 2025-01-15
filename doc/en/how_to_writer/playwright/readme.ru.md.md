How to use this code block
=========================================================================================

Description
-------------------------
This document explains how to use the `Playwright Crawler Module` which provides a custom implementation of `PlaywrightCrawler` from the Crawlee library. The module simplifies the automation of browser interactions and data extraction from websites by loading configurations from `playwrid.json`. It supports setting user-agent, proxy settings, viewport size, and custom browser options.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that `playwright` and `crawlee` are installed. Install them using pip:
    ```bash
    pip install playwright crawlee
    ```
    Also make sure to install browsers:
     ```bash
    playwright install
    ```
2.  **Locate the configuration file**: The module loads its settings from the `playwrid.json` file located in the `src/webdriver/playwright` directory.
3.  **Understand the configuration**: The `playwrid.json` file includes:
    -   `browser_type`: The browser type (`chromium`, `firefox`, or `webkit`). Defaults to `chromium`.
    -   `headless`: A boolean to run browser in headless mode. Defaults to `true`.
    -   `options`: A list of command-line options to pass to the browser (e.g., `--disable-dev-shm-usage`, `--no-sandbox`, `--disable-gpu`).
    -   `user_agent`: A user agent string used for requests.
    -   `proxy`: Proxy server settings (enabled, server, username, password).
    -   `viewport`: Dimensions of the browser window including `width` and `height`.
    -   `timeout`: Timeout for operations in milliseconds. Default is 30000 (30 seconds).
    -   `ignore_https_errors`: Boolean to ignore HTTPS errors, default to `false`.
4.  **Initialize the `Playwrid` class**: Create an instance of the `Playwrid` class, optionally providing `user_agent` and `options` arguments to override config settings.
    -  Example: `browser = Playwrid()` (to initialize using configuration from `playwrid.json`)
    -  Example with custom options:  `browser = Playwrid(options=["--headless"])`
     - Example with custom user agent: `browser = Playwrid(user_agent="custom_user_agent")`
5. **Start crawling**: Use the `start` method providing the URL you want to crawl. This initializes Playwright, navigates to the specified URL, and executes the crawler.
   -  Example: `await browser.start("https://www.example.com")`
6. **Access extracted data**: The module provides methods to interact with the page:
    -  Use `current_url` property to get the current URL.
    - Use the `get_page_content` method to get the HTML content of current page.
    -  Use the `get_element_content` method with CSS selector to get the inner HTML content of a matching element.
    - Use `get_element_value_by_xpath` method with XPath expression to get text value of the matching element.
    - Use `click_element` method with CSS selector to click the matching element.
     - Use the `execute_locator` method to interact with the page based on specific configurations.
7.  **Handle exceptions**: Errors and warnings during initialization or execution will be logged, and it is important to review the logs for any issues.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.playwright.playwrid import Playwrid
from playwright.async_api import async_playwright
from types import SimpleNamespace

async def main():
    # Example 1: Initialize and start the Playwright crawler with default settings
    browser = Playwrid()
    await browser.start("https://www.example.com")
    print("Successfully navigated to the URL using default settings.")

    # Example 2: Get HTML content of the page
    html_content = browser.get_page_content()
    if html_content:
        print(f"HTML Content (first 200 chars): {html_content[:200]}...")
    else:
        print("Failed to get HTML content.")

    # Example 3: Get content of h1 element using CSS selector
    element_content = await browser.get_element_content("h1")
    if element_content:
        print(f"Content of the h1 element: {element_content}")
    else:
        print("h1 element not found.")


    # Example 4: Get the value of the page's title using XPath
    xpath_value = await browser.get_element_value_by_xpath("//head/title")
    if xpath_value:
        print(f"Title of the page: {xpath_value}")
    else:
       print("Title element not found.")

    # Example 5: Click a button by css selector
    await browser.click_element("button")
    print("Clicked button.")

    # Example 6: Initialize Playwright Crawler with custom options and user agent
    browser = Playwrid(options=["--headless", "--disable-gpu"], user_agent="custom_user_agent")
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
- Provided a detailed description of the Playwright Crawler Module and its features.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanation of configuration options from `playwrid.json`.
- Added examples for using custom settings, user agent, and options and how to use all the provided methods.
- Added logging and error handling explanation.
- Improved the clarity of the description for methods used in the example.
- Added an example showing how to execute a locator for extracting the page title and for clicking the button.