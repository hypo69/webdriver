## <algorithm>

### Workflow of the Custom Chrome WebDriver Module

This document outlines the workflow of the custom Chrome WebDriver module, focusing on its configuration, initialization, and usage.

1.  **Initialization (`__init__`)**:
    *   The `Chrome` class is initialized with optional parameters such as `profile_name`, `chromedriver_version`, `user_agent`, `proxy_file_path`, `options`, and `window_mode`.
    *   **Example**: `driver = Chrome(profile_name='test_profile', options=['--headless'])`
    *   It loads settings from the `chrome.json` file using `j_loads_ns` for easy access to settings as attributes.
    *   It constructs the path to `chromedriver` using the loaded settings.
    *   It initializes the Selenium `Service` object with the `chromedriver` path.
    *   It initializes the Selenium `Options` object.
    *   It adds default options from the loaded `chrome.json` file to the options object using `options_obj.add_argument(option)`.
    *   It sets window mode from configuration or init parameter (e.g., `--kiosk`, `--headless`, or `--start-maximized`).
    *   Adds options passed directly to the constructor to the `options_obj`.
    *   Sets a user agent using the provided parameter or a randomly generated one using `fake_useragent`.
    *   If proxy is enabled in settings, it calls the `set_proxy` method to configure it.
    *  Constructs profile directory based on settings from the json file.
    *  If a custom profile name is provided it will create a folder in a directory of default profile directory.
    *  Replaces `%LOCALAPPDATA%` in profile path with an environment variable.
    *   Initializes the `WebDriver` by calling the parent constructor `super().__init__(service=service, options=options_obj)`.
    *    Calls the `_payload()` method to set up the JavaScript helper and locator execution functionalities.
    *   Handles exceptions during driver initialization, logs them using `logger.critical`, and returns from the constructor.

2.  **Setting Proxy (`set_proxy`)**:
    *   Takes a Selenium `Options` object as an argument.
    *   **Example**: `self.set_proxy(options_obj)`
    *   Fetches the proxy list using the `get_proxies_dict()` function from `src.webdriver.proxy`.
    *   Combines proxies from `socks4` and `socks5` lists into a single list.
    *    Iterates over a shuffled list of proxies and uses `check_proxy()` to check the first working one.
    *   If working proxy is found, sets proxy settings to `options` based on proxy protocol using `options.add_argument(f'--proxy-server=...')`.
    *   Logs proxy information if the proxy was found and configured, or logs a warning if no proxy was found.

3.  **Setting Payload (`_payload`)**:
    *   Sets up JavaScript and locator execution instances.
    *   **Example**: `self._payload()`
    *   Initializes a `JavaScript` helper object with the `WebDriver` instance.
    *    Assigns Javascript methods to the `Chrome` object by using `self.get_page_lang = j.get_page_lang` syntax.
    *   Initializes an `ExecuteLocator` object with the `WebDriver` instance.
    *   Assigns methods from the `ExecuteLocator` instance to the `Chrome` instance (`execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message` and `send_key_to_webelement`).

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
    *   The core of the module, responsible for creating and configuring the `Chrome` WebDriver instance. It handles loading settings, setting up proxies, and integrating JavaScript functionalities.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *   **`AH`**: Represents the fully initialized object after setting payload with all attributes, end of the `_payload` method.
    *   **`AB`**: End of `set_proxy` method, indicating that proxy settings were either applied successfully or that no proxies were found.
    *   **`P`**: Represents the correctly initialized object of `Chrome`, return of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**:  Provides operating system-dependent functionality. Used here for getting environment variable values with `os.environ.get('LOCALAPPDATA')`.
