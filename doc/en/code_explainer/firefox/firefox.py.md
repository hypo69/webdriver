## <algorithm>

### Workflow of the Custom Firefox WebDriver Module

This document describes the custom Firefox WebDriver module, focusing on the `Firefox` class, its initialization process, and how it integrates with other components.

1.  **Initialization (`__init__`)**:
    *   The `Firefox` class is initialized with optional parameters for `profile_name`, `geckodriver_version`, `firefox_version`, `user_agent`, `proxy_file_path`, `options`, and `window_mode`.
    *   **Example**: `driver = Firefox(profile_name='test_profile', options=['--headless'])`
    *   Initializes variables `service`, `profile`, and `options_obj` to None.
    *   Loads settings from `firefox.json` using `j_loads_ns`.
    *   Constructs the path to the `geckodriver` executable and Firefox binary using settings from config and `gs.path.root`.
    *   Initializes the Selenium `Service` object using the constructed geckodriver path.
    *   Initializes the Selenium `Options` object.
    *    Adds options specified in the loaded `settings.options` list, if it exists.
    *    Sets window mode using the parameter from `window_mode` or from settings, by adding arguments (`"--kiosk"`, `--headless`, or `--start-maximized`) to `options_obj`.
    *   Adds the options provided during initialization to the `options_obj`.
    *   Adds headers from the `headers` section in the loaded `firefox.json` configuration.
    *  Sets the user agent, either using the provided `user_agent` parameter or by generating a random one with `UserAgent().random` and adding it to `options_obj` by calling `options_obj.set_preference('general.useragent.override', user_agent)`.
    *   If proxy is enabled in settings, calls the `set_proxy` method to configure proxy settings.
     *   Constructs the path to the profile directory based on the `profile_directory.os` or `profile_directory.internal` properties from settings, and if the profile name was provided during initialization it will create a subfolder in the parent directory of profile.
     * Replaces `%LOCALAPPDATA%` in the profile path with the environment variable if it is present in the path.
    *  Initializes the `FirefoxProfile` object using the constructed profile directory path.
    *   Initializes the `WebDriver` by calling the parent constructor `super().__init__`, passing the `service`, and `options_obj`.
    *   Calls `_payload()` to setup JavaScript methods and locator execution functionalities.
    *   If `WebDriverException` occurs during initialization, it logs it as a critical error and returns.
     *   Handles general exceptions and logs them using `logger.critical` and returns if exception occurs.

2.  **Setting Proxy (`set_proxy`)**:
    *   Takes a Selenium `Options` object as an argument.
    *   **Example**: `self.set_proxy(options_obj)`
    *   Gets the proxy list using `get_proxies_dict()` from `src.webdriver.proxy` module.
    *   Combines all available proxies from `'socks4'` and `'socks5'` keys from the proxy dictionary into a single list.
    *  Shuffles the list of proxies and iterates over the shuffled list of proxies to find first working one using `check_proxy` method.
    *    If a working proxy is found, configures the proxy settings in the `options` object, by using `set_preference` for given protocol:
         *   If the `protocol` is `'http'`, sets the `network.proxy.type`, `network.proxy.http`, and `network.proxy.http_port` preferences.
         *  If the `protocol` is `'socks4'`, sets the `network.proxy.type`, `network.proxy.socks`, and `network.proxy.socks_port` preferences.
         *   If the `protocol` is `'socks5'`, sets the `network.proxy.type`, `network.proxy.socks`, and `network.proxy.socks_port` preferences.
         *   Logs a warning if protocol is not `http`, `socks4` or `socks5`.
    *  Logs a warning if no working proxy was found.

3.  **Setting Payload (`_payload`)**:
    *   Sets up JavaScript and locator execution helpers.
    *   **Example**: `self._payload()`
    *   Initializes a `JavaScript` helper instance.
    *   Assigns the JavaScript methods (`get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element`, `window_focus`) from the `JavaScript` helper object to the current `Firefox` instance.
    *   Initializes an `ExecuteLocator` instance with the `WebDriver` instance.
    *   Assigns methods from the `ExecuteLocator` instance to the `Firefox` instance (`execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message` and `send_key_to_webelement`).

## <mermaid>

