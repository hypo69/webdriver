## <algorithm>

### Workflow of the `driver.py` Module

The `driver.py` module provides a class `Driver` to interact with Selenium web drivers. Here is a step-by-step explanation of how this module works:

1.  **Initialization (`__init__`)**:
    *   The `Driver` class is instantiated with a `webdriver_cls` (e.g., `Chrome`, `Firefox`) and optional arguments (`*args`, `**kwargs`).
    *   **Example**: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`
    *   The constructor checks if the provided `webdriver_cls` has the `get` method, raising a `TypeError` if not, ensuring that it's a valid Selenium WebDriver class.
    *   If valid, the driver object is initialized: `self.driver = webdriver_cls(*args, **kwargs)`.

2.  **Subclass Initialization (`__init_subclass__`)**:
    *   When a subclass of `Driver` is created, this method is automatically called.
    *   **Example**: `class CustomDriver(Driver, browser_name='Chrome'): ...`
    *   It checks if `browser_name` is provided during subclass creation, raising a `ValueError` if missing.
    *   The `browser_name` attribute is stored in the subclass for future use: `cls.browser_name = browser_name`.

3.  **Attribute Proxy (`__getattr__`)**:
    *   When accessing an attribute of the `Driver` instance that is not directly defined in the `Driver` class, the `__getattr__` method is called.
    *   **Example**: Accessing `driver.page_source` calls `self.driver.page_source` where `driver` is instance of the `Driver` class.
    *   This method proxies the attribute access to the underlying Selenium WebDriver: `return getattr(self.driver, item)`.

4.  **Scrolling (`scroll`)**:
    *   The `scroll` method is called with parameters `scrolls`, `frame_size`, `direction`, and `delay` to scroll the page in specified direction.
    *   **Example**: `driver.scroll(scrolls=2, direction='down')`
    *   It uses a nested `carousel` function, which uses `execute_script` to perform the scrolling. It waits for the given delay between scrolls using the `wait()` method.
    *   The direction can be `'forward'`/`'down'`, `'backward'`/`'up'`, or `'both'`, determining the scroll direction.

5.  **Determining Page Language (`locale`)**:
    *   The `locale` property attempts to extract the page language from the `<meta>` tag or using JavaScript method (`get_page_lang()` which is not implemented in this code).
    *   **Example**: `lang = driver.locale`
    *   It uses `find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")` to locate the `<meta>` tag, and then extracts its `content` attribute.
    *   If a meta tag cannot be found or the JavaScript method fails, it returns `None`.

6.  **Navigating to URL (`get_url`)**:
    *   The `get_url` method navigates to the given URL by calling `self.driver.get(url)`.
    *   **Example**: `driver.get_url('https://example.com')`
    *   Before navigation, saves a copy of `current_url` using `copy.copy(self.current_url)`.
    *   It waits for the page to fully load using `while self.ready_state != 'complete':` loop.
    *   It updates the previous URL `self.previous_url` if the new URL is different from the previous one.
    *   It saves cookies locally using `self._save_cookies_localy()` after loading the page.
    *   It handles `WebDriverException`, `InvalidArgumentException`, and generic `Exception`.

7.  **Opening New Tab (`window_open`)**:
    *   The `window_open` method opens a new tab and switches the focus to it.
    *   **Example**: `driver.window_open('https://newtab.com')`
    *   It uses `execute_script('window.open();')` to open a new tab, then uses `switch_to.window(self.window_handles[-1])` to switch to that new tab. If a URL is provided, the new tab will open that URL using the `get()` method.

8.  **Waiting (`wait`)**:
    *   The `wait` method pauses execution for specified amount of time.
    *   **Example**: `driver.wait(2)`
    *   It calls `time.sleep(delay)` to introduce a delay.

9.  **Saving Cookies Locally (`_save_cookies_localy`)**:
    *   The `_save_cookies_localy` method saves the cookies to a file defined in `gs.cookies_filepath`.
    *   **Example**: `driver._save_cookies_localy()`
    *   It uses `pickle.dump()` to save cookies.
    *   The method is currently stubbed with `return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`.

