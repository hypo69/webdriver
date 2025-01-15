## <algorithm>

### Workflow of the Playwright Crawler Module

This document describes the Playwright Crawler module, detailing its configuration, initialization, and usage with the `Playwrid` class.

1.  **Initialization (`__init__`)**:
    *   The `Playwrid` class is initialized with optional parameters such as `user_agent` and `options`, and other `*args` and `**kwargs` for `PlaywrightCrawler` constructor.
    *   **Example**: `browser = Playwrid(options=["--headless"])`
    *    Sets the `driver_name` attribute to `'playwrid'`.
    *   Sets `base_path` to `gs.path.src / 'webdriver' / 'playwright'`, where config file should be located.
    *   Loads settings from `playwrid.json` using `j_loads_ns` and saves them to `config`.
    *   Sets `context` to `None`
    *   Prepares the `launch_options` dictionary using `_set_launch_options()`.
     *  Initializes the parent class `PlaywrightCrawler` by providing the `browser_type` from config, and ignoring `launch_options` in `super().__init__` call, as it can cause an error if this parameter is not supported.
    *  If the `PlaywrightCrawler` has attribute `set_launch_options`, the `launch_options` dictionary is passed to this method to correctly setup launch options.

2.  **Setting Launch Options (`_set_launch_options`)**:
    *   Takes an optional user agent and options as input.
    *   **Example**: `launch_options = self._set_launch_options(user_agent='custom_user_agent', options=['--headless'])`
    *   Creates dictionary named `launch_options` to store parameters for browser launch:
        *   sets `headless` option using value from `self.config`, or defaults to `True` if there is no `headless` attribute in settings.
        *   sets `args` option using the value from `self.config.options` or an empty list if options are not defined in the settings.
     * If `user_agent` was passed as parameter it sets the `user_agent` key of the `launch_options` to the given value.
    *   Merges passed options to `launch_options['args']` list.
    *  Returns dictionary with combined parameters.

3.  **Starting the Crawler (`start`)**:
    *   Takes a `url` string to start crawling from.
    *    **Example**:  `await browser.start("https://www.example.com")`
    *   Logs an information message using `logger.info()` indicating crawler starting.
    *   Initializes the playwright browser by calling `await self.executor.start()`.
    *   Navigates to the given URL using  `await self.executor.goto(url)`.
    *   Runs the crawler using `super().run(url)`, which comes from parent class.
    *    Saves current `crawling_context` to `self.context` for further usage.
    *   Handles exceptions by logging critical error message and continues execution.

4.  **Getting Current URL (`current_url`)**:
    *   A property method that takes no parameters.
    *   **Example**: `url = browser.current_url`
    *   Returns current URL of the browser from `self.context.page.url` if both `self.context` and `self.context.page` are set, otherwise returns `None`.

5.  **Getting Page Content (`get_page_content`)**:
    *   Takes no parameters.
    *    **Example**: `content = browser.get_page_content()`
    *   Returns the content of the page from `self.context.page.content()`, if both `self.context` and `self.context.page` are set, otherwise returns `None`.

6.  **Getting Element Content by CSS Selector (`get_element_content`)**:
    *   Takes a CSS `selector` as a string.
    *   **Example**: `content = await browser.get_element_content("h1")`
    *   If both `self.context` and `self.context.page` are set it retrieves an element with the given selector using `self.context.page.locator(selector)`.
    *   Returns inner HTML content of the element, or returns `None` if the element wasn't found, or any other exception occured.

7.  **Getting Element Value by XPath (`get_element_value_by_xpath`)**:
     *   Takes a XPath `xpath` as a string.
    *   **Example**: `value = await browser.get_element_value_by_xpath("//head/title")`
    *   If both `self.context` and `self.context.page` are set it locates element by XPath using `self.context.page.locator(f'xpath={xpath}')`.
    *   Returns text content of the found element, or `None` if element was not found, or other error occured.

