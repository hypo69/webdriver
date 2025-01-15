# Module: src.webdriver.driver

## Overview

This module provides a `Driver` class for interacting with Selenium web drivers. It offers functionalities for driver initialization, navigation, cookie management, exception handling, and more, making web automation tasks easier and more efficient.

## Table of Contents
1. [Classes](#classes)
    - [Driver](#driver-class)
2. [Functions](#functions)
    - [`__init_subclass__`](#__init_subclass__)
    - [`__getattr__`](#__getattr__)
    - [`scroll`](#scroll)
    - [`locale`](#locale)
    - [`get_url`](#get_url)
    - [`window_open`](#window_open)
    - [`wait`](#wait)
    - [`_save_cookies_localy`](#_save_cookies_localy)
    - [`fetch_html`](#fetch_html)

## Classes

### `Driver` Class

**Description**: This class provides an abstraction layer for interacting with Selenium web drivers. It includes methods for common web automation tasks such as navigation, cookie management, and error handling.

**Methods**:

- [`__init__`](#__init__)
- [`__init_subclass__`](#__init_subclass__)
- [`__getattr__`](#__getattr__)
- [`scroll`](#scroll)
- [`locale`](#locale)
- [`get_url`](#get_url)
- [`window_open`](#window_open)
- [`wait`](#wait)
- [`_save_cookies_localy`](#_save_cookies_localy)
- [`fetch_html`](#fetch_html)

#### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Initializes the Driver instance with a specified WebDriver class and its arguments.

    Args:
        webdriver_cls (type): The WebDriver class to be instantiated (e.g., Chrome, Firefox).
        *args: Positional arguments for the WebDriver class.
        **kwargs: Keyword arguments for the WebDriver class.

    Raises:
        TypeError: If `webdriver_cls` does not have a `get` attribute.
    """
```
**Description**: Initializes a `Driver` instance with a specified WebDriver class.
**Parameters**:
    - `webdriver_cls` (type): The WebDriver class to be instantiated (e.g., `Chrome`, `Firefox`).
    - `*args` (tuple): Positional arguments for the WebDriver class.
    - `**kwargs` (dict): Keyword arguments for the WebDriver class.
**Raises**:
    - `TypeError`: If `webdriver_cls` is not a valid WebDriver class (does not have a `get` method).


## Functions

### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    """
    Initializes subclasses of the Driver class, ensuring the 'browser_name' argument is specified.

    Args:
        cls (type): The subclass being initialized.
        browser_name (str, optional): The name of the browser the subclass is for.
        **kwargs: Additional keyword arguments passed to the superclass.

    Raises:
        ValueError: If `browser_name` is not specified.
    """
```
**Description**: Initializes subclasses of the `Driver` class and sets `browser_name` attribute.
**Parameters**:
    - `cls` (type): The subclass being initialized.
    - `browser_name` (str, optional): The name of the browser.
    - `**kwargs` (dict): Additional keyword arguments.
**Raises**:
    - `ValueError`: If `browser_name` is not specified during subclass creation.

### `__getattr__`

```python
def __getattr__(self, item):
    """
    Retrieves an attribute from the underlying Selenium driver instance.

    Args:
        item (str): The name of the attribute to retrieve.

    Returns:
        Any: The value of the attribute.
    """
```
**Description**: Allows access to attributes of the underlying Selenium WebDriver instance.
**Parameters**:
    - `item` (str): The attribute name.
**Returns**:
    - `Any`: The attribute value.

### `scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    Scrolls the webpage in the specified direction.

    Args:
        scrolls (int, optional): Number of scrolls to perform. Defaults to 1.
        frame_size (int, optional): Scroll distance in pixels. Defaults to 600.
        direction (str, optional): Scrolling direction ('both', 'forward'/'down', 'backward'/'up'). Defaults to 'both'.
        delay (float, optional): Delay in seconds between scrolls. Defaults to 0.3.

    Returns:
        bool: True if scrolling was successful, False otherwise.
    """
```
**Description**: Scrolls the web page in the specified direction.
**Parameters**:
    - `scrolls` (int, optional): The number of scroll actions to perform. Defaults to 1.
    - `frame_size` (int, optional): The distance to scroll in pixels. Defaults to 600.
    - `direction` (str, optional): The direction of the scroll ('both', 'forward', 'down', 'backward', 'up'). Defaults to 'both'.
    - `delay` (float, optional): The delay in seconds between each scroll action. Defaults to 0.3.
**Returns**:
    - `bool`: `True` if the scrolling was successful, `False` otherwise.

### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Retrieves the page language from the meta tag or JavaScript.

    Returns:
        Optional[str]: The language code if found, None otherwise.
    """
```
**Description**: Retrieves the page's language code from the meta tag or through JavaScript.
**Returns**:
    - `Optional[str]`: The language code if found, `None` otherwise.

### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Navigates to the specified URL, waits for the page to load, saves cookies, and updates previous URL.

    Args:
        url (str): The URL to navigate to.

    Returns:
        bool: True if the navigation was successful, False otherwise.
    """
```
**Description**: Navigates to the specified URL, waits for the page to load, saves cookies, and updates the previous URL.
**Parameters**:
    - `url` (str): The URL to navigate to.
**Returns**:
    - `bool`: `True` if navigation was successful, `False` otherwise.

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """
    Opens a new tab in the browser and switches to it, optionally navigates to a specified URL.

    Args:
        url (Optional[str], optional): The URL to navigate to in the new tab. Defaults to None.
    """
```
**Description**: Opens a new tab in the browser and switches to it, optionally navigating to a given URL.
**Parameters**:
    - `url` (Optional[str], optional): The URL to navigate to in the new tab. Defaults to `None`.
**Returns**:
    - `None`

### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Pauses execution for a specified delay.

    Args:
        delay (float, optional): Time to wait in seconds. Defaults to 0.3.
    """
```
**Description**: Pauses the script execution for a specified time.
**Parameters**:
    - `delay` (float, optional): Time to wait in seconds. Defaults to 0.3.
**Returns**:
    - `None`

### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Saves the current browser cookies to a local file.
    """
```
**Description**: Saves the current browser cookies to a local file.
**Returns**:
    - `None`

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Fetches HTML content from a file or web page and stores it in self.html_content.

    Args:
        url (str): The URL (or file path) to fetch HTML content from.

    Returns:
        Optional[bool]: True if the content is successfully fetched, False otherwise.
    """
```
**Description**: Fetches HTML content from a file or web page.
**Parameters**:
    - `url` (str): The URL or local file path to fetch HTML content from.
**Returns**:
    - `Optional[bool]`: `True` if the content is successfully fetched, `False` otherwise.