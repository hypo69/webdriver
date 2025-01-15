How to use this code block
=========================================================================================

Description
-------------------------
The `header.py` module is designed to dynamically identify the root directory of a project and ensure that this root directory is added to the Python system path. This enables the project to import modules correctly regardless of the script's execution location. The module uses a marker file or directory to locate the project's root.

Execution steps
-------------------------
1.  **Import necessary modules**: The module imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.
2.  **Call `set_project_root` function**: Call the `set_project_root` function. You can optionally pass a tuple of custom marker filenames or directory names to identify the project root, or it defaults to `('__root__', '.git')`.
    -   Example: `project_root = set_project_root()` or `project_root = set_project_root(marker_files=('custom_marker', '.git'))`
3.  **Understand the function logic**:
    -   The function starts by setting the current path of the script as initial root path.
    - It iterates upwards through the parent directories, searching for directories containing any of the specified `marker_files`.
    - If a directory containing marker files is found, it sets that directory as the root and stops iterating.
    - If no marker files are found, the initial path remains as the project root.
4.  **Add project root to system path**: The function then checks if the determined root directory is already in `sys.path`. If not, it inserts it at the beginning of `sys.path`, ensuring that the project's modules can be imported.
5.  **Access the `__root__` variable**: The module defines a global variable `__root__` that stores the determined project root. You can access this variable after importing the module.

Usage example
-------------------------
```python
import sys
from pathlib import Path
from src.webdriver.chrome.header import set_project_root, __root__

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

    # Example 4: Access the root directory via the global variable
    print(f"Project root via global variable: {__root__}")


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
- Added explanations on how the project root is located and how sys path is configured.
- Added examples for using custom markers and checking the sys path.
- Added an example of accessing root directory using the global `__root__` variable.