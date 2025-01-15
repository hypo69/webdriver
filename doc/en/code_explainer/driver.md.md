## <algorithm>

### Workflow of `driver.py` Module

1.  **Initialization (`__init__`)**:
    *   **Input**: `webdriver_cls` (WebDriver class like `Chrome`, `Firefox`), `*args`, `**kwargs` for WebDriver initialization.
    *   **Process**:
        *   Checks if `webdriver_cls` has a `get` method, raising a `TypeError` if not, ensuring a valid WebDriver.
        *   Initializes WebDriver using `webdriver_cls(*args, **kwargs)` assigning it to `self.driver`.
        *   **Example**: `Driver(Chrome, executable_path='/path/to/chromedriver')` initializes a Chrome WebDriver.
    *   **Output**: A `Driver` object with the WebDriver instance.

2.  **Subclass Initialization (`__init_subclass__`)**:
    *   **Input**: `browser_name` (string for browser name), `**kwargs`.
    *   **Process**:
        *   Ensures `browser_name` is specified, raises `ValueError` if not.
        *   Sets `browser_name` as an attribute of the subclass.
        *   **Example**: When a class `ChromeDriver(Driver, browser_name='chrome')` is created.
    *   **Output**: Subclass of `Driver` with `browser_name` set.

3.  **Attribute Access (`__getattr__`)**:
    *   **Input**: `item` (attribute name).
    *   **Process**:
        *   Accesses the attribute of the underlying WebDriver using `getattr(self.driver, item)`.
        *    **Example**: `driver.title` will return `driver.driver.title`.
    *   **Output**: Value of the requested attribute.

4.  **Scrolling (`scroll`)**:
    *   **Input**: `scrolls`, `frame_size`, `direction` ('both', 'forward', 'backward', 'up', 'down'), `delay`.
    *   **Process**:
        *   Defines nested `carousel` function to perform scrolling using `window.scrollBy()` with a direction and size.
        *   Determines scroll direction based on the `direction` parameter, calling `carousel` with appropriate arguments.
        *   Handles exceptions during scrolling and logs errors using the `logger`.
        *   **Example**: `driver.scroll(scrolls=2, direction='both', frame_size=300)` will scroll down and up two times with 300px frames.
    *   **Output**: `True` for successful scrolling, `False` for errors.

5.  **Locale Detection (`locale`)**:
    *   **Input**: None.
    *   **Process**:
        *   Attempts to extract the language from `meta` tags by finding an element using a CSS selector.
        *   If the meta tag is not found it tries to get it using the method `self.get_page_lang()`.
        *   Logs errors if retrieval fails, returning `None` if no language can be found.
         *   **Example**: Extracts page language from a meta tag or JavaScript.
    *   **Output**: Language code or `None` if the language cannot be detected.

6.  **URL Navigation (`get_url`)**:
    *   **Input**: `url`.
    *   **Process**:
        *   Copies the current URL to `_previous_url` before navigation.
        *   Navigates to `url` using `self.driver.get(url)`.
        *   Waits for the page to be fully loaded.
        *   Updates `self.previous_url` if navigation resulted in a URL change.
        *   Saves cookies using `self._save_cookies_localy()`.
        *   Handles exceptions: `WebDriverException`, `InvalidArgumentException`, logging all errors.
        *   **Example**: `driver.get_url('https://example.com')` will navigate to the specified page.
    *   **Output**: `True` on success, `False` on failure.

7.  **Opening New Tab (`window_open`)**:
    *   **Input**: Optional `url`.
    *   **Process**:
        *   Opens a new tab via `window.open()` JavaScript.
        *   Switches the driver context to the new tab using its handle from `self.window_handles`.
        *   Navigates to `url` if provided using `self.get(url)`.
        *   **Example**: `driver.window_open('https://example.com')` will open a new tab and navigate to this url.
    *   **Output**: None.

8.  **Waiting (`wait`)**:
    *   **Input**: `delay`.
    *   **Process**:
        *   Pauses execution for `delay` seconds using `time.sleep(delay)`.
        *    **Example**: `driver.wait(2)` pauses execution for 2 seconds.
    *   **Output**: None.

