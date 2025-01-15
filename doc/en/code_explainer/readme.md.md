## <algorithm>

### Workflow of the WebDriver Executor Module

This document describes the workflow of the WebDriver Executor module, which includes the `Driver`, `ExecuteLocator` classes and their interactions.

**I. `Driver` Class Workflow:**

1.  **Initialization**:
    *   A `Driver` instance is created with a `webdriver_cls` (e.g., `Chrome`) and optional arguments.
    *   **Example**: `chrome_driver = Driver(Chrome)`
    *   The constructor sets up the WebDriver and checks if the passed object is valid `WebDriver` class.

2.  **Navigation**:
    *   The `get_url(url)` method navigates to the specified URL.
    *    **Example**: `chrome_driver.get_url("https://www.example.com")`
    *   It uses the selenium `driver.get()` method to navigate to the provided url.

3.  **Domain Extraction**:
    *   The `extract_domain(url)` method extracts the domain from the given URL string.
    *   **Example**: `domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")`

4.  **Cookie Management**:
    *   The `_save_cookies_localy()` method saves cookies from the current session to a file.
    *   **Example**: `success = chrome_driver._save_cookies_localy()`

5.  **Page Operations**:
    *   The `page_refresh()` method refreshes the current page.
    *    **Example**: `chrome_driver.page_refresh()`
    *   The `scroll(scrolls, direction, frame_size, delay)` method scrolls the page in a given direction with a given frame size.
    *   **Example**:  `chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1)`

6.  **Language Detection**:
    *   The `locale` property attempts to extract the page language.
    *    **Example**: `page_language = chrome_driver.locale`

7. **Custom User Agent**:
    *  Creates instance of `Driver` with specified `user_agent`.
    *   **Example**:
        ```python
        user_agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
        ```

8.  **Element Search**:
    *   The `find_element(by, selector)` method finds a web element based on `by` (e.g., `By.CSS_SELECTOR`) and selector.
    *  **Example**: `element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')`

9.  **Current URL**:
    * The `current_url` property returns current URL string.
    *  **Example**: `current_url = chrome_driver.current_url`

10. **Window Focus**:
    *   The `window_focus()` method sets the focus to the browser window.
    *   **Example**: `chrome_driver.window_focus()`

**II. `ExecuteLocator` Class Workflow:**

1.  **Initialization**:
    *   An `ExecuteLocator` instance is created with a `WebDriver` instance.
    *   **Example**: `executor = ExecuteLocator(driver=driver)`
    *   The constructor initializes `ActionChains` object.

2.  **Locator Execution**:
    *   The `execute_locator(locator, message, typing_speed, continue_on_error)` method takes a locator, message, typing speed and continue on error flag as input.
    *   **Example**:  `result = await executor.execute_locator(locator)`
    *   It processes the locator dictionary, performs specific actions on web elements, and retrieves data if specified.

3.  **Element Retrieval**:
    *   The `get_webelement_by_locator(locator)` method uses specified `by` and `selector` from locator object to locate elements and returns it or list of elements.
    *   **Example**: `element = await executor.get_webelement_by_locator(locator)`

4.  **Attribute Retrieval**:
    *   The `get_attribute_by_locator(locator)` method retrieves attributes from web elements found using the locator and returns a list or a single attribute or a dict of attributes.
    *   **Example**: `attribute = await executor.get_attribute_by_locator(locator)`

5.  **Message Sending**:
    *   The `send_message(locator, message, typing_speed, continue_on_error)` method sends text input to web elements with optional typing speed simulation.
     *   **Example**: `await executor.send_message(locator, "Test", typing_speed=0.1)`

6.  **Screenshot Taking**:
    *   The `get_webelement_as_screenshot(locator)` method takes a screenshot of a web element.
    *  **Example**: `screenshot = await executor.get_webelement_as_screenshot(locator)`

7.   **Event Execution**:
    *   The `execute_event(locator)` method executes specific event based on the event string that can contain multiple events.
    *  **Example**: `await executor.execute_event(locator, "click()")`

8.  **Locator Evaluation**:
    *   The `evaluate_locator(attribute)` method evaluates the locator attribute to resolve placeholder values like `Keys` enum members.
    *  **Example**: `attribute = await executor.evaluate_locator(attribute)`

