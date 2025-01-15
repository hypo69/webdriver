# Module: src.webdriver.playwright.executor

This module provides a `PlaywrightExecutor` class for executing commands based on locator configurations using Playwright. It allows you to interact with web pages and extract data using Playwright's API.

## Table of Contents
1.  [Classes](#classes)
    -   [PlaywrightExecutor](#playwrightexecutor-class)
        -   [`__init__`](#__init__)
        -   [`start`](#start)
        -   [`stop`](#stop)
        -   [`execute_locator`](#execute_locator)
        -   [`evaluate_locator`](#evaluate_locator)
        -   [`get_attribute_by_locator`](#get_attribute_by_locator)
        -   [`get_webelement_by_locator`](#get_webelement_by_locator)
        -   [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
        -   [`execute_event`](#execute_event)
        -   [`send_message`](#send_message)
        -   [`goto`](#goto)

## Classes

### `PlaywrightExecutor`

**Description**: This class executes commands based on locator configurations using Playwright.

**Attributes**:

-   `driver`:  Playwright driver instance.
-   `browser_type` (str): Type of browser to launch (e.g., `'chromium'`, `'firefox'`, `'webkit'`).
-   `page` (Optional[Page]): Playwright Page instance.
-   `config` (SimpleNamespace): Configuration loaded from `playwrid.json`.

**Methods**:

-   [`__init__`](#__init__)
-   [`start`](#start)
-   [`stop`](#stop)
-   [`execute_locator`](#execute_locator)
-   [`evaluate_locator`](#evaluate_locator)
-   [`get_attribute_by_locator`](#get_attribute_by_locator)
-   [`get_webelement_by_locator`](#get_webelement_by_locator)
-   [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
-   [`execute_event`](#execute_event)
-  [`send_message`](#send_message)
-  [`goto`](#goto)

#### `__init__`

```python
def __init__(self, browser_type: str = 'chromium', **kwargs):
    """
    Initializes the Playwright executor.

    Args:
        browser_type (str, optional): Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit'). Defaults to 'chromium'.
    """
```
**Description**: Initializes the Playwright executor.
**Parameters**:
    -   `browser_type` (str, optional): Type of browser to launch (e.g., `'chromium'`, `'firefox'`, `'webkit'`). Defaults to `'chromium'`.

#### `start`

```python
async def start() -> None:
    """
    Initializes Playwright and launches a browser instance.
    """
```
**Description**: Initializes Playwright and launches a browser instance.
**Returns**:
    - `None`

#### `stop`

```python
async def stop() -> None:
    """
    Closes Playwright browser and stops its instance.
    """
```
**Description**: Closes the Playwright browser and stops its instance.
**Returns**:
    - `None`

#### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | dict | bytes | bool:
    """
    Executes actions based on locator and event.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        message (Optional[str], optional): Optional message for events. Defaults to None.
        typing_speed (float, optional): Optional typing speed for events. Defaults to 0.

    Returns:
        str | List[str] | dict | bytes | bool: Result of the operation.

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
**Description**: Executes actions based on locator and event.
**Parameters**:
    - `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
    -   `message` (Optional[str], optional): Optional message for events. Defaults to `None`.
    -   `typing_speed` (float, optional): Optional typing speed for events. Defaults to 0.
**Returns**:
    -   `str | List[str] | dict | bytes | bool`: Result of the operation.

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
    -  `Optional[str | List[str] | dict]`: Evaluated attributes.

#### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Gets the specified attribute from the web element.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).

    Returns:
        Optional[str | List[str] | dict]: Attribute or None.
    """
```
**Description**: Gets the specified attribute from the web element.
**Parameters**:
    -   `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
**Returns**:
    -   `Optional[str | List[str] | dict]`: Attribute or `None`.

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Gets a web element using the locator.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).

    Returns:
        Optional[Locator | List[Locator]]: Playwright Locator.
    """
```
**Description**: Gets a web element using the locator.
**Parameters**:
    - `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
**Returns**:
    - `Optional[Locator | List[Locator]]`: Playwright Locator or list of Locator.

#### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Takes a screenshot of the located web element.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        webelement (Optional[Locator], optional): The web element Locator. Defaults to None.

    Returns:
        Optional[bytes]: Screenshot in bytes or None.
    """
```
**Description**: Takes a screenshot of the located web element.
**Parameters**:
    -   `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
    - `webelement` (Optional[Locator], optional): The web element Locator. Defaults to `None`.
**Returns**:
   - `Optional[bytes]`: Screenshot in bytes or `None`.

#### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Executes the event associated with the locator.

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        message (Optional[str], optional): Optional message for events. Defaults to None.
        typing_speed (float, optional): Optional typing speed for events. Defaults to 0.

    Returns:
         str | List[str] | bytes | List[bytes] | bool: Execution status.
    """
```
**Description**: Executes the event associated with the locator.
**Parameters**:
    -   `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
    - `message` (Optional[str], optional): Optional message for events. Defaults to `None`.
    -  `typing_speed` (float, optional): Optional typing speed for events. Defaults to 0.
**Returns**:
    -  `str | List[str] | bytes | List[bytes] | bool`: Execution status.

#### `send_message`

```python
async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
    """Sends a message to a web element.

    Args:
        locator (dict | SimpleNamespace): Information about the element's location on the page.
        message (Optional[str], optional): The message to be sent to the web element. Defaults to `None`.
        typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

    Returns:
        bool: Returns `True` if the message was sent successfully, `False` otherwise.
    """
```
**Description**: Sends a message to a web element.
**Parameters**:
    -   `locator` (dict | SimpleNamespace): Information about the element's location on the page.
    -   `message` (Optional[str], optional): The message to be sent to the web element. Defaults to `None`.
    -   `typing_speed` (float, optional): Speed of typing the message in seconds. Defaults to 0.
**Returns**:
    -  `bool`: Returns `True` if the message was sent successfully, `False` otherwise.

#### `goto`

```python
async def goto(self, url: str) -> None:
    """
    Navigates to a specified URL.

    Args:
        url (str): URL to navigate to.
    """
```
**Description**: Navigates to a specified URL.
**Parameters**:
    -   `url` (str): URL to navigate to.
**Returns**:
    - `None`