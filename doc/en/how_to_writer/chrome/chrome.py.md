How to use this code block
=========================================================================================

Description
-------------------------
The `chrome.py` module provides an extended implementation of Selenium's Chrome WebDriver. It includes functionalities for setting up Chrome with custom profiles, user agents, proxy configurations, and various browser options. The module also integrates with JavaScript utilities and an executor for managing interactions with web elements.

Execution steps
-------------------------
1.  **Import necessary modules**: Ensure all required modules are imported. These include standard libraries like `os`, `pathlib`, `typing`, and external libraries such as `selenium`, `fake_useragent`, and internal modules from `src`.
2.  **Initialize the `Chrome` class**: Create an instance of the `Chrome` class. You can customize its behavior by passing optional parameters during initialization:
    -   `profile_name`: The name of the Chrome user profile to use.
    -   `chromedriver_version`: The version of the Chrome driver.
    -   `user_agent`: A custom user-agent string. If none is provided, a random user agent is selected using `fake_useragent`.
    -   `proxy_file_path`: The path to a file containing proxy configurations.
    -   `options`: A list of Chrome browser options (e.g., `--headless`, `--disable-gpu`).
    -  `window_mode`: Sets the browser window mode ('kiosk', 'windowless' or 'full_window').
    -   Example: `driver = Chrome(profile_name='my_profile', user_agent='custom_user_agent', options=['--headless'])`
    -   Example without parameters: `driver = Chrome()`
3.  **Understand the initialization process**:
    -   The constructor loads settings from `chrome.json`.
    -   It sets the path to the `chromedriver` executable.
    -   It initializes Chrome options using the settings from the JSON and passed parameters.
    -  It configures the browser window mode.
    -   It sets a custom user agent or chooses a random one using `fake_useragent`.
    -   It sets a proxy server if enabled in the config.
    -   It configures the profile directory, replacing `%LOCALAPPDATA%` with the environment variable.
    -   It initializes the `WebDriver` and calls the `_payload` method.
4.  **Set proxy (if enabled)**: The `set_proxy` method, if enabled in `chrome.json`, reads proxies from a proxy file and configures them in Chrome options, it validates the proxies using the `check_proxy` method.
5. **Use payload**:
     - The `_payload` method initializes `JavaScript` and `ExecuteLocator` classes by creating an instance of the classes and passing the current `Chrome` driver instance.
     - It assigns methods and properties from those classes to the `Chrome` instance.
6. **Use the WebDriver**: After initialization, use the methods from `selenium.webdriver.Chrome` and extended methods from `src.webdriver.js` and `src.webdriver.executor` modules.
7. **Handle exceptions**: The module includes try-except blocks to catch and log errors. Check the logs for any issues.

Usage example
-------------------------
```python
from src.webdriver.chrome.chrome import Chrome
from selenium.webdriver.common.by import By


def main():
    # Example 1: Initialize a Chrome driver with default settings
    driver = Chrome()
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with default settings")

    # Example 2: Find an element by its CSS selector
    element = driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
      print(f"Found element with text: {element.text}")
    else:
       print("Did not find element by specified CSS")

    # Example 3: Focus the window
    driver.window_focus()
    print("Focused the window")

    # Example 4: Scroll the page
    driver.scroll(scrolls=3, direction='down')
    print("Successfully scrolled down")

    # Example 5: Get the page language
    page_language = driver.get_page_lang()
    print(f"Page language: {page_language}")

    # Example 6: Initialize a Chrome driver in kiosk mode
    driver = Chrome(window_mode='kiosk')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode")

    # Example 7: Initialize a Chrome driver with a custom user agent
    driver = Chrome(user_agent='custom_user_agent')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with a custom user agent")


    # Example 8: Initialize a Chrome driver with custom profile name
    driver = Chrome(profile_name='my_custom_profile')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with a custom profile")


if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `chrome.py` module and its functionality.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations about the initialization process and how the driver is configured, including proxy setting and profile directory.
- Added examples for different use cases and parameters to demonstrate usage.
- Added comments to the usage example.
- Updated the explanation to include the `_payload` method functionality.