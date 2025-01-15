How to use this code block
=========================================================================================

Description
-------------------------
This document describes the custom `Chrome` WebDriver module for Selenium. This module integrates settings defined in a `chrome.json` file, allowing flexible and automated interactions with web pages using Chrome. It provides capabilities for managing user agents, browser profiles, proxy settings, and handling errors.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that the following libraries are installed: `selenium`, and `fake_useragent`. You can install them using pip:
    ```bash
    pip install selenium fake_useragent
    ```
2.  **Locate the configuration file**: The module relies on the `chrome.json` configuration file to manage settings for the WebDriver, this file should be placed in `src/webdriver/chrome/`.
3.  **Understand Configuration**: The `chrome.json` file has the following main sections:
    -   `options`: A dictionary containing various Chrome parameters, such as log level, disabling `/dev/shm`, and setting a remote debugging port.
    -   `disabled_options`: Contains options that are explicitly disabled.
    -   `profile_directory`: Specifies paths to Chrome user data directories for different environments.
    -  `binary_location`: Specifies paths for various Chrome binaries (executable, chromedriver and chrome binary).
    -   `headers`: Defines custom HTTP headers for browser requests.
    -   `proxy_enabled`: Enables/disables proxy server settings.
4.  **Initialize the `Chrome` class**: Create an instance of the `Chrome` class by importing it from `src.webdriver.chrome` module.  You can optionally pass parameters such as `user_agent` and `options` which will override the settings in the config file.
     -  Example:  `browser = Chrome()` or `browser = Chrome(user_agent="Mozilla/5.0", options=["--headless"])` or `browser = Chrome(window_mode="kiosk")`
    -   The class loads the configuration from `chrome.json` automatically.
    - The class uses a Singleton pattern - if an instance exists it will reuse the same instance.
5.  **Use the WebDriver**: After initialization, use the `browser` object to interact with web pages. Use methods from selenium like `get`, and use the methods from the extended driver for additional functionality like `scroll`, `locale` etc.
6.  **Handle exceptions**: The module uses try-except blocks to catch and log errors during various operations. Refer to the logs for debugging information.

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
        print(f"Did not find any element with selector h1")

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

    # Example 6: Focus the window
    browser.window_focus()
    print("Focused the window")

    # Example 7: Use the scroll functionality
    browser.scroll(scrolls=2, direction='down')
    print("Successfully scrolled the page")

    # Example 8: Save cookies
    browser._save_cookies_localy()
    print("Cookies saved")


    browser.quit()


if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the custom `Chrome` WebDriver module and its functionality.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added details on configuration from the `chrome.json` file.
- Explained the Singleton pattern usage.
- Added examples to show how to set a custom user agent, use headless mode and kiosk mode.
- Added examples of using methods such as `window_focus` and `scroll` from the extended driver.
- Added an example of saving cookies.