## <algorithm>

### Workflow of the Playwright Executor Module

This document describes the `PlaywrightExecutor` class, outlining its methods for interacting with web pages using Playwright.

1.  **Initialization (`__init__`)**:
    *   The `PlaywrightExecutor` class is initialized with an optional `browser_type` (defaulting to `'chromium'`) and other keyword arguments.
    *   **Example**: `executor = PlaywrightExecutor(browser_type='firefox')`
    *   Initializes `self.driver` to `None`, assigns `browser_type` to `self.browser_type`, initializes `self.page` to `None`, and loads settings from `playwrid.json` into `self.config` using `j_loads_ns`.

2.  **Starting Playwright (`start`)**:
    *   This method initializes Playwright and launches a browser instance with default or user-defined settings.
    *   **Example**: `await self.start()`
    *  It initializes the `async_playwright` object, launches a browser instance by using `getattr(self.driver, self.browser_type).launch()`, and creates a new page with `browser.new_page()`, storing the results to class attributes `self.driver` and `self.page` respectively.
    *   Handles exceptions during initialization, logging errors using `logger.critical`.

3.  **Stopping Playwright (`stop`)**:
    *   Closes the Playwright browser and stops its instance.
    *   **Example**: `await self.stop()`
    *   Closes the current page using `await self.page.close()`, if `self.page` is set.
    *    Stops playwright driver using  `await self.driver.stop()`, if `self.driver` is set.
    *    Sets `self.driver` to `None`.
    *  Logs the action using `logger.info('Playwright stopped')`.
    *   Handles exceptions during stopping using `logger.error`.

4.  **Executing Locator (`execute_locator`)**:
    *   Takes a `locator` (dict or `SimpleNamespace`), optional `message`, and `typing_speed` as input.
    *   **Example**: `result = await self.execute_locator(locator, message="test", typing_speed=0.1)`
    *   Converts locator to a `SimpleNamespace` if it is a dictionary.
    *  If the locator does not have `attribute` and `selector` keys, it returns `None`.
    *   Defines async function `_parse_locator` for processing locators:
        *   Checks if the locator has an `event`, `attribute`, or `mandatory` keys, if none returns `None`.
        *   If an attribute exists, the attributes is evaluated using `evaluate_locator`. If `by` is equal to `VALUE`, it returns that attribute immediately.
        *   If an `event` key exists, executes the event using `execute_event`.
        *   If `attribute` key exists, gets it using `get_attribute_by_locator`.
        *   If neither `event` or `attribute` is present, gets a web element with `get_webelement_by_locator`.
        *   Returns result of evaluation.
    *   The method returns result of executing `_parse_locator` method.

5.  **Evaluating Locator (`evaluate_locator`)**:
    *   Takes a locator `attribute` which can be a string, a list of strings or a dictionary.
    *   **Example**: `result = await self.evaluate_locator(attribute)`
    *   Defines an async function `_evaluate` which currently returns given `attribute`, as playwright does not use `Keys` enum, which is used in the selenium implementation.
    *   If the `attribute` is a list, it maps over this list using `_evaluate` and uses `asyncio.gather` to collect the results and returns the results as a list.
    *    If it's a single value, calls `_evaluate` for it and returns result.

6.  **Getting Attribute by Locator (`get_attribute_by_locator`)**:
    *   Takes a `locator` object as input, which can be either `dict` or `SimpleNamespace`.
    *   **Example**: `attribute = await self.get_attribute_by_locator(locator)`
    *   Converts locator to `SimpleNamespace` if it is a `dict`.
    *   Gets web element using `get_webelement_by_locator`.
    *  If the element is not found, returns `None` and logs a debug message.
    *   Defines inner function `_parse_dict_string` to parse attribute strings which are like a dictionary (e.g. `"{attr1:attr2}"`), and returns parsed dict if parsing successful or `None` otherwise and logs error during parsing process.
     *  Defines inner async function `_get_attribute` to extract attribute from locator.
      * Defines inner async function `_get_attributes_from_dict` to extract a dict of attributes based on passed `attr_dict`.
    *   If the attribute is a dictionary-like string, it parses it to a dictionary using `_parse_dict_string()` and retrieves the attributes by using `_get_attributes_from_dict()` and returns a list of results or a single result using `asyncio.gather`.
     *   If attribute is a list, it retrieves each attribute using `_get_attribute` and returns it as list using `asyncio.gather`.
    *   If attribute is a single value, returns result of `_get_attribute` method.

