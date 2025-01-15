# Module: src.webdriver.driver

## Overview

This module provides a `Driver` class for interacting with Selenium web drivers. It offers functionalities for driver initialization, navigation, cookie management, exception handling, and more. This class simplifies web automation tasks by providing a unified interface for managing web drivers like Chrome, Firefox, and Edge.

## Table of Contents
1.  [Classes](#classes)
    -   [Driver](#driver-class)
2.  [Functions](#functions)
    -   [`__init_subclass__`](#__init_subclass__)
    -   [`__getattr__`](#__getattr__)
    -   [`scroll`](#scroll)
    -   [`locale`](#locale)
    -   [`get_url`](#get_url)
    -   [`window_open`](#window_open)
    -   [`wait`](#wait)
    -   [`_save_cookies_localy`](#_save_cookies_localy)
    -   [`fetch_html`](#fetch_html)

## Classes

### `Driver` Class

**Description**: This class provides a unified interface for interacting with Selenium web drivers. It provides methods for common web automation tasks such as navigation, scrolling, and cookie management.

**Methods**:

-   [`__init__`](#__init__)
-   [`__init_subclass__`](#__init_subclass__)
-   [`__getattr__`](#__getattr__)
-   [`scroll`](#scroll)
-   [`locale`](#locale)
-   [`get_url`](#get_url)
-   [`window_open`](#window_open)
-   [`wait`](#wait)
-   [`_save_cookies_localy`](#_save_cookies_localy)
-   [`fetch_html`](#fetch_html)

#### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Initializes the Driver instance.

    Args:
        webdriver_cls (type): WebDriver class (e.g., Chrome, Firefox).
        *args: Positional arguments for the driver initialization.
        **kwargs: Keyword arguments for the driver initialization.

    Raises:
        TypeError: If `webdriver_cls` does not have a `get` attribute.
    
    Example:
        >>> from selenium.webdriver import Chrome
        >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """
```
**Description**: Initializes a `Driver` instance with a specified WebDriver class and its arguments.
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
    Automatically called when creating a subclass of `Driver`.

    Args:
        cls (type): The subclass being initialized.
        browser_name (str, optional): The name of the browser.
        **kwargs: Additional keyword arguments.

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
    Proxy for accessing driver attributes.

    Args:
        item (str): The name of the attribute.

    Returns:
        Any: The value of the attribute.

    Example:
        >>> driver.current_url
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
    Scrolls the page in the specified direction.

    Args:
        scrolls (int, optional): Number of scrolls, default is 1.
        frame_size (int, optional): Scroll size in pixels, default is 600.
        direction (str, optional): Scroll direction ('both', 'down', 'up'), default is 'both'.
        delay (float, optional): Delay between scrolls, default is 0.3.

    Returns:
        bool: True if successful, otherwise False.
    
    Example:
        >>> driver.scroll(scrolls=3, direction='down')
    """
```
**Description**: Scrolls the web page in the specified direction.
**Parameters**:
    - `scrolls` (int, optional): The number of scroll actions to perform. Defaults to 1.
    - `frame_size` (int, optional): The distance to scroll in pixels. Defaults to 600.
    - `direction` (str, optional): The direction of the scroll (`'both'`, `'forward'`, `'down'`, `'backward'`, `'up'`). Defaults to `'both'`.
    - `delay` (float, optional): The delay in seconds between each scroll action. Defaults to 0.3.
**Returns**:
    - `bool`: `True` if the scrolling was successful, `False` otherwise.

### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Determines the page language based on meta tags or JavaScript.

    Returns:
        Optional[str]: Language code if found, otherwise None.
    
    Example:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' or None
    """
```
**Description**: Retrieves the page's language code from the meta tag or through JavaScript.
**Returns**:
    - `Optional[str]`: The language code if found, `None` otherwise.

### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Navigates to the specified URL and saves the current URL, previous URL, and cookies.

    Args:
        url (str): URL to navigate to.

    Returns:
        bool: True if the navigation is successful, False otherwise.

    Raises:
        WebDriverException: If there is a WebDriver error.
        InvalidArgumentException: If the URL is invalid.
        Exception: For any other navigation errors.
    """
```
**Description**: Navigates to the specified URL, waits for the page to load, saves cookies, and updates the previous URL.
**Parameters**:
    - `url` (str): The URL to navigate to.
**Returns**:
    - `bool`: `True` if navigation was successful, `False` otherwise.
**Raises**:
    - `WebDriverException`: If an error occurs with the WebDriver.
    - `InvalidArgumentException`: If the URL is invalid.
    - `Exception`: For any other errors during navigation.

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """
    Open a new tab in the current browser window and switch to it.

    Args:
        url (Optional[str], optional): URL to open in the new tab. Defaults to `None`.
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
    Waits for the specified amount of time.

    Args:
        delay (float, optional): Delay time in seconds. Defaults to 0.3.

    Returns:
        None
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
    Saves the current web driver cookies to a local file.

    Returns:
        None

    Raises:
        Exception: If there is an error saving cookies.
    """
```
**Description**: Saves the current browser cookies to a local file.
**Returns**:
    - `None`
**Raises**:
    - `Exception`: If an error occurs while saving cookies.

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Extracts HTML content from a file or web page.

    Args:
        url (str): File path or URL to extract the HTML content from.

    Returns:
        Optional[bool]: Returns `True` if content is successfully extracted, otherwise `None`.

    Raises:
        Exception: If there is an error during content extraction.
    """
```
**Description**: Fetches HTML content from a file or web page.
**Parameters**:
    - `url` (str): The URL or local file path to fetch HTML content from.
**Returns**:
    - `Optional[bool]`: `True` if the content is successfully fetched, `False` otherwise.
**Raises**:
    - `Exception`: If an error occurs while fetching content.