*   **`pathlib.Path`**: Used for handling file paths, creating paths to chromedriver and profile directories with `Path(gs.path.root, settings.executable_path.chromedriver)`.
*   **`typing.Optional`, `typing.List`**: Used for type annotations, which help with code clarity and prevent type-related bugs.
*   **`selenium.webdriver.Chrome as WebDriver`**: Imports the `Chrome` class from Selenium for browser automation, aliasing it to `WebDriver`.
*   **`selenium.webdriver.chrome.options.Options`**: Used to set up browser options with `Options()`.
*    **`selenium.webdriver.chrome.service.Service`**: Used for creating a service object to run the chromedriver executable, using `Service(chromedriver_path)`.
*   **`selenium.common.exceptions.WebDriverException`**: Used for handling exceptions specific to Selenium WebDriver.
*   **`src`**: Used to import the global settings object `gs` from the `src` package.
*   **`src.webdriver.executor import ExecuteLocator`**: Used to import the `ExecuteLocator` class for handling interactions with web elements.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` class for executing javascript on a web page.
*   **`src.webdriver.proxy import get_proxies_dict, check_proxy`**: Used to import functions to handle proxy servers.
*   **`src.utils.jjson import j_loads_ns`**: Used for loading settings from a JSON file with `j_loads_ns()`.
*   **`src.logger.logger import logger`**: Used for logging messages and errors.
*  **`fake_useragent import UserAgent`**: Used to generate fake user agents with `UserAgent().random`.
*  **`random`**: Used for randomizing the proxy list with `random.sample(all_proxies, len(all_proxies))`.

**Classes:**

*   **`Chrome(WebDriver)`**:
    *   **Purpose**: Extends Selenium's `webdriver.Chrome` with added functionality for better automation.
    *   **Attributes**:
         *   `driver_name` (`str`):  Stores the driver name set to `chrome`.
    *   **Methods**:
        *    `__init__(self, profile_name, chromedriver_version, user_agent, proxy_file_path, options, window_mode, *args, **kwargs)`: Initializes the `Chrome` instance, configuring the driver with custom settings.
        *   `set_proxy(self, options: Options) -> None`:  Sets proxy settings by using the output of `get_proxies_dict`, and validating proxy with `check_proxy` function.
        *   `_payload(self) -> None`: Sets up JavaScript and locator execution instances.

**Functions:**

*   **`__init__(self, profile_name: Optional[str] = None, chromedriver_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
         *   `profile_name` (`Optional[str]`): Profile name.
         *   `chromedriver_version` (`Optional[str]`): Chromedriver version.
         *   `user_agent` (`Optional[str]`):  User agent string.
         *   `proxy_file_path` (`Optional[str]`): Path to proxy file.
         *   `options` (`Optional[List[str]]`): List of chrome options.
         *   `window_mode` (`Optional[str]`): String to define the window mode (`kiosk`, `windowless` or `full_window`).
        *    `*args`, `**kwargs`: Additional arguments for the selenium `WebDriver` constructor.
    *   **Purpose**: Initializes the `Chrome` class, setting up the web driver with the custom settings.
    *   **Return**: `None`.
*   **`set_proxy(self, options: Options) -> None`**:
     *   **Arguments**: `options` (`Options`): Selenium `Options` object to add the proxy settings to.
     *   **Purpose**: Sets proxy configurations for the WebDriver based on the `proxies.txt` file.
     *  **Return**: `None`.
*  **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Chrome`).
    *   **Purpose**: Loads JavaScript helper and sets locator execution functionalities.
    *   **Return**: `None`.

**Variables:**

*   `driver_name` (`str`): Name of the driver set to `"chrome"`.
*   `service` (`Service`): Instance of selenium service used to start chromedriver.
*  `options_obj` (`Options`): Instance of selenium `Options` used to set up chrome options.
*   `chromedriver_path` (`str`): Path to the chromedriver executable.
*   `settings` (`SimpleNamespace`): Settings from a configuration json file.
*    `profile_directory` (`str`): Path to the directory of chrome profile.
*    `user_agent` (`str`): String that represents the user agent value.
*    `proxies_dict` (`dict`): Dictionary that stores proxies, grouped by their protocol.
*    `all_proxies` (`list`): A list of all available proxies.
*   `working_proxy` (`dict`): A proxy, that was found to be working from `all_proxies` list.
* `proxy` (`dict`): A dictionary that represents the proxy data.
*   `protocol` (`str`): Proxy protocol from the proxy data.
*  `j` (`JavaScript`): Instance of the `JavaScript` class.
*   `execute_locator` (`ExecuteLocator`): Instance of `ExecuteLocator` class.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: The `j_loads_ns` call for loading settings can be improved by adding more specific error handling.
*    **Hardcoded Paths**: The path to the settings JSON file can be configured using the global settings object.
*   **Proxy Handling**:  The proxy handling can be improved by adding more sophisticated logic for choosing the right proxy.
*  **Error Handling**: While basic error handling is present, it can be improved by catching more specific exceptions and providing more detailed error messages.
*  **Type Hinting**: Some parameters and variables can benefit from more precise type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is a part of the `src.webdriver` package, which is used to manage web driver related functionalities.
*   It utilizes the `ExecuteLocator` class from `src.webdriver.executor` and `JavaScript` class from `src.webdriver.js` module.
*   It also uses proxy handling functions from `src.webdriver.proxy` module.
*  It utilizes the global settings object from `src`.
*  It uses `src.utils.jjson` to parse json config files.
*   It uses `src.logger.logger` for error logging.

This detailed explanation provides a comprehensive understanding of the `chrome.py` module, its functionalities, and its interaction with other components in the project.