9.  **Saving Cookies Locally (`_save_cookies_localy`)**:
    *   **Input**: None.
    *   **Process**:
        *   It is currently set to `return True` as a debug measure.
        *   The intention is to save cookies from `self.driver` by using pickle serialization to a file path specified in `gs.cookies_filepath`.
        *   Error logging for any exception using the `logger`.
        *  **Example**:  Will serialize cookies to a file (if not in debug mode).
    *   **Output**: None.

10. **Fetching HTML (`fetch_html`)**:
    *   **Input**: `url`.
    *   **Process**:
        *   Determines the protocol of the `url`:
            *   `file://`: Extracts local file path, checks if the file exists, reads content, stores it in `self.html_content`.
            *   `http://` or `https://`: Navigates to the URL using `self.get_url`, saves page source to `self.html_content`.
            *    Logs and returns `False` for any errors, or unsupported protocols.
    *   **Output**: `True` for success, `False` otherwise.

## <mermaid>

```mermaid
flowchart TD
    subgraph Driver Class
        A[__init__ <br> (webdriver_cls, *args, **kwargs)] --> B{Valid WebDriver Class?}
        B -- Yes --> C[Initialize WebDriver <br> self.driver]
        B -- No --> D[Raise TypeError]
        C --> E[Instance of Driver]
        D --> E
        
        F[__init_subclass__ <br> (browser_name, **kwargs)] --> G{browser_name Provided?}
        G -- Yes --> H[Set browser_name Attribute]
        G -- No --> I[Raise ValueError]
        H --> J[Subclass with browser_name]
        I --> J
        
        K[__getattr__ <br> (item)] --> L[Get Attribute from self.driver]
        L --> M[Attribute Value]

        N[scroll <br> (scrolls, frame_size, direction, delay)] --> O{direction?}
        O -- forward/down --> P[carousel<br> (direction:'', scrolls, frame_size, delay)]
        O -- backward/up --> Q[carousel<br> (direction='-', scrolls, frame_size, delay)]
        O -- both --> R[carousel <br> (direction:'', scrolls, frame_size, delay) AND carousel<br> (direction='-', scrolls, frame_size, delay)]
        P --> S[Scroll the Page]
        Q --> S
        R --> S
        S --> T[Return Status of scrolling]

        U[locale] --> V[Find Meta Language Element]
        V --> W{Meta Language Found?}
        W -- Yes --> X[Get Content Attribute]
        W -- No --> Y[get_page_lang()]
        X --> Z[Return Language]
        Y --> Z
        Z --> AA[Language or None]

        AB[get_url <br> (url)] --> AC[Copy current_url]
        AC --> AD[Navigate to url using self.driver.get()]
        AD --> AE[Wait for ready_state to complete]
        AE --> AF{URL changed?}
        AF -- Yes --> AG[Update previous_url]
        AF -- No --> AH
        AG --> AH[Save Cookies]
        AH --> AI[Return True]
        
        AJ[window_open <br> (url)] --> AK[Execute JavaScript window.open()]
        AK --> AL[Switch to New Tab]
        AL --> AM{URL is set?}
        AM -- Yes --> AN[Navigate to URL]
        AM -- No --> AO
        AN --> AO
        AO --> AP

        AQ[wait <br> (delay)] --> AR[Wait for delay seconds]
        AR --> AS

        AT[_save_cookies_localy] --> AU[Save cookies locally]
        AU --> AV

        AW[fetch_html <br> (url)] --> AX{URL Protocol?}
        AX -- file:// --> AY[Read content from file]
        AX -- http/https --> AZ[Navigate to URL and fetch content]
        AX -- other --> BA[Error: Unsupported Protocol]
        AY --> BB[Return HTML content or None]
        AZ --> BB
        BA --> BB
    end
    
    
    subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
        
        BB:::global
        Z:::global
        AI:::global
        AP:::global
        AS:::global
        AV:::global
        T:::global
        M:::global
        J:::global
        E:::global
    end

```

### Dependencies Analysis:

