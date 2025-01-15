# Module: src.webdriver.crawlee_python.crawlee_python

## Overview

This module provides a custom implementation of `PlaywrightCrawler` using the Crawlee library. It allows you to configure browser settings, handle requests, and extract data from web pages.

## Table of Contents

1.  [Classes](#classes)
    -   [CrawleePython](#crawleepython-class)
        -   [`__init__`](#__init__)
        -   [`setup_crawler`](#setup_crawler)
        -   [`run_crawler`](#run_crawler)
        -   [`export_data`](#export_data)
        -   [`get_data`](#get_data)
        -   [`run`](#run)

## Classes

### `CrawleePython`

**Description**: This class provides a custom implementation of `PlaywrightCrawler` using the Crawlee library.

**Attributes**:

-   `max_requests` (int): Maximum number of requests to perform during the crawl.
-   `headless` (bool): Whether to run the browser in headless mode.
-   `browser_type` (str): The type of browser to use (`'chromium'`, `'firefox'`, `'webkit'`).
-   `crawler` (PlaywrightCrawler): The PlaywrightCrawler instance.

**Methods**:

-   [`__init__`](#__init__)
-   [`setup_crawler`](#setup_crawler)
-   [`run_crawler`](#run_crawler)
-   [`export_data`](#export_data)
-   [`get_data`](#get_data)
-  [`run`](#run)

#### `__init__`

```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
    """
    Initializes the CrawleePython crawler with the specified parameters.

    Args:
        max_requests (int, optional): Maximum number of requests to perform during the crawl. Defaults to 5.
        headless (bool, optional): Whether to run the browser in headless mode. Defaults to False.
        browser_type (str, optional): The type of browser to use ('chromium', 'firefox', 'webkit'). Defaults to 'firefox'.
        options (Optional[List[str]], optional): A list of custom options to pass to the browser. Defaults to None.
    """
```
**Description**: Initializes the `CrawleePython` crawler with the specified parameters.
**Parameters**:
    -   `max_requests` (int, optional): Maximum number of requests to perform during the crawl. Defaults to 5.
    -   `headless` (bool, optional): Whether to run the browser in headless mode. Defaults to `False`.
    -  `browser_type` (str, optional): The type of browser to use (`'chromium'`, `'firefox'`, `'webkit'`). Defaults to `'firefox'`.
    -   `options` (Optional[List[str]], optional): A list of custom options to pass to the browser. Defaults to `None`.
**Returns**:
    - `None`

#### `setup_crawler`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
```
**Description**: Sets up the PlaywrightCrawler instance with the specified configuration.
**Returns**:
    - `None`

#### `run_crawler`

```python
async def run_crawler(self, urls: List[str]):
    """
    Runs the crawler with the initial list of URLs.

    Args:
        urls (List[str]): List of URLs to start the crawl.
    """
```
**Description**: Runs the crawler with the initial list of URLs.
**Parameters**:
    -  `urls` (List[str]): List of URLs to start the crawl.
**Returns**:
    - `None`

#### `export_data`

```python
async def export_data(self, file_path: str):
    """
    Exports the entire dataset to a JSON file.

    Args:
        file_path (str): Path to save the exported JSON file.
    """
```
**Description**: Exports the entire dataset to a JSON file.
**Parameters**:
    -   `file_path` (str): Path to save the exported JSON file.
**Returns**:
    - `None`

#### `get_data`

```python
async def get_data(self) -> Dict[str, Any]:
    """
    Retrieves the extracted data.

    Returns:
        Dict[str, Any]: Extracted data as a dictionary.
    """
```
**Description**: Retrieves the extracted data.
**Returns**:
    -   `Dict[str, Any]`: Extracted data as a dictionary.

#### `run`

```python
async def run(self, urls: List[str]):
    """
    Main method to set up, run the crawler, and export data.

    Args:
        urls (List[str]): List of URLs to start the crawl.
    """
```
**Description**: Main method to set up, run the crawler, and export data.
**Parameters**:
    -  `urls` (List[str]): List of URLs to start the crawl.
**Returns**:
    - `None`