8.  **Clicking an Element (`click_element`)**:
     * Takes a `selector` (string) as an argument, to click an element with a given css selector.
     *    **Example**: `await browser.click_element("button")`
     *  If both `self.context` and `self.context.page` are set, retrieves element by CSS selector and performs click action, using `await element.click()` method.
    *  Logs a warning in case of error during `click` execution, or if no element was found.

9.  **Executing Locator (`execute_locator`)**:
    *   Takes `locator` (`dict` or `SimpleNamespace`), optional `message` (`Optional[str]`) and `typing_speed` (`float`).
    *   **Example**: `result = await browser.execute_locator(locator, message="test")`
    *    Calls the `execute_locator` method from the `PlaywrightExecutor` instance using the provided locator object and message and returns the result.

## <mermaid>

```mermaid
flowchart TD
   subgraph Playwrid Class
         A[__init__ <br> (user_agent, options, *args, **kwargs)] --> B[Load Settings from JSON]
         B --> C[Set launch options using _set_launch_options method]
         C --> D[Initialize PlaywrightExecutor]
        D --> E[Initialize PlaywrightCrawler with browser_type and launch_options from config]
          E --> F{Does PlaywrightCrawler have `set_launch_options` method?}
        F -- Yes --> G[Set launch_options using `set_launch_options` method]
        F -- No --> H[Do nothing]
         G --> H[Return Instance of Playwrid]
        
         I[start <br> (url: str)] --> J[Log starting message]
         J --> K[Call self.executor.start()]
         K --> L[Navigate to URL using self.executor.goto()]
        L --> M[Run the crawler using super().run()]
         M --> N[Save crawling context to self.context]

       O[current_url] --> P{Is context and context.page set?}
        P -- Yes --> Q[Return current url from context.page.url]
        P -- No --> R[Return None]
        Q --> S[Current url]
        R --> S

        T[get_page_content] --> U{Is context and context.page set?}
        U -- Yes --> V[Get page content from context.page.content()]
         U -- No --> W[Return None]
         V --> X[Page content]
         W --> X

        Y[get_element_content <br> (selector)] --> Z{Is context and context.page set?}
        Z -- Yes --> AA[Get web element by selector]
       AA --> AB{Did it found element?}
        AB -- Yes --> AC[Get inner html content]
        AB -- No --> AD[Log warning and return None]
        AC --> AE[Return inner html content]
        AD --> AE
         Z -- No --> AF[Return None]
        AF --> AE
    
         AG[get_element_value_by_xpath <br> (xpath)] --> AH{Is context and context.page set?}
        AH -- Yes --> AI[Get web element by xpath]
       AI --> AJ{Did it found element?}
       AJ -- Yes --> AK[Get element text content]
        AJ -- No --> AL[Log warning and Return None]
       AK --> AM[Return element text content]
      AL --> AM
         AH -- No --> AN[Return None]
         AN --> AM

      AO[click_element <br> (selector)] --> AP{Is context and context.page set?}
      AP -- Yes --> AQ[Get web element using selector]
      AQ --> AR[Click the element]
        AR --> AS
        AP -- No --> AT[Do Nothing]
        AT --> AS

      AU[execute_locator <br> (locator, message, typing_speed)] --> AV[Call self.executor.execute_locator]
        AV --> AW[Return execute_locator results]
   end
   
      subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
         
        AM:::global
       AE:::global
       X:::global
        S:::global
        AW:::global
       O:::global
        H:::global
    end
```

### Dependencies Analysis:

1.  **`Playwrid Class`**:
    *  The core of the module, extending the `PlaywrightCrawler` with custom configurations, and methods for interacting with web pages by using `Playwright` API.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
    *   **`AM`**: The extracted value from a web element by xpath, return of the `get_element_value_by_xpath` method.
     *  **`AE`**: The extracted inner html content from a web element, return value of the method `get_element_content`.
    *   **`X`**: The HTML content of a page, a return value of the `get_page_content` method.
     *   **`S`**: The current URL of a page, return value of the `current_url` property method.
    *  **`AW`**: Result of executing `execute_locator` method.
    *   **`O`**: Representing start of the crawling, a return value of `start` method.
    *   **`H`**: Represents the correctly initialized object of `Playwrid` class, return of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`asyncio`**:  Used for asynchronous operations.