```mermaid
flowchart TD
     subgraph Firefox Class
        A[__init__ <br> (profile_name, geckodriver_version, firefox_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)] --> B[Load Firefox Settings from JSON]
        B --> C[Construct geckodriver and firefox binary path]
        C --> D[Initialize Selenium Service]
        D --> E[Initialize Firefox Options]
        E --> F[Add Options from config]
         F --> G{Is window mode in settings?}
          G -- Yes --> H[Set Window mode from config]
         G -- No -->  I
         H --> I{Is window mode provided?}
          I -- Yes --> J[Set window mode from parameters]
          I -- No --> K
          J --> K[Set Headers from config]
        K --> L[Set User Agent]
         L --> M{Is proxy enabled?}
        M -- Yes --> N[Set proxy from settings and check it]
         M -- No --> O
        N --> O[Set profile directory]
         O --> P[Initialize WebDriver and set payload]
        P --> Q[Return Firefox Driver instance]


         R[set_proxy <br> (options: Options)] --> S[Get proxies from file]
         S --> T[Create a list of all available proxies]
          T --> U[Shuffle proxies list]
         U --> V[Iterate over proxies to find a working one]
          V --> W{Is proxy working?}
          V -- Yes --> X[Use working proxy]
          V -- No --> Y[Log warning and check next]
          X --> Z[Set proxy to options]
          Y --> U
           U --> AA{All proxies checked?}
           AA -- No --> U
          AA -- Yes --> AB[Log warning, if no working proxy found]
          AB --> AC[Return]

         AD[_payload] --> AE[Initialize JavaScript helper]
         AE --> AF[Assign Javascript methods to Firefox object]
        AF --> AG[Initialize ExecuteLocator]
         AG --> AH[Assign ExecuteLocator methods to Firefox object]
         AH --> AI
    end
     subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
       
        AI:::global
         AC:::global
        Q:::global
    end
```

### Dependencies Analysis:

1.  **`Firefox Class`**:
    *   The core of the module, responsible for creating and configuring the `Firefox` WebDriver instance, it manages options, profiles, proxy settings, and interactions with JavaScript and locators.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *  **`AI`**:  Represents the fully initialized object after setting payload with all attributes, end of method `_payload`.
    *    **`AC`**:  End of the `set_proxy` method, the result of proxy configuration.
    *   **`Q`**: Represents the correctly initialized object of class `Firefox`, return of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**: Provides access to operating system-dependent functions, specifically for getting environment variables for profile path with `os.environ.get('LOCALAPPDATA')`.
