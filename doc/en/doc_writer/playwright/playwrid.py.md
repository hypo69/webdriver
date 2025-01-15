# Module: src.webdriver.playwright.playwrid

This module defines a custom implementation of `PlaywrightCrawler` called `Playwrid`. It provides additional functionality, such as setting custom browser settings, profiles, and launch options using Playwright.

## Table of Contents
1.  [Classes](#classes)
    -   [Playwrid](#playwrid-class)
        -   [`__init__`](#__init__)
        -   [`_set_launch_options`](#_set_launch_options)
        -   [`start`](#start)
        -   [`current_url`](#current_url)
        -   [`get_page_content`](#get_page_content)
        -   [`get_element_content`](#get_element_content)
        -   [`get_element_value_by_xpath`](#get_element_value_by_xpath)
        -   [`click_element`](#click_element)
        -   [`execute_locator`](#execute_locator)
        -   [`send_message`](#send_message)
        -   [`goto`](#goto)
2.  [Example Usage](#example-usage)

## Classes

### `Playwrid`

**Description**: This class provides a custom implementation of `PlaywrightCrawler` with enhanced functionality.

**Attributes**:

-   `driver_name` (str): Name of the driver, defaults to `'playwrid'`.
-   `base_path` (Path): Path to the `playwright` directory.
-  `config` (SimpleNamespace): Configuration loaded from `playwrid.json`.
-  `context`: Crawling context.

**Methods**:

-   [`__init__`](#__init__)
-  [`_set_launch_options`](#_set_launch_options)
-   [`start`](#start)
-   [`current_url`](#current_url)
-  [`get_page_content`](#get_page_content)
-   [`get_element_content`](#get_element_content)
-   [`get_element_value_by_xpath`](#get_element_value_by_xpath)
-   [`click_element`](#click_element)
-  [`execute_locator`](#execute_locator)
-  [`send_message`](#send_message)
-  [`goto`](#goto)

#### `__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
    """
    Initializes the Playwright Crawler with the specified launch options, settings, and user agent.

    Args:
        user_agent (Optional[str], optional): The user-agent string to be used. Defaults to None.
        options (Optional[List[str]], optional): A list of Playwright options to be passed during initialization. Defaults to None.
    """
```
**Description**: Initializes the `Playwrid` crawler with the specified launch options, settings, and user agent.
**Parameters**:
    -   `user_agent` (Optional[str], optional): The user-agent string to be used. Defaults to `None`.
    -   `options` (Optional[List[str]], optional): A list of Playwright options to be passed during initialization. Defaults to `None`.
    -   `*args`: Variable length argument list.
    -  `**kwargs`: Arbitrary keyword arguments.
**Returns**:
    - `None`

#### `_set_launch_options`

```python
def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Configures the launch options for the Playwright Crawler.

    Args:
        user_agent (Optional[str], optional): The user-agent string to be used. Defaults to None.
        options (Optional[List[str]], optional): A list of Playwright options to be passed during initialization. Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary with launch options for Playwright.
    """
```
**Description**: Configures the launch options for the Playwright Crawler.
**Parameters**:
    -  `user_agent` (Optional[str], optional): The user-agent string to be used. Defaults to `None`.
    -   `options` (Optional[List[str]], optional): A list of Playwright options to be passed during initialization. Defaults to `None`.
**Returns**:
    -  `Dict[str, Any]`: A dictionary with launch options for Playwright.

#### `start`

```python
async def start(self, url: str) -> None:
    """
    Starts the Playwrid Crawler and navigates to the specified URL.

    Args:
        url (str): The URL to navigate to.
    """
```
**Description**: Starts the Playwrid Crawler and navigates to the specified URL.
**Parameters**:
    - `url` (str): The URL to navigate to.
**Returns**:
    -  `None`

#### `current_url`

```python
@property
def current_url(self) -> Optional[str]:
    """
    Returns the current URL of the browser.

    Returns:
        Optional[str]: The current URL.
    """
```
**Description**: Returns the current URL of the browser.
**Returns**:
    -   `Optional[str]`: The current URL.

#### `get_page_content`

```python
def get_page_content(self) -> Optional[str]:
    """
    Returns the HTML content of the current page.

    Returns:
        Optional[str]: HTML content of the page.
    """
```
**Description**: Returns the HTML content of the current page.
**Returns**:
    -  `Optional[str]`: HTML content of the page.

#### `get_element_content`

```python
async def get_element_content(self, selector: str) -> Optional[str]:
    """
    Returns the inner HTML content of a single element on the page by CSS selector.

    Args:
        selector (str): CSS selector for the element.

    Returns:
        Optional[str]: Inner HTML content of the element, or None if not found.
    """
```
**Description**: Returns the inner HTML content of a single element on the page by CSS selector.
**Parameters**:
    -   `selector` (str): CSS selector for the element.
**Returns**:
   - `Optional[str]`: Inner HTML content of the element, or `None` if not found.

#### `get_element_value_by_xpath`

```python
async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
    """
    Returns the text value of a single element on the page by XPath.

    Args:
        xpath (str): XPath of the element.

    Returns:
        Optional[str]: The text value of the element, or None if not found.
    """
```
**Description**: Returns the text value of a single element on the page by XPath.
**Parameters**:
    -   `xpath` (str): XPath of the element.
**Returns**:
   -   `Optional[str]`: The text value of the element, or `None` if not found.

#### `click_element`

```python
async def click_element(self, selector: str) -> None:
    """
    Clicks a single element on the page by CSS selector.

    Args:
        selector (str): CSS selector of the element to click.
    """
```
**Description**: Clicks a single element on the page by CSS selector.
**Parameters**:
    - `selector` (str): CSS selector of the element to click.
**Returns**:
    - `None`

#### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Executes locator through executor

    Args:
        locator (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
        message (Optional[str], optional): Optional message for events. Defaults to None.
        typing_speed (float, optional): Optional typing speed for events. Defaults to 0.

    Returns:
        str | List[str] | bytes | List[bytes] | bool: Execution status.
    """
```
**Description**: Executes locator through executor.
**Parameters**:
    - `locator` (dict | SimpleNamespace): Locator data (dict or SimpleNamespace).
    -   `message` (Optional[str], optional): Optional message for events. Defaults to `None`.
    -  `typing_speed` (float, optional): Optional typing speed for events. Defaults to 0.
**Returns**:
    -  `str | List[str] | bytes | List[bytes] | bool`: Execution status.

#### `send_message`
```python
async def send_message(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> bool:
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
   -   `bool`: Returns `True` if the message was sent successfully, `False` otherwise.

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
    -  `url` (str): URL to navigate to.
**Returns**:
   -  `None`

## Example Usage

```python
if __name__ == "__main__":
    async def main():
        browser = Playwrid(options=["--headless"])
        await browser.start("https://www.example.com")
        
        # Получение HTML всего документа
        html_content = browser.get_page_content()
        if html_content:
            print(html_content[:200])  # Выведем первые 200 символов для примера
        else:
            print("Не удалось получить HTML-контент.")
        
        # Получение HTML элемента по селектору
        element_content = await browser.get_element_content("h1")
        if element_content:
            print("
Содержимое элемента h1:")
            print(element_content)
        else:
            print("
Элемент h1 не найден.")
        
        # Получение значения элемента по xpath
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
             print(f"
Значение элемента по XPATH //head/title: {xpath_value}")
        else:
             print("
Элемент по XPATH //head/title не найден")

        # Нажатие на кнопку (при наличии)
        await browser.click_element("button")

        locator_name = {
        "attribute": "innerText",
        "by": "XPATH",
        "selector": "//h1",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "mandatory": True,
        "locator_description": "Название товара"
        }

        name = await browser.execute_locator(locator_name)
        print("Name:", name)

        locator_click = {
        "attribute": None,
        "by": "CSS",
        "selector": "button",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "mandatory": True,
        "locator_description": "название товара"
        }
        await browser.execute_locator(locator_click)
        await asyncio.sleep(3)
    asyncio.run(main())
```