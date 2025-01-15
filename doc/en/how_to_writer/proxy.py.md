How to use this code block
=========================================================================================

Description
-------------------------
The `proxy.py` module provides functionality for downloading, parsing, and verifying proxy lists. It downloads a list of proxies from a specified URL, parses the list into categories (HTTP, SOCKS4, SOCKS5), and checks the validity of individual proxies. This module is useful for managing and utilizing proxy servers in web automation tasks.

Execution steps
-------------------------
1.  **Import necessary modules**: The module imports `re`, `requests`, `Path` from `pathlib`, and `typing` for type hints, `header`, `gs`, `pprint` and `logger`. Make sure these are installed.
2.  **Define proxy list URL and path**: The module defines a default URL for downloading proxies and a file path to save the downloaded list. These can be modified.
3.  **Download the proxy list**: Call the `download_proxies_list()` function with an optional URL and save path.
    -   If successful, the file is downloaded and saved to the specified path, and a log message is generated.
    -   If an error occurs, it's logged and the function returns `False`.
4.  **Parse the proxy list**: Call the `get_proxies_dict()` function with an optional file path (defaults to the saved path).
    -   This function first calls the `download_proxies_list` function to ensure the latest file is downloaded.
    -   It then parses the proxy list from the specified file, categorizing them into HTTP, SOCKS4, and SOCKS5 proxies and returns them as a dictionary.
    -   If the file is not found or parsing fails, appropriate errors are logged.
5.  **Check proxy validity**: Call the `check_proxy()` function with a proxy dictionary (containing `protocol`, `host`, and `port`).
    -   This function sends a request to "https://httpbin.org/ip" through the provided proxy.
    -   If the proxy is valid, the function returns `True`. If not, it logs a warning and returns `False`.
6.  **Use the main block**: The `if __name__ == '__main__':` block shows an example of how to use the functions to download, parse, and log the number of parsed proxies.

Usage example
-------------------------
```python
from src.webdriver.proxy import download_proxies_list, get_proxies_dict, check_proxy
from src.logger.logger import logger
import asyncio

async def main():
    # Download the proxy list
    if download_proxies_list():
        print("Proxy list downloaded successfully.")
    else:
        print("Proxy list download failed.")

    # Parse the proxy list
    proxies = get_proxies_dict()
    if proxies:
        print("Proxies parsed successfully.")

        # Check some proxies
        if proxies["http"]:
            is_working = check_proxy(proxies["http"][0])
            print(f"HTTP proxy working : {is_working}")
        else:
            print("No HTTP proxies found")

        if proxies["socks4"]:
            is_working = check_proxy(proxies["socks4"][0])
            print(f"SOCKS4 proxy working : {is_working}")
        else:
           print("No SOCKS4 proxies found")

        if proxies["socks5"]:
             is_working = check_proxy(proxies["socks5"][0])
             print(f"SOCKS5 proxy working : {is_working}")
        else:
            print("No SOCKS5 proxies found")

        # Log number of processed proxies
        total_proxies = sum(len(v) for v in proxies.values())
        logger.info(f"Total proxies processed: {total_proxies}")
    else:
       print("Proxy parsing failed.")

if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Added a detailed description of the `proxy.py` module, including its purpose and functionalities.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added information about how to call each function and interpret the results.
- Added a demonstration of how to use the functions in the `__main__` block.
- Added error handling explanations.
- Updated the usage example to run async and import the `logger`.