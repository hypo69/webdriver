How to use this code block
=========================================================================================

Description
-------------------------
The `driver.py` module provides a `Driver` class designed to simplify interactions with Selenium web drivers. It offers a unified interface for tasks such as initializing a web driver, navigating to URLs, scrolling through pages, managing cookies, and fetching HTML content. It also includes robust error handling and logging capabilities.

Execution steps
-------------------------
1. **Import necessary modules**: Ensure that all required modules are imported. These include `copy`, `pickle`, `time`, `re`, `pathlib`, `typing`, `selenium.webdriver.common.by`, `selenium.common.exceptions`, `header`, `src.gs` , `src.logger.logger`, and `src.logger.exceptions`.
2. **Initialize the `Driver`**: Create an instance of the `Driver` class by providing a web driver class (e.g., `Chrome`, `Firefox`) and any necessary arguments like the path to the driver executable.
    - Example: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`
3. **Utilize Driver Methods**:
    - `get_url(url)`: Navigates to a specified URL.
    - `scroll(scrolls, frame_size, direction, delay)`: Scrolls the web page in a given direction.
    - `locale`: Retrieves the language of the page.
    - `window_open(url)`: Opens a new browser tab, optionally loading a given URL.
    - `wait(delay)`: Pauses the script execution for a specified time.
    - `_save_cookies_localy()`: Saves cookies locally. Note that this method is currently stubbed for debugging.
    - `fetch_html(url)`: Fetches HTML content from either a URL or a local file path.
4.  **Subclassing**: You can create subclasses of `Driver` specifying the `browser_name`.
    - Example: `class CustomDriver(Driver, browser_name='Chrome'): ...`
5. **Handle Exceptions**: The code includes exception handling for various scenarios. It is important to check the logs using the logger instance from `src.logger.logger` for any errors or issues.
6. **Work with Different Browsers**: The `Driver` class supports different browsers by passing the correct `webdriver_cls` when instantiating it.

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

# Get the page language
page_language = driver.locale
if page_language:
    print(f'Page language: {page_language}')
else:
    print('Could not determine the page language')

# Open new tab and navigate to the given url
driver.window_open('https://newtab.example.com')

# Wait for 1 second
driver.wait(1)

# Fetch HTML content from a local file
if driver.fetch_html('file:///path/to/local.html'):
   print('Successfully fetched HTML content from file')
else:
   print('Failed to fetch HTML content from local file')

# Fetch HTML content from a URL
if driver.fetch_html('https://example.com'):
    print('Successfully fetched HTML content from URL')
else:
    print('Failed to fetch HTML content from URL')

# Save cookies locally
driver._save_cookies_localy()
```
```

## Changes
- Provided a detailed description of the `driver.py` module.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Included a section about using subclasses of the `Driver` class.
- Expanded explanation about logging and error handling.