## <mermaid>

```mermaid
flowchart TD
    subgraph Driver Class
        A[Driver Initialization] --> B[Set up WebDriver]
        B --> C[get_url(url)]
        C --> D[Navigate to URL]
        B --> E[extract_domain(url)]
        E --> F[Return Domain]
        B --> G[_save_cookies_localy()]
        G --> H[Save cookies locally]
         B --> I[page_refresh()]
         I --> J[Refresh the page]
         B --> K[scroll(scrolls, direction, frame_size, delay)]
         K --> L[Scroll the page]
        B --> M[locale]
        M --> N[Get page language]
        B --> O[Driver Initialization with user_agent]
        O --> P[Set user agent for chrome driver]
          B --> Q[find_element(by, selector)]
        Q --> R[Find element by locator]
         B --> S[current_url]
        S --> T[Return current url]
        B --> U[window_focus()]
        U --> V[Focus browser window]
    end
    
    
    subgraph ExecuteLocator Class
        AA[ExecuteLocator Initialization] --> BB[Initialize ActionChains]
        BB --> CC[execute_locator(locator, message, typing_speed, continue_on_error)]
        CC --> DD[Parse locator data]
        DD --> EE{Locator has event?}
        EE -- Yes --> FF[execute_event(locator)]
         EE -- No --> GG{Locator has attribute?}
         GG -- Yes --> HH[get_attribute_by_locator(locator)]
         GG -- No --> II[get_webelement_by_locator(locator)]
         FF --> JJ[Return event result]
        HH --> KK[Return attribute result]
         II --> LL[Return web element]
        
         BB --> MM[get_webelement_by_locator(locator)]
         MM --> NN[Return web element or list of web elements]
         
         BB --> OO[get_attribute_by_locator(locator)]
        OO --> PP[Return extracted attribute(s)]
        
        BB --> QQ[send_message(locator, message, typing_speed, continue_on_error)]
        QQ --> RR[Sends a message to web element]
        
       BB --> SS[get_webelement_as_screenshot(locator)]
       SS --> TT[Take a screenshot of web element]
       
       BB --> UU[evaluate_locator(attribute)]
        UU --> VV[Return evaluated attribute]
        

    end
    
      subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
    
        V:::global
        T:::global
        R:::global
        N:::global
        L:::global
       LL:::global
       KK:::global
       JJ:::global
        VV:::global
    end
```

### Dependencies Analysis:

1.  **`Driver Class`**:
    * The `Driver` class is a wrapper around Selenium `WebDriver`. It is designed to provide a single point to manage all web driver functionalities. It initializes, configures and manages the WebDriver object, providing methods for navigation, scrolling, and more.
2.  **`ExecuteLocator Class`**:
    *   The `ExecuteLocator` class is designed for performing various actions on web page elements using Selenium WebDriver.
3. **Global Dependencies**: Represents the outputs and interactions with the classes and outer world (logger, selenium methods, etc):
    *   **`V`**: Representing browser window focus, return value of `window_focus` method of `Driver` class.
    *  **`T`**:  The current URL of the page, a return value of the `current_url` property of `Driver` class.
    *  **`R`**: The located web element, or list of web elements, a return value of the `find_element` method of the `Driver` class.
    *   **`N`**: The detected page language, return value of the `locale` property method of `Driver` class.
    *   **`L`**:  The status of page scrolling, a return value of the `scroll` method of `Driver` class.
    *  **`LL`**:  The located web element or list of web elements, a return value of the `get_webelement_by_locator` method of `ExecuteLocator` class.
    *  **`KK`**:  The extracted attribute(s) from a web element, a return value of the `get_attribute_by_locator` method of `ExecuteLocator` class.
    *  **`JJ`**: The result of the executed event, return value of `execute_event` method of `ExecuteLocator` class.
    *   **`VV`**: The evaluated attribute from `evaluate_locator` method of `ExecuteLocator` class.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`src.webdriver.driver import Driver, Chrome`**: Imports `Driver` class and `Chrome` class used as `webdriver_cls` from `src.webdriver.driver` module.
