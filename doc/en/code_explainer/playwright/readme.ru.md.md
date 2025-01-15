## <algorithm>

### Workflow of the Playwright Crawler Module

This document outlines the configuration and usage of the Playwright Crawler module, focusing on the `Playwrid` class and its interaction with other components.

1.  **Initialization (`__init__`)**:
    *   The `Playwrid` class is initialized with optional parameters such as `user_agent` and `options`.
    *   **Example**: `browser = Playwrid(user_agent="custom_user_agent", options=["--headless"])`
    *    Sets the `driver_name` attribute to `"playwrid"`.
    *   Sets `base_path` to the directory of the settings file: `gs.path.src / 'webdriver' / 'playwright'`.
    *   Loads configurations from `playwrid.json` using `j_loads_ns` and stores them in the attribute `config`.
    *    Sets `self.context` attribute to `None`, it will be used for saving current crawling context.
     *  Calls `_set_launch_options` to setup launch options for the browser by using parameters passed to init, and settings from the config.
    *   Initializes the parent class `PlaywrightCrawler` with the `browser_type` from settings, ignoring `launch_options` if it is not supported.
    *   If the `PlaywrightCrawler` class has method `set_launch_options`, the `launch_options` is passed to it using call `self.set_launch_options(launch_options)`.

2.  **Setting Launch Options (`_set_launch_options`)**:
    *   Takes an optional `user_agent` (string) and `options` (list of strings) as input parameters.
    *   **Example**: `launch_options = self._set_launch_options(user_agent="custom_user_agent", options=["--headless"])`
    *   Initializes a dictionary to store launch options, setting the following options:
        *   Sets the `headless` mode using the value from config, if present, otherwise defaults to `True`.
        *  Sets the browser `args` from settings if present, otherwise defaults to empty list.
    *   If a `user_agent` is provided, adds it to `launch_options` dictionary.
    *  If  `options` were provided they are merged with the browser arguments from the `launch_options` dictionary using `extend` method.
    *   Returns the dictionary with the combined launch options.

3.  **Starting Crawler (`start`)**:
    *   Takes a `url` (string) to navigate to as input.
    *   **Example**: `await browser.start("https://www.example.com")`
     * Logs a message indicating that crawling is starting.
    *   Initializes `Playwright` and the browser instance using `self.executor.start()`.
    *   Navigates to the specified URL using `self.executor.goto(url)`.
    *   Starts crawling using `super().run(url)` by calling parent class method.
    *   Saves the `crawling_context` to `self.context`.
    *  Catches and logs exceptions using `logger.critical` if an exception appears.

4. **Getting Current URL (`current_url`):**
    *  Property method that takes no parameters.
    * **Example**: `url = browser.current_url`
    *    Returns the current URL of the browser by accessing the `self.context.page.url` attribute. Returns `None` if the browser context or page is not initialized.

5.  **Getting Page Content (`get_page_content`)**:
    *    Takes no input parameters.
    *    **Example**: `content = browser.get_page_content()`
    *    Returns current page HTML content using `self.context.page.content()` or `None` if page is not initialized.

6.  **Getting Element Content by CSS Selector (`get_element_content`)**:
    *   Takes a CSS `selector` as string input.
    *   **Example**: `content = await browser.get_element_content("h1")`
    *   If `self.context` and `self.context.page` are set, it uses  `self.context.page.locator(selector)` to find the element with CSS selector.
    *   Returns inner HTML of that element using `await element.inner_html()` or `None` if element is not found.

7.  **Getting Element Value by XPath (`get_element_value_by_xpath`)**:
    * Takes a string with `xpath` as argument.
    *    **Example**: `value = await browser.get_element_value_by_xpath("//head/title")`
    *    If `self.context` and `self.context.page` are set, finds an element by using `self.context.page.locator(f'xpath={xpath}')`.
    *  Retrieves text content from element by using  `await element.text_content()`.
    *  Returns text content or None if no element found or an exception occurs during extraction.

8.  **Clicking an Element (`click_element`)**:
     *   Takes a CSS `selector` string as input parameter.
     *    **Example**: `await browser.click_element("button")`
     *   If `self.context` and `self.context.page` is set, it locates an element on page by selector, using `self.context.page.locator(selector)` and performs click action using `await element.click()` method.
     *   Logs a warning message if the element is not found or if an error occurred during the click.

9.  **Executing a Locator (`execute_locator`)**:
    *   Takes a `locator` (dict or `SimpleNamespace`), `message` and `typing_speed` as input parameters.
    *   **Example**: `result = await browser.execute_locator(locator, message="test", typing_speed=0.1)`
    *   Executes a locator using `self.executor.execute_locator` and returns the result.

## <mermaid>

