# Module: src.webdriver.bs.bs

## Overview

This module provides a custom implementation for parsing HTML content using BeautifulSoup and XPath. It enables extracting data from local files or web pages using XPath selectors.

## Table of Contents
1.  [Classes](#classes)
    -   [BS](#bs-class)
        -   [`__init__`](#__init__)
        -   [`get_url`](#get_url)
        -   [`execute_locator`](#execute_locator)

## Classes

### `BS`

**Description**: This class provides functionalities for parsing HTML content using BeautifulSoup and XPath.

**Attributes**:

-   `html_content` (str): The HTML content to be parsed.

**Methods**:

-   [`__init__`](#__init__)
-   [`get_url`](#get_url)
-   [`execute_locator`](#execute_locator)

#### `__init__`

```python
def __init__(self, url: Optional[str] = None):
    """
    Initializes the BS parser with an optional URL.

    Args:
        url (Optional[str], optional): The URL or file path to fetch HTML content from. Defaults to None.
    """
```
**Description**: Initializes the `BS` parser with an optional URL.
**Parameters**:
    -  `url` (Optional[str], optional): The URL or file path to fetch HTML content from. Defaults to `None`.

#### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath.

    Args:
        url (str): The file path or URL to fetch HTML content from.

    Returns:
        bool: True if the content was successfully fetched, False otherwise.
    """
```
**Description**: Fetches HTML content from a file or URL and parses it with BeautifulSoup and XPath.
**Parameters**:
    -  `url` (str): The file path or URL to fetch HTML content from.
**Returns**:
    -   `bool`: `True` if the content was successfully fetched, `False` otherwise.

#### `execute_locator`

```python
def execute_locator(self, locator: Union[SimpleNamespace, dict], url: Optional[str] = None) -> List[etree._Element]:
    """
    Execute an XPath locator on the HTML content.

    Args:
        locator (Union[SimpleNamespace, dict]): The locator object containing the selector and attribute.
        url (Optional[str], optional): Optional URL or file path to fetch HTML content from. Defaults to None.

    Returns:
        List[etree._Element]: A list of elements matching the locator.
    """
```
**Description**: Executes an XPath locator on the HTML content.
**Parameters**:
    -   `locator` (Union[SimpleNamespace, dict]): The locator object containing the selector and attribute.
    -  `url` (Optional[str], optional): Optional URL or file path to fetch HTML content from. Defaults to `None`.
**Returns**:
    -  `List[etree._Element]`: A list of elements matching the locator.