10. **Fetching HTML Content (`fetch_html`)**:
    *   The `fetch_html` method gets the HTML content from a specified URL (either local file or HTTP/HTTPS).
    *   **Example**: `driver.fetch_html('file:///path/to/local.html')` or `driver.fetch_html('https://example.com')`
    *   It checks if the URL is a local file or a web address.
    *   For a local file, it opens the file and reads its content and saves to `self.html_content`.
    *   For a web address, it navigates to the URL by calling `get_url()` and gets the `page_source`.
    *   It handles exceptions and logs errors if fails to read or load the page.

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> InitDriver[Initialize Driver: <br><code>Driver(webdriver_cls, *args, **kwargs)</code>]
    InitDriver --> CheckWebDriver[Check if <br><code>webdriver_cls</code> is valid]
    CheckWebDriver -- Yes --> CreateWebDriver[Create driver instance <br><code>self.driver = webdriver_cls(*args, **kwargs)</code>]
    CheckWebDriver -- No --> TypeError[Raise TypeError]
    CreateWebDriver --> SubclassInit[Subclass Initialization: <br><code>__init_subclass__</code>]
    SubclassInit --> CheckBrowserName[Check if <br><code>browser_name</code> is specified]
    CheckBrowserName -- Yes --> SetBrowserName[Set browser name: <br><code>cls.browser_name = browser_name</code>]
    CheckBrowserName -- No --> ValueError[Raise ValueError]
    SetBrowserName --> AttributeProxy[Access Attribute: <br><code>__getattr__(self, item)</code>]
    AttributeProxy --> GetDriverAttribute[Get attribute from <br><code>self.driver</code>]
    GetDriverAttribute --> ScrollPage[Scroll Page: <br><code>scroll(self, scrolls, frame_size, direction, delay)</code>]
    ScrollPage --> CarouselFunction[<code>carousel(direction, scrolls, frame_size, delay)</code>]
    CarouselFunction --> ExecuteScript[Execute scroll by script:<br><code>execute_script(window.scrollBy(0,{direction}{frame_size}))</code>]
    ExecuteScript --> WaitAfterScroll[Wait for a while:<br><code>wait(delay)</code>]
    WaitAfterScroll -->  ScrollLoop[Loop if <br><code>scrolls</code> remain ]
    ScrollLoop -- Yes --> ExecuteScript
    ScrollLoop -- No --> ScrollComplete[Scroll operation complete]
    ScrollComplete --> GetLocale[Get Page Locale:<br><code>locale</code>]
    GetLocale --> GetMetaTag[Get <br><code>meta</code> tag]
     GetMetaTag -- Success --> GetContent[Get <br><code>content</code> attribute]
     GetContent --> ReturnLocale[Return language code]
     GetMetaTag -- Fail --> TryJavaScript[Try JavaScript <br><code>get_page_lang()</code>]
    TryJavaScript -- Success --> ReturnLocale
    TryJavaScript -- Fail --> ReturnNone[Return None]
    ReturnLocale --> NavigateToURL[Navigate to URL: <br><code>get_url(self, url)</code>]
    ReturnNone --> NavigateToURL
    NavigateToURL --> GetCurrentURL[Get current URL]
     GetCurrentURL -- Success --> SavePreviousURL[Save to <br><code>previous_url</code> if changed]
     GetCurrentURL -- Fail -->  ReturnFalse1[Return False]
    SavePreviousURL --> LoadURL[Load URL: <br><code>self.driver.get(url)</code>]
    LoadURL --> WaitForComplete[Wait until <br><code>readyState == 'complete'</code>]
    WaitForComplete -- Yes --> SaveCookies[Save Cookies: <br><code>_save_cookies_localy()</code>]
    WaitForComplete -- No --> WaitForComplete
    SaveCookies --> ReturnTrue[Return True]
    LoadURL -- Fail --> CatchWebDriverError[Catch <br><code>WebDriverException</code>]
     CatchWebDriverError --> LogWebDriverError[Log error]
     LogWebDriverError --> ReturnFalse2[Return False]
    LoadURL -- Fail --> CatchInvalidArgError[Catch <br><code>InvalidArgumentException</code>]
     CatchInvalidArgError --> LogInvalidArgError[Log error]
    LogInvalidArgError --> ReturnFalse3[Return False]
      LoadURL -- Fail --> CatchAnyError[Catch other exceptions]
    CatchAnyError --> LogAnyError[Log error]
    LogAnyError --> ReturnFalse4[Return False]
    ReturnFalse1 --> End[End]
    ReturnFalse2 --> End
    ReturnFalse3 --> End
    ReturnFalse4 --> End
    ReturnTrue --> End
    End --> OpenNewTab[Open New Tab: <br><code>window_open(self, url)</code>]
    OpenNewTab --> ExecuteNewTabScript[Execute: <br><code>execute_script('window.open();')</code>]
    ExecuteNewTabScript --> SwitchToNewTab[Switch to new tab]
    SwitchToNewTab --> LoadURLinNewTab[Load URL if specified]
    LoadURLinNewTab --> End1[End]
   End1 --> WaitTime[Wait Time: <br><code>wait(self, delay)</code>]
   WaitTime --> SleepTime[<code>time.sleep(delay)</code>]
   SleepTime --> End2[End]
   End2 --> SaveCookiesLocally[Save Cookies Locally: <br><code>_save_cookies_localy(self)</code>]
   SaveCookiesLocally --> OpenCookieFile[Open cookie file in <br><code>gs.cookies_filepath</code>]
    OpenCookieFile --> DumpCookies[Save cookies using <br><code>pickle.dump()</code>]
    DumpCookies -->  ReturnTrueDebug[Return True for debugging]
    SaveCookiesLocally -- Fail --> LogErrorSaveCookies[Log error saving cookies]
    LogErrorSaveCookies --> End3[End]
    ReturnTrueDebug --> End3
  End3 --> FetchHTML[Fetch HTML: <br><code>fetch_html(self, url)</code>]
    FetchHTML --> CheckURLType[Check if url starts with file, http or https]
    CheckURLType -- File --> ExtractFilePath[Extract File path]
    ExtractFilePath --> CheckFileExists[Check if file exists]
     CheckFileExists -- Yes --> ReadFile[Read the file content]
    ReadFile --> SetHTMLContent[Set html content as `self.html_content`]
       SetHTMLContent --> ReturnTrue4[Return True]
    CheckFileExists -- No -->  LogFileNotFound[Log "Local file not found"]
    LogFileNotFound --> ReturnFalse5[Return False]
    CheckURLType -- HTTP/HTTPS --> NavigateAndGetHTML[Call <br><code>get_url(url)</code>]
    NavigateAndGetHTML -- Success --> GetPageSource[Get the page source]
    GetPageSource --> SetHTMLContent
    NavigateAndGetHTML -- Fail --> LogErrorFetchingURL[Log error fetching URL]
    LogErrorFetchingURL --> ReturnFalse6[Return False]
    CheckURLType -- Other --> LogUnsupportedProtocol[Log unsupported protocol error]
    LogUnsupportedProtocol --> ReturnFalse7[Return False]
     ReturnFalse5 --> End4[End]
    ReturnFalse6 --> End4
    ReturnFalse7 --> End4
   ReturnTrue4 --> End4
