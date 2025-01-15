# Module: src.webdriver.chrome.chrome

## Overview

This module provides an enhanced `Chrome` class for working with Selenium WebDriver. It extends the base `webdriver.Chrome` class with additional functionalities such as proxy configuration, custom user agent, and window mode settings.

## Table of Contents

1.  [Classes](#classes)
    -   [Chrome](#chrome-class)
        -   [`__init__`](#__init__)
        -   [`set_proxy`](#set_proxy)
        -   [`_payload`](#_payload)

## Classes

### `Chrome`

**Description**: This class extends `selenium.webdriver.Chrome` with additional functionalities for setting up Chrome web drivers.

**Attributes**:
- `driver_name` (str): The name of the driver.

**Methods**:
-   [`__init__`](#__init__)
-   [`set_proxy`](#set_proxy)
-   [`_payload`](#_payload)

#### `__init__`

```python
def __init__(self, profile_name: Optional[str] = None,
             chromedriver_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             options: Optional[List[str]] = None,
             window_mode: Optional[str] = None,
             *args, **kwargs) -> None:
    """
    Initializes the Chrome WebDriver with additional functionalities.

    Args:
        profile_name (Optional[str], optional): Name of the Chrome user profile. Defaults to None.
        chromedriver_version (Optional[str], optional): Version of the chromedriver. Defaults to None.
        user_agent (Optional[str], optional): User agent string. Defaults to None.
        proxy_file_path (Optional[str], optional): Path to the proxy file. Defaults to None.
        options (Optional[List[str]], optional): List of Chrome options. Defaults to None.
        window_mode (Optional[str], optional): Browser window mode (`windowless`, `kiosk`, `full_window`, etc.). Defaults to None.
    """
```
**Description**: Initializes the Chrome WebDriver with additional functionalities.
**Parameters**:
    - `profile_name` (Optional[str], optional): Name of the Chrome user profile. Defaults to `None`.
    - `chromedriver_version` (Optional[str], optional): Version of the chromedriver. Defaults to `None`.
    - `user_agent` (Optional[str], optional): User agent string. Defaults to `None`.
    -  `proxy_file_path` (Optional[str], optional): Path to the proxy file. Defaults to `None`.
    -   `options` (Optional[List[str]], optional): List of Chrome options. Defaults to `None`.
    -  `window_mode` (Optional[str], optional): Browser window mode (`'windowless'`, `'kiosk'`, `'full_window'`, etc.). Defaults to `None`.
**Returns**:
    - `None`

#### `set_proxy`

```python
def set_proxy(self, options: Options) -> None:
    """
    Configures proxy settings from a dictionary returned by `get_proxies_dict`.

    Args:
        options (Options): Chrome options where proxy settings are added.
    """
```
**Description**: Configures proxy settings from a dictionary returned by `get_proxies_dict`.
**Parameters**:
    -  `options` (Options): Chrome options where proxy settings are added.
**Returns**:
    - `None`

#### `_payload`

```python
def _payload(self) -> None:
     """
    Loads executors for locators and JavaScript scenarios.
     """
```
**Description**: Loads executors for locators and JavaScript scenarios.
**Returns**:
    - `None`