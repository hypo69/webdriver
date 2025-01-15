## <algorithm>

### Workflow of the Crawlee Python Module

This document outlines the functionality of the Crawlee Python module, describing how it fetches web content using the `PlaywrightCrawler` from the `crawlee` library, and how it uses a JSON configuration file.

1.  **Initialization (`__init__`)**:
    *   The `CrawleePython` class is initialized with optional parameters such as `max_requests`, `headless`, `browser_type` and `options`.
    *   **Example**: `crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=["--headless"])`
    *   These parameters are assigned as attributes `self.max_requests`, `self.headless`, `self.browser_type`, and `self.options`.
     * The attribute `self.crawler` is set to None, to store the `PlaywrightCrawler` instance.

2.  **Setting up the Crawler (`setup_crawler`)**:
    *   This method initializes an instance of `PlaywrightCrawler` from the `crawlee` library.
    *   **Example**: `await self.setup_crawler()`
    *   It sets `max_requests_per_crawl`, `headless`, `browser_type`, and `launch_options` (from list of options) using parameters passed to the `__init__` method.
    *   It defines a default request handler using `@self.crawler.router.default_handler`.
        *   The handler logs the URL being processed using `context.log.info()`.
        *  It enqueues all links found on the current page using `context.enqueue_links()`.
        *   It extracts the current URL, title, and first 100 chars of the content from page using playwright's context API, and saves data to the dict.
        *    Pushes the extracted data to the default dataset using `context.push_data()`.

3.  **Running the Crawler (`run_crawler`)**:
    *   Takes a list of URLs as input and starts the crawling.
    *   **Example**: `await self.run_crawler(['https://example.com'])`
    *   Uses `self.crawler.run(urls)` to run the crawler with the given list of URLs.

4.  **Exporting Data (`export_data`)**:
    *   Takes a `file_path` (string) as input, to specify the location where to store exported results.
    *   **Example**: `await self.export_data('results.json')`
    *   Exports the collected dataset to a JSON file at given path using `self.crawler.export_data(file_path)`.

5. **Getting Data (`get_data`)**:
    *   Takes no input parameters.
    *  **Example**: `data = await self.get_data()`
    *   Retrieves the data collected by the crawler and returns it as a dictionary using `await self.crawler.get_data()`.

6.  **Main Run Method (`run`)**:
    *   Takes a list of URLs as input, starts the crawler, saves data, and logs the results.
    *   **Example**: `await self.run(['https://example.com'])`
    *   It calls the `setup_crawler()` method to setup crawler with the options, then calls `run_crawler` method to start the crawling from provided list of urls.
    *   Exports the scraped data into `results.json` file located in `tmp` folder, by calling `export_data`.
    *    Retrieves data using `get_data` method and logs it using `logger.info`.
    *    If an exception occurs during any step, it logs a critical error and continues execution.

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
    *   The core of the module, responsible for creating and configuring the `PlaywrightCrawler` instance, defining a default request handler for data extraction, and providing methods for running, exporting data, and retrieving the results of the crawling.
2.  **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
      *  **`AA`**: End of `run` method, indicating that all actions were executed and the extracted data were logged.
    *  **`T`**: A dictionary containing extracted data from the crawled pages, the return value of method `get_data`.
    *  **`Q`**:  End of `export_data` method, representing successful export of data to the file system.
    *  **`N`**: End of `run_crawler` method, indicating that crawler has finished running.
    *   **`K`**: End of the `setup_crawler` method, indicating that crawler has been successfully initialized.
    *   **`C`**: Instance of the `CrawleePython` class, a return value of the `__init__` method.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`pathlib.Path`**: Used for handling file paths, to define path for a results file, such as `Path(gs.path.tmp / 'results.json')`.
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations.
*   **`src`**: Used to import global settings object `gs` from `src` package, specifically to get path to temp directory.
*  **`asyncio`**: Used for running asynchronous operations, specifically `asyncio.run(main())`.
*   **`crawlee.playwright_crawler.PlaywrightCrawler`**: Imports the `PlaywrightCrawler` class from the `crawlee` library, which provides functionality to crawl websites using playwright.
*   **`crawlee.playwright_crawler.PlaywrightCrawlingContext`**: Imports the `PlaywrightCrawlingContext` class, which provides context for web crawling.
*   **`src.logger.logger import logger`**: Used for logging errors, warnings, and general information with custom logger.
*    **`src.utils.jjson import j_loads_ns`**: Used to load JSON files into a `SimpleNamespace`, but it's not used in the code itself.

**Classes:**

