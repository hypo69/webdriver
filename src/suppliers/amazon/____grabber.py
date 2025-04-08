## \file /src/suppliers/amazon/____grabber.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.amazon 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.amazon """


"""   [File's Description]


 
 @section libs imports:
  - typing 
  - gs 
  - helpers 
  - tools 
  - product 
  - suppliers 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""


""" Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
1. Заполняю поля, необходимые для создания нового товара
2. Получаю `id_product` созданного товара
3. Используя полученный `id_product` загружаю дефолтную картинку
4. итд.
"""

from typing import Union
# ----------------------------
from src import gs
from src.logger.logger import logger
from src.utils import StringFormatter, StringNormalizer
from src.product import Product, ProductFields
from src.suppliers import Supplier
# ----------------------------




def grab_product_page(s: Supplier, id_product: int = 0 , presta_api_version: str('V1') | str('V2') | str('V3') = 'V3') -> ProductFields:
    """ ПОКА ТОЛЬКО ДЛЯ НОВЫХ!!!!! СТРАНИЦ
        Собираю информацию со страницы товара. 
        Важно помнить, что драйвер уже должен быть на
        этой странице
        ---------------
        Attrs:
            s (Supplier)
        @returns
            f (ProductFields) с заполненными полями, else False
    """


    l = s.reread_locators('product')
    d = s.driver
   
    _ = d.execute_locator

    print('Start  function grabber for ')

    def add_new_product_stage_1(s: Supplier) -> ProductFields:
        """ Первая стадия добавления нового товара. Заполняю все необходимые поля
            Далее я отправлю их в PrestaShop и получу обратно ID вновь созданного товара
            На второй стадии, зная ID, я отправлю главную картинку и прочее
        """
        f: ProductFields = ProductFields()
       
        """ ID,ASIN,SKU,SUPPLIER SKU """
    

        def _set_defaults() -> bool:
            """ Set defaults for product of supplier """
            f.active = 1
            f.on_sale = 1
            f.min_qty = 1
            f.low_stock_level = 0
            f.low_stock_threshold = ''
            f.show_price = 1
            f.show_condition = 1
            f.aviable_online_only = 0
            f.advanced_stock_management = 0
            f.state = 1

        def set_price(s, format: str = 'str') -> str | float:
            """ Привожу денюшку к 
            [ ] float 
            [v] str
            """
            l = s.reread_locators('product')
            try:
                raw_price = _(l['price']['new'])[0]
            except Exception as ex:
                logger.error(f'ошибка {ex} в цене ')
                return
            raw_price = str(raw_price).split('\n')[0]
            return StringNormalizer.normalize_price(raw_price)
    

        """ Я добавляю в базу данных престашоп товар путем нескольких последовательных действий
        1. Добавляю поля, необходимые для создания нового товара
        2. Получаю `id_product` созданного товара
        3. Используя полученный `id_product` загружаю дефолтную картинку
        4. итд.
        """
        price = set_price(s, format = 'str')
        if price is False: return

        _set_defaults()
        l = s.reread_locators('product')
        ASIN = _(l['ASIN'])
        f.reference = f'{s.supplier_id}-{ASIN}'
        f.supplier_reference = ASIN
        f.price = price
        f.name = _(l['name'])[0]
        
        f.description_short = _(l['description_short'])[0]
        f.id_supplier = s.supplier_id
        
        _category_default = list(s.current_scenario['presta_categories']['default_category'].keys())[0]
        f.id_category_default = _category_default
        f.category_ids = Product.get_parent_categories(_category_default)

        affiliate = _(l['affiliate short link'])
        affiliate = affiliate[1][0]
        f.affiliate_short_link = affiliate

        #f.link_rewrite = d.current_url.split(f'''/''')[-4]



        f.link_rewrite = "test-link"
        return f

    def upload_image(id_product, image_url) -> ProductFields:
        """ После того, как я занес новый товар в бд - я получу его id
        Далее я гружу фото и получаю ее id
        Далее я догружаю осталные па
        ----------------------
        Attrs: 
            s (Supplier):
            f (ProductFields): Заполненные на первом этапе поля. Я беру из них только то, что мне надо для апдейта
        @returns
            ProductFields: поля для апдейта
        """

        img = Product.upload_product_default_image(id_product, image_url)
        return img
        
    



    if id_product == 0:
        f = add_new_product_stage_1(s)
        if f is False: return

        print("---------------------NEW PRODUCT-----------------------")


        product_dict = f.product_dict
         
        response = Product.add_2_PrestaShop(product_dict, presta_api_version)
        if 'error' in response.keys():
            pprint(response)
            return

        product = response['product']
        id_product = product['id']
        print("---------------------NEW PRODUCT ID-----------------------")
        print(id_product)
        image_url = _(l['additional_images_urls'])[0]
        img = upload_image(id_product, image_url)
        #return product, img

    
    ...