```

### Explanation of Mermaid Diagram

**Dependencies:**

*   **`time`**: Used in the `wait` method to pause execution for a specified time using `time.sleep(delay)`. This is a standard Python library for time-related operations.
*   **`copy`**: Used in the `get_url` method to create a copy of the current URL before navigation using `copy.copy(self.current_url)`. The `copy` module provides shallow and deep copy operations.
*   **`pickle`**: Used in the `_save_cookies_localy` method to serialize the cookies and save them to a file using `pickle.dump(self.driver.get_cookies(), cookiesfile)`. The `pickle` module is used for serializing and deserializing Python objects.
*   **`pathlib`**: Used in the `fetch_html` method to handle file paths using `Path(match.group(0))`. This is a standard Python library.
*   **`re`**: Used in the `fetch_html` method to extract file path using regular expression `re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)`. This is a standard Python library.
*   **`gs`**: Global settings imported from a project file (likely `src.config.settings`). The module provides access to the global settings of the project, including file paths like `gs.cookies_filepath`.
*   **`logger`**: Logging functionalities from `src.logger.logger`. Used for error handling and debugging.
*   **`selenium.webdriver`**: Used to interact with web drivers. The `webdriver_cls` argument of the `Driver` class is an instance of `selenium.webdriver`.
*   **`selenium.webdriver.common.by`**: Used to locate elements on a web page using CSS selectors (`By.CSS_SELECTOR`).
*   **`selenium.common.exceptions`**: Used to handle exceptions specific to selenium web drivers. `WebDriverException` and `InvalidArgumentException`.

## <explanation>

### Detailed Explanation

**Imports:**

*   `time`: Used for implementing delays in the `wait` method, allowing the script to pause execution.
*   `copy`: Used for creating a copy of the current URL in the `get_url` method, preserving it before navigation.
*   `pickle`: Used to serialize and save the web driver cookies to a local file in the `_save_cookies_localy` method for persistent storage.
*   `pathlib.Path`: Used in `fetch_html` for file path manipulations, such as checking if file exists.
*   `re`: Used for extracting file path from the URL in the `fetch_html` method.
*   `src.config.settings as gs`: Imports global settings from the `src.config.settings` module, specifically for accessing the cookies file path (`gs.cookies_filepath`).
*   `src.logger.logger as logger`: Imports the logging module for handling errors, warnings, and information messages within the class.
*   `selenium.webdriver`: Imports core classes for working with Selenium web drivers (e.g., `Chrome`, `Firefox`).
*   `selenium.webdriver.common.by.By`: Provides ways to locate elements on a web page.
*   `selenium.common.exceptions.WebDriverException`, `selenium.common.exceptions.InvalidArgumentException`: Imports exceptions from Selenium for handling specific webdriver-related errors.

**Classes:**

*   `Driver`:
    *   **Purpose**: Provides a high-level interface to manage Selenium web drivers, encapsulating initialization, navigation, scrolling, and cookie management.
    *   **Attributes**:
        *   `self.driver`: Stores the actual Selenium WebDriver instance.
        *   `self.html_content`: Stores the fetched HTML content from URL or file.
        *   `self.previous_url`: Stores the previous URL visited.
    *   **Methods**:
        *   `__init__(self, webdriver_cls, *args, **kwargs)`: Initializes the `Driver` instance by creating a WebDriver object, ensures a valid driver class is passed and raises `TypeError` if not.
        *   `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Called when a subclass is created, enforces providing a `browser_name`.
        *   `__getattr__(self, item)`: Attribute proxy, retrieves attributes not directly defined on the `Driver` instance.
        *   `scroll(self, scrolls, frame_size, direction, delay)`: Scrolls the web page in the specified direction and uses a nested function named `carousel` to do scrolling with `execute_script` method.
        *   `locale(self)`: Property that tries to determine page language. First attempts to get the language from meta tags, if fails to locate the meta tag it tries to use javascript call `get_page_lang()` (which is not implemented in the provided code).
        *   `get_url(self, url)`: Navigates to a URL using the Selenium web driver, handles exceptions such as `WebDriverException`, `InvalidArgumentException`, and saves the cookies and previous URL.
        *   `window_open(self, url)`: Opens a new tab and switches to it using javascript injection and loads URL if provided.
        *   `wait(self, delay)`: Introduces a delay for a specified amount of time using `time.sleep`.
        *   `_save_cookies_localy(self)`: Saves cookies locally using pickle.
        *   `fetch_html(self, url)`: Fetches HTML content from a local file or URL, supports `file://`, `http://`, and `https://` protocols.

