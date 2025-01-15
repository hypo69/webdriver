# Module: src.webdriver.edge.header

## Overview

This module is responsible for setting up the project root for the `src.webdriver.edge` package. It includes the function `set_project_root` that helps identify the root directory of the project.

## Table of Contents
1.  [Functions](#functions)
    -   [`set_project_root`](#set_project_root)
2.  [Variables](#variables)

## Functions

### `set_project_root`

```python
def set_project_root(marker_files=('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```
**Description**: Finds the root directory of the project.
**Parameters**:
    -   `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('__root__', '.git')`.
**Returns**:
    -  `Path`: Path to the root directory if found, otherwise the directory where the script is located.

## Variables
- `__root__` (Path): Path to the root directory of the project.