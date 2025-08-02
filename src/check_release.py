## \file /src/check_release.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль проверки актуальной версии
==================================

```rst
.. module:: src.check_release 
```
"""

import requests
from src.logger.logger import logger

def check_latest_release(repo: str, owner: str):
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
    url:str = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    response:requests.Response = requests.get(url)

    if response.status_code == 200:
        latest_release:dict = response.json()
        logger.info(latest_release)
        return latest_release['tag_name']

    else:
        logger.error(f"Error fetching data: {response.status_code}")
        #TODO: Код не проверен
        return 

