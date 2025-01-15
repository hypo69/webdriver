## <algorithm>

### Workflow of the Crawlee Python Module

This document describes the workflow of the Crawlee Python module, which uses the `crawlee` library to crawl websites and extract data, based on a JSON configuration file.

1.  **Initialization (`__init__`)**:
    *   The `CrawleePython` class is initialized with optional parameters: `max_requests`, `headless`, `browser_type`, and `options`.
    *   **Example**: `crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=["--headless"])`
    *   These parameters are stored in class attributes: `self.max_requests`, `self.headless`, `self.browser_type`, and `self.options`.
    *   The `self.crawler` is set to `None`.

2.  **Setting up the Crawler (`setup_crawler`)**:
    *   This method initializes the `PlaywrightCrawler` with the configurations defined in the `__init__` method using `PlaywrightCrawler` from the `crawlee` library.
    *   **Example**: `await self.setup_crawler()`
    *  It sets `max_requests_per_crawl`, `headless`, `browser_type` and `launch_options` from the class attributes.
    *   It sets up a default request handler using `@self.crawler.router.default_handler` decorator, to process every visited URL:
        *   It logs the URL being processed using  `context.log.info(f'Processing {context.request.url} ...')`.
        *    It enqueues all the links found on the current page using `await context.enqueue_links()`.
        *  It extracts the current URL, title, and first 100 characters of the page's content and saves it to the data dictionary.
        *   It then pushes extracted data to dataset using `await context.push_data(data)`.

3.  **Running the Crawler (`run_crawler`)**:
    *   Takes a list of URLs as input and starts the crawl.
    *   **Example**: `await self.run_crawler(['https://example.com'])`
    *   Runs the crawler with specified starting URLs using `self.crawler.run(urls)`.

4.  **Exporting Data (`export_data`)**:
    *   Takes a `file_path` (string) as input for saving results to a file.
    *    **Example**: `await self.export_data('results.json')`
    *   Exports all the data collected during crawl to a JSON file using `self.crawler.export_data(file_path)`.

5.  **Getting Data (`get_data`)**:
    *   Retrieves data extracted by the crawler.
    *   **Example**: `data = await self.get_data()`
    *  Returns dictionary with the collected dataset.

6.  **Main Execution Method (`run`)**:
    *   Takes a list of URLs as input and executes full workflow: setup, run, export, and log results.
    *   **Example**: `await self.run(['https://example.com'])`
    *   It calls the `setup_crawler()` method to prepare the crawler.
    *  Then it starts the crawling process by calling the `run_crawler()` method.
    *   Then calls `export_data` to save results to file (`results.json` in `tmp` folder).
    *   Retrieves data by calling the `get_data` method.
    *   Logs the collected data with `logger.info` function using a dictionary from `data.items()`.
    *   Handles exceptions using `try-except` block, logging critical errors with `logger.critical` function.

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
    *   The core of the module, responsible for creating and configuring the `PlaywrightCrawler` instance and managing the entire workflow of web crawling and data extraction.
2. **Global Dependencies**: Represents the outputs and interactions with the class and outer world (logger, playwright methods, etc):
    *   **`AA`**: End of the `run` method, with logging of extracted data.
    *   **`T`**: The dictionary with scraped data, return value of method `get_data`.
     *   **`Q`**:  End of method `export_data`, the result of data export.
     *   **`N`**: End of method `run_crawler`, the result of crawler run.
    *   **`K`**:  End of method `setup_crawler`, the crawler setup is complete.
    *   **`C`**: Instance of class `CrawleePython`, the return value of method `__init__`.

## <explanation>

### Detailed Explanation

**Imports:**

*   **`pathlib.Path`**: Used for handling file paths, specifically to create path for saving results to file with `Path(gs.path.tmp / 'results.json')`.
*   **`typing.Optional`, `typing.List`, `typing.Dict`, `typing.Any`**: Used for type annotations, helping code readability.
*   **`src`**: Used to import global settings object `gs`, for accessing temporary folder path.
*   **`asyncio`**: Used for asynchronous programming, particularly to use `asyncio.run(main())` in the example.
*    **`crawlee.playwright_crawler.PlaywrightCrawler`**: Imports the `PlaywrightCrawler` class from the `crawlee` library for web crawling, and is a main component of the class.
*   **`crawlee.playwright_crawler.PlaywrightCrawlingContext`**: Imports the `PlaywrightCrawlingContext` class, which provides context for the request handler.
*  **`src.logger.logger import logger`**: Used for logging, with `logger.info()` and `logger.critical()` calls.
*   **`src.utils.jjson import j_loads_ns`**: Used to load JSON settings into `SimpleNamespace` objects, it is not used in code.

**Classes:**

