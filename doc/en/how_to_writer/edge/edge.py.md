How to use this code block
=========================================================================================

Description
-------------------------
The `edge.py` module provides a custom implementation of the Edge WebDriver using Selenium. This module is designed to simplify Edge browser automation by integrating settings from a `edge.json` configuration file and providing methods to interact with the web page. It supports custom user agents, browser profiles, and various options.

Execution steps
-------------------------
1.  **Import necessary modules**: Ensure all required modules, including `os`, `pathlib`, `typing`, `selenium`, `fake_useragent`, and custom modules from `src`, are imported.
2.  **Initialize the `Edge` class**: Create an instance of the `Edge` class. You can pass optional parameters like `profile_name`, `user_agent`, `options`, and `window_mode` during initialization to customize the browser.
    - The module uses default configuration from `edge.json` by default.
    -   Example: `driver = Edge()` to initialize with default settings.
    -   Example with a custom profile and user agent: `driver = Edge(profile_name='my_profile', user_agent='custom_user_agent', options=['--headless'])`
    - Example with a specified window mode: `driver = Edge(window_mode='kiosk')`
3. **Understand the initialization process:**
     - The constructor loads settings from the `edge.json` file located in `src/webdriver/edge/`.
    -   It initializes Edge options with a user agent from config, a random user agent, or passed user agent, and other configuration settings.
    -  It configures the browser window mode.
    - It sets profile directory if defined in the settings or uses a default.
    -   It initializes the Edge service and the `WebDriver`, and then calls the `_payload` method.
4.  **Configure proxy**: The module does not directly use proxies from configuration file. If you need proxy support please refer to the `src.webdriver.proxy` module and implement proxy settings according to your needs.
5. **Customize options**: You can create EdgeOptions with `set_options` method by passing a list of options.
6.  **Use payload**: The `_payload` method initializes instances of `JavaScript` and `ExecuteLocator` passing the current `Edge` driver instance. It then assigns methods and properties from those classes to the current `Edge` driver instance.
7.  **Use WebDriver methods**: After initialization, you can use the methods inherited from `selenium.webdriver.Edge` to control the browser as well as extended methods from `JavaScript` and `ExecuteLocator` that have been injected in `_payload` method.
8. **Handle exceptions**: The module includes try-except blocks that log errors using `logger` from `src.logger.logger` during WebDriver initialization. Review logs for troubleshooting any issues.

Usage example
-------------------------
```python
from src.webdriver.edge.edge import Edge
from selenium.webdriver.common.by import By

def main():
    # Example 1: Initialize the Edge WebDriver with default settings
    driver = Edge()
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with default settings")


    # Example 2: Find element by CSS selector
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


    # Example 5: Initialize Edge WebDriver with custom user-agent
    driver = Edge(user_agent="custom_user_agent")
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with custom user agent.")

    # Example 6: Initialize Edge WebDriver in kiosk mode
    driver = Edge(window_mode='kiosk')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode.")


    # Example 7: Get the page language
    page_language = driver.get_page_lang()
    print(f"Page language: {page_language}")

    # Example 8: Initialize and use a custom list of options
    custom_options = ["--headless", "--disable-gpu"]
    driver = Edge(options=custom_options)
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL using custom options.")

    # Example 9: Save cookies
    driver._save_cookies_localy()
    print("Cookies Saved")


    driver.quit()

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `edge.py` module, including its purpose, methods, and how to use them.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations for the Edge initialization process and usage of profile, proxy, and custom options.
- Included examples for setting custom user-agent, `window_mode`, a list of custom options and saving cookies.
- Added examples for the use of methods from the `src.webdriver.js` and `src.webdriver.executor` modules.
- Added explanation about the `_payload` method.