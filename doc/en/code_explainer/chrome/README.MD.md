## <algorithm>

### Workflow of the Custom Chrome WebDriver Module

This document describes the workflow of the custom Chrome WebDriver module, focusing on its configuration, initialization, and interaction with settings and other modules.

1.  **Initialization (`__init__`)**:
    *   The `Chrome` class is initialized with optional parameters such as profile name, chromedriver version, user agent, proxy file path, chrome options, and window mode.
    *   **Example**: `driver = Chrome(profile_name='test_profile', options=['--headless'])`
    *   It loads settings from `chrome.json` using `j_loads_ns`, which converts the settings to a `SimpleNamespace` object.
    *   Constructs the path to the `chromedriver` executable using `gs.path.root` and the setting from the config.
    *   Initializes a Selenium `Service` object, passing the path to `chromedriver`.
    *   Initializes a Selenium `Options` object.
    *    Adds options from the `options` list inside `chrome.json` to the `options_obj` if the options key exists.
    *  Sets window mode from the config or provided parameter using  `window_mode` key from the settings or parameter, adding corresponding arguments (e.g., `--kiosk`, `--headless`, or `--start-maximized`).
    *  Adds the options that were passed directly to init method to options object.
    *   Sets a user agent using the provided parameter or a randomly generated user agent.
    *   If proxy is enabled in settings it calls the `set_proxy` method, to add proxy to options.
    *   Configures the profile directory by using the specified path from the config (os specific path or internal path) using the `profile_directory` key from the config.
    * If a `profile_name` is provided in init parameters, sets the profile directory path to a new folder with a given profile name.
    *   If the profile directory path contains `%LOCALAPPDATA%`, it replaces it with corresponding environment variable.
    *   Initializes the `WebDriver` object using `super().__init__`, passing the `Service` and `Options` objects.
    *    Calls `_payload()` method to set payload.
    *    If any `WebDriverException` occurs or any other general exception occurs, it logs it and returns from the constructor.

2.  **Setting Proxy (`set_proxy`)**:
    *   Takes a Selenium `Options` object as input.
    *   **Example**: `self.set_proxy(options_obj)`
    *   It fetches a list of proxies using the `get_proxies_dict()` function from the `src.webdriver.proxy` module.
    *   Combines all proxies from `'socks4'` and `'socks5'` keys into a single list, shuffles that list using `random.sample()` and then iterates over this list to find a working proxy by using `check_proxy()` function from  `src.webdriver.proxy` module.
    *    If a working proxy was found:
        *   Sets the appropriate proxy server option (`--proxy-server=http://...`, `--proxy-server=socks4://...` or `--proxy-server=socks5://...`) based on proxy `protocol`.
    * Logs the proxy info and a warning if no proxy was found.

3.  **Setting Payload (`_payload`)**:
    *   This method prepares the `Chrome` instance by setting up JavaScript execution and locator handling capabilities.
    *   **Example**: `self._payload()`
    *   Initializes a `JavaScript` instance using the current `Chrome` instance.
    *   Assigns `JavaScript` methods to the `Chrome` object (`get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element`, `window_focus`).
    *   Initializes `ExecuteLocator` with the current `Chrome` instance.
    *   Maps the methods from `ExecuteLocator` (`execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator`, and `send_message`) to the `Chrome` instance, also mapping `send_message` to  `send_key_to_webelement`.

## <mermaid>

```mermaid
flowchart TD
    subgraph Chrome Class
        A[__init__ <br> (profile_name, chromedriver_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)] --> B[Load Chrome Settings from JSON]
        B --> C[Construct chromedriver path]
        C --> D[Initialize Selenium Service]
        D --> E[Initialize Selenium Options]
        E --> F[Add Options from config]
          F --> G{Is window mode in settings?}
          G -- Yes --> H[Set Window mode from config]
         G -- No -->  I
         H --> I{Is window mode provided?}
          I -- Yes --> J[Set window mode from params]
           I -- No --> K
          J --> K[Set Custom User Agent]
         K --> L{Is proxy enabled?}
        L -- Yes --> M[Set proxy from settings and check it]
        L -- No --> N
         M --> N[Set profile directory]
         N --> O[Init WebDriver and set payload]
        O --> P[Return Chrome Driver instance]

         Q[set_proxy <br> (options: Options)] --> R[Get proxies from file]
         R --> S[Create a list of all available proxies]
          S --> T[Shuffle proxies list]
         T --> U[Iterate over proxies to find a working one]
          U --> V{Is proxy working?}
          V -- Yes --> W[Use working proxy]
          V -- No --> X[Log warning and check next]
          W --> Y[Set proxy to options]
          X --> U
           U --> Z{All proxies checked?}
           Z -- No --> U
          Z -- Yes --> AA[Log warning, if no working proxy found]
           AA --> AB[Return]

        AC[_payload] --> AD[Initialize JavaScript helper]
        AD --> AE[Assign Javascript methods to Chrome object]
        AE --> AF[Initialize ExecuteLocator]
        AF --> AG[Assign ExecuteLocator methods to Chrome object]
         AG --> AH
    end
     subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
         
         AH:::global
         AB:::global
         P:::global
    end
```

### Dependencies Analysis:

1.  **`Chrome Class`**:
    *   The core of the module, extending Selenium's `webdriver.Chrome` with added functionalities. It handles driver setup, options, proxy settings, and interactions with JavaScript and locators.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *   **`AH`**: Represents the fully initialized object after setting payload with all attributes, end of the method `_payload`.
    *   **`AB`**: End of the `set_proxy` method.
    *    **`P`**: Represents a correctly initialized object of `Chrome` class, end of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**:  Provides operating system-dependent functionalities. Used here for getting environment variable values with `os.environ.get('LOCALAPPDATA')`.