*   **`pathlib.Path`**: Used for handling file paths. Creating path objects to join paths for firefox binary and geckodriver, and to resolve profile directory.
*   **`typing.Optional`, `typing.List`**: Used for type annotations, which help with code clarity and prevent type-related errors.
*   **`selenium.webdriver import Firefox as WebDriver`**: Imports the `Firefox` class from Selenium, aliasing it to `WebDriver` for more convenient use.
*   **`selenium.webdriver.firefox.options import Options`**: Imports the `Options` class to setup Firefox specific options.
*   **`selenium.webdriver.firefox.service import Service`**: Imports the `Service` class to configure the driver executable path.
*   **`selenium.webdriver.firefox.firefox_profile import FirefoxProfile`**: Used to set up firefox profile with `FirefoxProfile(profile_directory=profile_directory)`.
*   **`selenium.common.exceptions import WebDriverException`**: Used to handle exceptions specific to Selenium WebDriver.
*    **`src`**: Used to import global settings object `gs` from the `src` package.
*   **`src.webdriver.executor import ExecuteLocator`**: Used to import the `ExecuteLocator` for handling interactions with web elements.
*  **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` helper class for executing Javascript.
*   **`src.webdriver.proxy import download_proxies_list, get_proxies_dict, check_proxy`**: Used to import proxy handling functions: `download_proxies_list`, `get_proxies_dict`, and  `check_proxy`.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file, using `j_loads_ns()`.
*   **`src.logger.logger import logger`**: Used for logging messages and errors using custom logger.
*   **`fake_useragent import UserAgent`**: Used to generate fake user agent with `UserAgent().random`.
*    **`import header`**: Imports custom module `header.py`

**Classes:**

*   **`Firefox(WebDriver)`**:
    *  **Purpose**: Extends Selenium's `webdriver.Firefox` with added functionalities like settings, profile and proxy management, and provides integration with javascript and locators handling.
    *   **Attributes**:
        *   `driver_name` (`str`):  Stores the driver name, set to `firefox`.
    *   **Methods**:
        *   `__init__(self, profile_name, geckodriver_version, firefox_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)`: Initializes the Firefox WebDriver with custom settings.
        *  `set_proxy(self, options: Options) -> None`:  Configures proxy settings using list of proxies.
         * `_payload(self) -> None`:  Sets the payload by configuring javascript and executor classes.

**Functions:**

*  **`__init__(self, profile_name: Optional[str] = None, geckodriver_version: Optional[str] = None, firefox_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *  **Arguments**:
        *   `profile_name` (`Optional[str]`): Name of the profile.
        *   `geckodriver_version` (`Optional[str]`): Geckodriver version.
        *   `firefox_version` (`Optional[str]`): Firefox version.
        *   `user_agent` (`Optional[str]`): User agent string.
        *    `proxy_file_path` (`Optional[str]`): Path to the file with proxy settings.
        *   `options` (`Optional[List[str]]`): List of options to pass to the browser.
        *  `window_mode` (`Optional[str]`): A string specifying the window mode.
        * `*args`, `**kwargs`: Positional and keyword arguments.
    *  **Purpose**: Initializes the `Firefox` WebDriver with custom settings by loading settings from config file, and handling `proxy`, `user_agent`, `profile`, options and window mode.
    *   **Return**: `None`.
*   **`set_proxy(self, options: Options) -> None`**:
    *   **Arguments**:
        *   `options` (`Options`): The Firefox options object, where to set the proxy.
    *   **Purpose**: Sets proxy settings for the firefox driver by using `get_proxies_dict()` and setting proxy preferences using `options.set_preference()`.
    *   **Return**: `None`.
*   **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Firefox` class).
    *  **Purpose**: Sets the `JavaScript` helper and `ExecuteLocator` instances, and maps its methods to instance, using dependency injection.
    *   **Return**: `None`.

**Variables:**

*  `driver_name` (`str`): Stores the name of the driver, set to `firefox`.
*   `service` (`Service`): Stores instance of the selenium `Service` object to handle geckodriver.
*   `profile` (`FirefoxProfile`):  Stores profile settings.
*   `options_obj` (`Options`): Stores browser options.
*  `settings` (`SimpleNamespace`): Parsed settings from a configuration JSON file.
*  `geckodriver_path` (`str`):  Path to the geckodriver executable.
*   `firefox_binary_path` (`str`):  Path to the firefox binary executable.
*   `user_agent` (`str`):  A string for custom user agent.
*   `proxies_dict` (`Dict`): Dictionary containing list of proxies, grouped by their type (http, socks4, socks5).
* `all_proxies` (`List[Dict[str, Any]]`):  List of all available proxies.
*   `working_proxy` (`Dict`): A dictionary which holds currently selected proxy from `all_proxies` list.
*    `proxy` (`Dict`): A dictionary with proxy parameters: `host`, `port` and `protocol`.
*   `protocol` (`str`): The protocol of a proxy server (`http`, `socks4` or `socks5`).
*   `j` (`JavaScript`): Instance of the `JavaScript` class.
*   `execute_locator` (`ExecuteLocator`): Instance of the `ExecuteLocator` class.
* `profile_directory` (`str`): Profile directory string.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: The `j_loads_ns` call for loading settings can be improved by adding more specific error handling.
*  **Hardcoded Paths**: The paths to the geckodriver and settings JSON file are hardcoded, and should use `gs.path` for configuration.
*   **Proxy Handling**: The code has proxy handling that shuffles the list of proxies and tries to find a working one which may not be most efficient way to do it, better proxy selection and handling approach should be used.
*    **Error Handling**: While basic error handling is present, it could be improved by adding more specific exceptions and logging.
*   **Type Hinting**: Some parameters and variables could benefit from more precise type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is a part of the `src.webdriver` package.
*   It utilizes the `ExecuteLocator` class from the `src.webdriver.executor` module and the `JavaScript` class from the `src.webdriver.js` module.
*   It also uses `src.webdriver.proxy` module to retrieve and check proxies.
*   It uses `src.utils.jjson` to load configuration files and `src.logger.logger` for logging.
*   It relies on `fake_useragent` library to generate fake user agents.
*   It also depends on the global settings object `gs` from `src` package.

This detailed explanation provides a comprehensive understanding of the `firefox.py` module and its interactions with other components in the project.