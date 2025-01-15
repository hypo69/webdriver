How to use this code block
=========================================================================================

Description
-------------------------
The `header.py` module is designed to identify the root directory of a project and add it to the Python system path. This allows for consistent and easy importing of modules within the project, regardless of where the script is executed from. It automatically searches upwards from the location of the current file until it finds a directory containing specific marker files.

Execution steps
-------------------------
1. **Import necessary modules**: Ensure that `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib` are imported.
2. **Call `set_project_root` function**: Call the `set_project_root` function. You can optionally pass a tuple of custom marker filenames or directory names to identify the project root, but if not, it defaults to `('__root__', '.git')`.
    -   Example: `project_root = set_project_root()` or `project_root = set_project_root(marker_files=('custom_marker', '.git'))`
3. **Understand the function logic**:
    - The function initializes `__root__` with the path to the directory containing the current script.
    - It then iterates upwards through the parent directories, checking if any of the directories contains the marker files.
    - If a directory with the marker file is found, the loop stops and sets the `__root__` variable to that directory.
    - If no marker files are found, the `__root__` variable will remain the directory where the current script is located.
4. **Add to System Path**: The function then checks if the determined `__root__` path is in the Python system path, and if not, it inserts it into `sys.path`. This ensures that the project's modules can be imported correctly.
5. **Access the `__root__`**: The module defines a global variable `__root__` which contains the resolved root directory for use in other modules.

Usage example
-------------------------
```python
import sys
from src.webdriver.bs.header import set_project_root, __root__
from pathlib import Path

def main():
    # Example 1: Get the project root using default marker files
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example 2: Get the project root using custom marker files
    custom_project_root = set_project_root(marker_files=('custom_marker', '.git'))
    print(f"Project root with custom markers: {custom_project_root}")


    #Example 3: Check that the root is added to the system path
    if project_root in sys.path:
      print("Project root is in sys.path")
    else:
       print("Project root is not in sys.path")


    #Example 4: Access the root directory using the global variable
    print(f"Project root from global variable {__root__}")


if __name__ == "__main__":
    main()

```
```

## Changes
- Added a detailed description of the `header.py` module and its purpose.
- Outlined clear execution steps for using the code block.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations about how `set_project_root` function works.
- Added a section on how to access the global `__root__` variable.
- Updated the usage example to show how to use custom marker files, check for `sys.path` and use the global variable.