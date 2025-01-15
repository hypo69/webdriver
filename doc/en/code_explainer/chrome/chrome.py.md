## <algorithm>

### Workflow of the `chrome.py` Module

The `chrome.py` module defines a custom `Chrome` class that extends Selenium's `webdriver.Chrome` and provides additional functionalities such as proxy handling, custom user agents, and JavaScript execution.

1.  **Initialization (`__init__`)**:
    *   The `Chrome` class is initialized with optional parameters for profile name, chromedriver version, user agent, proxy file path, chrome options, and window mode.
    *   **Example**: `driver = Chrome(profile_name='test_profile', options=['--headless'])`
    *   It loads settings from `chrome.json` using `j_loads_ns`.
    *   Constructs the path to `chromedriver`.
    *   Initializes the Selenium `Service` object.
    *   Initializes the Selenium `Options` object.
    *   Adds options from the config file, handling specific `window_mode`.
        *   If `window_mode` is set to `kiosk` then `"--kiosk"` option is added.
        *   If `window_mode` is set to `windowless` then `"--headless"` option is added.
        *   If `window_mode` is set to `full_window` then `"--start-maximized"` option is added.
    *   Adds the options that were passed directly to init method.
    *   Sets a user agent, either provided or from a fake user agent generator.
    *   If proxy is enabled in settings, calls the `set_proxy` method to configure proxy settings.
    *   Constructs the path to the user data directory using the setting from config file and sets the user data directory using option `"--user-data-dir={profile_directory}"`
    *   Initializes the `WebDriver` by calling the parent constructor `super().__init__`.
    *   Calls `_payload()` to set up JavaScript methods and locator execution.
    *   Handles exceptions during driver initialization, logs and returns if any.

2.  **Setting Proxy (`set_proxy`)**:
    *   Takes `options` (`Options`) object as an argument.
    *   **Example**: `self.set_proxy(options_obj)`
    *   Fetches proxy list using the `get_proxies_dict()` function from `src.webdriver.proxy`.
    *   Combines all available proxies from `'socks4'` and `'socks5'` keys.
    *   Iterates through a shuffled list of proxies, calls `check_proxy()` to find the first working proxy.
    *   If a working proxy is found sets the proxy server option using the found `protocol`, `host` and `port`.
        *    If `protocol` is `http`, proxy is set using `options.add_argument(f'--proxy-server=http://{proxy["host"]}:{proxy["port"]}')`
         *    If `protocol` is `socks4`, proxy is set using `options.add_argument(f'--proxy-server=socks4://{proxy["host"]}:{proxy["port"]}')`
         *  If `protocol` is `socks5`, proxy is set using `options.add_argument(f'--proxy-server=socks5://{proxy["host"]}:{proxy["port"]}')`
        *  Logs a warning if the proxy type is unknown.
    *   Logs a warning if no working proxy is found.

3.  **Setting Payload (`_payload`)**:
    *   This method sets up the `JavaScript` helper and the `ExecuteLocator` instances.
    *   **Example**: `self._payload()`
    *   Initializes a `JavaScript` instance.
    *    Assigns Javascript methods to the `Chrome` object.
    *   Initializes `ExecuteLocator` and assigns its methods (`execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message`) to the `Chrome` instance.

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
2.   **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
     *   **`AH`**:  Represents the fully initialized object after setting payload with all attributes, end of method `_payload`.
    *   **`AB`**: End of `set_proxy` method.
    *   **`P`**: Represents the correctly initialized object of `Chrome`, return of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**: Used for operating system-dependent functionality, specifically `os.environ.get('LOCALAPPDATA')` to get local application data path, which can be used for profiles.
