# Module: src.webdriver.proxy

## Overview

This module provides functionalities for downloading and parsing lists of proxies. It loads a text file with proxy addresses and categorizes them by protocol.

## Table of Contents
1.  [Functions](#functions)
    -   [`download_proxies_list`](#download_proxies_list)
    -   [`get_proxies_dict`](#get_proxies_dict)
    -   [`check_proxy`](#check_proxy)

## Functions

### `download_proxies_list`

```python
def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Downloads a file from the specified URL and saves it to the given path.

    Args:
        url (str, optional): URL of the file to download. Defaults to the module's `url` constant.
        save_path (Path, optional): Path to save the downloaded file. Defaults to the module's `proxies_list_path` constant.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
```
**Description**: Downloads a file from the specified URL and saves it to the given path.
**Parameters**:
    -   `url` (str, optional): URL of the file to download. Defaults to the module's `url` variable.
    -  `save_path` (Path, optional): Path to save the downloaded file. Defaults to the module's `proxies_list_path` variable.
**Returns**:
    -   `bool`: `True` if the operation was successful, `False` otherwise.

### `get_proxies_dict`

```python
def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Parses a file with proxy addresses and categorizes them by protocol.

    Args:
        file_path (Path, optional): Path to the file with proxies. Defaults to the module's `proxies_list_path` constant.

    Returns:
        Dict[str, List[Dict[str, Any]]]: A dictionary with proxies categorized by type.
    """
```
**Description**: Parses a file with proxy addresses and categorizes them by protocol.
**Parameters**:
    -   `file_path` (Path, optional): Path to the file with proxies. Defaults to the module's `proxies_list_path` variable.
**Returns**:
    - `Dict[str, List[Dict[str, Any]]]`: A dictionary with proxies categorized by type.

### `check_proxy`

```python
def check_proxy(proxy: dict) -> bool:
    """
    Checks if a proxy server is working.

    Args:
        proxy (dict): A dictionary with proxy data (host, port, protocol).

    Returns:
        bool: True if the proxy is working, False otherwise.
    """
```
**Description**: Checks if a proxy server is working.
**Parameters**:
    -   `proxy` (dict): A dictionary with proxy data (`host`, `port`, `protocol`).
**Returns**:
    - `bool`: `True` if the proxy is working, `False` otherwise.