7.  **Getting Web Element by Locator (`get_webelement_by_locator`)**:
    *   Takes a `locator` (dictionary or `SimpleNamespace`) as an input.
    *  **Example**: `element = await self.get_webelement_by_locator(locator)`
    *   Converts the `locator` to a `SimpleNamespace` object if it was passed as a dictionary, otherwise it uses it as is. If not a `dict` or `SimpleNamespace` raises an error.
    *   Finds elements with the playwright method `self.page.locator()`, if `locator.by` is equal to "XPATH" than the `locator` is used as xpath expression, otherwise the `locator` is used as a css selector.
    *   If `locator.if_list` is specified as `all`, it returns all found elements using the method `elements.all()`.
    *  If `locator.if_list` is specified as `first`, returns the first element using `elements.first`.
    *   If `locator.if_list` is specified as `last`, it returns last element using `elements.last`.
    *   If `locator.if_list` is `even` or `odd` it returns a list of even or odd elements from all elements respectively using Python list comprehension.
    *  If `locator.if_list` is a list, it returns list of the elements specified by indexes in the locator list.
    *  If `locator.if_list` is an integer, it returns element at the specified index.
    *  If no `if_list` is specified it returns Locator object.
    *   Returns the located web element(s) or `None` if an exception occurs, and logs an error.

8.  **Taking Screenshot (`get_webelement_as_screenshot`)**:
    *   Takes a `locator` (dict or `SimpleNamespace`) and an optional `webelement` as an input.
    *   **Example**: `screenshot = await self.get_webelement_as_screenshot(locator)`
    *    If `webelement` parameter is not provided, the web element is retrieved by calling `get_webelement_by_locator` method.
     *   If the web element is not found, returns `None` after logging debug information.
    *   Takes a screenshot of the located element using `await webelement.screenshot()` and returns it as byte array, also logs an error if taking a screenshot failed.

9.  **Executing an Event (`execute_event`)**:
    *   Takes a `locator` (dict or `SimpleNamespace`), optional `message`, and `typing_speed` as input, parses event from `locator` object and executes it.
    *   **Example**: `result = await self.execute_event(locator, message="test", typing_speed=0.1)`
    *  Parses list of events from `locator.event` string using `;` as a separator.
    *   Gets the web element using `get_webelement_by_locator`.
    *    If element is not found, logs debug information and returns `False`.
    *   Iterates over the list of events:
          * If an event equals to `click()`, performs a click by calling `await element.click()`.
        * If the event starts with `pause(`, parses the pause time and pauses execution for defined time with `asyncio.sleep(pause_duration)`.
          * If an event is `upload_media()` it sets input files using `set_input_files` with the `message` as value.
          *  If an event is equal to `screenshot()` calls `get_webelement_as_screenshot()` method to take screenshot of a web element.
         * If an event is `clear()`, clears input element using `await element.clear()`.
         * If the event starts with `send_keys(`, it extracts keys to send, and for every key calls `await element.type(key)`.
        * If the event starts with `type(`, it extracts the message to type, and if typing speed is provided, types character by character with a pause, otherwise types all at once using `await element.type(message)`.
    *   Returns `result` list if the event was screenshot event, or `True` otherwise and `False` if an error occured or element was not found.

10. **Sending a Message (`send_message`)**:
    *   Takes a `locator` (dict or `SimpleNamespace`), an optional `message` (string) and `typing_speed` (float).
    *   **Example**:  `await self.send_message(locator, message='test message', typing_speed=0.1)`
    *  Converts the `locator` to a `SimpleNamespace` if it was a `dict`.
    *   Gets the web element using `get_webelement_by_locator`.
    *    If element is not found, it returns `None`.
    *    If typing speed is greater than zero, types the message with a pause between each character using loop and `await element.type(character)` call.
    *   Otherwise, types the message at once by calling  `await element.type(message)`.
    *   Returns `True` on success.

11. **Navigating to URL (`goto`)**:
    *    Takes an URL string as an argument.
    *    **Example**: `await self.goto("https://www.example.com")`
    *   If `self.page` is set, navigates to the given url using `await self.page.goto(url)`.
    *  If an exception occurs during navigation it is caught, logged using logger.error, and then continues execution.

## <mermaid>

