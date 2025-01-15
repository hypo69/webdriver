## <algorithm>

### Workflow of the `crawlee_python.py` Module

The `crawlee_python.py` module implements a custom web crawler using the `crawlee` and `playwright` libraries. Here's a step-by-step breakdown of its workflow:

1.  **Initialization (`__init__`)**:
    *   The `CrawleePython` class is initialized with optional parameters like `max_requests`, `headless`, `browser_type`, and `options`.
    *   **Example**: `crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox')`
    *   The constructor stores these parameters as attributes: `self.max_requests`, `self.headless`, `self.browser_type`, and `self.options`. It initializes `self.crawler` to `None`.

2.  **Setting up the Crawler (`setup_crawler`)**:
    *   Initializes `PlaywrightCrawler` instance using the values from class attributes.
        *    **Example**: `await self.setup_crawler()`
    *   Defines a default request handler using the `@self.crawler.router.default_handler` decorator, which is executed for every URL visited by the crawler.
    *  The request handler performs following actions:
        *   Logs the URL being processed using `context.log.info(f'Processing {context.request.url} ...')`.
        *   Enqueues all links found on the page using `await context.enqueue_links()`.
        *   Extracts data from the page, including the URL, title, and first 100 characters of the page's content and stores it in `data` dictionary.
        *   Pushes extracted data to the dataset using `await context.push_data(data)`.

3.  **Running the Crawler (`run_crawler`)**:
    *   Takes a list of URLs as input.
    *   **Example**: `await self.run_crawler(['https://example.com'])`
    *   Runs the crawler using `self.crawler.run(urls)`, it starts crawling process from the provided urls.

4.  **Exporting Data (`export_data`)**:
    *   Takes a `file_path` (string) as input.
    *   **Example**: `await self.export_data('results.json')`
    *   Exports the dataset gathered by crawler to a JSON file at the specified path.

5. **Getting Data (`get_data`)**:
    *   Takes no input parameters.
    *   **Example**: `data = await self.get_data()`
    *   Retrieves the data collected by the crawler and returns a dictionary.

6.  **Main Run Method (`run`)**:
    *   Takes a list of URLs as input.
    *   **Example**: `await self.run(['https://example.com'])`
    *   It orchestrates the entire process:
        *  Calls `setup_crawler()` to initialize the crawler.
        * Calls `run_crawler(urls)` to start crawling from given urls.
        *  Calls `export_data` to save data into `results.json` file located in the `tmp` folder.
        *  Retrieves the data using `get_data` method.
        *   Logs the retrieved data using `logger.info`.
    *   If exception occurs during any step, it catches it, logs the error and returns.

## <mermaid>

```mermaid
flowchart TD
    subgraph CrawleePython Class
        A[__init__ <br> (max_requests, headless, browser_type, options)] --> B[Set attributes]
        B --> C[Instance of CrawleePython]

        D[setup_crawler] --> E[Initialize PlaywrightCrawler]
        E --> F[Define request handler <br> using router.default_handler]
         F --> G[Log processing URL]
        G --> H[Enqueue links]
        H --> I[Extract URL, title, content from page]
         I --> J[Push data to dataset]
         J --> K[Crawler setup complete]

        L[run_crawler <br> (urls: List[str])] --> M[Run the crawler using crawler.run()]
         M --> N[Crawling Complete]

        O[export_data <br> (file_path: str)] --> P[Export dataset to a JSON file]
        P --> Q[Export Complete]

        R[get_data] --> S[Retrieve the data]
        S --> T[Return extracted data]

        U[run <br> (urls: List[str])] --> V[Call setup_crawler]
         V --> W[Call run_crawler(urls)]
         W --> X[Call export_data]
        X --> Y[Call get_data]
        Y --> Z[Log the extracted data]
        Z --> AA[Return]
    end
      subgraph Global Dependencies
        classDef global fill:#f9f,stroke:#333,stroke-width:2px
         
        AA:::global
        T:::global
        Q:::global
         N:::global
         K:::global
        C:::global
    end
```

### Dependencies Analysis:

1.  **`CrawleePython Class`**:
    *   The core of the module, responsible for creating and configuring the `PlaywrightCrawler` instance. It handles the logic of crawling, data extraction and exporting of data to the file system.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
    *   **`AA`**: End of the `run` method, with logging of extracted data.
    *   **`T`**: Return value of `get_data` method, the dictionary with extracted data.
    *   **`Q`**:  End of the  `export_data` method, indicating that data was exported.
    *   **`N`**: End of the  `run_crawler` method, indicating that crawling is complete.
    *   **`K`**: End of the `setup_crawler` method, indicating the crawler is ready.
    *    **`C`**:  Instance of `CrawleePython` class, result of `__init__`.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`pathlib.Path`**: Used for handling file paths. Used here to create path to the results file with `Path(gs.path.tmp / 'results.json')`
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations.
*    **`src`**: Used to import global settings object `gs`, which is used to create path to the results file.
*   **`asyncio`**: Used for asynchronous operations.
*   **`crawlee.playwright_crawler.PlaywrightCrawler`**: Imports the `PlaywrightCrawler` class from the `crawlee` library, used for web crawling.
*   **`crawlee.playwright_crawler.PlaywrightCrawlingContext`**:  Imports the `PlaywrightCrawlingContext` used in the request handler.
*   **`src.logger.logger import logger`**:  Used for logging messages and errors using custom logger.
*  **`src.utils.jjson import j_loads_ns`**: Used for loading configurations from a JSON file using `j_loads_ns`, but not used in the code itself.

