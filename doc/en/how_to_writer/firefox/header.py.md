How to use this code block
=========================================================================================

Description
-------------------------
This `header.py` module is designed to identify the root directory of a project, add it to the Python system path, and load project metadata. It determines the project's root directory by searching upwards for specific marker files, loads settings from a `settings.json` file, and reads project documentation from a `README.MD` file. All these are accessible via global variables within the project.

Execution steps
-------------------------
1.  **Import necessary modules**: The module imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.
2.  **Set project root**: The `set_project_root` function is called to locate the project's root.
    - It searches upwards from the current file's directory for a directory containing the marker files (`__root__`, `.git`).
    -   The function accepts an optional `marker_files` tuple that defaults to  `('__root__', '.git')`.
    -  If a directory with marker files is found the path is set as `__root__`, or if not, the path of the directory containing the script will be used.
    -   The resolved project root directory path is added to the system path, ensuring that project modules can be imported.
3.  **Load settings**: The module attempts to load settings from a `settings.json` file located in the `src` directory relative to the project root.
    - It catches `FileNotFoundError` and `json.JSONDecodeError`, so if file is not present or corrupted, no settings will be loaded.
4.  **Load documentation**: The module attempts to load project documentation from a `README.MD` file, also in the `src` directory relative to the project root.
     - It handles `FileNotFoundError` and if file is not found the doc string will be empty.
5.  **Define global project variables**: The module defines the following global variables based on the loaded settings and documentation:
    -   `__project_name__`: The project's name from `settings.json`, defaulting to `'hypotez'` if not present.
    -   `__version__`: The project's version from `settings.json`, defaulting to an empty string if not present.
    -   `__doc__`: The project's documentation from `README.MD`, defaulting to an empty string if the file was not found.
    -   `__details__`: An empty string.
    -   `__author__`: The project's author from `settings.json`, defaulting to an empty string if not present.
    -   `__copyright__`: The project's copyright information, defaulting to an empty string if not present.
    -   `__cofee__`: A message encouraging support of the developer, defaulting to a link to boosty if not present in the settings file.

Usage example
-------------------------
```python
import sys
from pathlib import Path
from src.webdriver.firefox.header import set_project_root, __root__, __project_name__, __version__, __doc__, __author__, __copyright__, __cofee__

def main():
    # Example 1: Get the project root using default marker files
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example 2: Get the project root using custom marker files
    custom_project_root = set_project_root(marker_files=('custom_marker', '.git'))
    print(f"Project root with custom markers: {custom_project_root}")

    # Example 3: Check if project root is in sys.path
    if project_root in sys.path:
        print("Project root is in sys.path")
    else:
        print("Project root is not in sys.path")

    # Example 4: Access project root using the global variable
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
- Provided a detailed description of the `header.py` module and its purpose.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for `set_project_root` function and all other steps in the module.
- Added examples that show how to use the global variables and methods in the `header.py` module.
- Added an example of how to use custom markers.
- Added examples showing the usage of each global variable.