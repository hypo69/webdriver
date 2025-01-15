## <algorithm>

### Workflow of the Edge WebDriver Module

This document outlines the configuration and usage of the custom Edge WebDriver module, detailing how it integrates with `edge.json` settings and other components.

1.  **Initialization (`__init__`)**:
    *   The `Edge` class is initialized with optional parameters such as `profile_name`, `user_agent`, `options`, and `window_mode` and other `*args` and `**kwargs` for `WebDriver`.
    *   **Example**: `driver = Edge(user_agent='custom_user_agent', options=['--headless'])`
    *   Sets the `user_agent` attribute by using passed parameter, or generates a random user agent using `fake_useragent`.
    *   Loads settings from the `edge.json` file using `j_loads_ns`.
    *   Initializes an `EdgeOptions` object.
    *   Adds the user-agent to the options by using f-string interpolation.
    *  Sets the window mode from configuration or provided parameter using `window_mode` key from settings or parameter, adding corresponding arguments (e.g., `--kiosk`, `--headless`, or `--start-maximized`).
    *   Adds options passed during initialization to the `options_obj`.
    *   Adds arguments from the `options` list specified in `edge.json` to the `options_obj`.
    *  Adds headers from the `headers` dictionary from `edge.json` settings to the `options_obj`.
    *   Sets the profile directory path by using `profiles.os` key from the configuration or by building the internal path from `profiles.internal` from the settings.
     *   If a `profile_name` is specified during init, it will create a subfolder for profile in profile directory.
     *   Replaces `%LOCALAPPDATA%` with corresponding environment variable from the system, if it is present in profile path.
     *    Adds the profile directory to the `options_obj` with  `--user-data-dir` argument.
    *   Initializes the `WebDriver` using `super().__init__`, passing the configured `options_obj` and `Service` object, which is created using path from the config `executable_path.default`.
    *   Calls the `_payload()` method to load javascript executors, and also map locator methods to `Edge` instance.
    *   Catches `WebDriverException` and general exceptions and logs them with `logger.critical` and returns from constructor.

2.  **Setting Payload (`_payload`)**:
    *   Sets up JavaScript and locator execution for current class.
    *  **Example**: `self._payload()`
    *   Initializes the `JavaScript` helper using `JavaScript(self)`.
    *   Assigns JavaScript methods to the `Edge` instance: `get_page_lang`, `ready_state`, `get_referrer`, `unhide_DOM_element`, `window_focus`.
    *   Initializes the `ExecuteLocator` with the `WebDriver` instance.
    *    Maps `ExecuteLocator` methods to the `Edge` instance to allow to call them directly: `execute_locator`, `get_webelement_as_screenshot`, `get_webelement_by_locator`, `get_attribute_by_locator`, and `send_message` and `send_key_to_webelement`.

3.  **Setting Options (`set_options`)**:
    *   Takes an optional list of options (`opts`).
    *   **Example**: `options = self.set_options(["--headless"])`
    *   Creates a new `EdgeOptions` object.
    *   If `opts` is present, adds every option to the created options object using `options.add_argument(opt)`.
    *   Returns the created `EdgeOptions` object.

## <mermaid>

```mermaid
flowchart TD
    subgraph Edge Class
        A[__init__ <br> (profile_name, user_agent, options, window_mode, *args, **kwargs)] --> B[Load Edge Settings from JSON]
         B --> C[Initialize EdgeOptions]
        C --> D[Set User Agent]
        D --> E{Is window mode in settings?}
        E -- Yes --> F[Set window mode from config]
         E -- No --> G
        F --> G{Is window mode provided?}
         G -- Yes --> H[Set window mode from parameters]
         G -- No --> I
         H --> I[Set options passed to init]
        I --> J[Add options from config]
        J --> K[Add headers from config]
         K --> L[Set Profile Directory]
         L --> M[Initialize Service with executable_path]
        M --> N[Initialize WebDriver and Set Payload]
        N --> O[Return Edge Driver instance]

        P[set_options <br> (opts: Optional[List[str]])] --> Q[Initialize EdgeOptions]
         Q --> R{Is opts is set?}
         R -- Yes --> S[Add opts to options]
         R -- No --> T
          S --> T[Return options object]


       AC[_payload] --> AD[Initialize JavaScript helper]
        AD --> AE[Assign Javascript methods to Edge object]
        AE --> AF[Initialize ExecuteLocator]
        AF --> AG[Assign ExecuteLocator methods to Edge object]
         AG --> AH
    end
     subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
         
        AH:::global
         T:::global
        O:::global
    end
```

### Dependencies Analysis:

1.  **`Edge Class`**:
    *  The core of the module, responsible for creating and configuring the Edge WebDriver instance and provides methods for setting up options, profiles and handling JavaScript execution.
