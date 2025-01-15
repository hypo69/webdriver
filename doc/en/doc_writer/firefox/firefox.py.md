# Firefox WebDriver Module for Selenium

This module provides a custom implementation of the Firefox WebDriver using Selenium. It enhances the standard `webdriver.Firefox` by adding functionalities for custom profiles, kiosk mode, user-agent, and proxy settings.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Requirements](#requirements)
3.  [Configuration](#configuration)
    -   [Example Configuration (`firefox.json`)](#example-configuration-firefoxjson)
    -   [Configuration Fields Description](#configuration-fields-description)
        -   [`options`](#1-options)
        -   [`profile_directory`](#2-profile_directory)
        -   [`executable_path`](#3-executable_path)
        -   [`headers`](#4-headers)
        -   [`proxy_enabled`](#5-proxy_enabled)
4.  [Usage](#usage)
    -   [Initialization](#initialization)
    -   [Example](#example)
5.  [Logging and Debugging](#logging-and-debugging)
    -   [Example Logs](#example-logs)
6.  [License](#license)

## Key Features

-   **Custom Profile**: Supports custom Firefox profiles for personalized browser settings.
-   **Kiosk Mode**: Enables launching Firefox in kiosk mode.
-   **User-Agent Configuration**: Allows you to set a custom user-agent for the browser.
-   **Proxy Support**: Integrates proxy settings from a file.
-  **Centralized Configuration**: Configuration is managed via the `firefox.json` file.
-   **Enhanced Logging**: Provides detailed logs for debugging and error tracking.

## Requirements

Before using this module, ensure the following dependencies are installed:

-   Python 3.x
-   Selenium
-   Fake User Agent
-   Firefox WebDriver binary (e.g., `geckodriver`)

Install the required Python dependencies:

```bash
pip install selenium fake_useragent
```

Additionally, ensure the `geckodriver` binary is available in your system's `PATH` or specify its path in the configuration.

## Configuration

The configuration for the Firefox WebDriver is stored in the `firefox.json` file. Below is an example structure of the configuration file and its description:

### Example Configuration (`firefox.json`)

```json
{
  "options": ["--kiosk", "--headless"],
  "profile_directory": {
    "os": "%LOCALAPPDATA%\\\\Mozilla\\\\Firefox\\\\Profiles\\\\default",
    "internal": "webdriver\\\\firefox\\\\profiles\\\\default"
  },
  "executable_path": {
    "firefox_binary": "bin\\\\webdrivers\\\\firefox\\\\ff\\\\core-127.0.2\\\\firefox.exe",
    "geckodriver": "bin\\\\webdrivers\\\\firefox\\\\gecko\\\\33\\\\geckodriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  },
  "proxy_enabled": false
}
```

### Configuration Fields Description

#### 1. `options`

A list of options to pass to the Firefox WebDriver. Examples:
-   `--kiosk`: Launch Firefox in kiosk mode.
-   `--headless`: Launch Firefox in headless mode.

#### 2. `profile_directory`

Paths to Firefox user data directories for different environments:

-  **os**: Path to the default user data directory (typically for Windows systems).
-  **internal**: Internal path for the default WebDriver profile.

#### 3. `executable_path`

Paths to the Firefox binaries:

-   **firefox_binary**: Path to the Firefox binary executable.
-  **geckodriver**: Path to the geckodriver executable.

#### 4. `headers`

Custom HTTP headers used in browser requests:

-   **User-Agent**: Sets the user-agent string for the browser.
-   **Accept**: Sets the types of data the browser is willing to accept.

#### 5. `proxy_enabled`

A boolean value indicating whether proxy settings are enabled for the WebDriver.

## Usage

To use the `Firefox` WebDriver in your project, simply import and initialize it:

### Initialization

Create an instance of `Firefox` class. The constructor automatically initializes the Firefox WebDriver with settings from `firefox.json`. You can also specify custom user-agent and pass additional options during WebDriver initialization.

### Example

```python
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    browser = Firefox(
        profile_name=profile_name,
        geckodriver_version=geckodriver_version,
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Logging and Debugging

The WebDriver class uses the `logger` from `src.logger` to log errors, warnings, and general information. All issues encountered during initialization, configuration, or execution will be logged for easy debugging.

### Example Logs

-   **Error during WebDriver initialization**: `Error initializing Firefox WebDriver: <error details>`
-   **Configuration issues**: `Error in firefox.json file: <issue details>`

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.