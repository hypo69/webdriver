How to use this code block
=========================================================================================

Description
-------------------------
This document describes the custom Edge WebDriver module for Selenium. The module is designed to simplify Edge browser automation by integrating settings from an `edge.json` configuration file. This allows setting user agents, browser profiles, and various other options, providing flexible and automated browser interactions.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that the required libraries are installed: `selenium`, and `fake_useragent`. Install them using pip:
    ```bash
    pip install selenium fake_useragent
    ```
    Also, ensure that the `msedgedriver` binary is available in your system's `PATH` or specify its path in the configuration.
2.  **Locate the configuration file**: The module uses a `edge.json` file for configuration. This file should be placed in the `src/webdriver/edge/` directory.
3.  **Understand configuration**: The `edge.json` file has the following structure:
    -   `options`: A list of command-line arguments passed to the browser. Example: `--disable-dev-shm-usage`, or  `--remote-debugging-port=0`.
    -   `profiles`: Specifies paths to Edge user data directories using `os` for the operating system's path and `internal` for webdriver's internal profile path.
    -   `executable_path`: The path to the `msedgedriver.exe` binary, with the `default` key holding its location.
    -   `headers`: Defines custom HTTP headers, including `User-Agent`, `Accept`, `Accept-Charset`, `Accept-Encoding`, `Accept-Language` and `Connection`.
4.  **Initialize the `Edge` class**: Create an instance of the `Edge` class. You can pass parameters during initialization to customize the browser.
      - Example: `driver = Edge()` for initialization using default configurations from the `edge.json` file.
    -  Example with a custom user-agent:  `driver = Edge(user_agent="custom_user_agent")`
    -  Example with custom options: `driver = Edge(options=["--headless", "--disable-gpu"])`
    - Example with a specific window mode: `driver = Edge(window_mode='kiosk')`
    -   The `Edge` class automatically loads settings from the `edge.json` file.
    - The module uses the Singleton pattern, ensuring that only one instance of the WebDriver is created.
5.  **Use WebDriver methods**: After initializing the driver, use the methods from the base class or extended methods to interact with the web page using Selenium.
6.  **Handle exceptions**: The module uses try-except blocks to catch and log errors using `logger` from `src.logger`. Make sure to check the logs to handle any issues.

Usage example
-------------------------
```python
from src.webdriver.edge.edge import Edge
from selenium.webdriver.common.by import By

def main():
    # Example 1: Initialize Edge WebDriver with default settings
    driver = Edge()
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL using default settings.")

    # Example 2: Find element by CSS selector
    element = driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    else:
         print("Element with CSS selector h1 was not found")

    # Example 3: Focus the window
    driver.window_focus()
    print("Focused the window.")


    # Example 4: Initialize Edge WebDriver with a custom user-agent
    driver = Edge(user_agent="custom_user_agent")
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with custom user agent.")


     # Example 5: Initialize Edge WebDriver in kiosk mode
    driver = Edge(window_mode='kiosk')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode.")

    # Example 6: Use custom options
    driver = Edge(options=['--headless', '--disable-gpu'])
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL using custom options.")

    # Example 7: Scroll the page down
    driver.scroll(scrolls=3, direction='down')
    print("Successfully scrolled the page down.")

   # Example 8: Get the page language
    page_language = driver.get_page_lang()
    print(f"Page language: {page_language}")


    driver.quit()

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the custom `Edge WebDriver Module` and its features.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added a section that explains the configuration options of `edge.json` file.
- Included more details about the use of custom user agent, options and window mode.
- Added examples for methods such as `scroll` and `get_page_lang` from extended `Edge` class.
- Added an explanation of singleton implementation and error handling using `logger`.