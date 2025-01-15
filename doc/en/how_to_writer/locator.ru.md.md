How to use this code block
=========================================================================================

Description
-------------------------
This document explains how to use locators with the `executor` module for web automation. Locators are configuration objects that define how to locate and interact with web elements. They are used with the `ExecuteLocator` class to perform actions like clicking, sending messages, extracting attributes, and more. This guide provides examples of different locators and their keys, along with their interactions with the `executor`.

Execution steps
-------------------------
1.  **Define a locator**: Create a locator as a JSON object (or a Python dictionary) with the required keys.
2.  **Understand the keys**:
    -   `attribute`: Specifies the attribute to retrieve from an element or a static value to return. If not needed, it is set to `null`. It can be a string, integer, or dictionary.
    -   `by`: Defines the type of locator (e.g., "XPATH", "ID", "VALUE").
    -   `selector`: The expression used to locate the element (e.g., an XPATH or a CSS selector). If `by` is "VALUE", this key is not used.
    -   `if_list`: Specifies how to handle multiple found elements ("first", "last", "all", "even", "odd", or an integer for N-th element).
    -   `use_mouse`: Not directly used in provided code.
    -   `mandatory`: Indicates if the action is mandatory (`True`) or optional (`False`). If `True` and the element isn't found, an error is raised. If `False`, execution continues.
    -   `timeout`: Specifies the maximum time to wait for an element to be located, in seconds.
    -  `timeout_for_event`: Specifies the type of waiting condition (`presence_of_element_located`, `element_to_be_clickable`).
    -   `event`: Specifies the event to perform on the element (e.g., "click()", "screenshot()"). Can be set to `null` if no event is needed.
    -   `locator_description`: A description of the locator for documentation purposes.
3.  **Pass the locator to `executor`**: Use the locator dictionary with `ExecuteLocator` methods like `execute_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, or `get_webelement_as_screenshot`.
4.  **Interpret results**: Based on the locator configuration, the `executor` will:
    -   Perform the specified action (click, screenshot, etc.)
    -   Return the attribute value
    -   Return the found web element(s)
    -   Return a static value from the `attribute` field, if the `by` field is set to `VALUE`.
5.  **Handle errors**: If an element is not found:
    -   If `mandatory` is `False`, execution continues, and some methods may return `None` or `False`.
    -   If `mandatory` is `True`, an error is raised.

Usage example
-------------------------
```python
import asyncio
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from selenium.webdriver.common.by import By


async def main():
    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver=driver)

    # Example 1: Close Banner
    close_banner_locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//button[@id = 'closeXButton']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
    }
    result = await executor.execute_locator(close_banner_locator)
    print(f"Close Banner Result: {result}")

    # Example 2: Get Manufacturer ID (static value)
    id_manufacturer_locator = {
        "attribute": 11290,
        "by": "VALUE",
        "selector": None,
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "id_manufacturer"
    }
    result = await executor.execute_locator(id_manufacturer_locator)
    print(f"Manufacturer ID: {result}")

    # Example 3: Get Additional Image URLs
    additional_images_locator = {
        "attribute": "src",
        "by": "XPATH",
        "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None
    }
    result = await executor.get_attribute_by_locator(additional_images_locator)
    print(f"Additional Images URLs: {result}")

    # Example 4: Get Default Image as Screenshot
    default_image_locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//a[@id = 'mainpic']//img",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "screenshot()",
        "mandatory": True,
        "locator_description": "Attention! In Morlevi, the image is obtained via screenshot and returned as png (`bytes`)"
    }
    result = await executor.execute_locator(default_image_locator)
    print(f"Default Image Screenshot: {result}")

    # Example 5: Get Supplier ID
    id_supplier_locator = {
        "attribute": "innerText",
        "by": "XPATH",
        "selector": "//span[@class = 'ltr sku-copy']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "SKU morlevi"
    }
    result = await executor.get_attribute_by_locator(id_supplier_locator)
    print(f"Supplier ID: {result}")

    driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Provided a detailed explanation of locators and their interaction with the `executor` module.
- Outlined clear execution steps for using locators with `ExecuteLocator`.
- Provided a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Included explanations of how errors are handled based on the `mandatory` key.
- Provided examples for each of the five locators from the original code snippet to demonstrate different functionalities.
- Added explanation about what is returned from each method.
- Added `By` import to the usage example.