## \file /SANDBOX/davidka/product_fields.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль для демонстрации работы с полями продукта.
"""

import asyncio
from types import SimpleNamespace
import header
from src import gs
from src.endpoints.prestashop.product_fields import ProductFields
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.webdriver import Driver, Firefox
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint as print
from src.logger import logger

async def main():
    """Главная функция для демонстрации работы с полями продукта."""

    d:Driver = Driver(Firefox)
    lan_index: int = 2 # Индекс языка, для cms `PrestaShop`

    graber: 'Graber' = get_graber_by_supplier_url(d, 'https://www.morlevi.co.il/product/21695', lan_index)

    # Получаем поля товара
    f:ProductFields = await graber.grab_page_async()
    porduct_dit:dict = f.to_dict()
    ...
    print(porduct_dit)
    ...

if __name__ == "__main__":
    # Запускаем главную функцию
    asyncio.run(main())