*   **`selenium.webdriver.common.by import By`**: Imports `By` class used to locate elements from `selenium` library.

**Classes:**

*   **`Driver`**: (from `src.webdriver.driver`)
    *   **Purpose**: Provides a dynamic WebDriver implementation that combines common Selenium WebDriver functionalities with custom extensions.
    *   **Attributes:**
        *   `previous_url` - stores the previous URL.
        *   `referrer` - stores the referrer URL.
        *    `page_lang` - stores the detected page language.
        *   `driver` - WebDriver instance.
        *   `html_content` - html source of the page.
    *   **Methods:**
        *   `__init__(self, webdriver_cls, *args, **kwargs)` - Initializes the `Driver` instance.
        *   `get_url(self, url)` - Navigates to a given URL.
        *   `extract_domain(self, url)` - Extracts domain from URL.
        *   `_save_cookies_localy(self)` - saves cookies locally.
        *   `page_refresh(self)` - Refresh the current page.
        *   `scroll(self, scrolls, direction, frame_size, delay)` - Scrolls the page.
        *   `locale(self)` - Detects the page language from meta tag or using javascript.
        *   `find_element(self, by, selector)` - Finds element based on the specified by and selector.
        *  `window_focus(self)` - sets the focus to the browser window by executing a javascript code.
        *   `current_url` - property method which returns current url.
*   **`ExecuteLocator`**: (from `src.webdriver.executor`)
    *   **Purpose**:  Provides methods to perform actions on web elements based on provided locators.
    *   **Attributes**:
        *   `driver` - WebDriver instance.
        *    `actions` - ActionChains instance.
        *   `by_mapping` - Dictionary that maps locator types to Selenium `By` objects.
        *   `mode` - execution mode.
    *   **Methods**:
        *   `__init__(self, driver, *args, **kwargs)` - initializes WebDriver and ActionChains objects.
        *   `execute_locator(self, locator, message, typing_speed, continue_on_error)` - Main entry point for executing actions based on the locator.
        *    `get_webelement_by_locator(self, locator)` - Extracts web elements based on the provided locator.
        *    `get_attribute_by_locator(self, locator)` - Retrieves attribute(s) from the web element(s).
        *   `send_message(self, locator, message, typing_speed, continue_on_error)` - Sends message to a web element.
        *   `get_webelement_as_screenshot(self, locator)` - takes a screenshot of web element.
        *  `evaluate_locator(self, attribute)` - Evaluates locator attribute.
        *  `execute_event(self, locator)` - Executes event on the web element.

**Functions:**

*   **`main()`**:
    *   **Arguments**: None.
    *   **Purpose**: Contains usage examples of the `Driver` and `Chrome` classes, showcasing how to use their methods, navigate, extract data, set up user agent, and locate elements on a page.
    *   **Return**: None.

**Variables:**

*   `chrome_driver` (`Driver`): Instance of the `Driver` class.
*   `domain` (`str`): Extracted domain from url.
*   `success` (`bool`): Boolean which contains status of saving cookies.
*   `page_language` (`str`): String which contains the language of the page.
*   `user_agent` (`dict`): Dictionary for passing the user agent value.
*    `custom_chrome_driver` (`Driver`): Instance of `Driver` class with custom user agent.
*    `element` (`WebElement`): Web element instance, after searching it using `find_element` method.
*   `current_url` (`str`): String containing current URL of the web page.

**Potential Errors and Areas for Improvement:**

*   **Type Hinting**: While type hints are present, using `Optional` or `Union` can increase clarity.
*   **Error Handling**: Some try-except blocks log the errors but then continue the script execution, which can hide issues, it can be improved.
*   **Code Clarity:** Code blocks inside `main` function can be separated into different smaller functions for easier code reading.

**Relationship Chain with Other Parts of Project:**

*   This module is an example of how to use `src.webdriver.driver`, `src.webdriver.executor` and `selenium` libraries and modules.
*  It demonstrates how to interact with web pages, perform actions on web elements, extract data and setup custom user agent.
*  It depends on  `selenium` for web automation.

This detailed explanation provides a comprehensive understanding of how `Driver`, `Chrome` and `ExecuteLocator` classes are used to interact with web pages and perform various actions using Selenium.