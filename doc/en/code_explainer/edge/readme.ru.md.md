## <algorithm>

### Workflow of the Edge WebDriver Module

This document describes the custom Edge WebDriver module, detailing how it uses configurations from `edge.json` and other project components.

1.  **Initialization (`__init__`)**:
    *   The `Edge` class is initialized with optional parameters, including `profile_name`, `user_agent`, `options`, `window_mode`, and other `*args` and `**kwargs` for the WebDriver.
    *   **Example**: `driver = Edge(user_agent='custom_user_agent', options=['--headless'])`
    *   It sets the user-agent by using the passed parameter, or generates a random user agent with `fake_useragent`.
    *   Loads settings from `edge.json` using `j_loads_ns`, converting it to a `SimpleNamespace`.
    *   Initializes `EdgeOptions` object.
    *   Adds the user agent to the options using f-string interpolation.
    *   Sets window mode from config or provided parameter, adding corresponding arguments: `--kiosk`, `--headless`, or `--start-maximized`.
    *   Adds the custom options passed during initialization to `options_obj`.
    *   Adds options defined in the `edge.json` settings file to `options_obj`.
    *   Adds headers from the `headers` section in the loaded `edge.json` configuration to `options_obj`.
    *  Sets the profile directory, using  `profiles.os` from settings or by building internal path using `profiles.internal`.
    *   If `profile_name` parameter is present during init, creates a subfolder for profile using the provided profile name.
    *  Replaces `%LOCALAPPDATA%` with environment variable.
    *   Initializes the `WebDriver` using `super().__init__`, passing the configured `options_obj` and a service using the path to the driver executable specified in `settings.executable_path.default`.
    *  Calls `_payload()` to setup JavaScript methods and locator execution.
    *    If any `WebDriverException` occurs during initialization, it logs it as a critical error and returns.
    *    Handles general exceptions and logs them using `logger.critical` before returning.

2.  **Setting Payload (`_payload`)**:
    *   This method initializes the `JavaScript` helper and maps locator methods to the class.
    *   **Example**: `self._payload()`
    *   Initializes a `JavaScript` instance with the current `WebDriver` instance.
    *    Assigns `JavaScript` methods to `Edge` instance: `self.get_page_lang = j.get_page_lang` and others.
    *   Initializes an `ExecuteLocator` object with the current `WebDriver` instance.
    *   Maps `ExecuteLocator` methods to the `Edge` instance to allow to call them directly: `execute_locator`, `get_webelement_as_screenshot`, etc.

3.  **Setting Options (`set_options`)**:
    *   Takes an optional list of options (`opts`).
    *   **Example**: `options = self.set_options(["--headless"])`
    *   Initializes a new `EdgeOptions` object.
    *  If `opts` is provided, it iterates through each option, and adds it to the options object.
    *   Returns created `EdgeOptions` object.

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
    *   The core of the module, responsible for creating and configuring the Edge WebDriver instance by inheriting `selenium.webdriver.Edge`, and extending it's functionality with methods to setup profiles, handle proxy, user agent and JavaScript execution.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
    *   **`AH`**:  The fully initialized object with the payload, a return value of the `_payload` method.
    *   **`T`**:   The `EdgeOptions` object, a return value of the `set_options` method.
    *   **`O`**:  The correctly initialized object of `Edge`, a return value of the `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**: Used to access system-specific parameters and functions, such as for getting the local application data path with `os.environ.get('LOCALAPPDATA')` which can be used to setup profile directory.
*    **`pathlib.Path`**: Used for handling file paths, creating a `Path` object for the chromedriver executable and to build the paths for profiles, and settings.
*   **`typing.Optional`, `typing.List`**: Used for type hinting, which helps with code clarity.
*   **`selenium.webdriver.Edge as WebDriver`**: Imports the `Edge` class from Selenium, aliasing it as `WebDriver` for more convenient use.
*   **`selenium.webdriver.edge.service import Service as EdgeService`**: Imports the `Service` class to initialize the driver executable with `EdgeService(executable_path=str(edgedriver_path))`.
*   **`selenium.webdriver.edge.options import Options as EdgeOptions`**: Imports the `Options` class for creating Edge options for browser setup, and adding options.
*   **`selenium.common.exceptions import WebDriverException`**: Imports `WebDriverException` to handle Selenium errors.
*   **`src`**: Used to import global settings object `gs` from the `src` package, to resolve paths for configuration files.
*   **`src.webdriver.executor import ExecuteLocator`**: Imports the `ExecuteLocator` class, used for handling locators and performing actions on web elements.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` class for executing javascript on a web page.
*   **`fake_useragent import UserAgent`**: Used to generate fake user agents, with `UserAgent().random`.
*  **`src.logger.logger import logger`**: Used for logging messages and errors.
*   **`src.utils.jjson import j_loads_ns`**:  Used to load settings from a JSON file using `j_loads_ns()`.

