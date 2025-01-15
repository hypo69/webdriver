# Module: src.webdriver.edge.edge

## Overview

This module provides a custom `Edge` class that extends Selenium's `webdriver.Edge` with enhanced functionalities, including simplified configuration using `fake_useragent`, and additional methods for interacting with web pages.

## Table of Contents
1.  [Classes](#classes)
    -   [Edge](#edge-class)
        -   [`__init__`](#__init__)
        -   [`_payload`](#_payload)
        -   [`set_options`](#set_options)

## Classes

### `Edge`

**Description**: This class provides an extension for `selenium.webdriver.Edge` with custom configurations.

**Attributes**:
-   `driver_name` (str): Name of the WebDriver used, defaults to `'edge'`.

**Methods**:
-   [`__init__`](#__init__)
-   [`_payload`](#_payload)
-  [`set_options`](#set_options)

#### `__init__`

```python
def __init__(self,  profile_name: Optional[str] = None,
             user_agent: Optional[str] = None,
             options: Optional[List[str]] = None,
             window_mode: Optional[str] = None,
             *args, **kwargs) -> None:
    """
    Initializes the Edge WebDriver with the specified user agent and options.

    Args:
        profile_name (Optional[str], optional): The name of the user profile. Defaults to None.
        user_agent (Optional[str], optional): The user-agent string to be used. If `None`, a random user agent is generated. Defaults to None.
        options (Optional[List[str]], optional): A list of Edge options to be passed during initialization. Defaults to None.
        window_mode (Optional[str], optional): Browser window mode ('windowless', 'kiosk', 'full_window', etc.). Defaults to None.
    """
```
**Description**: Initializes the Edge WebDriver with the specified user agent and options.
**Parameters**:
    -   `profile_name` (Optional[str], optional): The name of the user profile. Defaults to `None`.
    -  `user_agent` (Optional[str], optional): The user-agent string to be used. If `None`, a random user agent is generated. Defaults to `None`.
    -   `options` (Optional[List[str]], optional): A list of Edge options to be passed during initialization. Defaults to `None`.
    -   `window_mode` (Optional[str], optional): Browser window mode (`'windowless'`, `'kiosk'`, `'full_window'`, etc.). Defaults to `None`.
**Returns**:
    - `None`

#### `_payload`

```python
def _payload(self) -> None:
    """
    Load executors for locators and JavaScript scenarios.
    """
```
**Description**: Loads executors for locators and JavaScript scenarios.
**Returns**:
    - `None`

#### `set_options`

```python
def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:
    """
    Create and configure launch options for the Edge WebDriver.

    Args:
        opts (Optional[List[str]], optional): A list of options to add to the Edge WebDriver. Defaults to None.

    Returns:
        EdgeOptions: Configured `EdgeOptions` object.
    """
```
**Description**: Creates and configures launch options for the Edge WebDriver.
**Parameters**:
    -   `opts` (Optional[List[str]], optional): A list of options to add to the Edge WebDriver. Defaults to `None`.
**Returns**:
    -   `EdgeOptions`: Configured `EdgeOptions` object.