```mermaid
flowchart TD
     subgraph PlaywrightExecutor Class
        A[__init__ <br> (browser_type, **kwargs)] --> B[Load Playwright Settings from JSON]
        B --> C[Initialize Playwright Driver and Page]

        D[execute_locator <br> (locator, message, typing_speed)] --> E[Check if locator is SimpleNamespace or dict]
         E --> F{Is locator SimpleNamespace?}
        F -- Yes --> G[Use locator as is]
        F -- No --> H[Convert dict to SimpleNamespace]
          H --> G
        G --> I[Define async function _parse_locator]
         I --> J[Check if locator has event, attribute, or mandatory]
        J -->|No| K[Return None]
         J -->|Yes| L[Try to map by and evaluate attribute]
         L --> M[Catch exceptions and log if needed]
        M --> N{Does locator have event?}
          N -->|Yes| O[Execute event]
        N -->|No| P{Does locator have attribute?}
         P -->|Yes| Q[Get attribute by locator]
        P -->|No| R[Get web element by locator]
         O --> S[Return result of event]
        Q --> S[Return attribute result]
         R --> S[Return web element result]
          S --> T[Return final result of _parse_locator]
        T --> U[Return result of execute_locator]
         U --> V[End]

       AA[evaluate_locator <br> (attribute)] --> AB{Is attribute list?}
       AB -- Yes --> AC[Iterate over attributes]
       AC --> AD[Call _evaluate for each attribute]
       AD --> AE[Return gathered results]
       AB -- No --> AF[Call _evaluate for single attribute]
        AF --> AG[Return evaluate result]
       AE --> AH
       AG --> AH[End]

       AI[get_attribute_by_locator <br> (locator)] --> AJ[Call get_webelement_by_locator]
       AJ --> AK{Is web element found?}
       AK -- Yes --> AL{Is attribute like dictionary string?}
        AL -- Yes --> AM[Parse attribute string to dictionary]
         AM --> AN{Is webelement list?}
        AN -- Yes --> AO[Get attributes from list of elements]
         AN -- No --> AP[Get attributes from single element]
          AO --> AQ[Return attributes]
         AP --> AQ
       AL -- No --> AR{Is webelement list?}
      AR -- Yes --> AS[Get list of attribute values]
        AR -- No --> AT[Get single attribute value]
       AS --> AQ
        AT --> AQ
       AK -- No --> AU[Log debug and return None]
         AU --> AQ

       AV[get_webelement_by_locator <br> (locator)] --> AW[Locate element using Playwright]
        AW --> AX{Is there an if_list parameter?}
         AX -- Yes --> AY[Filter element(s) based on if_list]
        AY --> AZ[Return located elements or None]
        AX -- No --> AZ

         BA[get_webelement_as_screenshot <br> (locator, webelement)] --> BB{Is webelement provided?}
         BB -- Yes --> BC[Use provided webelement]
          BB -- No --> BD[Get web element using get_webelement_by_locator]
        BD --> BE{Is webelement found?}
        BC --> BE
        BE -- Yes --> BF[Take screenshot]
        BF --> BG[Return screenshot as bytes]
        BE -- No --> BH[Log debug, return None]
         BH --> BG

        BI[execute_event <br> (locator, message, typing_speed)] --> BJ[Get web element from locator]
       BJ --> BK{Is web element found?}
        BK -- No --> BL[Log debug and return False]
        BK -- Yes --> BM[Parse event from locator]
         BM --> BN[Execute parsed event from list]
          BN --> BO[Return event execution results]
         BL --> BO

       BP[send_message <br> (locator, message, typing_speed)] --> BQ[Get web element using locator]
       BQ --> BR{Is web element found?}
       BR -- Yes --> BS[Send message using playwright method type()]
       BR -- No --> BT
       BS --> BU
       BT --> BU[Return]
        
       BV[goto <br> (url)] --> BW[Navigate to URL with self.page.goto()]
       BW --> BX
    end
    
    subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
      
      
        
        BX:::global
       BU:::global
      BO:::global
       BG:::global
      AZ:::global
      AQ:::global
      U:::global
      C:::global
    end
```

### Dependencies Analysis:

1.  **`PlaywrightExecutor Class`**:
    *   The core of the module, responsible for initializing `Playwright`, creating page object, and providing methods for web element manipulation, attribute extraction, and event handling.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
    *   **`BX`**:  Represents navigation to URL, return value of method `goto`.
    *   **`BU`**:  Represents message sending process, return value of the method `send_message`.
    *   **`BO`**:  Boolean or list with results of execution, return value of `execute_event` method.
    *   **`BG`**: The screenshot in bytes, return value of `get_webelement_as_screenshot` method.
    *    **`AZ`**:  List of located web elements, or `None` if no elements found, return value of `get_webelement_by_locator` method.
     *  **`AQ`**: A single attribute value or a list of attribute values or a dictionary with attribute values, a return value of method `get_attribute_by_locator`.
    *  **`U`**:   Result of execution of `execute_locator` function, which returns the result from a nested function `_parse_locator`.
    *   **`C`**: Instance of the `PlaywrightExecutor` class, result of the `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`asyncio`**: Used for asynchronous programming.
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations.
*   **`pathlib.Path`**: Used for handling file paths, specifically used for loading configurations from json file with `Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')`.
*   **`playwright.async_api.async_playwright`, `playwright.async_api.Page`, `playwright.async_api.Locator`**: Used for browser automation using Playwright library.
*   **`types.SimpleNamespace`**: Used for creating simple namespace objects, converting dictionaries into objects for easy access to locator's keys.
*   **`src`**: Used to import global settings object `gs` from `src` package.
*   **`src.logger.logger import logger`**: Used for logging messages and errors.
*    **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file, with `j_loads_ns()`.
*   **`src.logger.exceptions import WebDriverException`**: Imports custom `WebDriverException` for handling exceptions.
*   **`re`**: Used to extract pause duration from string using `re.match(r"pause\\((\\d+)\\)", event)`.

