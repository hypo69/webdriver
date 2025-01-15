How to use this code block
=========================================================================================

Description
-------------------------
The `executor.py` module is designed to perform actions on web elements using Selenium, based on provided configurations known as "locators." It provides functionalities for parsing locators, interacting with elements (e.g., clicks, typing), handling errors, and supporting various locator types. The module also allows for asynchronous operations, making it suitable for modern web automation.

Execution steps
-------------------------
1.  **Import necessary modules**: Import the required modules, including `asyncio`, `re`, `dataclasses`, `enum`, `pathlib`, `types`, `typing`, `selenium`, `header`, `src.gs`, `src.logger.logger`, `src.logger.exceptions`, `src.utils.jjson`, `src.utils.printer`, and `src.utils.image`.
2.  **Initialize `ExecuteLocator`**: Create an instance of the `ExecuteLocator` class, passing a Selenium WebDriver instance if available.
    -   Example: `executor = ExecuteLocator(driver=driver)`
3.  **Define locators**: Create locators as dictionaries or `SimpleNamespace` objects. These locators specify how to locate elements on the page. A locator should include `by` (e.g., "ID", "XPATH"), `selector` (the value of the locator), and optionally, an `event` (e.g., "click()", "type()"), `attribute` (e.g. "textContent"), `mandatory` (boolean) and `timeout` (time in seconds).
4.  **Use `execute_locator`**: Call the `execute_locator` method to perform an action specified in the locator. The method can return the result of event, an attribute value, or a web element, based on the locator definition.
    -   Example: `result = await executor.execute_locator(locator, message="some text")`
5.  **Use `get_attribute_by_locator`**: Call this method to retrieve attributes from a web element or a list of web elements. The method returns the attribute value(s) as a string, list or dict.
    -   Example: `attribute = await executor.get_attribute_by_locator(locator)`
6.  **Use `get_webelement_by_locator`**: Call this method to get the located web element or a list of web elements. The method returns the web element object, list of web elements or `None` if the element(s) are not found.
    -   Example: `element = await executor.get_webelement_by_locator(locator, timeout=10)`
7.  **Use `get_webelement_as_screenshot`**: Call this method to take a screenshot of the located web element. The method returns the screenshot as a binary stream or `None` if the screenshot cannot be taken.
    -   Example: `screenshot = await executor.get_webelement_as_screenshot(locator, filepath='screenshot.png')`
8.  **Use `send_message`**: Call this method to type a message into a web element. The method returns `True` if the message was successfully sent, `False` otherwise.
     -   Example: `result = await executor.send_message(locator, message="Hello")`
9.  **Asynchronous operations**: Remember that most methods are asynchronous and should be called with `await`.
10. **Error Handling**: This module includes robust error handling. Check logs using `src.logger.logger` for details if there are issues.

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
- Added a section about asynchronous operations and how to use `await`.
- Added examples for all methods: `execute_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, `get_webelement_as_screenshot`, and `send_message`.
- Improved error handling documentation.
- Updated the example to make use of the `send_message` method.