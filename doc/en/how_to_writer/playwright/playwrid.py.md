How to use this code block
=========================================================================================

Description
-------------------------
This module provides a custom implementation of `PlaywrightCrawler` using the `Crawlee` library, which simplifies the process of automating browser interactions and extracting data from web pages. This module, named `Playwrid`, allows configuring browser settings, profiles, and launch options using Playwright. It integrates with `PlaywrightExecutor` and `JavaScript` modules to enable flexible web scraping and data extraction tasks.

Execution steps
-------------------------
1.  **Import necessary modules**: Ensure that all required modules are imported, including `asyncio`, `pathlib`, `typing`, `crawlee`, `playwright`, and internal modules from `src`.
2.  **Initialize the `Playwrid` class**: Create an instance of the `Playwrid` class, using optional parameters like `user_agent` and `options` to customize the browser settings during initialization.
    - The constructor loads configurations from `playwrid.json`.
    - Example: `browser = Playwrid()` to use defaults.
    - Example with a custom user agent and options:  `browser = Playwrid(user_agent="custom_user_agent", options=["--headless"])`
3.  **Set launch options**: The `_set_launch_options` method configures the launch options for Playwright, combining settings from the config file (`playwrid.json`), provided `user_agent`, and the `options` list.
4. **Start the crawler**: Call the `start` method providing the URL you want to crawl. This method initializes Playwright, starts the browser, navigates to the given URL and then runs the crawler. It uses the `PlaywrightExecutor` to start Playwright and navigate to the provided URL.
   - Example: `await browser.start("https://www.example.com")`
5. **Access the current URL**: You can use `current_url` property to get the current URL of the browser.
   - Example: `url = browser.current_url`
6.  **Get page content**: Use the `get_page_content` method to get HTML content of the current page.
    -   Example: `html_content = browser.get_page_content()`
7.  **Extract elements**:
    -   **By CSS selector**: Use the `get_element_content` method to get the inner HTML content of a single element using a CSS selector.
          - Example: `element_content = await browser.get_element_content("h1")`
    -   **By XPath**: Use the `get_element_value_by_xpath` method to get the text content of a single element using an XPath expression.
          - Example:  `xpath_value = await browser.get_element_value_by_xpath("//head/title")`
8.  **Interact with elements**:
    -   **Click an element**: Use the `click_element` method to click a single element using a CSS selector.
           -  Example: `await browser.click_element("button")`
9. **Execute locators**: Use the `execute_locator` method, passing the locator to perform actions defined in locator object and extract data from elements based on the `event` and `attribute` fields.
    - Example: `name = await browser.execute_locator(locator_name)`
10. **Handle exceptions**: The module uses try-except blocks for error handling and logging. Ensure to review the logs for issues.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.playwright.playwrid import Playwrid
from playwright.async_api import async_playwright
from types import SimpleNamespace

async def main():
    # Example 1: Initialize and start the Playwright crawler with custom options
    browser = Playwrid(options=["--headless"])
    await browser.start("https://www.example.com")

    # Example 2: Get HTML content of the page
    html_content = browser.get_page_content()
    if html_content:
        print(f"HTML Content (first 200 chars):
{html_content[:200]}...")
    else:
        print("Failed to get HTML content.")

    # Example 3: Get content of the element using CSS selector
    element_content = await browser.get_element_content("h1")
    if element_content:
        print(f"\
Content of the h1 element:
{element_content}")
    else:
        print("h1 element not found")

    # Example 4: Get the value of the element using xpath
    xpath_value = await browser.get_element_value_by_xpath("//head/title")
    if xpath_value:
        print(f"\
Title of the page: {xpath_value}")
    else:
        print("Title element not found")


    # Example 5: Click a button
    await browser.click_element("button")
    print("Clicked button")

    # Example 6: Execute locator
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
- Provided a detailed description of the `Playwrid` module and its features.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Improved the explanations for configuration, and how to use the `start`, `get_page_content`, `get_element_content`, `get_element_value_by_xpath` and `click_element` and `execute_locator` methods.
- Added usage examples that show different ways to interact with the page using different methods.
- Added error handling explanations and logging.
- Updated the example to get data using the `execute_locator` and perform a click using a locator.