*   **`pathlib.Path`**: Used for handling file paths, such as constructing paths to chromedriver, profile directory etc.
*   **`typing.Optional`, `typing.List`**: Used for type annotations, enhancing code readability and helping to prevent type-related bugs.
*   **`selenium.webdriver.Chrome as WebDriver`**: Imports the `Chrome` class from Selenium for browser automation, aliasing it as `WebDriver`.
*   **`selenium.webdriver.chrome.options.Options`**: Used to set up browser options with `Options()`.
*   **`selenium.webdriver.chrome.service.Service`**: Used for creating a service object to run the chromedriver executable with `Service(chromedriver_path)`.
*    **`selenium.common.exceptions.WebDriverException`**:  Used to handle exceptions specific to Selenium WebDriver.
*  **`src`**: Used to import the global settings object `gs` from the `src` package.
*   **`src.webdriver.executor import ExecuteLocator`**: Imports the `ExecuteLocator` class for handling interactions with web elements.
*   **`src.webdriver.js import JavaScript`**: Imports the `JavaScript` class for executing JavaScript on the web page.
*   **`src.webdriver.proxy import get_proxies_dict, check_proxy`**: Imports the functions to handle proxy configurations and check proxy availability.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file with `j_loads_ns()`.
*   **`src.logger.logger import logger`**: Used for logging messages and errors.
*  **`fake_useragent.UserAgent`**: Used to generate fake user agents, with `UserAgent().random`.
*    **`random`**: Used for randomizing the proxy list with `random.sample(all_proxies, len(all_proxies))`.

**Classes:**

*   **`Chrome(WebDriver)`**:
    *   **Purpose**: Extends Selenium's `webdriver.Chrome` with additional functionality for web automation, including proxy handling, user agent configuration and javascript execution.
    *   **Attributes**:
        *   `driver_name` (`str`): Stores the driver name set to `chrome`.
    *   **Methods**:
        *   `__init__(self, profile_name, chromedriver_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)`: Initializes the Chrome WebDriver with custom settings.
        *    `set_proxy(self, options: Options) -> None`: Configures proxy settings from a proxy file.
        *   `_payload(self) -> None`: Sets up javascript execution and locator handling.

**Functions:**

*   **`__init__(self, profile_name: Optional[str] = None, chromedriver_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *    `profile_name` (`Optional[str]`): Optional profile name.
        *   `chromedriver_version` (`Optional[str]`): Optional chromedriver version.
        *   `user_agent` (`Optional[str]`): Optional user agent string.
        *   `proxy_file_path` (`Optional[str]`): Optional proxy file path.
        *   `options` (`Optional[List[str]]`): Optional list of chrome options.
        *    `window_mode` (`Optional[str]`): Optional window mode, can be `kiosk`, `windowless` or `full_window`.
        *    `*args`, `**kwargs`: Additional arguments for selenium `WebDriver` constructor.
    *   **Purpose**: Initializes the `Chrome` class and sets up the Chrome WebDriver with various settings.
    *   **Return**: `None`.
*   **`set_proxy(self, options: Options) -> None`**:
    *   **Arguments**:
        *   `options` (`Options`): Selenium Options object, where to add proxy options.
    *   **Purpose**: Sets proxy settings.
    *   **Return**: `None`.
*   **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Chrome`).
    *   **Purpose**: Sets up JavaScript helper and `ExecuteLocator` instances.
    *   **Return**: `None`.

**Variables:**

*   `driver_name` (`str`): Stores the driver name, which is set to `'chrome'`.
*   `service` (`Service`): Holds the Selenium service object used to run chromedriver.
*   `options_obj` (`Options`): Holds the Selenium options.
*   `chromedriver_path` (`str`): Path to the chromedriver.
*   `settings` (`SimpleNamespace`): Settings from `chrome.json`.
*    `profile_directory` (`str`): Directory of the Chrome user profile.
*    `user_agent` (`str`): User agent string.
*   `proxies_dict` (`dict`): Dictionary with available proxies, grouped by type (http, socks4, socks5).
*   `all_proxies` (`list`): List of all proxies.
*   `working_proxy` (`dict`): A working proxy from the `all_proxies` list.
*  `proxy` (`dict`):  Current proxy object.
* `protocol` (`str`): Protocol of current proxy object.
*    `j` (`JavaScript`): Instance of the `JavaScript` class.
*   `execute_locator` (`ExecuteLocator`): Instance of the `ExecuteLocator` class.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: Add more specific error handling for `j_loads_ns` to catch json parsing errors.
*   **Hardcoded Paths**: The path to the settings JSON file is hardcoded and should be read from global settings object.
*   **Proxy Handling**: The proxy handling mechanism is basic and could be more robust, maybe by adding different proxy selection strategies.
*    **Error Handling**: While basic error handling is present, it can be improved by catching more specific exceptions and providing more detailed error information.
*   **Type Hinting**: Some function arguments and variables can have more specific type hints.

**Relationship Chain with Other Parts of Project:**

*  This module is a part of the `src.webdriver` package and is used to create and setup `Chrome` webdriver instances.
*   It loads configurations from the `chrome.json` file.
*   It utilizes the `ExecuteLocator` class from `src.webdriver.executor` and the `JavaScript` helper from `src.webdriver.js` module.
*   It also interacts with the `src.webdriver.proxy` to load and validate proxy servers.
*  It uses `src.logger.logger` to log all errors, warnings and info messages.
*  It relies on `src.utils.jjson` for loading json configuration files.
*  It also utilizes the global settings object from `src`.

This detailed analysis provides a comprehensive understanding of the `chrome.py` module, including its functionality, structure, and interactions with other parts of the project.