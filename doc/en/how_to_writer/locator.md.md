How to use this code block
=========================================================================================

Description
-------------------------
This document explains the structure and usage of locators in conjunction with the `executor` module for web automation. Locators are configuration objects that define how to find and interact with web elements. They are used by the `ExecuteLocator` class to perform actions such as clicks, message sending, attribute extraction, and more.

Execution steps
-------------------------
1.  **Define a locator**: Create a locator as a JSON object (or Python dictionary) with the required keys.
2.  **Understand the keys**:
    -   `attribute`: Specifies an attribute to retrieve or a value to return directly. Can be `null` if not needed or a string value, integer or dictionary.
    -   `by`: Defines the type of locator (e.g., "XPATH", "ID", "VALUE").
    -   `selector`: The expression used to locate the element (e.g., XPATH, CSS selector). If `by` is "VALUE", this key is not used.
    -   `if_list`: If multiple elements are found, specifies which element to use ("first", "last", "all", "even", "odd" or an integer to get the N-th element).
    -   `use_mouse`: Not used directly in the code provided.
    -   `mandatory`: A boolean indicating whether the action is mandatory. If `True`, an error is raised if the element is not found. If `False`, execution continues.
    -   `timeout`: A number representing the timeout period (in seconds) to wait for an element to be located.
    -   `timeout_for_event`: The waiting condition (e.g. "presence_of_element_located", "element_to_be_clickable").
    -   `event`: Specifies an action to perform (e.g., "click()", "screenshot()"). Can be null if no event is needed.
    -   `locator_description`: A string describing the locator's purpose.
3.  **Pass the locator to `executor`**: Use the defined locator dictionary with the methods of the `ExecuteLocator` class (`execute_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, `get_webelement_as_screenshot`).
4.  **Interpret the results**: Based on the locator configuration, `executor` performs the defined actions and returns the result. The result can be:
    -   The result of an event (e.g., `True` if a click was successful).
    -   The value of a specified attribute.
    -   The located web element.
    -   A screenshot of a web element (as a binary stream).
    -   The value from `attribute` field if the locator's `by` is set to "VALUE".
5.  **Handle errors**: If the element is not found, `executor` will behave as follows:
    - If `mandatory` is set to `False`, execution will continue, and some methods may return `None` (or `False`).
    - If `mandatory` is set to `True`, an error will be raised.

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
- Included explanations for error handling depending on the `mandatory` key.
- Added examples for all five locators from the input code to demonstrate different functionalities.
- Added `By` import to the example.