*   **`CrawleePython`**:
    *   **Purpose**: Provides a custom implementation of `PlaywrightCrawler`, encapsulating configurations and handling of web scraping tasks.
    *   **Attributes**:
        *   `max_requests` (`int`): Maximum number of requests during the crawl.
        *   `headless` (`bool`): Whether to run the browser in headless mode.
        *   `browser_type` (`str`): Type of browser to use (`'chromium'`, `'firefox'`, or `'webkit'`).
        *   `options` (`Optional[List[str]]`): List of browser options.
        *   `crawler` (`Optional[PlaywrightCrawler]`):  Instance of the `PlaywrightCrawler` class.
    *   **Methods**:
        *   `__init__(self, max_requests, headless, browser_type, options)`: Initializes the `CrawleePython` instance.
        *   `setup_crawler(self)`:  Initializes the `PlaywrightCrawler` with specified options and default request handler.
        *  `run_crawler(self, urls)`: Runs the crawler using the provided urls as starting point.
        *   `export_data(self, file_path)`: Exports collected data to json file using crawlee's `export_data` method.
        *  `get_data(self) -> Dict[str, Any]`: Returns collected data as a dictionary.
        *   `run(self, urls)`: Sets up, runs and exports data of the crawler using provided urls.

**Functions:**

*   **`__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`**:
    *   **Arguments**:
        *   `max_requests` (`int`, default is 5): Maximum requests to perform.
        *   `headless` (`bool`, default is `False`):  Boolean to define headless mode.
        *   `browser_type` (`str`, default is `'firefox'`): Type of the browser.
        *  `options` (`Optional[List[str]]`, default is `None`): List of options to pass to the browser.
    *   **Purpose**: Initializes `CrawleePython` object and sets the attributes from the passed parameters.
    *   **Return**: None.
*   **`setup_crawler(self)`**:
    *   **Arguments**: `self` (instance of `CrawleePython` class).
    *   **Purpose**: Sets up PlaywrightCrawler and default request handler using options passed to the class.
    *   **Return**: `None`.
*   **`run_crawler(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`).
    *   **Purpose**: Runs the crawler with the list of URLs.
    *  **Return**: `None`.
*   **`export_data(self, file_path: str)`**:
    *   **Arguments**: `file_path` (`str`): path to save results.
    *   **Purpose**: Exports the collected dataset into a JSON file.
    *  **Return**: `None`.
*   **`get_data(self) -> Dict[str, Any]`**:
    *   **Arguments**: `self` (instance of `CrawleePython` class).
    *   **Purpose**: Gets all collected data from the crawler.
    *  **Return**: `Dict[str, Any]` : a dictionary with extracted data.
*   **`run(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`).
    *  **Purpose**: Sets up, runs the crawler, saves data and logs the results.
    *  **Return**: `None`.

**Variables:**

*   `max_requests` (`int`): The maximum number of requests during the crawl.
*   `headless` (`bool`): Whether to run the browser in headless mode.
*   `browser_type` (`str`): The type of browser to use (`'chromium'`, `'firefox'`, `'webkit'`).
*   `options` (`Optional[List[str]]`): A list of custom options for the browser.
*    `crawler` (`Optional[PlaywrightCrawler]`): A PlaywrightCrawler instance.
*   `urls` (`List[str]`): List of URLs to start the crawling from.
*   `file_path` (`str`): Path where results should be saved to.
*  `data` (`Dict[str, Any]`): Dictionary containing scraped data.

**Potential Errors and Areas for Improvement:**

*   **Configuration Loading**: The settings are not loaded from any external file, it would be better to use some configuration file, similar to other modules, for example `crawlee_python.json` file with parameters for `CrawleePython` class.
*   **Error Handling**: The `try-except` block in the `run` method is too broad, and could be improved by adding more specific exception handling and logging for different errors.
*   **Logging**: The logging in the request handler and main `run` method could be more detailed by adding data that is being logged, or the time it takes to finish some operations.
*   **Data Structure**: The structure of the extracted data can be made more flexible for different extraction scenarios.

**Relationship Chain with Other Parts of Project:**

*   This module is designed to be a part of the `src.webdriver` package and provides an implementation for web scraping using `crawlee` library.
*   It uses `src.logger.logger` for logging purposes.
*   It uses the global settings object from `src`.
*  It depends on `crawlee` for crawling implementation.
* It imports, but does not use `j_loads_ns` from `src.utils.jjson`.

This detailed explanation provides a comprehensive understanding of the `crawlee_python.py` module, its structure, functionalities, and interaction with other parts of the project.