How to use this code block
=========================================================================================

Description
-------------------------
This document explains how to use the WebDriver Executor module, which includes the `Driver` class and its interaction with the `ExecuteLocator` class (explained in separate documentation). This module provides a framework for automating web page navigation and interactions using Selenium WebDriver. It handles various actions on web elements, manages cookies, executes JavaScript, and takes screenshots.

Execution steps
-------------------------
1.  **Import necessary modules**: Import the required modules from `src.webdriver.driver` (including `Driver` and `Chrome`) and `selenium.webdriver.common.by` (including `By`).
2.  **Initialize the Driver**: Create an instance of the `Driver` class using a specific WebDriver class (e.g., `Chrome`).
    -   Example: `chrome_driver = Driver(Chrome)`
3.  **Navigate to a URL**: Use the `get_url` method to navigate to a web page.
    -   Example: `chrome_driver.get_url("https://www.example.com")`
4.  **Interact with web elements and the page**:
    -   **Extract domain**: Use the `extract_domain` method to get the domain from a URL.
    -   **Save cookies**: Use the `_save_cookies_localy` method to save cookies to a local file.
    -   **Refresh page**: Use the `page_refresh` method to reload the current page.
    -   **Scroll page**: Use the `scroll` method to scroll the page.
    -   **Get page language**: Access the `locale` property to get the page language.
    -   **Set custom user agent**: Create an instance of `Driver` class with the desired user-agent.
    -   **Find an element**: Use `find_element` method to locate a web element using `By` selectors like CSS.
    -   **Get current URL**: Access the `current_url` property to get the URL of the current page.
    -   **Focus the window**: Use `window_focus` to set focus to the browser window.
5. **Understand ExecuteLocator Class** (See linked `executor.ru.md`):
   - The `ExecuteLocator` class is responsible for interacting with elements based on provided locators.
   -  The class initializes with a WebDriver instance.
   - It contains the methods such as `execute_locator`, `get_webelement_by_locator`, `get_attribute_by_locator`, and `send_message`.
6. **Understand Locators** (See linked `locator.ru.md`):
   - Locators are dictionaries defining how to locate and interact with web elements.
   - They include keys such as `by`, `selector`, `attribute`, `event`, `mandatory`, and `timeout`.
7. **Handle Results**: The methods will return a `bool`, `str`, `WebElement`, `list`, or `None`.
8. **Error Handling**: Errors are logged using try-except blocks. Check the logs to identify issues during execution.

Usage example
-------------------------
```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the WebDriver Executor module.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Included links to external documents `executor.ru.md` and `locator.ru.md` for more details.
- Provided explanations for the different functionalities of the `Driver` class and how to interact with a web page.
- Added explanation of how to handle different returned values and errors.
- Added By import to the example.