**Functions:**

*   `__init__(self, webdriver_cls, *args, **kwargs)`:
    *   **Arguments**:
        *   `webdriver_cls` (`type`):  The WebDriver class (e.g., `Chrome`, `Firefox`).
        *   `*args`: Positional arguments for the WebDriver constructor.
        *   `**kwargs`: Keyword arguments for the WebDriver constructor.
    *   **Purpose**: Initializes a new instance of the `Driver` class by creating the underlying Selenium WebDriver and validating the `webdriver_cls`.
    *   **Return**: `None`.
*   `__init_subclass__(cls, *, browser_name=None, **kwargs)`:
    *   **Arguments**:
        *   `cls` (`type`): The class being initialized (subclass).
        *   `browser_name` (`Optional[str]`): Browser name.
        *   `**kwargs`: Additional keyword arguments.
    *   **Purpose**: Sets the browser name attribute in the subclass, ensuring it is specified during subclass creation.
    *   **Return**: `None`.
*   `__getattr__(self, item)`:
    *   **Arguments**:
        *   `item` (`str`): The name of the attribute to access.
    *   **Purpose**: Proxies attribute access to the underlying Selenium driver.
    *   **Return**: The attribute from the underlying driver.
*   `scroll(self, scrolls, frame_size, direction, delay)`:
    *   **Arguments**:
        *   `scrolls` (`int`): Number of scrolls.
        *   `frame_size` (`int`): Scroll frame size in pixels.
        *   `direction` (`str`): Scroll direction, can be `'forward'`, `'down'`, `'backward'`, `'up'` or `'both'`.
        *   `delay` (`float`): Delay between scrolls in seconds.
    *   **Purpose**: Scrolls the page.
    *   **Return**: `bool`.
