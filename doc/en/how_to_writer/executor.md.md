How to use this code block
=========================================================================================

Description
-------------------------
The `executor.py` module is designed to automate interactions with web elements using Selenium. It provides a flexible framework to locate, interact with, and extract data from web elements based on provided configurations (locators). It handles various actions like clicks, sending messages, and retrieving attributes, with robust error handling.

Execution steps
-------------------------
1. **Import necessary modules**: Ensure that all required modules are imported, including `selenium`, `asyncio`, `re`, `dataclasses`, `enum`, `pathlib`, `types`, and `typing`.
2. **Initialize the `ExecuteLocator` class**: Create an instance of the `ExecuteLocator` class by passing a Selenium WebDriver instance.
   - Example: `executor = ExecuteLocator(driver=driver)`.
3. **Define Locators**: Create a locator dictionary specifying the type of locator (`by`), the selector (`selector`), and optionally an event (`event`), an attribute to retrieve (`attribute`), or if it's mandatory `mandatory` .
   - Example:
     ```python
     locator = {
        "by": "ID",
        "selector": "some_element_id",
        "event": "click()"
     }
     ```
4. **Use the `execute_locator` method**: Call the `execute_locator` method with the locator dictionary to perform actions on the web element.
   - Example: `result = await executor.execute_locator(locator)`.
5. **Use `get_attribute_by_locator` method**: Call the `get_attribute_by_locator` method with the locator dictionary to retrieve attributes from located element(s).
   - Example: `result = await executor.get_attribute_by_locator(locator)`.
6. **Use `get_webelement_by_locator` method**: Call the `get_webelement_by_locator` method with the locator dictionary to get located element(s).
   - Example: `result = await executor.get_webelement_by_locator(locator)`.
7. **Use `get_webelement_as_screenshot` method**: Call the `get_webelement_as_screenshot` method with the locator dictionary to save the screenshot of the located element.
    - Example: `result = await executor.get_webelement_as_screenshot(locator, filepath='screenshot.png')`.
8.  **Handle Asynchronous Operations**: Since the module uses `asyncio`, ensure to use `await` when calling the methods.
9. **Handle Errors**: The module includes error handling to continue execution even if some elements are not found. Errors are logged. Review logs for any issues.

Usage example
-------------------------
```python
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.webdriver.executor import ExecuteLocator

async def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Initialize the ExecuteLocator class
    executor = ExecuteLocator(driver=driver)

    # Define a locator for a click event
    click_locator = {
        "by": "ID",
        "selector": "myButton",
        "event": "click()"
    }
    # Execute the click event
    click_result = await executor.execute_locator(click_locator)
    print(f"Click Result: {click_result}")

    # Define a locator to get an attribute
    attribute_locator = {
        "by": By.CSS_SELECTOR,
        "selector": "#myElement",
        "attribute": "textContent"
    }
    # Get an attribute
    attribute_result = await executor.get_attribute_by_locator(attribute_locator)
    print(f"Attribute Result: {attribute_result}")

    # Define a locator to get web element
    web_element_locator = {
      "by": By.ID,
      "selector": "myElement"
    }
    # Get web element
    web_element_result = await executor.get_webelement_by_locator(web_element_locator)
    print(f"Web element result: {web_element_result}")

    # Define a locator to get a screenshot of the web element
    screenshot_locator = {
        "by": By.ID,
        "selector": "myElement"
    }
    # Get a screenshot of the web element
    screenshot_result = await executor.get_webelement_as_screenshot(screenshot_locator, filepath='screenshot.png')
    print(f"Screenshot result: {screenshot_result}")


    driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
```
```

## Changes
- Provided a detailed description of the `executor.py` module.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added a section about handling asynchronous operations.
- Added examples for all methods: `execute_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, and `get_webelement_as_screenshot`.
- Improved error handling documentation.