**Classes:**

*   **`Edge(WebDriver)`**:
    *   **Purpose**: Extends Selenium's `webdriver.Edge` for improved control over browser automation by integrating settings from config files, and providing methods to setup custom user agent and profile directories.
    *   **Attributes**:
        *   `driver_name` (`str`): Stores the driver name, which is set to `'edge'`.
    *  **Methods**:
        *   `__init__(self, profile_name, user_agent, options, window_mode, *args, **kwargs)`: Initializes Edge WebDriver with provided parameters by creating `EdgeOptions` and loading configs from `edge.json` file, and using service for starting driver with `super().__init__` call.
        *   `_payload(self)`: Sets payload for executing JavaScript and location operations, by mapping method calls to the class instance.
         *    `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`: Creates and configures launch options for Edge WebDriver.

**Functions:**

*   **`__init__(self, profile_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
        *   `profile_name` (`Optional[str]`): Optional parameter for profile name.
        *   `user_agent` (`Optional[str]`): Optional string parameter that represents user agent.
        *   `options` (`Optional[List[str]]`): Optional list of chrome options.
        *  `window_mode` (`Optional[str]`):  Optional parameter, a string that specifies window mode (`kiosk`, `windowless`, or `full_window`).
        *    `*args`, `**kwargs`:  Additional arguments passed to the parent constructor.
    *   **Purpose**: Initializes a new instance of the `Edge` class, setting up the web driver with the custom settings.
    *   **Return**: `None`.
*    **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Edge` class).
    *   **Purpose**: Sets the JavaScript helper and `ExecuteLocator` instances, mapping its methods to class instance to allow for correct workflow.
    *   **Return**: `None`.
*    **`set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`**:
     *   **Arguments**:
        *   `opts` (`Optional[List[str]]`): Optional list of options to add to webdriver options.
    *   **Purpose**: Creates and configures launch options for the Edge WebDriver.
    *   **Return**: `EdgeOptions` object.

**Variables:**

*  `driver_name` (`str`): String representing the driver name, set to `edge`.
*   `user_agent` (`str`): A string value for the user agent setting of the browser.
*   `settings` (`SimpleNamespace`): Settings from `edge.json`, loaded using `j_loads_ns`.
*   `options_obj` (`EdgeOptions`): An object, that stores options for Edge browser.
*  `profile_directory` (`str`): String with the path of the profile directory.
*    `j` (`JavaScript`): Instance of `JavaScript` helper.
*   `edgedriver_path` (`str`): Path to the msedgedriver executable.
*    `service` (`EdgeService`): Instance of `EdgeService` used to start driver.
*   `execute_locator` (`ExecuteLocator`): Instance of the `ExecuteLocator` class.
* `opts` (`Optional[List[str]]`): Optional list of options passed to the set_options method.

**Potential Errors and Areas for Improvement:**

*   **Settings Loading**: The `j_loads_ns` for loading settings should have more specific error handling.
*  **Hardcoded Paths**: The path to the settings JSON file is hardcoded and should be resolved using `gs` object.
*   **Profile Directory Handling**: The profile directory logic is complex and can be simplified using `pathlib` and more structured settings.
*  **Error Handling**: While some error handling is present, it can be improved with more specific exceptions and logging, for example by logging errors from selenium.
*   **Type Hinting**: Some variables and parameters can benefit from more precise type hinting.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package.
*   It uses the `src.webdriver.executor` and `src.webdriver.js` modules for locator handling and JavaScript execution.
*   It uses `src.utils.jjson` for loading configuration files.
*  It uses the `src.logger.logger` for logging errors and messages.
* It utilizes `fake_useragent` library to generate user agent strings.
*  It relies on the global settings object `gs` from `src` package.

This detailed explanation provides a comprehensive understanding of the `edge.py` module, its functionalities, and its interactions with other parts of the project.