**Classes:**

*   **`CrawleePython`**:
    *   **Purpose**: Provides a custom implementation of `PlaywrightCrawler`, encapsulating configurations and handling of web scraping tasks.
    *   **Attributes**:
        *   `max_requests` (`int`):  Maximum number of requests during the crawl.
        *   `headless` (`bool`): Whether to run the browser in headless mode.
        *    `browser_type` (`str`):  Browser type to use (`chromium`, `firefox`, or `webkit`).
        *   `options` (`Optional[List[str]]`): List of browser options.
        *    `crawler` (`Optional[PlaywrightCrawler]`): Instance of the `PlaywrightCrawler`.
    *   **Methods**:
        *   `__init__(self, max_requests, headless, browser_type, options)`: Initializes the `CrawleePython` instance with specified parameters.
        *   `setup_crawler(self)`:  Sets up the `PlaywrightCrawler` instance, defining a default request handler.
        *   `run_crawler(self, urls)`: Runs the crawler with given URL list.
        *   `export_data(self, file_path)`: Exports the data to JSON file.
        *   `get_data(self) -> Dict[str, Any]`: Returns the extracted data.
        *    `run(self, urls)`: Main method which sets up, runs crawler and exports collected data.

**Functions:**

*   **`__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`**:
    *   **Arguments**:
        *   `max_requests` (`int`, default: 5): Max number of requests.
        *    `headless` (`bool`, default: `False`):  Boolean to run browser in headless mode or not.
        *   `browser_type` (`str`, default: `'firefox'`):  Browser type (`'chromium'`, `'firefox'`, `'webkit'`).
        *    `options` (`Optional[List[str]]`, default: `None`): List of options for browser.
    *   **Purpose**: Initializes the `CrawleePython` class with specified settings.
    *   **Return**: `None`.
*   **`setup_crawler(self)`**:
    *   **Arguments**: `self` (instance of `CrawleePython`).
    *   **Purpose**: Initializes PlaywrightCrawler and default request handler.
    *  **Return**: `None`.
*   **`run_crawler(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`):  List of urls to start crawling from.
    *   **Purpose**: Runs the crawler with given URLs.
    *   **Return**: `None`.
*  **`export_data(self, file_path: str)`**:
    *   **Arguments**: `file_path` (`str`):  Path to file, where data should be saved.
    *   **Purpose**: Exports the collected dataset to a JSON file.
    *   **Return**: `None`.
*   **`get_data(self) -> Dict[str, Any]`**:
    *   **Arguments**: `self` (instance of `CrawleePython`).
    *   **Purpose**: Gets all data that was collected by the crawler.
    *   **Return**: `Dict[str, Any]`, a dictionary with extracted data.
*    **`run(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`): List of URLs to be processed.
    *   **Purpose**: Runs the main workflow of the crawler: setup, run, export and logs the data.
    *   **Return**: `None`.

**Variables:**

*   `max_requests` (`int`): Maximum number of requests during the crawl.
*   `headless` (`bool`): Whether to run the browser in headless mode.
*   `browser_type` (`str`): Type of browser (`'chromium'`, `'firefox'`, `'webkit'`).
*   `options` (`List[str]`): List of browser options.
*   `crawler` (`Optional[PlaywrightCrawler]`): Instance of `PlaywrightCrawler` class.
*  `urls` (`List[str]`): List of URL strings.
*  `file_path` (`str`): String representing the path to file.
*  `data` (`Dict[str, Any]`): Dictionary containing extracted data.

**Potential Errors and Areas for Improvement:**

*   **Missing Configuration**: There is no handling of loading configuration from file, all parameters are passed directly to the `CrawleePython` constructor, it may be better to load settings from config file, similar to other classes of the project.
*   **Error Handling**: The `try-except` block in `run` method is too broad. It should catch specific exceptions and provide more detailed logging for specific types of errors.
*  **Hardcoded Output Path**: The output path for data export is hardcoded, it should use `gs` module and settings.
*  **Type Hinting**: Some methods can benefit from more specific type hints.

**Relationship Chain with Other Parts of Project:**

*   This module is designed to be part of `src.webdriver` package, which is responsible for web automation and data extraction.
*  It utilizes  `src.logger.logger` for logging.
*  It depends on the global settings object `gs` to define a path to a file where the result of crawling is stored.
*   It uses `crawlee` library for web crawling.
*   It does not use `j_loads_ns` method from the `src.utils.jjson` module, although it is imported.

This detailed explanation provides a comprehensive understanding of the `crawlee_python.py` module and its interaction with other parts of the project.