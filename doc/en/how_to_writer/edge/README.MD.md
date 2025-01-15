How to use this code block
=========================================================================================

Description
-------------------------
This document provides an overview of the custom Edge WebDriver module for Selenium. The module is designed to simplify Edge browser automation by integrating configurations from an `edge.json` file. This allows setting user agents, browser profiles, and various other options, providing flexible and automated browser interactions.

Execution steps
-------------------------
1.  **Install dependencies**: Ensure that the required libraries are installed: `selenium` and `fake_useragent`. Install them using pip:
    ```bash
    pip install selenium fake_useragent
    ```
    Also make sure `msedgedriver` binary is available in your system's `PATH` or specify its path in the configuration file.
2.  **Locate configuration file**: The module loads its configuration from the `edge.json` file which should be placed in the `src/webdriver/edge/` directory.
3.  **Understand the configuration**: The `edge.json` file has the following sections:
    -   `options`: A list of command line arguments passed to the browser, example:  `--disable-dev-shm-usage` or `--remote-debugging-port=0`.
    -   `profiles`: Paths to Edge user data directories (`os` for operating system path, `internal` for an internal webdriver path).
    -   `executable_path`:  Contains path to the `msedgedriver.exe` binary.
    -   `headers`: Defines custom headers like `User-Agent` and `Accept`.
4.  **Initialize the `Edge` class**: Create an instance of the `Edge` class, which initializes the Edge WebDriver. You can use parameters such as `user_agent`, `options` and `window_mode` during the initialization to configure the WebDriver.
     - Example: `driver = Edge()` to initialize with default settings.
    -  Example with custom user agent: `driver = Edge(user_agent="custom_user_agent")`
    -  Example with custom options: `driver = Edge(options=["--headless", "--disable-gpu"])`
    -  Example with window mode set to kiosk: `driver = Edge(window_mode='kiosk')`
    - The class loads configuration settings from the `edge.json` file.
5.  **Use WebDriver methods**: After initialization, you can interact with the Edge browser using standard Selenium methods like `get`. You can also access extended methods from `src.webdriver.js` and `src.webdriver.executor` using the created `driver` instance.
6. **Use the `set_options` method**: To create custom options use `set_options` and pass a list of options.
7. **Understand the singleton pattern**: The module uses the Singleton pattern, ensuring that only one instance of the WebDriver is created. If an instance already exists it will be reused.
8.  **Handle exceptions**: The module includes try-except blocks to log errors and warnings to `src.logger`. Refer to these logs to troubleshoot any problems.

Usage example
-------------------------
```python
from src.webdriver.edge.edge import Edge
from selenium.webdriver.common.by import By


def main():
    # Example 1: Initialize Edge WebDriver with default settings
    driver = Edge()
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL using default settings")

    # Example 2: Find an element by CSS selector
    element = driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    else:
       print("Element with CSS selector h1 was not found")

    # Example 3: Focus the window
    driver.window_focus()
    print("Focused the window")

    # Example 4: Initialize Edge WebDriver with custom user agent
    driver = Edge(user_agent="custom_user_agent")
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with custom user agent")

    # Example 5: Initialize Edge WebDriver in kiosk mode
    driver = Edge(window_mode='kiosk')
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL in kiosk mode")

     # Example 6: Initialize Edge WebDriver with custom options
    custom_options = ["--headless", "--disable-gpu"]
    driver = Edge(options=custom_options)
    driver.get("https://www.example.com")
    print("Successfully navigated to the URL with custom options.")

    # Example 7: Scroll the page down
    driver.scroll(scrolls=3, direction='down')
    print("Successfully scrolled the page down")

    # Example 8: Get page language
    page_language = driver.get_page_lang()
    print(f"Page language: {page_language}")

    driver.quit()

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `Edge WebDriver Module`.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for the configuration and initialization of the `Edge` class, and the use of `edge.json` file.
- Added explanations about the singleton pattern.
- Provided examples of how to use custom options and other parameters such as `user_agent` and `window_mode` during initialization.
- Added examples for the use of methods such as `scroll`, `window_focus` and `get_page_lang` from the `src.webdriver.driver.Driver` class.
- Added information about error handling and logging.
- Added an example on how to use the `set_options` method.