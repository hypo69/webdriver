How to use this code block
=========================================================================================

Description
-------------------------
This `header.py` module is designed to locate the root directory of a project and add it to the Python system path. This ensures that modules within the project can be imported correctly regardless of the current working directory when a script is executed. The module searches upwards from the directory containing the current file until it finds a directory with any of the specified marker files.

Execution steps
-------------------------
1. **Import necessary modules**: The module imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.
2. **Call `set_project_root` function**: The function `set_project_root` is called and will attempt to locate the root directory using the predefined markers.
     - You can pass a custom tuple of marker filenames or directories as an argument or use the default tuple.
     - Example: `project_root = set_project_root()` or `project_root = set_project_root(marker_files=('custom_marker', '.git'))`
3. **Understand the function logic**:
     -  The function starts by setting the directory of the current file as the initial root.
    - It then iterates through all parent directories, checking for the existence of the specified `marker_files`.
    - If any of the `marker_files` are found, that directory is identified as the project root and assigned to variable `__root__`.
    -   If no markers are found, the initial directory of the script is set as the `__root__` directory.
4.  **Add root to System Path**:  The function checks if the determined `__root__` path is already present in the system path, and if not, it inserts it at the beginning of `sys.path`, ensuring modules can be imported.
5.  **Access the `__root__` variable**: The module defines a global variable named `__root__` which contains the determined path of project root, allowing other modules to use it.

Usage example
-------------------------
```python
import sys
from pathlib import Path
from src.webdriver.playwright.header import set_project_root, __root__


def main():
    # Example 1: Get the project root using default marker files
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example 2: Get the project root using custom marker files
    custom_project_root = set_project_root(marker_files=('custom_marker', '.git'))
    print(f"Project root with custom markers: {custom_project_root}")

    # Example 3: Check if the root directory is present in the system path
    if str(project_root) in sys.path:
         print("Project root is in sys.path")
    else:
        print("Project root is not in sys.path")

     # Example 4: Access the root directory path from global variable
    print(f"Project root from global variable: {__root__}")


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
- Added explanations for the `set_project_root` function, including how it finds the root directory and how it is added to system path.
- Updated the usage example to demonstrate how to use custom markers and verify if the project root has been added to the sys path, and how to access the `__root__` variable.