How to use this code block
=========================================================================================

Description
-------------------------
This document provides a comprehensive guide on how to use the WebDriver Executor module, which includes the `Driver` and `ExecuteLocator` classes. The module facilitates web page navigation and interaction using Selenium WebDriver. It handles various actions on web elements, manages cookies, executes JavaScript, and takes screenshots, all based on configurations defined in locator dictionaries and methods within the Driver class.

Execution steps
-------------------------
1.  **Import necessary modules**: Import the required modules from `src.webdriver.driver` (including `Driver` and `Chrome`) and `selenium.webdriver.common.by` (including `By`).
2.  **Initialize the Driver**: Create an instance of the `Driver` class with a specific WebDriver class (e.g., `Chrome`). This sets up the browser driver and provides methods for web interactions.
    -   Example: `chrome_driver = Driver(Chrome)`
3.  **Navigate to a URL**: Use the `get_url` method to navigate to a specific web page.
    -   Example: `chrome_driver.get_url("https://www.example.com")`
4.  **Interact with web elements**:
    -   **Extract domain**: Use the `extract_domain` method to get the domain from a URL.
    -   **Save cookies**: Use `_save_cookies_localy` to save cookies locally.
    -   **Refresh page**: Use the `page_refresh` method to reload the current page.
    -   **Scroll page**: Use the `scroll` method to scroll the page in different directions with custom frame size and delay.
    -    **Get page language**: Use the `locale` property to get the language of the current page.
    -   **Set custom User-Agent**: Create a `Driver` instance with a custom user-agent.
    -   **Find element**: Use the `find_element` method to find an element using a specific locator type.
    -   **Get current URL**: Get the current URL with `current_url` property.
    -   **Focus the window**: Use the `window_focus` method to bring focus to the browser window.
5.  **Understand the ExecuteLocator Class**: (See the linked `executor.md` for detailed usage.)
    -  This class is used to perform action on web elements based on locators.
    - It takes a WebDriver instance as an argument.
    - It contains methods for `execute_locator`, `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message`, and more.
    - Please refer to the detailed `executor.md` guide for specific methods.
6. **Understand Locators**: (See the linked `locator.md` for details.)
    - Locators are dictionaries that define how to find and interact with elements.
    - They include the keys like `by` (locator type), `selector`, `attribute`, `event`, `mandatory`, `timeout`, and more.
    - Please refer to the linked `locator.md` guide for more detailed information.
7.  **Handle results**: Check the return values of methods, which may include a `bool`, `str`, `WebElement`, `list`, or other data types, based on the actions performed.
8.  **Handle exceptions**: The module handles exceptions using try-except blocks. Check the logs for any issues.

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
- Provided a detailed explanation of the WebDriver Executor module, including the `Driver` and `ExecuteLocator` classes.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations on how to use the `Driver` class, how to interact with elements on a web page, and how to manage cookies.
- Added references to external `executor.md` and `locator.md` files for more details about the ExecuteLocator class and locators.
- Added detailed usage for the methods of `Driver` class.