*   **`pathlib.Path`**: Used for handling file paths, specifically for creating path to settings with `Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')`.
*    **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations to make the code more readable.
*   **`types.SimpleNamespace`**: Used to create simple namespace objects from loaded settings.
*   **`crawlee.playwright_crawler.PlaywrightCrawler`, `crawlee.playwright_crawler.PlaywrightCrawlingContext`**: Used from `crawlee` library to implement crawling functionalities.
*   **`src`**: Used to import the global settings object `gs` from the `src` package.
*   **`src.webdriver.playwright.executor import PlaywrightExecutor`**: Imports `PlaywrightExecutor` for executing playwright commands.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` class for executing javascript in the browser.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from JSON file with `j_loads_ns()` method.
*   **`src.logger.logger import logger`**: Used for logging errors and information messages.
*   **`import header`**: Imports the `header.py` module to determine project root and access global settings.

**Classes:**

*   **`Playwrid(PlaywrightCrawler)`**:
    *   **Purpose**:  Extends `PlaywrightCrawler` with added functionality for easier browser automation and data extraction using playwright library.
    *   **Attributes**:
        *   `driver_name` (`str`):  The name of the driver, set to `'playwrid'`.
        *   `base_path` (`Path`): The base path to the configuration file which is `src / 'webdriver' / 'playwright'`.
        *   `config` (`SimpleNamespace`):  Settings from `playwrid.json`.
        *    `context` (`Optional[PlaywrightCrawlingContext]`): Stores current `PlaywrightCrawlingContext`.
    *   **Methods**:
        *   `__init__(self, user_agent, options, *args, **kwargs)`: Initializes the `Playwrid` instance by loading the settings from json, and passing browser options and user agent.
        *  `_set_launch_options(self, user_agent, options)`:  Sets up launch options for the Playwright browser.
        *   `start(self, url)`:  Initializes `PlaywrightExecutor`, navigates to URL and starts crawler.
        *  `current_url(self)`:  Property method to get current URL of the page.
         *  `get_page_content(self)`: Returns content of the page.
        *   `get_element_content(self, selector)`: Gets inner HTML from web element specified by css selector.
        *    `get_element_value_by_xpath(self, xpath)`: Gets text value of the web element by using XPath.
        *   `click_element(self, selector)`: Clicks a web element using css selector.
        *   `execute_locator(self, locator, message, typing_speed)`: Executes a locator on the page using playwright.

**Functions:**

*   **`__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *   `user_agent` (`Optional[str]`):  Optional parameter to set the user agent.
        *   `options` (`Optional[List[str]]`):  Optional list of options to pass to playwright.
        *    `*args`, `**kwargs`:  Additional arguments for `PlaywrightCrawler` constructor.
    *   **Purpose**: Initializes `Playwrid` object and sets required options and configurations.
    *   **Return**: `None`.
*   **`_set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]`**:
    *  **Arguments**:
        *  `user_agent` (`Optional[str]`): Custom user agent for browser.
        *  `options` (`Optional[List[str]]`): Options for browser.
    *  **Purpose**: Sets the launch options.
    *  **Return**: `Dict[str, Any]` representing the options.
*   **`start(self, url: str) -> None`**:
    *  **Arguments**: `url` (`str`): URL to start crawling.
    *   **Purpose**: Starts the `PlaywrightExecutor`, navigates to specified URL and starts the crawling process.
    *  **Return**: `None`.
*  **`current_url(self) -> Optional[str]`**:
     *   **Arguments**: `self` (instance of the `Playwrid` class).
     *   **Purpose**:  Gets current URL of the page, if page is initialized.
     *   **Return**: `Optional[str]`, current URL or `None`.
