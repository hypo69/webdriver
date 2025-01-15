How to use this code block
=========================================================================================

Description
-------------------------
The `driver.py` module provides a `Driver` class for interacting with Selenium web drivers. It handles driver initialization, navigation, cookie management, exception handling, and more. It supports scrolling, determining page language, fetching HTML content, and managing multiple browser tabs.

Execution steps
-------------------------
1. **Import the necessary modules**: The code uses `selenium.webdriver`, `copy`, `time`, `pickle`, `logging`, `re`, and `pathlib`. Make sure these modules are installed and available in your environment.
2. **Initialize the `Driver` class**: Create an instance of the `Driver` class by passing a WebDriver class (e.g., `Chrome`, `Firefox`) along with any required arguments.
3. **Use the driver methods**: Once the driver is initialized, use its methods to interact with the web page. For example:
    - `get_url(url)`: Navigate to a URL.
    - `scroll(scrolls, frame_size, direction, delay)`: Scroll the page.
    - `window_open(url)`: Open a new browser tab.
    - `fetch_html(url)`: Fetch HTML content from a given URL or file path.
    - `locale`: Get the page language.
4. **Handle exceptions**: The code includes exception handling to log errors. Make sure to check the logs for any issues while using the driver methods.
5. **Manage cookies**: The code has methods to save cookies locally. This is useful when working with applications that require session management.

Usage example
-------------------------
```python
from selenium.webdriver import Chrome
from src.webdriver.driver import Driver

# Initialize the driver
driver = Driver(Chrome, executable_path='/path/to/chromedriver')

# Navigate to a URL
if driver.get_url('https://example.com'):
    print('Successfully navigated to the URL')
else:
    print('Failed to navigate to the URL')

# Scroll the page
if driver.scroll(scrolls=2, direction='down'):
    print('Successfully scrolled down')
else:
     print('Failed to scroll down')

# Open a new tab and navigate to a URL
driver.window_open('https://newtab.example.com')

# Fetch HTML content
if driver.fetch_html('https://example.com'):
    print('Successfully fetched HTML content')
else:
    print('Failed to fetch HTML content')

# Get the page language
page_language = driver.locale
if page_language:
    print(f'Page language: {page_language}')
else:
     print('Could not determine the page language')
```
```

## Changes
- Added a detailed explanation of the `driver.py` module, including its purpose, methods, and how to use them.
- Provided a step-by-step guide on how to use the code block.
- Added a usage example showing how to initialize the driver, navigate to a URL, scroll, open a new tab, fetch HTML content, and get the page language.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Used specific terms like "initialize," "navigate," "fetch," and "scroll" instead of vague terms.
- The `Usage example` provides a more practical view on how to use the functions, including error handling.