```mermaid
flowchart TD
   subgraph Playwrid Class
         A[__init__ <br> (user_agent, options, *args, **kwargs)] --> B[Load Settings from JSON]
         B --> C[Set Launch Options with _set_launch_options method]
         C --> D[Initialize PlaywrightExecutor]
        D --> E[Initialize PlaywrightCrawler with browser_type and launch_options from config]
          E --> F{Does PlaywrightCrawler have `set_launch_options` method?}
        F -- Yes --> G[Set launch_options using `set_launch_options` method]
        F -- No --> H[Do nothing]
         G --> H[Return Instance of Playwrid]
        
         I[start <br> (url: str)] --> J[Log starting message]
         J --> K[Call self.executor.start()]
         K --> L[Navigate to URL using self.executor.goto()]
        L --> M[Call super().run(url)]
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
    *   The core of the module, responsible for creating and configuring the PlaywrightCrawler instance by extending crawlee's `PlaywrightCrawler` and adding more methods for interaction with page elements.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
    *  **`AM`**: The extracted text content from an element found by xpath, a return value of the `get_element_value_by_xpath` method.
    *  **`AE`**:  The extracted inner HTML of an element found by css selector, return value of the `get_element_content` method.
     *    **`X`**: The HTML page content from `context.page.content()`, the return value of the `get_page_content` method.
     *   **`S`**:  String representing current URL, the return value of the `current_url` property method.
     *   **`AW`**: Result of the locator execution which is returned by `execute_locator` method.
    *   **`O`**: Represents start of crawling using `start` method.
    *    **`H`**: Represents correctly initialized object of `Playwrid` after all settings are loaded and applied.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`asyncio`**:  Used for asynchronous programming.
*   **`pathlib.Path`**: Used for handling file paths, specifically to locate `playwrid.json` file using `Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')`.
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations to enhance code clarity.
*   **`types.SimpleNamespace`**: Used for creating simple namespace objects, used to load settings from a json file.
*   **`crawlee.playwright_crawler.PlaywrightCrawler`, `crawlee.playwright_crawler.PlaywrightCrawlingContext`**: Imports the `PlaywrightCrawler` and `PlaywrightCrawlingContext` classes from the `crawlee` library.
*    **`src`**: Used to import the global settings object `gs` from the `src` package.
*   **`src.webdriver.playwright.executor import PlaywrightExecutor`**: Used to import `PlaywrightExecutor` to execute commands on a web page.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` helper for executing javascript in the browser context.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from JSON file with `j_loads_ns` function.
*   **`src.logger.logger import logger`**: Used for logging messages, errors, warnings and information using custom logger.
*   **`import header`**: Imports the `header.py` module, to setup project environment.

**Classes:**

*  **`Playwrid(PlaywrightCrawler)`**:
    *   **Purpose**: Extends `PlaywrightCrawler` class with added functionalities, including simplified configuration from json files and providing additional methods to interact with web pages.
    *   **Attributes**:
        *   `driver_name` (`str`): String that holds the name of the driver, set to `playwrid`.
        *    `base_path` (`Path`): Path to the directory where settings file is located.
        *  `config` (`SimpleNamespace`): Settings loaded from `playwrid.json` using a simple namespace.
        *  `context` (`Optional[PlaywrightCrawlingContext]`): Object that saves crawling context when start method was called, to allow using methods from playwright in this class.
    *   **Methods**:
        *    `__init__(self, user_agent, options, *args, **kwargs)`: Initializes the `Playwrid` instance with specified parameters by loading config from json and setting browser launch options and calling parent `__init__` method.
        *   `_set_launch_options(self, user_agent, options)`:  Creates launch options dictionary by using parameters passed to the class and by loading settings from config.
         *   `start(self, url)`: Starts the crawling from specified url.
        *    `current_url(self)`: A property to get current URL.
        *  `get_page_content(self)`: Gets the HTML content of the current page.
        *    `get_element_content(self, selector)`: Gets the inner html content of a web element using the specified css selector.
        *    `get_element_value_by_xpath(self, xpath)`:  Gets text content of the web element specified by xpath expression.
        *   `click_element(self, selector)`: Clicks an element using the specified css selector.
         *  `execute_locator(self, locator, message, typing_speed)`: Executes locator on the page using `PlaywrightExecutor` class.

**Functions:**

*   **`__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *    `user_agent` (`Optional[str]`, default is `None`):  User agent string.
        *    `options` (`Optional[List[str]]`, default is `None`):  List of options for browser.
        *   `*args`, `**kwargs`: Additional arguments passed to the parent's constructor.
    *   **Purpose**:  Initializes the `Playwrid` object with specified parameters by loading config and setting up browser options.
    *   **Return**: `None`.
