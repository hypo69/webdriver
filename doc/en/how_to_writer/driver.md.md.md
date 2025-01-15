How to use this code block
=========================================================================================

Description
-------------------------
The `driver.py` module provides the `Driver` class to interact with Selenium web drivers. It manages driver initialization, navigation, scrolling, page language detection, cookie management, and fetching HTML content. This module abstracts the complexities of direct Selenium interaction, offering a simpler interface for web automation tasks.

Execution steps
-------------------------
1. **Import necessary modules**: Ensure that all necessary modules are installed and imported:
    - `selenium.webdriver` for interacting with web browsers.
    - `copy` for creating a copy of the current URL.
    - `time` for introducing delays.
    - `pickle` for saving cookies locally.
    - `pathlib` for file path operations.
    - `re` for regular expressions to extract file paths.
    - `src.config.settings as gs` for global settings (like cookie paths).
    - `src.logger.logger as logger` for error logging.
2. **Initialize the `Driver` class**: Create an instance of the `Driver` class by passing a WebDriver class (e.g., `Chrome`, `Firefox`) along with any required arguments, such as the path to the web driver executable.
   - Example: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
3. **Utilize driver methods**:
    - `get_url(url)`: Navigates to a specific URL.
    - `scroll(scrolls, frame_size, direction, delay)`: Scrolls the page.
    - `locale`: Retrieves the page language.
    - `window_open(url)`: Opens a new browser tab and navigates to the given url (if provided).
    - `fetch_html(url)`: Fetches HTML content from a URL (either a file path or a web address).
    - `wait(delay)`: Pauses execution for a specified duration.
    - `_save_cookies_localy()`: Saves cookies to a local file. Note: This method is currently stubbed for debugging purposes.
4. **Handle potential exceptions**: The `Driver` class handles various exceptions using try-except blocks. Always check the logs using the imported `logger` instance from `src.logger.logger` for errors or issues.
5. **Manage cookies**: If needed, use `_save_cookies_localy()` method to save cookies locally, this function is currently stubbed but you can remove the debugging line to enable it.
6. **Fetch HTML content**: The `fetch_html(url)` method can be used to get HTML content from a local file path or URL and store it in `self.html_content` attribute.
7. **Work with different browsers**: The `Driver` class is designed to work with different web drivers by passing the correct `webdriver_cls` in the constructor.
8. **Subclass**: If required, you can create subclasses of the `Driver` class, ensuring that you specify the `browser_name` attribute during subclass initialization.

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

# Scroll the page down 2 times
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

# Wait for 2 seconds
driver.wait(2)

# Fetch HTML content from local file path
if driver.fetch_html('file:///path/to/local.html'):
    print('Successfully fetched HTML content from file')
else:
    print('Failed to fetch HTML content from local file')

# Fetch HTML content from URL
if driver.fetch_html('https://example.com'):
    print('Successfully fetched HTML content from URL')
else:
    print('Failed to fetch HTML content from URL')

# Save Cookies
driver._save_cookies_localy()
```
```

## Changes
- Provided a detailed description of the `driver.py` module.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Included additional details about error handling and logging within the usage guide.
- Added explanation for how to use a subclass of the `Driver` class.