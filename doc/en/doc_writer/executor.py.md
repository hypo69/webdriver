# Module: src.webdriver.executor

## Overview

The `executor.py` module, part of the `src.webdriver` package, is designed to perform actions on web elements based on provided configurations, known as "locators." These locators are dictionaries containing information on how to locate and interact with elements on a web page. This module provides a flexible and versatile way to automate web interactions.

## Table of Contents
1.  [Key Features](#key-features)
2.  [Classes](#classes)
    -   [ExecuteLocator](#executelocator-class)
        -   [`__post_init__`](#__post_init__)
        -   [`execute_locator`](#execute_locator)
        -  [`evaluate_locator`](#evaluate_locator)
        -   [`get_attribute_by_locator`](#get_attribute_by_locator)
        -   [`get_webelement_by_locator`](#get_webelement_by_locator)
        -   [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
        -   [`execute_event`](#execute_event)
        -   [`send_message`](#send_message)
3.  [Dependencies](#dependencies)

## Key Features

1.  **Parsing and Handling Locators**: Converts dictionaries with configurations into `SimpleNamespace` objects, allowing for flexible manipulation of locator data.
2.  **Interacting with Web Elements**: Performs various actions such as clicks, sending messages, executing events, and retrieving attributes from web elements based on the provided data.
3.  **Error Handling**: Supports continuous execution in case of an error, allowing for the processing of web pages that might have unstable elements or require a special approach.
4.  **Support for Multiple Locator Types**: Handles both single and multiple locators, enabling the identification and interaction with one or several web elements simultaneously.

## Classes

### `ExecuteLocator`

**Description**: This class is responsible for handling web element interactions using Selenium based on provided locators.

**Attributes**:

-   `driver` (Optional[object]): The Selenium WebDriver instance.
-   `actions` (ActionChains): An `ActionChains` object for performing complex actions.
-  `by_mapping` (dict): A dictionary that maps locator types to Selenium's `By` methods.
-   `mode` (str): Execution mode ('debug', 'dev', etc.).

#### `__post_init__`

```python
def __post_init__(self):
    """Initializes the ActionChains object if a driver is provided."""
```
**Description**: Initializes the `ActionChains` object if a driver is provided.

#### `execute_locator`

```python
async def execute_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = 'presence_of_element_located',
    message: Optional[str] = None,
    typing_speed: Optional[float] = 0,
    continue_on_error: Optional[bool] = True,
) -> str | list | dict | WebElement | bool:
    """Executes actions on a web element based on the provided locator.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        timeout (Optional[float], optional): Timeout for locating the element. Defaults to 0.
        timeout_for_event (Optional[str], optional): The wait condition ('presence_of_element_located', 'element_to_be_clickable'). Defaults to 'presence_of_element_located'.
        message (Optional[str], optional): Optional message to send. Defaults to None.
        typing_speed (Optional[float], optional): Typing speed for send_keys events. Defaults to 0.
        continue_on_error (Optional[bool], optional): Whether to continue on error. Defaults to True.

    Returns:
        str | list | dict | WebElement | bool: Outcome based on locator instructions.

    ```mermaid
            graph TD
        A[Start] --> B[Check if locator is SimpleNamespace or dict]
        B --> C{Is locator SimpleNamespace?}
        C -->|Yes| D[Use locator as is]
        C -->|No| E[Convert dict to SimpleNamespace]
        E --> D
        D --> F[Define async function _parse_locator]
        F --> G[Check if locator has event, attribute, or mandatory]
        G -->|No| H[Return None]
        G -->|Yes| I[Try to map by and evaluate attribute]
        I --> J[Catch exceptions and log if needed]
        J --> K{Does locator have event?}
        K -->|Yes| L[Execute event]
        K -->|No| M{Does locator have attribute?}
        M -->|Yes| N[Get attribute by locator]
        M -->|No| O[Get web element by locator]
        L --> P[Return result of event]
        N --> P[Return attribute result]
        O --> P[Return web element result]
        P --> Q[Return final result of _parse_locator]
        Q --> R[Return result of execute_locator]
        R --> S[End]
    ```
    """
```
**Description**: Executes actions on a web element based on the provided locator.
**Parameters**:
    -   `locator` (dict | SimpleNamespace): Locator data as a dictionary or SimpleNamespace.
    -   `timeout` (Optional[float], optional): Timeout for locating the element. Defaults to 0.
    -  `timeout_for_event` (Optional[str], optional): The wait condition ('presence_of_element_located', 'element_to_be_clickable'). Defaults to 'presence_of_element_located'.
    -  `message` (Optional[str], optional): Optional message to send. Defaults to `None`.
    -   `typing_speed` (Optional[float], optional): Typing speed for `send_keys` events. Defaults to 0.
    -   `continue_on_error` (Optional[bool], optional): Whether to continue on error. Defaults to `True`.
**Returns**:
    -   `str | list | dict | WebElement | bool`: Outcome based on locator instructions.

#### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """Evaluates and processes locator attributes.

    Args:
        attribute (str | List[str] | dict): Attributes to evaluate.

    Returns:
        Optional[str | List[str] | dict]: Evaluated attributes.

    ```mermaid
            graph TD
        A[Start] --> B[Check if attribute is list]
        B -->|Yes| C[Iterate over each attribute in list]
        C --> D[Call _evaluate for each attribute]
        D --> E[Return gathered results from asyncio.gather]
        B -->|No| F[Call _evaluate for single attribute]
        F --> G[Return result of _evaluate]
        G --> H[End]
        E --> H
        ```
    """
```
**Description**: Evaluates and processes locator attributes.
**Parameters**:
    -   `attribute` (str | List[str] | dict): Attributes to evaluate.
**Returns**:
    -   `Optional[str | List[str] | dict]`: Evaluated attributes.

#### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(
    self,
    locator: SimpleNamespace | dict,
    timeout: Optional[float] = 0,
    timeout_for_event: str = 'presence_of_element_located',
    message: Optional[str] = None,
    typing_speed: float = 0,
    continue_on_error: bool = True,
) -> WebElement | list[WebElement] | None:
    """Retrieves attributes from an element or list of elements found by the given locator.

    Args:
        locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
        timeout (Optional[float], optional): Max wait time for the element to appear. Defaults to 0.
        timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.

    Returns:
        WebElement | list[WebElement] | None: The attribute value(s) or dictionary with attributes.

    ```mermaid
            graph TD
        A[Start] --> B[Check if locator is SimpleNamespace or dict]
        B -->|Yes| C[Convert locator to SimpleNamespace if needed]
        C --> D[Call get_webelement_by_locator]
        D --> E[Check if web_element is found]
        E -->|No| F[Log debug message and return]
        E -->|Yes| G[Check if locator.attribute is a dictionary-like string]
        G -->|Yes| H[Parse locator.attribute string to dict]
        H --> I[Check if web_element is a list]
        I -->|Yes| J[Retrieve attributes for each element in list]
        J --> K[Return list of attributes]
        I -->|No| L[Retrieve attributes for a single web_element]
        L --> K
        G -->|No| M[Check if web_element is a list]
        M -->|Yes| N[Retrieve attributes for each element in list]
        N --> O[Return list of attributes or single attribute]
        M -->|No| P[Retrieve attribute for a single web_element]
        P --> O
        O --> Q[End]
        F --> Q
        ```
    """
```
**Description**: Retrieves attributes from an element or list of elements found by the given locator.
**Parameters**:
    -   `locator` (SimpleNamespace | dict): Locator as a SimpleNamespace object or dictionary.
    -   `timeout` (Optional[float], optional): Max wait time for the element to appear. Defaults to 0.
    -   `timeout_for_event` (str, optional): Type of wait condition. Defaults to `'presence_of_element_located'`.
    -   `message` (Optional[str], optional): Message to send to the element. Defaults to `None`.
    -   `typing_speed` (float, optional): Speed of typing for send message events. Defaults to 0.
    -   `continue_on_error` (bool, optional): Whether to continue in case of an error. Defaults to `True`.
**Returns**:
    -   `WebElement | list[WebElement] | None`: The attribute value(s) or dictionary with attributes.

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = 'presence_of_element_located',
) -> WebElement | List[WebElement] | None:
    """
    Extracts a web element or a list of elements based on the provided locator.

     Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        timeout (Optional[float], optional): Timeout for locating the element. Defaults to 0.
        timeout_for_event (Optional[str], optional): The wait condition ('presence_of_element_located'). Defaults to 'presence_of_element_located'.

    Returns:
        WebElement | List[WebElement] | None: The web element or a list of web elements, or None if not found.
    """
```
**Description**: Extracts a web element or a list of elements based on the provided locator.
**Parameters**:
    -  `locator` (dict | SimpleNamespace): Locator data as a dictionary or SimpleNamespace.
    -   `timeout` (Optional[float], optional): Timeout for locating the element. Defaults to 0.
    -  `timeout_for_event` (Optional[str], optional): The wait condition ('presence_of_element_located'). Defaults to 'presence_of_element_located'.
**Returns**:
    -   `WebElement | List[WebElement] | None`: The web element or a list of web elements, or `None` if not found.

#### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = 'presence_of_element_located',
    message: Optional[str] = None,
    typing_speed: float = 0,
    continue_on_error: bool = True,
    webelement: Optional[WebElement] = None,
) -> BinaryIO | None:
    """Takes a screenshot of the located web element.

    Args:
        locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
        timeout (float, optional): Max wait time for the element to appear. Defaults to 5.
        timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.
        message (Optional[str], optional): Message to send to the element. Defaults to None.
        typing_speed (float, optional): Speed of typing for send message events. Defaults to 0.
        continue_on_error (bool, optional): Whether to continue in case of an error. Defaults to True.
        webelement (Optional[WebElement], optional): Pre-fetched web element. Defaults to None.

    Returns:
        BinaryIO | None: Binary stream of the screenshot or None if failed.
    """
```
**Description**: Takes a screenshot of the located web element.
**Parameters**:
    -   `locator` (SimpleNamespace | dict): Locator as a SimpleNamespace or dictionary.
    -   `timeout` (float, optional): Max wait time for the element to appear. Defaults to 5.
    -   `timeout_for_event` (str, optional): Type of wait condition. Defaults to `'presence_of_element_located'`.
    -   `message` (Optional[str], optional): Message to send to the element. Defaults to `None`.
    -   `typing_speed` (float, optional): Speed of typing for `send_message` events. Defaults to 0.
    -   `continue_on_error` (bool, optional): Whether to continue in case of an error. Defaults to `True`.
    -   `webelement` (Optional[WebElement], optional): Pre-fetched web element. Defaults to `None`.
**Returns**:
    -   `BinaryIO | None`: Binary stream of the screenshot or `None` if failed.

#### `execute_event`

```python
async def execute_event(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = 'presence_of_element_located',
    message: str = None,
    typing_speed: float = 0,
    continue_on_error: bool = True,
) -> str | list[str] | bytes | list[bytes] | bool:
    """
    Execute the events associated with a locator.

    Args:
        locator (SimpleNamespace | dict): Locator specifying the element and event to execute.
        timeout (float, optional): Timeout for locating the element. Defaults to 5.
        timeout_for_event (str, optional): Timeout for waiting for the event. Defaults to 'presence_of_element_located'.
        message (Optional[str], optional): Message to send with the event, if applicable. Defaults to None.
        typing_speed (int, optional): Speed of typing for send_keys events. Defaults to 0.

    Returns:
         str | list[str] | bytes | list[bytes] | bool: Returns True if event execution was successful, False otherwise.
    """
```
**Description**: Executes the events associated with a locator.
**Parameters**:
    -   `locator` (SimpleNamespace | dict): Locator specifying the element and event to execute.
    -   `timeout` (float, optional): Timeout for locating the element. Defaults to 5.
    -   `timeout_for_event` (str, optional): Timeout for waiting for the event. Defaults to `'presence_of_element_located'`.
    -   `message` (Optional[str], optional): Message to send with the event, if applicable. Defaults to `None`.
    -   `typing_speed` (int, optional): Speed of typing for `send_keys` events. Defaults to 0.
**Returns**:
    -  `str | list[str] | bytes | list[bytes] | bool`: Returns `True` if event execution was successful, `False` otherwise.

#### `send_message`

```python
async def send_message(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = 'presence_of_element_located',
    message: str = None,
    typing_speed: float = 0,
    continue_on_error: bool = True,
) -> bool:
    """Sends a message to a web element.

    Args:
        locator (dict | SimpleNamespace): Information about the element's location on the page.
                                          It can be a dictionary or a SimpleNamespace object.
        timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
        timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.
        message (Optional[str], optional): The message to be sent to the web element. Defaults to `None`.
        typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

    Returns:
        bool: Returns `True` if the message was sent successfully, `False` otherwise.

    Example:
        >>> driver = Driver()
        >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
        True
    """
```
**Description**: Sends a message to a web element.
**Parameters**:
    -   `locator` (SimpleNamespace | dict): Locator specifying the element.
    -  `timeout` (float, optional): Max wait time for the element to appear. Defaults to 5.
    - `timeout_for_event` (str, optional): Type of wait condition. Defaults to `'presence_of_element_located'`.
    -   `message` (Optional[str], optional): The message to send to the web element. Defaults to `None`.
    -   `typing_speed` (float, optional): Speed of typing the message in seconds. Defaults to 0.
    - `continue_on_error` (bool, optional): Whether to continue in case of an error. Defaults to `True`.
**Returns**:
    - `bool`: Returns `True` if the message was sent successfully, `False` otherwise.

## Dependencies

-   `asyncio`: For asynchronous operations.
-   `re`: For regular expressions.
-   `dataclasses`: For creating data classes.
-   `enum`: For creating enumerations.
-   `pathlib`: For handling file paths.
-  `types`: For creating simple namespaces.
-   `typing`: For type annotations.
-  `selenium`: For web automation.
- `header`: For project header.
-  `src`: For global settings, logger, and exceptions.
-  `src.utils.jjson`: For JSON handling.
-  `src.utils.printer`: For pretty printing.
-  `src.utils.image`: For image handling.