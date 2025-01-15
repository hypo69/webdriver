How to use this code block
=========================================================================================

Description
-------------------------
The `executor.py` module is designed to automate interactions with web elements using Selenium. It provides a flexible way to locate, interact with, and extract information from web elements based on provided configurations called "locators." This module supports various actions, error handling, and multiple locator types.

Execution steps
-------------------------
1.  **Import necessary modules**: Import the required modules, such as `asyncio`, `re`, `dataclasses`, `enum`, `pathlib`, `types`, `typing`, and `selenium`.
2.  **Initialize `ExecuteLocator`**: Create an instance of the `ExecuteLocator` class, passing a Selenium WebDriver instance if available.
    -   Example: `executor = ExecuteLocator(driver=driver)`
3.  **Define locators**: Create locators as dictionaries or `SimpleNamespace` objects. These locators define how to locate elements on a web page. Each locator should have a `by` (e.g., "ID", "XPATH"), a `selector` (the value to locate), and optionally an `event` (e.g., "click()"), an `attribute` to retrieve (e.g., "textContent"), and `timeout` (in seconds) and if the locator is `mandatory` or not.
    -   Example:
        ```python
        locator = {
            "by": "ID",
            "selector": "some_element_id",
            "event": "click()"
        }
        ```
4.  **Use `execute_locator`**: Call the `execute_locator` method to perform an action on the web element specified by the locator. This method can return a web element, the result of an event, or an attribute value based on the locator definition.
    -   Example: `result = await executor.execute_locator(locator)`
5.  **Use `get_attribute_by_locator`**: Call this method to extract an attribute value from a web element or list of web elements. It returns a string, a list of strings, or a dictionary, based on the attribute requested in the locator.
    -   Example: `attribute = await executor.get_attribute_by_locator(locator)`
6.  **Use `get_webelement_by_locator`**: Call this method to retrieve the located web element(s). It returns a web element or a list of web elements based on the locator.
    -   Example: `element = await executor.get_webelement_by_locator(locator)`
7.  **Use `get_webelement_as_screenshot`**: Call this method to take a screenshot of the located web element. It returns a binary stream of the screenshot.
    -   Example: `screenshot = await executor.get_webelement_as_screenshot(locator)`
8.  **Use `send_message`**: Call this method to send text to a web element.
    -    Example: `result = await executor.send_message(locator, "Hello World")`
9.  **Asynchronous Operations**: Remember that most methods are asynchronous and should be called with `await`.
10. **Error Handling**: The module has robust error handling to allow execution to continue even if some elements are not found or if there are other issues. Always check logs using the configured `logger` from `src.logger.logger`.

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
    screenshot_result = await executor.get_webelement_as_screenshot(screenshot_locator)
    print(f"Screenshot result: {screenshot_result}")

    # Define a locator for send message event
    send_message_locator = {
        "by": By.ID,
        "selector": "myInput"
    }
    # Send message
    send_message_result = await executor.send_message(send_message_locator, message="Hello World")
    print(f"Send message result: {send_message_result}")


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
- Added a section about asynchronous operations.
- Added examples for all main methods: `execute_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, `get_webelement_as_screenshot`, and `send_message`.
- Included information about error handling and the use of `logger`.
- Improved the structure of the explanation and usage guide.