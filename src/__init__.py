## \file /src/__init__.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Root of the project.
========================================================================================
•	USE_ENV:bool: Переменная, которая определяет, откуда читать секреты: API-ключи и т.д. 
•	Если USE_ENV равно True, модуль gs будет импортирован из gs.py, а секреты будут читаться из файлов .env.
•	Если USE_ENV равно False, модуль gs будет импортирован из credentials.py. и секреты будут читаться из объекта gs. (например, `token = gs.path.telegram.kazarinov_bot`)

```rst
.. module:: src
```
"""



USE_ENV:bool = True

if USE_ENV:
	from .gs import gs
# else:
# 	from .credentials import gs

from .check_release import check_latest_release
if check_latest_release(gs.git, gs.git_user):
            ...  # Логика что делать когда есть новая версия hypo69 на github 