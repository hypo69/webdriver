# Module: src.webdriver.js

## Overview

This module provides JavaScript utility functions for interacting with web pages using Selenium WebDriver. It extends the capabilities of Selenium by adding common JavaScript-based functions for visibility manipulation, retrieving page information, and managing browser focus.

## Table of Contents
1.  [Classes](#classes)
    -   [JavaScript](#javascript-class)
        -   [`__init__`](#__init__)
        -   [`unhide_DOM_element`](#unhide_dom_element)
        -   [`ready_state`](#ready_state)
        -   [`window_focus`](#window_focus)
        -   [`get_referrer`](#get_referrer)
        -   [`get_page_lang`](#get_page_lang)

## Classes

### `JavaScript`

**Description**: This class provides JavaScript utility functions for interacting with a web page.

**Methods**:

-   [`__init__`](#__init__)
-   [`unhide_DOM_element`](#unhide_dom_element)
-   [`ready_state`](#ready_state)
-   [`window_focus`](#window_focus)
-   [`get_referrer`](#get_referrer)
-   [`get_page_lang`](#get_page_lang)

#### `__init__`

```python
def __init__(self, driver: WebDriver):
    """Initializes the JavaScript helper with a Selenium WebDriver instance.

    Args:
        driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
    """
```
**Description**: Initializes the `JavaScript` helper with a Selenium WebDriver instance.
**Parameters**:
    -   `driver` (WebDriver): Selenium WebDriver instance to execute JavaScript.

#### `unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Makes an invisible DOM element visible by modifying its style properties.

    Args:
        element (WebElement): The WebElement object to make visible.

    Returns:
        bool: True if the script executes successfully, False otherwise.
    """
```
**Description**: Makes an invisible DOM element visible by modifying its style properties.
**Parameters**:
    -   `element` (WebElement): The WebElement object to make visible.
**Returns**:
    -   `bool`: `True` if the script executes successfully, `False` otherwise.

#### `ready_state`

```python
@property
def ready_state(self) -> str:
    """Retrieves the document loading status.

    Returns:
        str: 'loading' if the document is still loading, 'complete' if loading is finished.
    """
```
**Description**: Retrieves the document loading status.
**Returns**:
    -   `str`: `'loading'` if the document is still loading, `'complete'` if loading is finished.

#### `window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.
    """
```
**Description**: Sets focus to the browser window using JavaScript.
**Returns**:
    -  `None`

#### `get_referrer`

```python
def get_referrer(self) -> str:
    """Retrieves the referrer URL of the current document.

    Returns:
        str: The referrer URL, or an empty string if unavailable.
    """
```
**Description**: Retrieves the referrer URL of the current document.
**Returns**:
    -  `str`: The referrer URL, or an empty string if unavailable.

#### `get_page_lang`

```python
def get_page_lang(self) -> str:
    """Retrieves the language of the current page.

    Returns:
        str: The language code of the page, or an empty string if unavailable.
    """
```
**Description**: Retrieves the language of the current page.
**Returns**:
    -  `str`: The language code of the page, or an empty string if unavailable.