*   `locale(self)`:
    *   **Arguments**:
        *   `self` (`Driver`): Instance of the `Driver` class.
    *   **Purpose**: Attempts to determine the page language using meta tags or javascript.
    *   **Return**: `Optional[str]`, the language code if found, otherwise `None`.
*   `get_url(self, url)`:
    *   **Arguments**:
        *   `url` (`str`): The URL to navigate to.
    *   **Purpose**: Navigates to the given URL, waits for page load completion, saves cookies, and handles exceptions.
    *   **Return**: `bool`.
*   `window_open(self, url)`:
    *   **Arguments**:
        *   `url` (`Optional[str]`): URL to load in the new tab.
    *   **Purpose**: Opens a new tab and loads URL if provided.
    *   **Return**: `None`.
*   `wait(self, delay)`:
    *   **Arguments**:
        *   `delay` (`float`): Delay duration in seconds.
    *   **Purpose**: Introduces a delay in script execution.
    *   **Return**: `None`.
*   `_save_cookies_localy(self)`:
    *   **Arguments**:
        *   `self` (`Driver`): Instance of the `Driver` class.
    *   **Purpose**: Saves the web driver cookies to a local file using `pickle`.
    *   **Return**: `None`.
*   `fetch_html(self, url)`:
    *   **Arguments**:
        *   `url` (`str`): URL to fetch the HTML from (file, http, https).
    *   **Purpose**: Fetches and stores HTML content from the specified URL, supports local file paths, HTTP, and HTTPS URLs.
    *   **Return**: `Optional[bool]`.

**Variables:**

*   `self.driver`: Stores the instance of the Selenium WebDriver.
*   `self.html_content`: Stores the content of the page after navigation.
*   `self.previous_url`: Stores the previously visited URL.
*   `gs.cookies_filepath`: Path to the file for storing cookies, loaded from `src.config.settings`.
*   `logger`: Logger instance for logging errors.

**Potential Errors and Areas for Improvement:**

*   **`get_page_lang()`**: The `get_page_lang()` method is mentioned but not implemented. This needs to be implemented for full functionality.
*   **Cookie Saving**: The `_save_cookies_localy()` method is currently stubbed for debugging purposes (`return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`), which prevents saving cookies. This should be replaced by proper code using `pickle.dump()` with handling errors.
*   **Exception Handling**: The error handling could be improved with more specific logging.
*   **Scroll Method**: The nested carousel method could be simplified.
*   **File Reading**: The file reading could be improved by using the `read_text_file` function from the `src.utils.file` module for consistency.

**Relationship Chain with Other Parts of Project:**

*   **`src.config.settings`**: The module imports `gs` from `src.config.settings` to access the global settings of the project, specifically the file path where cookies are stored. This module must provide the cookies file path.
*   **`src.logger.logger`**: This module utilizes the logging functionality from the `src.logger.logger` module for logging errors and debug information. This module must be implemented for logging.
*   **`selenium`**: The module uses the `selenium` library to interact with web drivers, so `selenium` is a dependency.
*   **`src.utils.file`**: This module may benefit from using the functions of the `src.utils.file` module (e.g. the `read_text_file` function), but currently not used.

This comprehensive analysis provides a detailed understanding of the `driver.py` module and how it fits within a broader project.