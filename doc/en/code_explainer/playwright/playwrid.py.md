## <algorithm>

### Workflow of the Playwright Crawler Module

This document describes the functionality of the Playwright Crawler module, focusing on the `Playwrid` class, its initialization, and methods for web page interaction.

1.  **Initialization (`__init__`)**:
    *   The `Playwrid` class is initialized with optional parameters, including `user_agent` and `options`.
    *   **Example**: `browser = Playwrid(user_agent='custom_user_agent', options=['--headless'])`
    *   Sets the `driver_name` attribute to `'playwrid'`.
    *   Defines `base_path` and loads settings from `playwrid.json` into `self.config` using `j_loads_ns`.
    *  Calls the `_set_launch_options` method with `user_agent` and `options` to prepare `launch_options` for playwright.
    *   Initializes the `PlaywrightExecutor` instance, which handles locator execution.
    *   Initializes the parent class `PlaywrightCrawler`, passing parameters from the `self.config` (specifically `browser_type`) and other parameters passed to `__init__`, it also ignores `launch_options` in `super().__init__()` call, as it might not be supported by this class.
    *    If the `PlaywrightCrawler` instance has attribute `set_launch_options`, it will call it with `launch_options`, if that method is not available it will be ignored.

2.  **Setting Launch Options (`_set_launch_options`)**:
    *   Takes `user_agent` (`Optional[str]`) and `options` (`Optional[List[str]]`) as input parameters.
    *  **Example**: `launch_options = self._set_launch_options(user_agent, options)`
    *   It prepares a dictionary with launch options for playwright.
        *   Sets `headless` attribute from config or defaults to `True`.
        *  Sets browser `args` from config or default to empty list.
    *   If a custom `user_agent` is provided, adds it to launch options.
    *   Merges the custom options provided during initialization to the default options, that are loaded from `playwrid.json` and stores results into the  `launch_options` dictionary.
    *   Returns `launch_options` dictionary with merged configurations.

3.  **Starting Crawler (`start`)**:
    *   Takes a `url` string to start crawling from as input.
    *   **Example**: `await browser.start("https://www.example.com")`
    *   Logs a starting message using logger.
    *   Calls `self.executor.start()` to initialize Playwright.
    *   Navigates to the specified URL using  `self.executor.goto(url)`.
    *   Runs crawler using `super().run(url)`, using parent class `run` method.
    *    Saves the `crawling_context` to `self.context` attribute.
    *   Handles exceptions during startup logging critical error message with `logger.critical`.

4.  **Getting Current URL (`current_url`):**
    *  Property method that takes no parameters.
    *  **Example**: `url = browser.current_url`
    *   Retrieves the current URL from the `self.context.page` if `self.context` and  `self.context.page` are not `None`.
    *   Returns the URL string, or returns `None` if not available.

5.  **Getting Page Content (`get_page_content`)**:
    *   Takes no input parameters.
    *   **Example**: `html = browser.get_page_content()`
    *   Retrieves HTML content of current page, by using `self.context.page.content()` and returns it as a string, otherwise returns `None` if `self.context` or  `self.context.page` is not initialized.

6.  **Getting Element Content by CSS Selector (`get_element_content`)**:
    *  Takes a `selector` (`str`), which represents a CSS selector for element lookup.
    *   **Example**: `element_content = await browser.get_element_content("h1")`
    *   If `self.context` and `self.context.page` are set, locates the element using `self.context.page.locator(selector)`.
    *    Retrieves the inner HTML using `await element.inner_html()`.
    *   Returns the inner HTML content of found element as a string, or `None` if no element was found or if there is an exception.

7.  **Getting Element Value by XPath (`get_element_value_by_xpath`)**:
    *   Takes an `xpath` string, as a parameter, which is used to locate an element on the page.
    *   **Example**: `value = await browser.get_element_value_by_xpath("//head/title")`
    *  If `self.context` and `self.context.page` are set, locates the element using xpath expression with  `self.context.page.locator(f'xpath={xpath}')`.
    *   Retrieves text content from the found element using `await element.text_content()` method.
    *   Returns extracted text or `None` if no element found or if an error was raised.

8.  **Clicking an Element (`click_element`)**:
    *    Takes a `selector` string, representing a CSS selector to the element to click.
    *   **Example**: `await browser.click_element("button")`
    *    If `self.context` and `self.context.page` are set, locates element using CSS selector and performs click with `await element.click()` method.
    *   Logs a warning if element was not found, or if an error occurred during the click action.

9.  **Executing Locator (`execute_locator`)**:
    * Takes a `locator` object (which can be a `dict` or a `SimpleNamespace`) and optional `message` and `typing_speed`.
    * **Example**: `result = await browser.execute_locator(locator, message="test", typing_speed=0.1)`
    *   Calls the `execute_locator` method from the `PlaywrightExecutor` instance and returns it's result.

## <mermaid>

