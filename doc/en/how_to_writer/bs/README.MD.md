How to use this code block
=========================================================================================

Description
-------------------------
This document describes the `BeautifulSoup and XPath Parser Module`, which provides a custom implementation for parsing HTML content using `BeautifulSoup` and `lxml` for XPath. It allows you to fetch HTML from local files or URLs, parse it, and extract elements using XPath locators. This module supports logging, error handling and external configurations via `bs.json` file.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that the required dependencies are installed: `beautifulsoup4`, `lxml`, and `requests`. Install them using pip:
    ```bash
    pip install beautifulsoup4 lxml requests
    ```
2.  **Locate the configuration file**: The module's settings are loaded from `bs.json`. It includes settings for default URLs/files, default locators, logging, proxy, timeout, and encoding.
3.  **Initialize the `BS` parser**: Create an instance of the `BS` class, optionally providing a URL to fetch the HTML content during initialization.
    -   Example: `parser = BS()` or `parser = BS(url="https://example.com")`
4.  **Fetch HTML content**: If a URL was not provided during initialization, use the `get_url` method to fetch HTML content from a local file or web URL.
    -   Example: `parser.get_url('https://example.com')` or `parser.get_url('file:///path/to/your/file.html')`
5.  **Define a locator**: Define a locator as a dictionary or `SimpleNamespace` object, containing `by` (locator type), `attribute`, and `selector` (XPath expression).
    -   Example: `locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')`
6.  **Execute the locator**: Use the `execute_locator` method with the locator object to extract elements from the loaded HTML content. You can also pass a URL to fetch the HTML just for this locator.
    -   Example: `elements = parser.execute_locator(locator)` or `elements = parser.execute_locator(locator, url="https://example.com")`
7.  **Process results**: The `execute_locator` method returns a list of `lxml` elements that match the specified XPath selector.
8.  **Handle logging**:  The module uses the `logger` from `src.logger` to log errors and information. Review the configured log file for any issues.

Usage example
-------------------------
```python
from src.webdriver.bs.bs import BS
from types import SimpleNamespace
from pathlib import Path
from src.utils.jjson import j_loads_ns


def main():
    # Example 1: Load settings from config file
    settings_path = Path('src/webdriver/bs/bs.json')
    settings = j_loads_ns(settings_path)

    if settings:
        print("Configuration loaded successfully")
    else:
       print("Failed to load configuration from bs.json")
       return


    # Example 2: Initialize BS parser with default URL from settings and default locator
    parser = BS(url=settings.default_url)
    locator = SimpleNamespace(**settings.default_locator)
    elements = parser.execute_locator(locator)

    if elements:
      print(f"Found {len(elements)} elements using default locator.")
    else:
      print("No elements found using default locator.")


    # Example 3: Fetch HTML content from a file and execute locator by ID
    parser = BS()
    if parser.get_url("file:///path/to/your/local.html"):
        print("Successfully fetched HTML content from local file")
        locator = SimpleNamespace(by='ID', attribute='example_id', selector='//*[@id="example_id"]')
        elements = parser.execute_locator(locator)
        if elements:
            print(f"Found {len(elements)} elements using ID 'example_id'")
        else:
             print(f"No elements found using ID 'example_id'")
    else:
       print("Failed to fetch HTML content from local file")

    # Example 4: Fetch HTML content from a URL and execute locator by CSS
    parser = BS()
    if parser.get_url('https://example.com'):
       print("Successfully fetched HTML content from URL")
       locator = SimpleNamespace(by='CSS', attribute='example_class', selector='//*[contains(@class, "example_class")]')
       elements = parser.execute_locator(locator)
       if elements:
          print(f"Found {len(elements)} elements with class 'example_class'")
       else:
           print(f"No elements found with class 'example_class'")
    else:
        print("Failed to fetch HTML content from URL")



if __name__ == "__main__":
    main()

```
```

## Changes
- Added a detailed description of the `BeautifulSoup and XPath Parser Module`.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added descriptions of how to use the configuration from `bs.json` file.
- Added a section on logging and debugging.
- Added examples on how to fetch HTML from a file and from URL.
- Added an example of loading settings from config file using `j_loads_ns`.
- Updated the usage example to include error handling.