2. **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *  **`AH`**: Represents fully initialized `Edge` object after setting payload, return of `_payload` method.
    *   **`T`**: Represents the created option object, return of the `set_options` method.
    *   **`O`**: Represents the correctly initialized object of class `Edge`, return of the `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**: Provides operating system-dependent functionality, specifically used to get system environment variable using `os.environ.get('LOCALAPPDATA')` to get local application data folder.
*   **`pathlib.Path`**: Used for handling file paths, constructing path to executable file or profile directory, checking file existence.
*  **`typing.Optional`, `typing.List`**: Used for type annotations, which help with code readability and prevent type-related bugs.
*   **`selenium.webdriver.Edge as WebDriver`**: Imports the `Edge` class from Selenium for browser automation, aliasing it as `WebDriver`.
*   **`selenium.webdriver.edge.service import Service as EdgeService`**:  Imports the `Service` class for setting up the driver executable path using `EdgeService(executable_path=str(edgedriver_path))`.
*   **`selenium.webdriver.edge.options import Options as EdgeOptions`**: Imports the `Options` class from Selenium to setup browser options.
*  **`selenium.common.exceptions import WebDriverException`**: Imports the exception class used to handle selenium webdriver errors.
*   **`src`**: Imports the global settings object `gs` from the `src` package.
*   **`src.webdriver.executor import ExecuteLocator`**: Imports the `ExecuteLocator` class for handling interactions with web elements.
*   **`src.webdriver.js import JavaScript`**: Imports the `JavaScript` class for executing javascript on a web page.
*   **`fake_useragent import UserAgent`**: Used to generate fake user agents, with `UserAgent().random`.
*  **`src.logger.logger import logger`**: Used for logging messages and errors.
*   **`src.utils.jjson import j_loads_ns`**: Used to load settings from a JSON file with `j_loads_ns()`.

**Classes:**

*   **`Edge(WebDriver)`**:
    *   **Purpose**: Extends Selenium's `webdriver.Edge` with additional functionalities, such as setting profile, handling proxy and user agent.
    *   **Attributes**:
        *   `driver_name` (`str`): String that stores the driver name, which is `edge`.
    *   **Methods**:
        *  `__init__(self, profile_name, user_agent, options, window_mode, *args, **kwargs)`: Initializes the Edge WebDriver with custom settings, including reading options from `edge.json`, setting user agent and profile directory, and setting up proxies.
        *   `_payload(self)`: Sets payload for JavaScript execution, and maps locator methods.
         *   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`: Creates and configures launch options for Edge WebDriver.

**Functions:**

*   **`__init__(self, profile_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *   `profile_name` (`Optional[str]`): Name of the profile.
        *   `user_agent` (`Optional[str]`):  User agent string.
        *   `options` (`Optional[List[str]]`): List of chrome options.
        *  `window_mode` (`Optional[str]`): Browser window mode (`kiosk`, `windowless`, or `full_window`).
        *   `*args`, `**kwargs`: Additional arguments for selenium `WebDriver` constructor.
    *   **Purpose**: Initializes a new instance of the `Edge` class, setting up the web driver with custom settings.
    *   **Return**: `None`.
*  **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Edge`).
    *   **Purpose**:  Sets the JavaScript helper and `ExecuteLocator` instances.
    *   **Return**: `None`.
*    **`set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`**:
     *  **Arguments**: `opts` (`Optional[List[str]]`): List of `EdgeOptions`.
     *  **Purpose**: Initializes and configures launch options for the Edge WebDriver.
     *   **Return**: `EdgeOptions` object.

**Variables:**

*   `driver_name` (`str`): Stores the driver name which is set to `edge`.
*  `user_agent` (`str`):  User agent string.
*    `settings` (`SimpleNamespace`): Object that holds the settings from the `edge.json` file.
*    `options_obj` (`EdgeOptions`):  Object, which stores Edge options.
*   `profile_directory` (`str`): Stores path to the profile directory.
*   `j` (`JavaScript`):  Instance of the `JavaScript` class.
*   `edgedriver_path` (`str`): Path to the edge driver.
*   `service` (`EdgeService`): Instance of `EdgeService`, which is used to initialize the edge driver.
*   `execute_locator` (`ExecuteLocator`): Instance of `ExecuteLocator` class.
* `opts` (`Optional[List[str]]`): List of chrome options, which can be passed to `set_options` method.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: The `j_loads_ns` for loading settings could have more specific error handling.
*   **Hardcoded Paths**: The path to settings json file is hardcoded, and can be improved by using `gs.path` to build path for configurations.
*   **Profile Directory Handling**: The logic for setting profile directories is complex and could be simplified.
*    **Error Handling**: While some error handling is present, it can be improved by adding more specific exceptions for selenium initialization, and adding more logging.
*   **Type Hinting**:  Add more specific type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is a part of the `src.webdriver` package.
*   It uses the `src.webdriver.executor` and `src.webdriver.js` to provide extended functionalities.
*   It uses `src.utils.jjson` to load the configuration from a JSON file.
*   It uses the `src.logger.logger` module for logging.
*   It also uses global settings object `gs` from `src` package.
*    It depends on selenium library for web browser automation.

This detailed explanation provides a comprehensive understanding of the `edge.py` module, its functionality, and how it integrates with other parts of the project.