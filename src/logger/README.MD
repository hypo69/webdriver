```rst
.. module:: src.logger
```
<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> /

</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/logger/readme.ru.md'>Русский</A>
</TD>
</TABLE>

### Documentation for the `src.logger` Module

The `src.logger` module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application. The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

---


## File Descriptions

### `exceptions.py`

This file defines a set of custom exceptions that extend the base `Exception` class in Python.  These custom exceptions are designed to provide more specific error handling within the application, making it easier to identify and address issues.  The file also imports necessary exception classes from `pykeepass` (with a fallback in case `pykeepass` isn't installed) and `selenium`.

**Purpose:** Provides custom exception classes for better error handling and logging.

**Key Classes:**

*   **`CustomException`**: Base class for all custom exceptions in the application.  It includes functionality for logging the exception and the original exception that caused it.  It's designed to be subclassed by more specific exception types.

    *   **Attributes:**
        *   `original_exception` (Optional[Exception]): The original exception that caused this custom exception, if any.
        *   `exc_info` (bool): A flag to indicate if exception information should be logged.
    *   **Methods:**
        *   `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Initializes the `CustomException` with a message and an optional original exception.
        *   `handle_exception(self)`: Handles the exception by logging the error and original exception, if available.  This method can be extended in subclasses to include additional error handling logic.

*   **`FileNotFoundError`**: Raised when a file is not found.  Inherits from both `CustomException` and `IOError`.

*   **`ProductFieldException`**: Raised for errors related to product fields.  Inherits from `CustomException`.

*   **`KeePassException`**: Raised for connection issues with a KeePass database. Inherits from `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin` from `pykeepass` (or fallback classes if `pykeepass` is not installed).

*   **`DefaultSettingsException`**: Raised for issues with default settings. Inherits from `CustomException`.

*   **`WebDriverException`**: Raised for WebDriver-related issues. Inherits directly from `selenium.common.exceptions.WebDriverException`.

*   **`ExecuteLocatorException`**: Raised for errors related to locator executors. Inherits from `CustomException`.

*   **`PrestaShopException`**: Generic exception for PrestaShop WebService errors.  Provides detailed error information specific to PrestaShop.

    *   **Attributes:**
        *   `msg` (str): A custom error message.
        *   `error_code` (Optional[int]): The error code returned by the application.
        *   `ps_error_msg` (str): The error message from PrestaShop.
        *   `ps_error_code` (Optional[int]): The PrestaShop error code.

    *   **Methods:**
        *   `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Initializes the `PrestaShopException` with the provided message and error details.
        *   `__str__(self)`: Returns the string representation of the exception.

*   **`PrestaShopAuthenticationError`**: Raised for PrestaShop authentication errors. Inherits from `PrestaShopException`.

**Dependencies:**

*   `typing`
*   `src.logger.logger` (specifically, the `logger` instance)
*   `selenium.common.exceptions.WebDriverException`
*   `pykeepass` (optional)
*  `header` (appears to be a project-specific header file)

### `logger.py`

This file implements a Singleton logger class that provides console, file, and JSON logging. It uses the `logging` module and `colorama` for colored console output.

**Purpose:** Provides a centralized, configurable logging system for the application.

**Key Classes:**

*   **`SingletonMeta`**: Metaclass for implementing the Singleton pattern, ensuring that only one instance of the `Logger` class exists.

*   **`JsonFormatter`**: Custom formatter for logging in JSON format.  This formatter creates JSON strings containing the log message, timestamp, level, and exception information.

*   **`Logger`**: The main logger class.  It manages multiple loggers (console, info file, debug file, errors file, and JSON file) and provides methods for logging messages at different levels.  It implements the Singleton pattern.

    *   **Attributes:**
        *   `log_files_path` (Path): The base path for log files, created using a timestamped directory.
        *   `info_log_path` (Path): Path to the info log file.
        *   `debug_log_path` (Path): Path to the debug log file.
        *   `errors_log_path` (Path): Path to the errors log file.
        *   `json_log_path` (Path): Path to the JSON log file.
        *   `logger_console` (logging.Logger): Logger for console output.
        *   `logger_file_info` (logging.Logger): Logger for info log file.
        *   `logger_file_debug` (logging.Logger): Logger for debug log file.
        *   `logger_file_errors` (logging.Logger): Logger for errors log file.
        *   `logger_file_json` (logging.Logger): Logger for JSON log file.

    *   **Methods:**
        *   `__init__(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None)`: Initializes the `Logger` instance, configures file paths, creates directories and files, and sets up the different loggers. It reads configuration from `src/config.json`.
        *   `_format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None)`: Formats the log message, adding color and exception information. Uses the `LOG_SYMBOLS` dictionary for log level icons.
        *   `_ex_full_info(self, ex)`: Returns detailed exception information, including the filename, function name, and line number where the exception occurred.
        *   `log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None)`: General method to log messages at the specified level with optional color.
        *   `info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = "")`: Logs an info message.
        *   `success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = "")`: Logs a success message.
        *   `warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = "")`: Logs a warning message.
        *   `debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "")`: Logs a debug message.
        *   `exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray")`: Logs an exception message.
        *   `error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "")`: Logs an error message.
        *   `critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white")`: Logs a critical message.

**Dependencies:**

*   `logging`
*   `colorama`
*   `datetime`
*   `json`
*   `inspect`
*   `threading`
*   `pathlib`
*   `typing`
*   `header` (appears to be a project-specific header file)

**Configuration:**

The logger's file paths are configured using a `config.json` file located in the `src` directory.  This file should contain a `path` key with a `log` key inside it, specifying the base directory for logs. An example `config.json` structure is:

```json
{
  "path": {
    "log": "/path/to/your/logs"
  }
}
```

## Usage Examples

**`exceptions.py`:**

```python
from src.logger.exceptions import ProductFieldException, CustomException

try:
    # Code that might raise a product field error
    raise ProductFieldException("Invalid product field", e=ValueError("Field is empty"))
except ProductFieldException as e:
    # Handle the exception
    print(f"Error: {e}")

try:
    #simulate file not found error
    with open("nonexistent_file.txt", "r") as f:
        pass
except FileNotFoundError as e:
    print(f"File not found error: {e}")

except CustomException as e:
    print(f"Custom Exception: {e}")
```

**`logger.py`:**

```python
from src.logger.logger import logger

logger.info("This is an informational message.")
logger.debug("This is a debug message.", exc_info=True)
logger.warning("This is a warning message.", ex=ValueError("Something went wrong"))
logger.error("This is an error message.", ex=Exception("Generic error"))
logger.critical("This is a critical message.")

try:
  1/0
except Exception as e:
  logger.exception("An exception occurred", ex=e)

logger.success("Operation completed successfully!", text_color="blue", bg_color="light_yellow")
```

## Additional Notes

*   The `header.py` file, imported in both `exceptions.py` and `logger.py`, is assumed to contain project-specific header information and global variables, such as the root directory of the project (`__root__`).  Its content is not shown in the provided files.  It likely defines the `__root__` variable.

*   The `LOG_SYMBOLS` dictionary in `logger.py` allows you to customize the icons used for different log levels.

*   The JSON logging format in `logger.py` is customizable through the `JsonFormatter` class.

*   The fallback implementation for `pykeepass` exceptions in `exceptions.py` is a good practice for handling optional dependencies.

*   Consider adding more comprehensive unit tests for both the exception handling and logging functionalities.
```