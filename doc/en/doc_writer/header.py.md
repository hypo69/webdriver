# Module: src.webdriver.header

## Overview

This module provides essential configurations and utilities for the `src.webdriver` package. It includes functionalities for setting the project root, loading settings, and defining project-level metadata.

## Table of Contents
1.  [Functions](#functions)
    -   [`set_project_root`](#set_project_root)
2.  [Variables](#variables)

## Functions

### `set_project_root`

```python
def set_project_root(marker_files=('__root__', '.git')) -> Path:
    """Finds the root directory of the project starting from the current file's directory,
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

-   `__root__` (Path): Path to the root directory of the project.
-   `settings` (dict): Loaded settings from `settings.json`.
-    `doc_str` (str): Content of the `README.MD` file.
-   `__project_name__` (str): Name of the project from settings or `'hypotez'` if not found.
-   `__version__` (str): Version of the project from settings or `''` if not found.
-   `__doc__` (str): Project documentation loaded from `README.MD` or `''` if not found.
-  `__details__` (str): Additional details about project (currently not used).
-  `__author__` (str): Author of the project from settings or `''` if not found.
-   `__copyright__` (str): Copyright information from settings or `''` if not found.
-   `__cofee__` (str): A string containing a message and a link for donation, taken from settings or default value if not found.