How to use this code block
=========================================================================================

Description
-------------------------
This `__init__.py` file in the `src.webdriver.bs` module serves as an initialization file. It makes the `BS` class available directly from the `src.webdriver.bs` package, simplifying imports in other parts of the project. Instead of importing `BS` from `src.webdriver.bs.bs`, you can import it directly from `src.webdriver.bs`.

Execution steps
-------------------------
1. **Import the `BS` class**: In another module, import the `BS` class directly from the `src.webdriver.bs` package using `from src.webdriver.bs import BS`.
2. **Use the `BS` class**:  You can then instantiate and use the `BS` class as if it were directly defined in the `src.webdriver.bs` directory.

Usage example
-------------------------
```python
from src.webdriver.bs import BS
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

    # Example 3: Fetch HTML content from a local file and use xpath locator
    parser = BS()
    if parser.get_url("file:///path/to/your/local.html"):
       print("Successfully fetched HTML content from local file")
       locator = SimpleNamespace(by='XPATH', attribute=None, selector='//h1')
       elements = parser.execute_locator(locator)
       if elements:
          print(f"Found {len(elements)} h1 element(s)")
       else:
          print(f"No h1 element(s) found")
    else:
        print("Failed to fetch HTML content from local file")


    # Example 4: Fetch HTML content from a URL and use css locator
    parser = BS()
    if parser.get_url('https://example.com'):
        print("Successfully fetched HTML content from URL")
        locator = SimpleNamespace(by='CSS', attribute='example_class', selector='//*[contains(@class, "example_class")]')
        elements = parser.execute_locator(locator)
        if elements:
           print(f"Found {len(elements)} element(s) with the class 'example_class'")
        else:
           print(f"No elements found with the class 'example_class'")

    else:
        print("Failed to fetch HTML content from URL")

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the purpose of the `__init__.py` file.
- Outlined clear execution steps for importing and using the `BS` class.
- Included a comprehensive usage example with comments demonstrating how to use `BS` after importing it.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added a usage example with how to use it with and without loading settings.