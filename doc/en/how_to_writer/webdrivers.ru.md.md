How to use this code block
=========================================================================================

Description
-------------------------
This document provides an overview of various web drivers available in the project, including their settings and options. Each web driver is configured through a JSON file that allows customization for specific use cases. This guide covers Firefox, Chrome, Edge, Playwright, and BeautifulSoup with XPath parser.

Execution steps
-------------------------
This document does not contain code for direct execution but provides configuration details and instructions for using different web drivers. Here are the steps to understand and utilize the information:

1.  **Identify the web driver**: Choose the appropriate web driver based on your project's requirements (Firefox, Chrome, Edge, Playwright, or BeautifulSoup with XPath parser).
2.  **Locate the configuration file**: Each web driver has a corresponding JSON configuration file (e.g., `firefox.json`, `chrome.json`, `edge.json`, `playwrid.json`, `bs.json`). These files contain the settings for the driver.
3.  **Understand the settings**: Each configuration file contains various settings specific to the web driver:
    -   **Firefox WebDriver**:
        -   `profile_name`: User profile name.
        -   `geckodriver_version`: Version of geckodriver.
        -   `firefox_version`: Version of Firefox.
        -   `user_agent`: Custom user agent string.
        -   `proxy_file_path`: Path to the file containing proxy configurations.
        -   `options`: A list of browser options (e.g., `["--kiosk", "--headless"]`).
    -   **Chrome WebDriver**:
        -   `profile_name`: User profile name.
        -   `chromedriver_version`: Version of chromedriver.
        -   `chrome_version`: Version of Chrome.
        -   `user_agent`: Custom user agent string.
        -   `proxy_file_path`: Path to the file containing proxy configurations.
        -   `options`: A list of browser options (e.g., `["--headless", "--disable-gpu"]`).
    -   **Edge WebDriver**:
        -   `profile_name`: User profile name.
        -   `edgedriver_version`: Version of edgedriver.
        -   `edge_version`: Version of Edge.
        -   `user_agent`: Custom user agent string.
        -   `proxy_file_path`: Path to the file containing proxy configurations.
        -   `options`: A list of browser options (e.g., `["--headless", "--disable-gpu"]`).
    -   **Playwright Crawler**:
        -   `max_requests`: Maximum number of requests.
        -   `headless`: Flag to enable headless mode.
        -   `browser_type`: Type of browser to use (`chromium`, `firefox`, or `webkit`).
        -   `user_agent`: Custom user agent string.
        -   `proxy`: Proxy server settings.
        -   `viewport`: Browser viewport settings.
        -   `timeout`: Request timeout settings.
        -   `ignore_https_errors`: Flag to ignore HTTPS errors.
    -   **BeautifulSoup and XPath Parser**:
        -   `default_url`: Default URL for loading HTML.
        -   `default_file_path`: Default file path for loading HTML.
        -   `default_locator`: Default locator settings (by, attribute, selector).
        -   `logging`: Settings for logging (level and file).
        -   `proxy`: Proxy server settings.
        -    `timeout`: Timeout for requests.
        -    `encoding`: Encoding type for reading files or requests.
4.  **Customize the configuration**: Modify the JSON configuration file to match your needs, such as specifying a user-agent string, setting up proxy server, adding browser options, etc.
5.  **Use the configuration**:
    - In your project, read the settings from the JSON file using `j_loads` or `j_loads_ns`.
    - Pass the settings to your chosen web driver initialization process to configure the driver accordingly.

Usage example
-------------------------
This example shows how to load a config file and access it's values, but not how to use the driver itself, as this is a documentation guide and does not contain runnable code.

```python
import json
from pathlib import Path
from src.utils.jjson import j_loads

def main():
    # Example 1: Load the config file
    config_file_path = Path('src') / 'webdriver' / 'chrome.json'
    chrome_config = j_loads(config_file_path)

    if chrome_config:
        print("Configuration loaded successfully")

        # Example 2: Access a specific value
        print(f"Chrome Options: {chrome_config.get('options')}")
        print(f"User agent: {chrome_config.get('headers').get('User-Agent')}")
        print(f"Is proxy enabled: {chrome_config.get('proxy_enabled')}")
        print(f"Chrome executable path : {chrome_config.get('executable_path').get('chrome_binary')}")

    else:
        print("Failed to load configuration file")

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the web driver configurations.
- Outlined clear steps to understand and use the configuration files.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for each web driver and their respective settings.
- Included a usage example for loading and accessing values in a config file.
- Added a note about using `j_loads` or `j_loads_ns` for loading the config.