**Classes:**

*   **`PlaywrightExecutor`**:
    *   **Purpose**:  Executes commands based on executor-style locator commands using Playwright library.
    *   **Attributes**:
         *   `driver` (`Optional[async_playwright]`): Instance of `async_playwright`, initialized to `None`.
        *   `browser_type` (`str`): The type of the browser used (e.g. `chromium`, `firefox` etc), defaults to chromium.
        *    `page` (`Optional[Page]`): Stores the current `Page` object in order to interact with the page, initialized to `None`.
        *  `config` (`SimpleNamespace`): A simple namespace object that stores the loaded settings from the configuration file, initialized with `j_loads_ns`.
    *   **Methods**:
        *   `__init__(self, browser_type, **kwargs)`: Initializes the `PlaywrightExecutor` instance.
        *    `start(self) -> None`: Starts the playwright library and creates page object.
        *   `stop(self) -> None`: Closes playwright browser.
        *    `execute_locator(self, locator, message, typing_speed)`: Executes actions based on the locator by calling nested helper methods.
         * `evaluate_locator(self, attribute)`: Evaluates locator attributes by using helper method `_evaluate`.
         *   `get_attribute_by_locator(self, locator)`: Retrieves specified attribute from found web element(s).
         *    `get_webelement_by_locator(self, locator)`: Extracts a web element using playwright Locator by using the provided locator.
         * `get_webelement_as_screenshot(self, locator, webelement)`: Takes a screenshot of the located web element.
        *   `execute_event(self, locator, message, typing_speed)`: Executes an event on located element based on the provided `locator`.
         *   `send_message(self, locator, message, typing_speed)`: Sends message to the element.
         *   `goto(self, url)`: Navigates to specified URL.

**Functions:**

*  **`__init__(self, browser_type: str = 'chromium', **kwargs)`**:
    *   **Arguments**:
        *   `browser_type` (`str`, default: `'chromium'`): The type of browser to launch.
        *   `**kwargs`:  Additional keyword arguments.
    *   **Purpose**: Initializes the `PlaywrightExecutor` class by loading settings from config file, and setting the browser type.
    *   **Return**: `None`.
*   **`start(self) -> None`**:
    *   **Arguments**: `self` (instance of `PlaywrightExecutor`).
    *   **Purpose**:  Initializes Playwright and browser instance.
    *   **Return**: `None`.
*    **`stop(self) -> None`**:
    *   **Arguments**: `self` (instance of `PlaywrightExecutor`).
    *  **Purpose**: Closes Playwright browser and page.
    *   **Return**: `None`.
*   **`execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | dict | bytes | bool`**:
    *   **Arguments**:
        *  `locator` (`dict | SimpleNamespace`): Locator object, which is used to locate a web element.
        *   `message` (`Optional[str]`, default is `None`): Message to send to the element.
        *  `typing_speed` (`float`, default is `0`): Typing speed for typing actions.
    *   **Purpose**: Executes actions based on locator and event.
    *  **Return**: `str | List[str] | dict | bytes | bool` which represents a result of the actions defined by locator object.
*  **`evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`**:
    *  **Arguments**:
        *   `attribute` (`str | List[str] | dict`): Attribute or attributes for evaluation.
    *   **Purpose**: Evaluates and processes locator attributes using helper method `_evaluate`.
    *   **Return**: `Optional[str | List[str] | dict]` : result of evaluation of attribute or attributes.
*    **`get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`**:
    *  **Arguments**: `locator` (`dict | SimpleNamespace`): Locator object.
    *   **Purpose**: Gets specified attribute from located web element(s).
    *  **Return**:  `Optional[str | List[str] | dict]`, returns `None` if attribute not found.
