How to use this code block
=========================================================================================

Description
-------------------------
This `firefox.py` module provides a custom implementation of the Firefox WebDriver using Selenium. It enhances the standard `webdriver.Firefox` class by providing options for custom profiles, kiosk mode, proxy settings and user agent management. It integrates with `JavaScript` and `ExecuteLocator` modules to extend functionality, making it easier to automate Firefox browser interactions.

Execution steps
-------------------------
1.  **Import necessary modules**: Ensure that necessary modules including `os`, `pathlib`, `typing`, `selenium`, `fake_useragent` and other custom modules from `src` are imported.
2.  **Initialize the `Firefox` class**: Create an instance of the `Firefox` class, optionally providing the following parameters for customization:
    -   `profile_name`: The name of the Firefox user profile to use.
    -   `geckodriver_version`: The version of the geckodriver.
    -   `firefox_version`: The version of Firefox.
    -   `user_agent`: A custom user-agent string. If `None`, a random user agent is used.
    -   `proxy_file_path`: A path to a file containing proxy configurations.
    -   `options`: A list of options to pass to the browser (e.g., `--headless`, `--kiosk`).
    -  `window_mode`: Sets the browser window mode (`windowless`, `kiosk`, `full_window` etc.)
     - Example: `driver = Firefox()` to initialize using default configurations from `firefox.json`.
     - Example with custom user agent, profile and options: `driver = Firefox(profile_name='my_profile', user_agent='custom_user_agent', options=['--headless'])`
     - Example with window mode set to kiosk: `driver = Firefox(window_mode='kiosk')`
3.  **Understand the initialization process**:
    - The constructor loads settings from `firefox.json`.
    - It sets paths for geckodriver and Firefox binary.
    - It initializes a `Service` for geckodriver and `Options` for Firefox.
    - It sets the browser window mode if provided using settings from configuration file or passed as an argument.
    -  It applies custom options, if passed during instantiation or defined in settings.
    - It sets the custom or random user agent.
    - It configures proxies if enabled in the settings.
    - It sets the Firefox profile directory, replacing `%LOCALAPPDATA%` with the appropriate environment variable.
    - It initializes `WebDriver` using configured `options` and `service` parameters and calls `_payload` method.
4. **Set proxy if enabled**:
    -   The `set_proxy` method reads proxy settings from a file (if the proxy is enabled), validates the proxies, and configures Firefox to use a working proxy by setting the proper `network.proxy` preferences.
5. **Use payload**:
     - The `_payload` method initializes the `JavaScript` and `ExecuteLocator` classes and then assigns their methods and properties to the current instance of the `Firefox` driver.
6.  **Use WebDriver methods**: After the driver is initialized, use standard methods from the `selenium.webdriver.Firefox` and extended methods using `JavaScript` and `ExecuteLocator` that have been injected using the `_payload` method.
7.  **Handle exceptions**: The module uses try-except blocks to catch and log errors using `logger` from `src.logger.logger`. Refer to these logs for debugging.

Usage example
-------------------------
```python
from src.webdriver.firefox.firefox import Firefox
from selenium.webdriver.common.by import By


def main():
    # Example 1: Initialize Firefox WebDriver with default settings
    driver = Firefox()
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with default settings")

    # Example 2: Find an element by CSS selector
    element = driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    else:
        print("Element with CSS selector h1 was not found")

    # Example 3: Focus the window
    driver.window_focus()
    print("Focused the window")

    # Example 4: Scroll the page
    driver.scroll(scrolls=3, direction='down')
    print("Successfully scrolled the page")

    # Example 5: Get the page language
    page_language = driver.get_page_lang()
    print(f"Page language: {page_language}")

    # Example 6: Initialize Firefox WebDriver in kiosk mode
    driver = Firefox(window_mode='kiosk')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode")

   # Example 7: Initialize Firefox WebDriver with custom user agent and profile name
    driver = Firefox(profile_name='my_profile', user_agent="custom_user_agent")
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with a custom user agent and profile")

    # Example 8: Initialize Firefox WebDriver with custom options
    driver = Firefox(options=['--headless'])
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL using custom options")

    # Example 9: Save cookies
    driver._save_cookies_localy()
    print("Cookies Saved")

    driver.quit()

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `firefox.py` module, including its purpose, methods, and how to use them.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added a comprehensive explanation for configuration and initialization of Firefox driver, including handling for proxy, profiles, user agent and custom options.
- Added examples of how to use various methods from the extended driver.
- Added explanation on how the driver loads Javascript and Executor functionality with `_payload` method.
- Improved descriptions of exceptions and logging.