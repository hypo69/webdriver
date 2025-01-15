## <algorithm>

### Workflow of the `edge.py` Module

The `edge.py` module defines a custom `Edge` class that extends Selenium's `webdriver.Edge` and provides additional functionalities such as custom user agents, window mode settings, and integration with JavaScript and locator execution.

1.  **Initialization (`__init__`)**:
    *   The `Edge` class is initialized with optional parameters for `profile_name`, `user_agent`, `options`, and `window_mode`, and other `*args` and `**kwargs` for `WebDriver`.
    *   **Example**: `driver = Edge(user_agent='custom_user_agent', options=['--headless'])`
    *   It sets the user agent, either passed as a parameter, or using `fake_useragent`.
    *   Loads settings from `edge.json` using `j_loads_ns`.
    *   Initializes `EdgeOptions` object.
    *   Adds a user-agent setting to the options using passed user agent or a random one from `fake_useragent`.
    *   Sets window mode from config or from parameter using `window_mode` key from settings or passed as argument. Adds corresponding arguments (`--kiosk`, `--headless`, or `--start-maximized`) to the `options_obj`.
    *   If the `options` parameter is not empty, it adds the provided options to the `options_obj`.
    *   Adds arguments from the `options` key from loaded `edge.json` configuration.
    *   Adds header arguments from loaded `edge.json` configuration using a loop through `settings.headers`, for every key and value pair in the headers, creates a new argument using f-string and adds it to the `options_obj`.
    *   Sets the user data directory by using the specified path from `profile_directory` key in settings, and sets an appropriate option to `options_obj` using`"--user-data-dir"`.
    *    If `profile_name` is specified during init, it will create a subfolder for profile in profile directory.
    *  Replaces `%LOCALAPPDATA%` in profile path with an environment variable, if it is present in the path.
    *   Initializes the `WebDriver` using `super().__init__`, passing the configured options, and a service, which initializes a driver using `edgedriver_path`.
    *    Calls `_payload()` to set JavaScript methods and locator execution functionalities.
    *   If a `WebDriverException` or general exception occurs, logs the error and returns from the constructor.

2.  **Setting Payload (`_payload`)**:
    *   Sets up JavaScript and locator execution by using helper methods and classes.
    *   **Example**: `self._payload()`
    *    Initializes the `JavaScript` helper object with the current `WebDriver` instance.
    *    Assigns `JavaScript` methods to the `Edge` instance to allow for calling them directly: `self.get_page_lang = j.get_page_lang` and so on.
    *   Initializes `ExecuteLocator` object by passing the current `WebDriver` instance.
    *    Maps the methods from the `ExecuteLocator` instance to the `Edge` instance to allow for easier calls: `self.execute_locator = execute_locator.execute_locator` and so on.

3.  **Setting Options (`set_options`)**:
     * Takes an optional list of options (`opts`).
     *   **Example**: `options = self.set_options(["--headless"])`
    *   Initializes a new `EdgeOptions` object.
    *   If `opts` is present, it iterates over the list and adds every option to the options object using `options.add_argument(opt)`.
    *  Returns created options object.

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
    *  The core of the module, extending Selenium's `webdriver.Edge` with added functionalities. It manages driver options, profiles, proxy settings, and javascript execution.