```mermaid
flowchart TD
    subgraph Playwrid Class
        A[__init__ <br> (user_agent, options, *args, **kwargs)] --> B[Load Settings from JSON]
        B --> C[Set Launch Options with _set_launch_options method]
        C --> D[Initialize PlaywrightExecutor]
        D --> E[Initialize PlaywrightCrawler with launch_options]
        E --> F[Call set_launch_options if present in PlaywrightCrawler]
         F --> G
          G --> H[Instance of Playwrid]
         
        I[start <br> (url: str)] --> J[Log starting message]
         J --> K[Call self.executor.start()]
        K --> L[Call self.executor.goto(url)]
          L --> M[Call super().run(url)]
           M --> N[Save the crawling context to self.context]

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
       AH:::global
       
        O:::global
    end
```

### Dependencies Analysis:

1.  **`Playwrid Class`**:
    *   The core of the module, extending the `PlaywrightCrawler` and integrating it with configurations from `playwrid.json`, and provides methods for interacting with web pages using Playwright library.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
     *   **`AM`**: String with text content of the found element, the return value of the `get_element_value_by_xpath` method.
     *   **`AE`**:  String with inner html content of found element, a return value of the `get_element_content` method.
     *  **`X`**: String with content of page, return value of method `get_page_content`.
    *   **`S`**: String representing current url of the page, a return value of property method `current_url`.
     *  **`AW`**: Result of the locator execution, the return value of `execute_locator` method.
      *  **`AH`**: The start point of xpath lookup , check in `get_element_value_by_xpath` method.
      *  **`O`**: Represents the start point of fetching page content, and executing all actions related to playwright, the return of `start` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`asyncio`**: Used for asynchronous operations, specifically to start crawler with `asyncio.run`.
*   **`pathlib.Path`**: Used for handling file paths, creating a Path object from a configuration file with `Path(gs.path.src / 'webdriver' / 'playwright' / 'playwrid.json')`.
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations, improving code clarity and maintainability.
*    **`types.SimpleNamespace`**: Used for creating simple namespace objects, specifically to store configuration from `playwrid.json` file.
*   **`crawlee.playwright_crawler.PlaywrightCrawler`, `crawlee.playwright_crawler.PlaywrightCrawlingContext`**:  Used for web crawling with `PlaywrightCrawler` class, and its context.
*  **`src`**: Used to import global settings object `gs` from the `src` package.
*   **`src.webdriver.playwright.executor import PlaywrightExecutor`**: Imports the `PlaywrightExecutor` class for performing actions on the web page.
*   **`src.webdriver.js import JavaScript`**: Imports `JavaScript` class, for executing javascript code on the page.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file using `j_loads_ns()`.
*   **`src.logger.logger import logger`**: Used for logging information, warnings, and errors.
*    **`import header`**: Imports custom module `header.py`

**Classes:**

*   **`Playwrid(PlaywrightCrawler)`**:
    *   **Purpose**: Extends `PlaywrightCrawler` with additional functionalities such as the ability to set custom browser settings, profiles, and launch options using Playwright.
    *   **Attributes**:
        *   `driver_name` (`str`): Stores driver name which is set to `"playwrid"`.
        *  `base_path` (`Path`):  Defines base path to locate `playwrid.json`.
        *  `config` (`SimpleNamespace`):  Stores settings loaded from `playwrid.json`.
        *  `context` (`Optional[PlaywrightCrawlingContext]`):  Stores current crawling context.
    *   **Methods**:
        *   `__init__(self, user_agent, options, *args, **kwargs)`: Initializes the `Playwrid` instance with custom launch options.
        *   `_set_launch_options(self, user_agent, options)`: Configures the launch options, including handling of user agent and custom options from configuration.
        *  `start(self, url)`: Starts the crawler from a provided URL and sets `crawling_context`.
        *  `current_url(self)`: Returns current url of the page.
        *   `get_page_content(self)`: Returns HTML content of the page.
        *   `get_element_content(self, selector)`: Gets inner HTML of an element by css selector.
        *  `get_element_value_by_xpath(self, xpath)`: Gets text content of an element using xpath.
        *   `click_element(self, selector)`: Clicks an element using provided CSS selector.
         *  `execute_locator(self, locator, message, typing_speed)`: Executes a locator on the page and returns the result.

**Functions:**

*   **`__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None`**:
    *  **Arguments**:
        *  `user_agent` (`Optional[str]`, default: `None`): User agent string.
        *   `options` (`Optional[List[str]]`, default: `None`): List of options.
        *   `*args`, `**kwargs`: Additional arguments for `PlaywrightCrawler` constructor.
    *   **Purpose**: Initializes `Playwrid` object, loading configurations and setting up the `PlaywrightCrawler` instance.
    *   **Return**: `None`.
*  **`_set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]`**:
    *    **Arguments**:
         * `user_agent` (`Optional[str]`, default: `None`):  User agent string.
         * `options` (`Optional[List[str]]`, default: `None`): Options list.
    *   **Purpose**: Configures the launch options for Playwright, taking user-agent and options from class attributes and methods parameters, and returns dictionary with merged options.
    *   **Return**:  A dictionary with launch options.
