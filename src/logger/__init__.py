## \file /src/logger/__init__.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""

"""


from .logger import logger
#from .beeper import Beeper
try:
    from .exceptions import ( ExecuteLocatorException, 
                         DefaultSettingsException, 
                         CredentialsError, 
                         PrestaShopException, 
                         PayloadChecksumError
                        )
except ImportError:
    print("Error importing exceptions. Ensure the module is correctly installed.")