1.  **`Driver Class`**: The core of the module, responsible for all driver-related actions. It initializes, configures and manages the WebDriver object, providing methods for navigation, scrolling, and more.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *   **`BB`**: Result of fetching HTML content, essential for parsing web page content or file, a return value of function `fetch_html`.
    *   **`Z`**: Detected page language, useful for localization, return value of function `locale`.
    *   **`AI`**: Boolean, result of navigation operations, return value of function `get_url`.
    *   **`AP`**: Representing new tab opening actions, return value of function `window_open`.
    *   **`AS`**: Represents the waiting process for the defined time, return value of function `wait`.
    *   **`AV`**: Represents cookie saving actions, return value of function `_save_cookies_localy`.
    *   **`T`**: Boolean result of scrolling operations, return value of function `scroll`.
    *    **`M`**: The proxied result of a driver attribute call (e.g., `driver.title`), return value of `__getattr__`.
    *  **`J`**: Represents a correctly initialized subclass of `Driver` return value of  `__init_subclass__`.
    *  **`E`**: Represents a correctly initialized instance of `Driver`, return value of `__init__`.

## <explanation>

### Imports:

*   **`from selenium.webdriver.remote.webdriver import WebDriver`**: Imports `WebDriver` from Selenium, used for type hinting and as a base class for the implemented Driver class.
*   **`from selenium.common.exceptions import WebDriverException, InvalidArgumentException`**: Imports specific exceptions for handling Selenium errors (e.g., navigation issues or invalid arguments).
*   **`from selenium.webdriver.common.by import By`**: Imports `By` for locating elements using CSS selectors, etc.
*   **`from src.logger.logger import logger`**: Imports a custom logger from within the project, for uniform error logging.
*   **`import time`**: Used for adding delays to code execution using `time.sleep()`.
*   **`from pathlib import Path`**: Facilitates handling of file paths and file operations.
*   **`import re`**: Imports the regular expression module for pattern matching within HTML and filepaths.
*   **`import pickle`**: Enables object serialization, for saving cookies, is disabled in debug mode.
*  **`import copy`**: Used to create a copy of the current URL to track navigation history.
*   **`from typing import Optional`**: Used to handle optional types (values that may be None).
*    **`from src import gs`**: Imports global settings from `src.gs`, specifically `gs.cookies_filepath` for the cookie file location.

### Classes:

