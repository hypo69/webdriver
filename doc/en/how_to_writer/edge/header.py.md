How to use this code block
=========================================================================================

Description
-------------------------
This `header.py` module is designed to identify the root directory of a project and ensure that this root directory is added to the Python system path. This allows for consistent and easy importing of modules within the project, regardless of where the script is executed from. It searches for a directory containing predefined marker files, such as `__root__` or `.git`.

Execution steps
-------------------------
1. **Import necessary modules**: The module imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.
2. **Call `set_project_root` function**: Call the `set_project_root` function, optionally passing a tuple with custom marker filenames or directory names to identify the project root. If no argument is passed it defaults to `('__root__', '.git')`.
    - Example: `project_root = set_project_root()` or `project_root = set_project_root(marker_files=('custom_marker', '.git'))`
3.  **Understand the function logic**:
    - The function initializes the `__root__` variable with the directory where the current file is located.
    - It then checks all parent directories to see if they contain any of the marker files from the `marker_files` tuple.
    - If a directory containing marker files is found, the loop stops and sets `__root__` variable to the directory where those marker files are present.
    - If not, the initial directory path will be set as `__root__`.
4.  **Add to System Path**: The function checks if the determined `__root__` path is already in the Python system path. If it isn't, it inserts it to the beginning of the `sys.path`.
5.  **Access the `__root__`**: The module defines a global variable `__root__` which contains the located project root path. This variable can be used in other modules after importing this module.

Usage example
-------------------------
```python
import sys
from pathlib import Path
from src.webdriver.edge.header import set_project_root, __root__

def main():
    # Example 1: Get the project root using default marker files
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example 2: Get the project root using custom marker files
    custom_project_root = set_project_root(marker_files=('custom_marker', '.git'))
    print(f"Project root with custom markers: {custom_project_root}")

     # Example 3: Check if the project root is in sys.path
    if str(project_root) in sys.path:
      print("Project root is in sys.path")
    else:
       print("Project root is not in sys.path")

    # Example 4: Access the root directory via global variable
    print(f"Project root via global variable: {__root__}")

if __name__ == "__main__":
    main()
```
```

## Changes
- Provided a detailed description of the `header.py` module, including its purpose, functionality, and how to use it.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations for the process of locating the root directory, and how it's added to the `sys.path`.
- Added usage examples to show custom marker files, using default marker files and how to check if the project root was correctly added to the system path.
- Included an example on how to access the `__root__` global variable.