*   **`CrawleePython`**:
    *   **Purpose**: Provides a custom implementation of `PlaywrightCrawler`, encapsulates crawling process, parameters, and the data extraction flow.
    *   **Attributes**:
        *   `max_requests` (`int`): Maximum number of requests during a crawl.
        *   `headless` (`bool`): Boolean value to run browser in headless mode or not.
        *   `browser_type` (`str`): Type of browser to use (`'chromium'`, `'firefox'`, `'webkit'`).
        *  `options` (`Optional[List[str]]`):  List of browser options.
        *   `crawler` (`Optional[PlaywrightCrawler]`): Instance of the `PlaywrightCrawler` class.
    *   **Methods**:
        *   `__init__(self, max_requests, headless, browser_type, options)`: Initializes the `CrawleePython` instance.
        *   `setup_crawler(self)`: Sets up the `PlaywrightCrawler` instance and defines the request handler.
        *   `run_crawler(self, urls)`: Runs the crawler from the given starting urls.
        *   `export_data(self, file_path)`: Exports collected data into a JSON file.
        *    `get_data(self) -> Dict[str, Any]`: Returns collected data as dictionary.
        *   `run(self, urls)`: Sets up, runs the crawler, and exports results.

**Functions:**

*   **`__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`**:
    *   **Arguments**:
        *   `max_requests` (`int`, default is 5):  The maximum number of requests during crawling.
        *   `headless` (`bool`, default is `False`): A boolean value to define if the browser will be in headless mode or not.
        *    `browser_type` (`str`, default is `'firefox'`):  A string representing type of the browser (`chromium`, `firefox` or `webkit`).
        *    `options` (`Optional[List[str]]`, default is `None`): List of options for the browser.
    *  **Purpose**: Initializes `CrawleePython` object with provided parameters.
    *   **Return**: `None`.
*    **`setup_crawler(self)`**:
    *   **Arguments**: `self` (instance of `CrawleePython` class).
    *   **Purpose**: Sets up `PlaywrightCrawler` with the options set in `__init__`, also setting default request handler to process each page.
    *  **Return**: `None`.
*   **`run_crawler(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`): A list of URLs to start crawling from.
    *   **Purpose**: Runs the crawler with the specified URLs.
    *  **Return**: `None`.
*   **`export_data(self, file_path: str)`**:
     *  **Arguments**: `file_path` (`str`): The path to save the data to.
     *   **Purpose**: Exports the collected dataset to a JSON file.
     * **Return**: `None`.
*   **`get_data(self) -> Dict[str, Any]`**:
    *   **Arguments**: `self` (instance of `CrawleePython` class).
    *   **Purpose**: Retrieves extracted data.
    *   **Return**: `Dict[str, Any]` dictionary with scraped data.
*    **`run(self, urls: List[str])`**:
    *   **Arguments**: `urls` (`List[str]`): The list of URLs to start crawling from.
    *   **Purpose**:  Sets up, runs, and exports results of the crawler.
    *   **Return**: `None`.

**Variables:**

*   `max_requests` (`int`): Maximum number of requests during a crawl.
*  `headless` (`bool`): Indicates whether browser should run in headless mode.
*   `browser_type` (`str`): The browser type (e.g., `chromium`, `firefox`, `webkit`).
*   `options` (`List[str]`): List of options for playwright browser.
*   `crawler` (`PlaywrightCrawler`): Stores an instance of the `PlaywrightCrawler`.
*   `urls` (`List[str]`): List of starting URLs for crawling.
*   `file_path` (`str`): Path to the file, where results will be stored.
*  `data` (`Dict[str, Any]`): Dictionary with scraped data.

**Potential Errors and Areas for Improvement:**

*   **Configuration**: The settings are passed as parameters to constructor instead of loading them from an external config file.
*  **Error Handling**: The `try-except` block in the `run` method is very broad, making it difficult to understand what exactly went wrong. It could be improved by adding more granular exception handling for every operation.
*   **Logging**: More context and detail could be added to logging.
*  **Flexibility of Extraction Logic**: The way data is extracted (`title`, `content`) is hardcoded. More flexibility can be introduced by allowing user to provide a list of fields that are needed to be extracted.
*   **Type Hinting**:  Add more specific type hints for the returned data in methods.
*    **Missing Dependency**: Although `j_loads_ns` is imported, it is not used anywhere.

**Relationship Chain with Other Parts of Project:**

*   This module is part of the `src.webdriver` package.
*   It relies on the `crawlee` and `playwright` libraries for web crawling.
*   It uses `src.logger.logger` for logging.
*    It imports `gs` from `src` package to get path for temporary directory, where results file is saved.
*    It does not use `src.utils.jjson`, although it is imported.

This detailed explanation provides a comprehensive understanding of the `crawlee_python.py` module and how it integrates with other parts of the project.