*   **`Driver`**:
    *   **Role**: A wrapper around Selenium `WebDriver`. It is designed to provide a single point to manage all web driver functionalities.
    *   **Attributes**:
        *   `self.driver`: The Selenium `WebDriver` instance.
        *   `self.previous_url`: Stores the URL from the previous navigation.
        *    `self.html_content`: String holding html source of current page.
    *   **Methods**:
        *   `__init__(self, webdriver_cls, *args, **kwargs)`: Initializes the `Driver` instance with a WebDriver class and its parameters.
        *   `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Automatically called when subclassing `Driver`, to set the browser name.
        *   `__getattr__(self, item)`: Proxies access to attributes of the wrapped `WebDriver` instance.
        *   `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`: Scrolls the web page up, down, or both.
        *   `locale(self) -> Optional[str]`: Detects the page language from the meta tag or using JavaScript.
        *   `get_url(self, url: str) -> bool`: Navigates to a given URL, also handles saving of cookies.
        *   `window_open(self, url: Optional[str] = None) -> None`: Opens a new browser tab, optionally navigating to a URL.
        *    `wait(self, delay: float = .3) -> None`: Pauses the script execution for specified `delay` in seconds.
        *   `_save_cookies_localy(self) -> None`: Saves the current cookies to a file (debug mode).
        *   `fetch_html(self, url: str) -> Optional[bool]`: Fetches HTML content from local file or a web URL.

### Functions:

*   **`carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool`** (nested in `scroll`): Helper function to execute scroll actions using JavaScript code (`window.scrollBy`).
    *   **Arguments**: `direction`, `scrolls`, `frame_size`, `delay`.
    *   **Returns**: `True` on successful scroll, `False` on error.
*   **`__init__(self, webdriver_cls, *args, **kwargs)`**: Class constructor for `Driver`, sets up the `WebDriver` instance.
    *   **Arguments**: `webdriver_cls`, `*args`, `**kwargs`.
    *   **Returns**: None.
*    **`__init_subclass__(cls, *, browser_name=None, **kwargs)`**: Method is automatically invoked when a subclass is created, setting the browser name for each specific driver type.
    *   **Arguments**: `browser_name`, `**kwargs`
    *   **Returns**: None
*    **`__getattr__(self, item)`**: Method allows accessing attributes of the underlying `WebDriver` object.
    *   **Arguments**: `item` (attribute name)
    *  **Returns**: Attribute value.
*   **`scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`**: Scrolls the web page up, down, or both.
    *   **Arguments**: `scrolls` (int), `frame_size` (int), `direction` (str), `delay` (float).
    *   **Returns**: `True` if scrolling is successful, `False` otherwise.
*   **`locale(self) -> Optional[str]`**: Detects the language from meta tags or JavaScript.
    *   **Arguments**: None.
    *   **Returns**: Language code (`str`) or `None` if not found.
*   **`get_url(self, url: str) -> bool`**: Navigates the browser to given `url`.
    *   **Arguments**: `url` (str).
    *   **Returns**: `True` for success, `False` for failure.
*   **`window_open(self, url: Optional[str] = None) -> None`**: Opens a new tab in the browser.
    *   **Arguments**: `url` (optional string of the URL).
    *   **Returns**: None.
*  **`wait(self, delay: float = .3) -> None`**: Pauses script execution for `delay` seconds.
    *  **Arguments**: `delay` (float) number of seconds to wait.
    *  **Returns**: None.
*   **`_save_cookies_localy(self) -> None`**: Intended to save current cookies locally (currently in debug mode).
    *   **Arguments**: None.
    *   **Returns**: None.
*   **`fetch_html(self, url: str) -> Optional[bool]`**: Fetches HTML content from a local file or from a web URL.
    *   **Arguments**: `url` (str).
    *   **Returns**: `True` on success, `False` otherwise.

### Variables:

*   `self.driver`:  An instance of the Selenium `WebDriver`.
*   `self.previous_url`: String holding the previously visited URL.
*   `self.html_content`: String holding html source of current page.
*   `webdriver_cls`: WebDriver class for initialization (e.g., `Chrome` or `Firefox`).
*   `*args`, `**kwargs`: Positional and keyword arguments for the WebDriver constructor.
*   `item`: String holding the attribute name.
*   `scrolls`: Integer number of scroll actions.
*   `frame_size`: Integer representing scroll size in pixels.
*   `direction`: String that define direction of scroll (`'both'`, `'forward'`, `'backward'`, `'up'`, `'down'`).
*   `delay`: Float, representing pause between scrolls or waits.
*   `url`: String holding URL or file path.
*   `meta_language`: Selenium web element of meta tag used for language detection.
*    `file_path`:  `Pathlib.Path` object representing a local file path.

### Potential Errors and Areas for Improvement:

*   The `_save_cookies_localy` method is currently in debug mode (`return True`), and it should be replaced with an actual implementation for saving cookies if this is desired.
*   The logic for file path verification in `fetch_html` is using a regular expression for drive letters, which can be improved using `Path.is_absolute()`.
*   The function `get_page_lang()` used to obtain page language with JavaScript is not implemented, leading to a possible error when the language cannot be extracted from meta tags.
*   The `while self.ready_state != 'complete':` loop in `get_url` might lead to infinite loops if the page doesn't complete loading.
*   The error handling in `fetch_html` could return `None` instead of `False` for more clarity in cases when error appears in reading file or fetching url.
*   The type of variable `_previous_url` in method `get_url`  is not strictly defined, which can cause potential type errors and may require additional handling.

### Chain of Relationships:

*   The `Driver` class is a part of the `src.webdriver` package, which is used for web automation and testing.
*   The class depends on `src.logger.logger` for central logging of all errors and debugging information.
*   It also depends on `src.gs` which contains global settings and file paths.
*   The code uses `selenium` library for browser automation.
*   The `fetch_html` demonstrates the ability to operate with the local file system, expanding its possibilities.