*   **`get_page_content(self) -> Optional[str]`**:
    *    **Arguments**: `self` (instance of the `Playwrid` class).
    *   **Purpose**: Returns page content.
    *   **Return**: `Optional[str]`, page content or `None`.
*   **`get_element_content(self, selector: str) -> Optional[str]`**:
     *   **Arguments**: `selector` (`str`): CSS selector to find the element on the page.
     *   **Purpose**:  Gets inner HTML of a web element using css selector.
     *   **Return**: `Optional[str]`, element content as string, or `None`.
*  **`get_element_value_by_xpath(self, xpath: str) -> Optional[str]`**:
    *    **Arguments**: `xpath` (`str`): xpath to find the element.
    *    **Purpose**: Gets inner text of the element using xpath selector.
    *   **Return**: `Optional[str]`, text content of the element or `None`.
*   **`click_element(self, selector: str) -> None`**:
     *  **Arguments**: `selector` (`str`): CSS selector of element to click on.
     *   **Purpose**: Clicks on an element specified by css selector.
     *   **Return**: `None`.
*  **`execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool`**:
     *   **Arguments**:
         *   `locator` (`dict | SimpleNamespace`): Locator object.
         *   `message` (`Optional[str]`, default is `None`): Optional message parameter.
         *   `typing_speed` (`float`, default is `0`): Optional typing speed parameter.
    *    **Purpose**: Executes a locator on the page using `PlaywrightExecutor` and returns the result.
    *   **Return**: `str | List[str] | bytes | List[bytes] | bool`, result of locator execution.

**Variables:**

*   `driver_name` (`str`): Represents driver name, set to `playwrid`.
*    `base_path` (`Path`): Path to the directory of configurations file for the module.
*  `config` (`SimpleNamespace`): Contains loaded configurations from the `playwrid.json` file.
*    `context` (`PlaywrightCrawlingContext`): Variable to hold current crawling context from `PlaywrightCrawler`.
*   `user_agent` (`str`): Stores user agent string.
*   `options` (`List[str]`):  Stores options for the playwright browser.
*    `launch_options` (`Dict[str, Any]`): Dictionary with all parameters to launch the browser.
*   `url` (`str`): URL string.
*   `selector` (`str`):  CSS selector string.
*   `xpath` (`str`): xpath expression string.
*    `message` (`str`): Message string that is passed to the `send_message` or `execute_event` methods of `PlaywrightExecutor`.
*    `typing_speed` (`float`): Value for setting the typing speed when sending a message.

**Potential Errors and Areas for Improvement:**

*   **Configuration Loading**: The settings loading could have more specific error handling.
*  **Hardcoded Paths**: The path to settings JSON file is hardcoded and should be configurable via `gs.path` from `src` package, similar to other modules.
*  **Error Handling**:  While some error handling is present, it can be improved by adding more specific exception handling for different errors that might occur, and it can be improved by adding more verbose logging.
*  **Missing Configuration for Playwright**: The `PlaywrightCrawler` initialization is hardcoded with only browser type, it should be flexible and get more parameters from settings file.
* **Code Clarity**: Some code blocks are hard to read because of the usage of `if hasattr() and settings.attribute`, it would be more readable to have defaults set for the config object, for example using `settings.attribute or default_value`
*    **Type Hinting**:  Some variables and function parameters can benefit from more specific type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package, and specifically `src.webdriver.playwright`.
*   It uses the `crawlee.playwright_crawler` library for web crawling.
*   It uses `src.webdriver.playwright.executor` to interact with elements on the page by using playwright.
*   It uses `src.webdriver.js` to inject and execute javascript code.
*  It depends on global settings object `gs` from `src` package.
*  It utilizes the `j_loads_ns` method from the `src.utils.jjson` module to load settings.
*   It uses  `src.logger.logger` for logging errors.
*  It also utilizes the `header` module to set root of the project.

This detailed explanation provides a comprehensive understanding of the `playwrid.py` module and how it is used to perform web scraping with playwright and crawlee libraries.