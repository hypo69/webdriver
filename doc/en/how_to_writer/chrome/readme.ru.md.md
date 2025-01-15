How to use this code block
=========================================================================================

Description
-------------------------
This document explains how to use the custom Chrome WebDriver module for Selenium. This module is designed to provide a flexible and automated way to interact with the Chrome browser using configurations stored in a `chrome.json` file, along with support for user agent, browser profile settings, and custom options.

Execution steps
-------------------------
1. **Install dependencies**: Ensure you have the following libraries installed: `selenium`, and `fake_useragent`. You can install them using pip:
    ```bash
    pip install selenium fake_useragent
    ```
    Also, make sure `chromedriver` is accessible in your system's `PATH` or that you specify its location in the configuration file.
2.  **Locate the configuration file**: The module reads settings from a `chrome.json` file, which should be located in the `src/webdriver/chrome/` directory.
3.  **Understand configuration**: The `chrome.json` file is used to configure various aspects of the Chrome WebDriver:
    -   `options`: Specifies Chrome parameters like log levels, disabling `/dev/shm`, and setting a remote debugging port. `arguments`  contain a list of command line options.
    -   `disabled_options`: Contains options that are explicitly disabled. For example, disables headless mode.
    -   `profile_directory`: Specifies paths for Chrome user data for different environments, such as `os` (default), `internal` (default for WebDriver) and `testing` (testing profile).
    -  `binary_location`: Specifies path to different chrome binaries such as `os` (installed Chrome binary), `exe` (chromedriver) and `binary` (binary for testing).
    -   `headers`: Defines custom HTTP headers for browser requests.
    -   `proxy_enabled`: Boolean that indicates if a proxy server is enabled.
4.  **Import and initialize the `Chrome` class**: In your Python script, import the `Chrome` class from the `src.webdriver.chrome` module, and create an instance of this class. During initialization, you can pass optional parameters like `user_agent` and `options`, which will override the `chrome.json` settings.
    - Example: `browser = Chrome()`
    - Example with a custom user agent and headless mode: `browser = Chrome(user_agent="custom_user_agent", options=["--headless", "--disable-gpu"])`
5.  **Interact with the browser**: After initialization, use the `browser` object to interact with web pages using Selenium methods like `get` and customized methods from the `src.webdriver.driver.Driver` class like `scroll` and `locale`.
6.  **Handle exceptions**: The module logs errors and warnings using the `logger` from the `src.logger` module. Ensure to review these logs for debugging and to address any issues.
7. **Singleton pattern**: The module implements the Singleton pattern, ensuring only one instance of the `Chrome` driver exists.

Usage example
-------------------------
```python
from src.webdriver.chrome.chrome import Chrome
from selenium.webdriver.common.by import By

def main():
    # Example 1: Initialize Chrome WebDriver with default settings
    browser = Chrome()
    browser.get("https://www.example.com")
    print("Successfully navigated to the URL with default settings")

    # Example 2: Find an element by CSS selector
    element = browser.find_element(By.CSS_SELECTOR, 'h1')
    if element:
      print(f"Found element with text: {element.text}")
    else:
      print("Did not find any element with selector h1")

    # Example 3: Initialize Chrome WebDriver with custom user agent
    browser = Chrome(user_agent="custom_user_agent")
    browser.get("https://www.example.com")
    print("Successfully navigated to the URL with custom user agent")

    # Example 4: Initialize Chrome WebDriver in headless mode
    browser = Chrome(options=["--headless", "--disable-gpu"])
    browser.get("https://www.example.com")
    print("Successfully navigated to the URL in headless mode")

    # Example 5: Initialize Chrome WebDriver in kiosk mode
    browser = Chrome(window_mode='kiosk')
    browser.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode")


    # Example 6: Scroll the page down
    browser.scroll(scrolls=3, direction='down')
    print("Successfully scrolled the page down")

    # Example 7: Get the page language
    page_language = browser.locale
    print(f"Page language: {page_language}")

    # Example 8: Focus the window
    browser.window_focus()
    print("Focused the window")

    # Example 9: Save cookies
    browser._save_cookies_localy()
    print("Cookies saved.")

    browser.quit()

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the custom `Chrome` WebDriver module, including its key features and components.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Explained the configuration options in `chrome.json`.
- Explained the singleton pattern implementation for WebDriver.
- Provided detailed logging and debugging instructions.
- Added examples for various use cases such as custom user agent, headless mode, kiosk mode, getting the page language and saving cookies.
- Added an example of scrolling the page down.