*   **`_set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]`**:
    *   **Arguments**:
         *  `user_agent` (`Optional[str]`, default is `None`): User agent string.
        *  `options` (`Optional[List[str]]`, default is `None`): Options list.
    *   **Purpose**:  Sets launch options from configurations, using parameters or by loading config from json.
    *   **Return**: `Dict[str, Any]` which represent launch options.
*   **`start(self, url: str) -> None`**:
    *   **Arguments**: `url` (`str`): Url to start crawling from.
    *   **Purpose**: Starts the playwright instance, navigates to url using executor and calls `run` method.
    *   **Return**: `None`.
*  **`current_url(self) -> Optional[str]`**:
    *   **Arguments**: `self` (instance of `Playwrid` class).
    *  **Purpose**:  Gets the current URL of the browser window if it is set.
    *  **Return**: `Optional[str]`, returns the url or `None`.
*   **`get_page_content(self) -> Optional[str]`**:
    *   **Arguments**: `self` (instance of `Playwrid` class).
    *   **Purpose**: Gets the HTML content of the current page, if the page is loaded.
    *   **Return**: `Optional[str]`, returns string with HTML content or `None`.
*   **`get_element_content(self, selector: str) -> Optional[str]`**:
    *   **Arguments**: `selector` (`str`): CSS selector to locate the element.
    *   **Purpose**: Returns inner HTML of an element on page.
    *   **Return**: `Optional[str]`, element content as string, or `None` if element not found.
*  **`get_element_value_by_xpath(self, xpath: str) -> Optional[str]`**:
    *  **Arguments**: `xpath` (`str`):  XPath expression to locate an element on the page.
    *    **Purpose**: Returns the text content of an element found by xpath expression.
    *    **Return**: `Optional[str]`, text content of found element, or `None`.
*   **`click_element(self, selector: str) -> None`**:
    *   **Arguments**: `selector` (`str`): CSS selector to locate the element on the page.
    *   **Purpose**:  Clicks the specified element on the page using CSS selector.
    *   **Return**: `None`.
*    **`execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool`**:
    *  **Arguments**:
          * `locator` (`dict | SimpleNamespace`):  Locator object which is used to find element on page.
         *   `message` (`Optional[str]`, default is `None`): Optional message parameter, that can be passed to `send_message` or `execute_event`.
         *   `typing_speed` (`float`, default is `0`): Optional parameter for typing speed when sending messages.
    *   **Purpose**: Executes a locator using `PlaywrightExecutor` and returns the result.
    *    **Return**:  `str | List[str] | bytes | List[bytes] | bool`, that represents a result of execution of the locator.

**Variables:**

*  `driver_name` (`str`): Stores the name of the driver which is set to `"playwrid"`.
*   `base_path` (`Path`):  Path where the `playwrid.json` is located, using `gs` object for paths.
*   `config` (`SimpleNamespace`): Object, which holds configuration settings loaded from the json file.
*  `context` (`Optional[PlaywrightCrawlingContext]`): Object that holds current crawling context from playwright library.
*   `user_agent` (`str`): String that represents the user agent value.
*   `options` (`List[str]`): List of string with browser options.
*  `launch_options` (`Dict[str, Any]`): Dictionary that stores all combined launch options.
*   `url` (`str`): URL string for navigation.
*    `selector` (`str`): String containing a CSS selector.
*   `xpath` (`str`): String containing xpath expression.
*  `message` (`str`):  Message to send to the element.
*   `typing_speed` (`float`): Value that defines typing speed.
*  `element` (`Locator`): Locator object from playwright to perform actions on.
* `data` (`Dict[str, Any]`):  Dictionary with scraped data.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: The `j_loads_ns` call to load settings could have more specific error handling to catch json parsing errors.
*   **Hardcoded Paths**: The path to the `playwrid.json` file is hardcoded and can be improved using `gs.path` for building paths.
*  **Configuration Handling**: The `_set_launch_options` can be more flexible and use more parameters to setup browser from the config.
*  **Error Handling**: Error handling could be improved by adding more verbose logging.
*   **Type Hinting**: Some parameters and variables can have more specific type hints, for example, instead of `Optional[str]` a `str | None` type can be used for more clarity.
* **Data Extraction**: The methods for data extraction are very basic, and can be extended by allowing to pass a list of elements for extraction.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package, and specifically `src.webdriver.playwright`.
*   It relies on `crawlee` library to implement crawling workflow.
*    It uses `src.utils.jjson` to load the configuration from a json file.
*   It uses the `PlaywrightExecutor` class from `src.webdriver.playwright.executor`.
*   It uses `src.webdriver.js` to provide javascript execution.
*   It also imports the global settings object `gs` from `src` package.
*   It uses the logger from `src.logger.logger` to log all errors and info messages.
*    It also imports `header` module to determine the project root.

This detailed explanation provides a comprehensive understanding of the `playwrid.py` module, including its functionalities, structure, and interactions with other components in the project.