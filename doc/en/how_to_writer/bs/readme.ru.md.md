How to use this code block
=========================================================================================

Description
-------------------------
This document explains how to use the `BeautifulSoup and XPath Parser Module`, which provides a custom implementation for parsing HTML content using `BeautifulSoup` and `lxml` with XPath support. The module allows fetching HTML from files or URLs, parsing it, and extracting elements using XPath locators. It supports logging, error handling, and external configuration via the `bs.json` file.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that `beautifulsoup4`, `lxml`, and `requests` are installed. You can install them using pip:
    ```bash
    pip install beautifulsoup4 lxml requests
    ```
2.  **Locate the configuration file**: The module uses a `bs.json` file for configuration, which includes settings for `default_url`, `default_file_path`, `default_locator`, `logging`, `proxy`, `timeout`, and `encoding`.
3.  **Initialize the `BS` parser**: Create an instance of the `BS` class, providing an optional URL to load content during initialization.
    -   Example: `parser = BS()` or `parser = BS(url='https://example.com')`
4.  **Fetch HTML content**: If you did not provide a URL during initialization, use the `get_url` method to fetch HTML from a local file or web URL.
    -   Example: `parser.get_url('https://example.com')` or `parser.get_url('file:///path/to/your/file.html')`
5.  **Define a locator**: Define a locator using a `SimpleNamespace` object or a dictionary. The locator should include the `by` (locator type: `ID`, `CSS`, `TEXT` or `XPATH`), `attribute`, and `selector`.
    -   Example: `locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')`
6.  **Execute the locator**: Use the `execute_locator` method with the locator to perform an XPath query on the loaded HTML content. You can also pass a URL to this method to load and process HTML just for this locator.
    -   Example: `elements = parser.execute_locator(locator)` or `elements = parser.execute_locator(locator, url='https://example.com')`
7.  **Process the results**: The `execute_locator` method returns a list of `lxml` elements.
8.  **Handle logging**: The module logs errors and information using `logger` from the `src.logger` module, review the log files to handle any errors.

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



    # Example 3: Fetch HTML from file and execute locator by ID
    parser = BS()
    if parser.get_url("file:///path/to/your/local.html"):
       print("Successfully fetched HTML content from local file")
       locator = SimpleNamespace(by='ID', attribute='example_id', selector='//*[@id="example_id"]')
       elements = parser.execute_locator(locator)
       if elements:
           print(f"Found {len(elements)} elements with id 'example_id'")
       else:
          print("No elements found with id 'example_id'")
    else:
        print("Failed to fetch HTML content from local file")



    # Example 4: Fetch HTML from URL and execute locator by CSS
    parser = BS()
    if parser.get_url('https://example.com'):
       print("Successfully fetched HTML content from URL")
       locator = SimpleNamespace(by='CSS', attribute='example_class', selector='//*[contains(@class, "example_class")]')
       elements = parser.execute_locator(locator)
       if elements:
          print(f"Found {len(elements)} elements with class 'example_class'")
       else:
           print("No elements found with class 'example_class'")
    else:
        print("Failed to fetch HTML content from URL")


if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `BeautifulSoup and XPath Parser Module`.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanation of how to use the configuration from the `bs.json` file.
- Added description of how logging and debugging is done.
- Added an example of how to use different locators to find web elements (`ID`, `CSS`, `XPATH`).
- Added an example of how to load settings from `bs.json` file using `j_loads_ns`.
- Expanded the example to include error checking.