*   **`start(self, url: str) -> None`**:
     *   **Arguments**: `url` (`str`): The URL to start crawling from.
     *  **Purpose**: Initializes the `PlaywrightExecutor`, navigates to the URL and starts crawling using a `PlaywrightCrawler`.
     *   **Return**: `None`.
*    **`current_url(self) -> Optional[str]`**:
    *   **Arguments**: `self` (instance of the `Playwrid` class).
    *   **Purpose**: Returns current URL from `self.context.page` if the context and page is set, or returns `None`.
    *   **Return**: `Optional[str]` , URL of current page or `None` if page is not loaded yet.
*   **`get_page_content(self) -> Optional[str]`**:
    *   **Arguments**: `self` (instance of `Playwrid` class).
    *   **Purpose**: Returns the HTML content of the current page.
    *   **Return**: `Optional[str]`, the page content as a string, or `None` if page was not loaded yet.
*   **`get_element_content(self, selector: str) -> Optional[str]`**:
    *    **Arguments**: `selector` (`str`): A CSS selector to locate the element on the page.
    *    **Purpose**: Retrieves the inner HTML content of the located web element using a CSS selector.
    *    **Return**: `Optional[str]` string containing the inner HTML of the element or `None` if not found.
*  **`get_element_value_by_xpath(self, xpath: str) -> Optional[str]`**:
    *    **Arguments**: `xpath` (`str`): XPath of the element to look for.
    *   **Purpose**:  Retrieves text content from the web element using XPath.
    *   **Return**: `Optional[str]`, a string with inner text content, or `None` if not found.
*  **`click_element(self, selector: str) -> None`**:
    *   **Arguments**: `selector` (`str`): A CSS selector that specifies which element should be clicked.
    *   **Purpose**: Clicks the specified element on the page using CSS selector.
    *   **Return**: `None`.
*    **`execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool`**:
     *    **Arguments**:
        *  `locator` (`dict | SimpleNamespace`): A dictionary or SimpleNamespace object that defines the locator parameters.
        *    `message` (`Optional[str]`, default: `None`): Optional parameter to pass message to `execute_event` or `send_message` method.
        *  `typing_speed` (`float`, default: `0`): Optional parameter to specify the typing speed.
    *   **Purpose**: Execute a locator on the page with playwright using `PlaywrightExecutor` and returns the result.
    *   **Return**: `str | List[str] | bytes | List[bytes] | bool`, which represents a result of the execution.

**Variables:**

*   `driver_name` (`str`): Stores driver name which is set to `playwrid`.
*   `base_path` (`Path`): Stores the base path where `playwrid.json` is located.
*    `config` (`SimpleNamespace`): Stores settings from `playwrid.json` using SimpleNamespace object.
*   `context` (`PlaywrightCrawlingContext`): Stores current `crawling_context` if crawling is started.
*  `user_agent` (`str`): String for setting custom user agent.
*   `options` (`List[str]`): List of options for playwright browser.
*   `launch_options` (`Dict[str, Any]`): Dictionary with combined launch options.
*   `url` (`str`): String representing the URL.
*  `selector` (`str`): String containing CSS selector.
*   `xpath` (`str`): String containing xpath expression.
* `element` (`playwright.Locator`): Element object from playwright for performing actions on it.
* `message` (`str`): String containing message that should be sent to a web element.
* `typing_speed` (`float`): Value representing the typing speed for sending a message.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: There is no error handling when `j_loads_ns` fails to load the `playwrid.json` file. Add error handling for configuration loading.
*   **Type Hinting**: Some variables and methods can benefit from more precise type hints.
*   **Inconsistent Naming**: The variable name `Playwrid` in the class declaration and module name is slightly different from `Playwright`, which may cause confusion.
*   **Limited Functionality**: The module has limited functionality, and could benefit from more methods for easier access to different playwright API features.
*  **Error Handling**: Error handling is very basic. Add better logging with specific error messages, for various stages, when performing actions, or navigating to URL, etc.
*    **Missing configuration for Playwright**: `PlaywrightCrawler` initialization is hardcoded, use settings file to define all available parameters.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package, which is intended for web automation and data extraction.
*   It uses the `crawlee.playwright_crawler.PlaywrightCrawler` library for web crawling.
*  It also uses  `src.webdriver.playwright.executor` module for executing locators using playwright.
*   It interacts with `src.webdriver.js` to execute javascript.
*    It imports the settings from  `src.utils.jjson` using `j_loads_ns`.
*   It uses `src.logger.logger` for logging.
*    It utilizes global settings object `gs` from `src` package.
*  It also imports  `header` module.

This detailed explanation provides a comprehensive understanding of the `playwrid.py` module, including its functionalities and its relationships with other components in the project.