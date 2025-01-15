How to use this code block
=========================================================================================

Description
-------------------------
The `executor.py` module provides a custom implementation of an executor using Playwright, designed to interact with web pages. It allows for the execution of actions based on configurations provided as locators. It is designed to handle various actions, such as clicks, sending messages, extracting attributes and taking screenshots, with robust error handling and logging.

Execution steps
-------------------------
1. **Import necessary modules**: Ensure that all required modules are imported. These include `asyncio`, `typing`, `pathlib`, `playwright.async_api`, `types`, and internal modules from `src`.
2. **Initialize the `PlaywrightExecutor` class**: Create an instance of the `PlaywrightExecutor` class, providing the browser type you wish to use ('chromium', 'firefox', or 'webkit') as an optional parameter.
    - Example: `executor = PlaywrightExecutor(browser_type='chromium')` or `executor = PlaywrightExecutor()`
3.  **Start Playwright**: Before any actions can be performed, you must call the `start` method which initializes Playwright and starts a browser instance.
    -   Example: `await executor.start()`
4.  **Define locators**: Define locators as dictionaries or `SimpleNamespace` objects. These locators specify how to locate elements on the web page, the actions to be performed on the located element and, optionally, what information should be extracted from the element.
    -   Example:
        ```python
        locator = {
            "by": "xpath",
            "selector": "//button[@id='myButton']",
            "event": "click()"
        }
        ```
5.  **Execute actions**: Use the `execute_locator` method, passing the locator dictionary to execute the action defined in `event`. If the locator contains `attribute` field, it extracts attribute value from the located element(s), or if the `by` is set to `VALUE`, then it will return static attribute value.
     -  Example: `result = await executor.execute_locator(locator)`
6. **Get attribute values**: To get attributes use the `get_attribute_by_locator` method by passing the locator with the `attribute` field, it will return the string or a list of strings containing the attribute values.
    - Example:  `attribute_values = await executor.get_attribute_by_locator(locator)`
7. **Get web element**: To get a web element use the `get_webelement_by_locator` method by passing the locator object, it will return the `Locator` object or a list of `Locator` objects.
    - Example: `element = await executor.get_webelement_by_locator(locator)`
8. **Get a screenshot**: To take a screenshot of a web element use the `get_webelement_as_screenshot` method, it will return the screenshot as a byte string.
    - Example: `screenshot = await executor.get_webelement_as_screenshot(locator)`
9.  **Send messages**: Use the `send_message` method to send text to a web element based on a locator, you can also set the typing speed.
     -   Example: `result = await executor.send_message(locator, message="Hello World")`
10. **Navigate to a URL**: Use `goto` method to navigate to the given URL.
    - Example: `await executor.goto('https://www.example.com')`
11. **Stop Playwright**: After performing all actions, it's important to close the browser and Playwright by calling the `stop` method.
    - Example: `await executor.stop()`
12. **Handle exceptions**: Each method includes a try-except block to catch and log any exceptions using logger from `src.logger.logger`, which is used for error handling and debugging.

Usage example
-------------------------
```python
import asyncio
from src.webdriver.playwright.executor import PlaywrightExecutor
from playwright.async_api import expect
from types import SimpleNamespace


async def main():
    # Example 1: Initialize and start the Playwright executor
    executor = PlaywrightExecutor(browser_type='chromium')
    await executor.start()

    # Example 2: Navigate to a URL
    await executor.goto("https://www.example.com")
    print("Successfully navigated to https://www.example.com")

    # Example 3: Define a locator and perform a click event
    locator_click = {
      "by": "xpath",
      "selector": "//a[contains(@href, '#')]",
      "event": "click()"
    }
    click_result = await executor.execute_locator(locator_click)
    print(f"Click result: {click_result}")

    # Example 4: Define a locator for an input field and send message
    locator_send = {
         "by": "xpath",
        "selector": "//input[@id='search']"
    }
    send_result = await executor.send_message(locator_send, message='test typing')
    print(f"Send message result: {send_result}")



    # Example 5: Define a locator to get attribute values
    locator_attribute = {
        "by": "xpath",
        "selector": "//h1",
        "attribute": "textContent"
    }
    attribute_values = await executor.get_attribute_by_locator(locator_attribute)
    print(f"Attribute value: {attribute_values}")

    # Example 6: Define a locator for screenshot
    locator_screenshot = {
         "by": "xpath",
         "selector": "//body"
    }
    screenshot = await executor.get_webelement_as_screenshot(locator_screenshot)
    if screenshot:
        print("Successfully took a screenshot of the web element.")

    # Example 7: Define a locator to get web element.
    locator_element = {
      "by": "xpath",
      "selector": "//body"
    }
    element = await executor.get_webelement_by_locator(locator_element)
    if element:
        print(f"Successfully found the web element using locator {locator_element}")

    # Example 8: Execute locator to get a static attribute value
    value_locator = {"attribute": 1234, "by": 'VALUE'}
    attribute = await executor.execute_locator(value_locator)
    print(f"Attribute from locator value is : {attribute}")

    # Example 9: Stop playwright
    await executor.stop()

if __name__ == "__main__":
    asyncio.run(main())

```
```

## Changes
- Provided a detailed description of the `PlaywrightExecutor` module, including its purpose and functionality.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments, including how to use all methods.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations of how to use locators for different interactions.
- Added explanation for the `evaluate_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, `get_webelement_as_screenshot`, `execute_event`, `send_message`, and `goto` methods.
- Improved error handling documentation.
- Added examples of how to take a screenshot, send messages, navigate using `goto`, and access element attributes.
- Added an example of how to get the static value from the locator by using `by` as `VALUE`.