## \file /src/suppliers/ebay/___scrapper.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.ebay 
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
  
""" module: src.suppliers.ebay """


"""   [File's Description]

@namespace src: src
 \package src.suppliers.ebay
\file scrapper.py
 
 @section libs imports:
  - product 
  - helpers 
  - tools 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""



from src.product import Product

from src.logger.logger import logger
from src.utils import StringFormatter


def grab_product_page(s) -> Product:
    p = Product(supplier = s)
    _s = s
    _l : dict = s.locators['product']
    _d = s.driver
    _field = p.fields
    ''' 
    Вытаскиваю со страницы товара все поля по локаторам
    ------------
    p - товар
    '''
    
    #field = p.fields

    def set_id():
        _id = _d.current_url.split('/')[-1].split('?')[0]
        _field['sku'] = _field['id'] = _id
    def set_sku_suppl():
        _field['sku suppl'] = f'''{s.settings['supplier_id']}-{_field['id']}'''

    def set_sku_prod():...
    def set_title():
        title = _d.execute_locator(_l['product_name_locator'])
        _field['title'] = StringFormatter.remove_special_characters(title)
        
    def set_cost_price():
        _price = _d.execute_locator(_l['price_locator'])
        '''  Может прийти все, что угодно  
        Например, товара больше нет в наличии - цены не будет
        '''
        if not _price or _price is None or len(_price)==0:
            return

        _price = StringFormatter.clear_price(_price)
        _field['price tax excluded'] = _field['cost price'] = _price
        
        return True
    def set_before_tax_price():
        _field['price tax excluded']  = _field['cost price']
    def set_delivery():...

    def set_images():
        _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
        _img_name = f'''{_field['sku']}.png'''
        _field['img url'] =f'''{_http_server}/{_img_name}'''
        screenshot = _d.execute_locator(_l['main_image_locator'])
        s.save_and_send_via_ftp({_img_name:screenshot})
        

    def set_combinations():...

    def set_qty():
        _qty=_d.execute_locator(_l['qty_locator'])
        if not _qty: 
            return
        elif 'Last one' in _qty:
            _qty = 1
        else:
            _qty = StringFormatter.clear_number(_qty)

        _field['qty'] = _qty

    def set_byer_protection():...

    def set_description():
        ...
        # _field['description'] = _d.execute_locator(_l['description_locator'])

    def set_summary():
        _field['summary'] = _d.execute_locator(_l['summary_locator'])

    def set_specification():...

    def set_customer_reviews():...

    def set_affiliate_short_link():
        _field["affiliate short link"] = _d.current_url
    
    set_id()
    set_sku_suppl()
    set_sku_prod()
    set_title()
    set_cost_price()
    set_before_tax_price()
    #set_delivery(),
    set_images()
    #set_combinations(),
    set_qty()
    #set_byer_protection(),
    set_description()
    set_summary()
    #set_specification(),
    #set_customer_reviews()
    set_affiliate_short_link()
    return p
    ...