2.   **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, selenium methods, etc):
      *   **`AH`**: End of the `_payload` method, representing a fully initialized object with all attributes.
    *   **`T`**: Represents the options object, return of the `set_options` method.
    *  **`O`**: Represents a correctly initialized object of `Edge` class, end of `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`os`**: Used for operating system-dependent functionality, specifically `os.environ.get('LOCALAPPDATA')` to get local application data path for browser profiles.
*   **`pathlib.Path`**: Used for handling file paths, constructing paths to the chromedriver and profile directories, using methods like `Path(gs.path.src, settings.executable_path.chromedriver)`.
*   **`typing.Optional`, `typing.List`**: Used for type annotations, enhancing code readability and helping to prevent type-related bugs.
*   **`selenium.webdriver.Edge as WebDriver`**: Imports the `Edge` class from Selenium for browser automation, aliasing it as `WebDriver`.
*    **`selenium.webdriver.edge.service import Service as EdgeService`**: Imports `Service` class from Selenium to handle driver execution.
*   **`selenium.webdriver.edge.options import Options as EdgeOptions`**: Imports `Options` class from Selenium for creating driver options.
*   **`selenium.common.exceptions import WebDriverException`**: Imports exception to handle Selenium webdriver errors.
*   **`src`**: Used to import the global settings object `gs` from the `src` package.
*   **`src.webdriver.executor import ExecuteLocator`**: Used to import the `ExecuteLocator` class for handling interactions with web elements.
*   **`src.webdriver.js import JavaScript`**: Used to import the `JavaScript` class for executing javascript code on a web page.
*   **`fake_useragent import UserAgent`**: Used to generate fake user agents with `UserAgent().random`.
*   **`src.logger.logger import logger`**: Used for logging messages and errors.
*   **`src.utils.jjson import j_loads_ns`**: Used for loading settings from a JSON file with `j_loads_ns()`.

**Classes:**

*   **`Edge(WebDriver)`**:
    *   **Purpose**: Extends Selenium's `webdriver.Edge` to enable more specific and flexible automation of Microsoft Edge browsers.
    *   **Attributes**:
         * `driver_name` (`str`):  Stores the driver name, set to `'edge'`.
    *   **Methods**:
        *   `__init__(self, profile_name, user_agent, options, window_mode, *args, **kwargs)`: Initializes the `Edge` WebDriver with custom settings.
        *   `_payload(self)`: Sets payload for executing JavaScript and locators.
        *   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`: Creates and configures launch options for Edge WebDriver.

**Functions:**

*   **`__init__(self, profile_name: Optional[str] = None, user_agent: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`**:
    *   **Arguments**:
         *  `profile_name` (`Optional[str]`): The profile name.
         *   `user_agent` (`Optional[str]`): User-agent string.
         *    `options` (`Optional[List[str]]`): List of edge options.
        *    `window_mode` (`Optional[str]`):  String to specify window mode (`kiosk`, `windowless`, or `full_window`).
        *    `*args`, `**kwargs`: Additional arguments for selenium `WebDriver` constructor.
    *   **Purpose**: Initializes an instance of the `Edge` class by setting up the Edge WebDriver with given configurations.
    *   **Return**: `None`.
*   **`_payload(self) -> None`**:
    *   **Arguments**: `self` (instance of `Edge` class).
    *  **Purpose**: Configures the `JavaScript` helper and maps locator methods to `Edge` instance.
    *   **Return**: `None`.
*   **`set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`**:
    *  **Arguments**: `opts` (`Optional[List[str]]`): Optional list of options.
    *   **Purpose**: Creates `EdgeOptions` object and adds options from the `opts` list.
    *   **Return**: `EdgeOptions` object.

**Variables:**

*   `driver_name` (`str`):  String containing the driver name which is set to `"edge"`.
*   `user_agent` (`str`): String that represents the user agent value.
*    `settings` (`SimpleNamespace`): Parsed settings from the `edge.json` file.
*   `options_obj` (`EdgeOptions`):  Instance of selenium `EdgeOptions`, used to set up Edge driver settings.
*   `profile_directory` (`str`): String representing the path to the profile directory.
*   `j` (`JavaScript`): Instance of the `JavaScript` class.
*   `edgedriver_path` (`str`): String containing path to the `msedgedriver.exe` executable.
*  `service` (`EdgeService`): Instance of selenium `EdgeService`.
*    `execute_locator` (`ExecuteLocator`): Instance of `ExecuteLocator` class.

**Potential Errors and Areas for Improvement:**

*   **Configuration Loading**: The settings loading using `j_loads_ns` could use more specific error handling.
*   **Hardcoded Paths**: The path to the settings JSON file is hardcoded, and can be improved by using `gs.path` to build path for configurations.
*   **Profile Directory Handling**: The logic for handling profile directories is complex and could be simplified, using `Path` object for all file operations.
*  **Error Handling**: While basic error handling is present, it can be improved by adding more specific exception handling and logging.
*    **Type Hinting**: Some variables and parameters can benefit from more specific type hints.

**Relationship Chain with Other Parts of Project:**

*  This module is part of the `src.webdriver` package, and is used to create and configure the `Edge` webdriver instances.
*   It depends on `src.logger.logger` for logging.
*   It loads configuration parameters from `edge.json` file using `j_loads_ns` from `src.utils.jjson`.
*   It utilizes the `ExecuteLocator` from  `src.webdriver.executor` and `JavaScript` helper from  `src.webdriver.js` modules.
*   It uses `fake_useragent` to generate user agent strings.
*   It utilizes global settings from the `src` package.

This detailed explanation provides a comprehensive understanding of the `edge.py` module, its functionalities and interactions with other modules in the project.