*   **`pathlib.Path`**: Used for handling file paths and joining paths for the chromedriver, and profile directories using methods like `Path(gs.path.root, settings.executable_path.chromedriver)`.
*   **`typing.Optional`, `typing.List`**: Used for type annotations, which help with code clarity and prevent type-related bugs.
*   **`selenium.webdriver.Chrome as WebDriver`**: Imports the `Chrome` class from Selenium for browser automation.
*   **`selenium.webdriver.chrome.options.Options`**: Used to set up browser options with `Options()`.
*   **`selenium.webdriver.chrome.service.Service`**: Used for creating a service object to run the chromedriver executable with `Service(chromedriver_path)`.
*   **`selenium.common.exceptions.WebDriverException`**: Imports exception to handle Selenium webdriver errors.
*   **`src`**: Used to import the global settings object `gs` with `from src import gs`.
*    **`src.webdriver.executor import ExecuteLocator`**: Used to import the `ExecuteLocator` for handling interactions with web elements.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` for executing javascript functions on a web page.
*   **`src.webdriver.proxy import get_proxies_dict, check_proxy`**: Used to import functions to handle proxy servers.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file as a `SimpleNamespace`.
*  **`src.logger.logger import logger`**: Used for logging messages and errors.
*   **`fake_useragent.UserAgent`**: Used to generate fake user agents with `UserAgent().random`.
*   **`random`**: Used for shuffling the list of proxies with `random.sample(all_proxies, len(all_proxies))`.

**Classes:**

*   **`Chrome(WebDriver)`**:
    *   **Purpose**:  Extends Selenium's `webdriver.Chrome` with added functionalities for better automation.
    *   **Attributes**:
        *    `driver_name` (`str`):  Stores the driver name which is `chrome`.
    *   **Methods**:
        *   `__init__(self, profile_name, chromedriver_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)`: Initializes Chrome driver with custom settings.
        *    `set_proxy(self, options: Options) -> None`:  Sets proxy settings using data from a proxy list by using `get_proxies_dict` and `check_proxy` functions.
        *   `_payload(self) -> None`: Sets payload for executing JavaScript code and locators.

**Functions:**

*  **`__init__(self, profile_name: Optional[str] = None, chromedriver_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *    `profile_name` (`Optional[str]`): profile name.
        *    `chromedriver_version` (`Optional[str]`): chromedriver version.
        *    `user_agent` (`Optional[str]`): user agent string.
        *   `proxy_file_path` (`Optional[str]`): path to file with proxy.
        *    `options` (`Optional[List[str]]`): list of chrome options.
        *   `window_mode` (`Optional[str]`): string for setting window mode (`kiosk`, `windowless` or `full_window`).
        *   `*args`, `**kwargs`:  Additional arguments and keyword arguments.
    *   **Purpose**: Initializes a new instance of the `Chrome` class, setting up the web driver with the custom settings.
    *   **Return**: None
*   **`set_proxy(self, options: Options) -> None`**:
    *   **Arguments**:
        *    `options` (`Options`): Selenium `Options` object to add the proxy to.
    *   **Purpose**: Sets proxy using provided options object.
    *   **Return**: `None`.
*   **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Chrome`).
    *   **Purpose**: Sets the JavaScript helper and `ExecuteLocator` instances, mapping its methods to the `Chrome` instance.
    *   **Return**: `None`.

**Variables:**

*   `driver_name` (`str`): Name of the driver set to `"chrome"`.
*   `service` (`selenium.webdriver.chrome.service.Service`): Instance of selenium service used to start chromedriver.
*   `options_obj` (`selenium.webdriver.chrome.options.Options`): Options object, which is used to set up chromedriver settings.
*    `chromedriver_path` (`str`): Path to the chromedriver executable.
*   `settings` (`SimpleNamespace`): Parsed settings from a configuration JSON file.
*  `profile_directory` (`str`): The directory where the browser profile is located.
*   `user_agent` (`str`):  A string for custom user agent.
*   `proxies_dict` (`Dict`): Dictionary with available proxies, grouped by proxy type.
*  `all_proxies` (`List[Dict[str, Any]]`): List of all available proxies.
*    `working_proxy` (`Dict`):  A proxy that was found to be working from `all_proxies` list.
*   `proxy` (`Dict`): Dictionary that represents proxy.
* `protocol` (`str`): Represents protocol for proxy.
*  `j` (`JavaScript`):  Instance of `JavaScript` class.
*  `execute_locator` (`ExecuteLocator`):  Instance of `ExecuteLocator` class.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**:  The `j_loads_ns` for loading settings could have more specific error handling.
*   **Hardcoded Paths**: The path to settings json file can be configured using global settings.
*  **Proxy Handling**: The code has proxy handling, but it shuffles the list of proxies and tries to find a working one which is not optimal, better proxy selection and handling approach should be used.
*   **Error Handling**: While basic error handling is present, it can be improved with more specific exceptions and logging.
*   **Type Hinting**: Some parameters can benefit from more precise type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package, which is designed for handling web driver related functionality.
*   It utilizes the `ExecuteLocator` class from `src.webdriver.executor`, the `JavaScript` helper from `src.webdriver.js` module and the proxy handling from  `src.webdriver.proxy` module.
*   It uses `src.logger.logger` for logging.
*   It also uses the `src.utils.jjson` module for loading configurations from JSON files.
*   It utilizes global settings from `src` package.

This detailed explanation provides a comprehensive understanding of the `chrome.py` module, its functionalities, and its interaction with other parts of the project.