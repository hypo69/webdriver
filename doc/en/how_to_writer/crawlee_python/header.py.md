How to use this code block
=========================================================================================

Description
-------------------------
The `header.py` module is designed to identify the project's root directory, add it to the Python system path, and load project metadata. It automatically determines the project root and makes project settings, documentation, and project information accessible as global variables.

Execution steps
-------------------------
1.  **Import necessary modules**: Ensure that `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib` are imported.
2.  **Set the project root**: The `set_project_root` function locates the project's root by searching upwards from the current file's directory for a directory containing the marker files (`__root__`, `.git`).
    - It uses a default tuple of marker files or a custom one that is passed as an argument.
    - If found, the project root directory is added to `sys.path` to enable the project's modules to be imported correctly.
3.  **Load settings**: The module attempts to load the project settings from a `settings.json` file located in the `src` directory relative to the determined root.
    - It handles `FileNotFoundError` and `json.JSONDecodeError` exceptions, so if the file is missing or corrupted, those are logged and no settings are loaded.
4.  **Load documentation**: The module attempts to load the project's documentation from the `README.MD` file also in the `src` directory relative to the project root.
    - It handles the `FileNotFoundError` exception when a file is not present or if its corrupted.
5.  **Define global project variables**: The module defines several global variables:
    -   `__project_name__`: The project's name loaded from `settings.json`, or defaults to `'hypotez'`.
    -   `__version__`: The project's version. If not in `settings.json` defaults to an empty string.
    -   `__doc__`: Project documentation loaded from `README.MD` or an empty string if the file is not found.
    -   `__details__`: An empty string.
    -   `__author__`: The project author loaded from `settings.json` or an empty string if not present in the file.
    -   `__copyright__`: The copyright info loaded from `settings.json` or an empty string if not present.
    -  `__cofee__`: The text to display a link to donate to the author, or a default link if not present in `settings.json`.

Usage example
-------------------------
```python
import sys
from pathlib import Path
from src.webdriver.crawlee_python.header import set_project_root, __root__, __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__

def main():
    # Example 1: Get the project root using default marker files
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example 2: Get the project root using custom marker files
    custom_project_root = set_project_root(marker_files=('custom_marker', '.git'))
    print(f"Project root with custom markers: {custom_project_root}")

    # Example 3: Check if the project root is in sys.path
    if project_root in sys.path:
        print("Project root is in sys.path")
    else:
        print("Project root is not in sys.path")

    # Example 4: Access the root via the global variable
    print(f"Project root from global variable: {__root__}")


    # Example 5: Display project metadata
    print(f"Project Name: {__project_name__}")
    print(f"Project Version: {__version__}")
    print(f"Project Author: {__author__}")
    print(f"Project Copyright: {__copyright__}")
    print(f"Project Documentation: {__doc__[:100]}...")
    print(f"Support the developer: {__cofee__}")



if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `header.py` module, explaining its functionality and purpose.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations about each step of the process, including how the project root is found, settings and documentation are loaded, and how global variables are accessed.
- Provided an example of how to use all global variables, such as `__project_name__`, `__version__`, `__doc__`, etc.
- Added an example of how to use custom marker files when calling the `set_project_root` function.