*   **`get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`**:
    *   **Arguments**: `locator` (`dict | SimpleNamespace`): Locator object.
    *   **Purpose**:  Finds a web element or a list of elements from locator object.
    *  **Return**: `Optional[Locator | List[Locator]]`, returns `None` if element is not found.
*   **`get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`**:
    *   **Arguments**:
         *   `locator` (`dict | SimpleNamespace`): Locator object.
         *   `webelement` (`Optional[Locator]`, default: `None`):  Optional web element to use.
    *   **Purpose**: Takes screenshot of the found web element, using `screenshot` method of playwright.
    *   **Return**: `Optional[bytes]`, screenshot as a bytes array or `None`.
*   **`execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool`**:
    *   **Arguments**:
         *  `locator` (`dict | SimpleNamespace`): Locator object.
         *   `message` (`Optional[str]`, default is `None`):  Optional message parameter.
         *   `typing_speed` (`float`, default is `0`): Optional typing speed parameter.
    *  **Purpose**: Executes event based on locator.
    *   **Return**: `str | List[str] | bytes | List[bytes] | bool` - result of event execution, or `False` if failed to execute event.
*  **`send_message(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> bool`**:
    *   **Arguments**:
         * `locator` (`dict | SimpleNamespace`): Locator object.
        *  `message` (`Optional[str]`, default is `None`): Message to send to the element.
         *  `typing_speed` (`float`, default is `0`):  Typing speed.
    *   **Purpose**: Sends a message to a web element using type() method.
    *   **Return**: `True` if the message was sent successfully, `False` otherwise or `None` if no element was found.
*   **`goto(self, url: str) -> None`**:
    *   **Arguments**:
         *  `url` (`str`):  Url of the page to navigate to.
    *   **Purpose**: Navigates to specified url using playwright api.
    *    **Return**: `None`.

**Variables:**

*    `driver` (`Optional[async_playwright]`):  Playwright Driver Instance.
*    `browser_type` (`str`): Type of the browser set during initialization.
*  `page` (`Optional[Page]`): Instance of the playwright `Page`.
* `config` (`SimpleNamespace`): Object that holds settings from `playwrid.json`.
*   `locator` (`dict | SimpleNamespace`): Stores the locator data.
*  `message` (`Optional[str]`): String that represents a message to be typed to input or textarea.
*  `typing_speed` (`float`): Value that defines typing speed in seconds.
*   `attribute` (`str`): Attribute string extracted from the locator.
*   `element` (`Locator | List[Locator]`): Locator object.
*  `attr_dict` (`dict`): Parsed string, when `attribute` from locator is like dictionary string (e.g. `"{attr1:attr2}"`).
*    `attr` (`str`): String with the name of attribute to extract from the web element.
*   `elements` (`Optional[Locator | List[Locator]]`):  Locator or a list of locators.
*   `screenshot_bytes` (`bytes`): Bytes array of a screenshot.
*   `events` (`list`):  List of events to perform on element, created by parsing locator.event string.
*   `event` (`str`):  Current event in a loop, when iterating over a list of events from `events` variable.
*    `pause_duration` (`int`): Pause duration.
*    `keys_to_send` (`list`): List of keys to send to the element, created by parsing `send_keys` event string.
*   `key` (`str`): Single key from list of `keys_to_send` list.
*   `character` (`str`): Single character, when iterating through message for typing.
*  `result` (`str | List[str] | dict | bytes | bool`):  Variable that contains result of executing events on web element, also contains the result of `_parse_locator` method.
*    `attr_string` (`str`):  String, where attribute is like a dictionary string.

**Potential Errors and Areas for Improvement:**

*   **Configuration Loading**: The configuration loading could have more specific error handling.
*  **Locator handling**:  Locator handling can be improved by using a more flexible xpath selectors implementation.
*   **Error Handling**:  While basic error handling is present in `try except` blocks, it can be improved by adding more specific exceptions and logging, instead of generic `Exception` class.
*  **Type Hinting**: Some parameters and variables can benefit from more precise type hints.
*  **Attribute Handling**: The handling of attributes using `_parse_dict_string` and `_get_attributes_from_dict` can be improved to work with more complex scenarios, instead of hardcoded parsing from a dictionary like string.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver.crawlee_python` package.
*   It uses the `PlaywrightCrawler` class from the `crawlee` library for web crawling.
*   It utilizes a `JavaScript` helper from the `src.webdriver.js` module for injecting and executing JavaScript in browser context.
*   It uses  `src.utils.jjson` to load the configuration from json files.
*  It also uses the custom logger from  `src.logger.logger`.
*  It depends on global settings object `gs` from `src` package.

This detailed explanation provides a comprehensive understanding of the `executor.py` module, its functionality, structure, and its interaction with other parts of the project.