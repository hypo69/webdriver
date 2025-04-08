## \file /src/suppliers/hb/___grabber.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.hb 
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
  
""" module: src.suppliers.hb """


"""  Модуль заполнения полей HB -> product_fields 
### Flowchart
            
@image html graber.png
"""

import os, sys, asyncio
from pathlib import Path
from typing import List, Union, Dict
from selenium.webdriver.remote.webelement import WebElement

################# добавление корневой директории позволяет мне плясать от печки ###################
# dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind("hypotez") + 7])
# sys.path.append(str(dir_root))  # Adding the root folder to sys.path
# dir_src = Path(dir_root, 'src')
# sys.path.append(str(dir_root))

#from src.webdriver import execute_locator
"""  добавление корневой директории позволяет мне плясать от печки. """
####################################################################################################


from src import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.category import Category
from src.webdriver.driver import Driver
from src.utils import StringFormatter, StringNormalizer
from src.endpoints.PrestaShop import PrestaShop
from src.suppliers.hb.graber import 	grab_page
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException


# Функция grabber() собирает поля товара. Для каждого поля есть своя функия заполнитель

s: Supplier = None
c: Category = None 
l: Dict = {}
d: Driver = None
f: ProductFields = None




def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields :
	""" Собираю со страницы товара значения вебэлементов и привожу их к полям ProductFields
	
	@param s `Supplier` класс поставщика 
	 - вебдрайвер должен быть установлен на странице товара. 
	- в моей учетной записи я вижу линейку "Affiliate links" - я беру из нее информацию о партнерской ссылке
	 на али работает AJAX, это важно для сбора комбинаций! Они не передаются по URL
   
	"""
	
	global s
	s = supplier

	global c
	c = Category()

	global f
	f = ProductFields()

	
	d = s.driver
	
	global l
	l = s.locators["product"]
	
	d.wait(5)
	d.execute_locator(l["close_banner"])	
	""" закрываю баннер """
	
	d.scroll()
	""" прокручиваю страницу товара, чтобы захватить области, которые подгружаются через AJAX """



	######################################################################################
	# 
	# 
	#			""" Функции, специфичные для конкретного  поставщика """ 
	#
	#
	if async_run: asyncio.run(grab_page(supplier))
	
	def product_reference_and_volume_and_price_for_100():
		"""  Функция вытаскивает 3 поля:
		- volume,
		- supplier_reference,
		- цена за единицу товара 
		@todo Реализовать поле `цена за единицу товара`"""
		global f,s
		webelements: List[WebElement] = d.execute_locator(l["product_reference_and_volume_and_price_for_100"])
        
		for webelement in webelements:
			if ('Fl.oz' and 'מ"ל' )	in webelement.text:
				""" объем """
				f.volume = webelement.text
			elif str(r'מחיר ל100 מ"ל') in webelement.text:
				""" цена за единицу товара
				@todo придумать куда
				"""
				print(f'цена за единицу товара:{webelement.text}')
			elif 'מקט' in webelement.text:
				f.supplier_reference = StringNormalizer.get_numbers_only(webelement.text)
			...
		...


	
	def set_references(f, s):
		""" все, что касается id товара """
		#f.supplier_reference = field_supplier_reference()
		f.id_supplier = int(s.supplier_id)
		f.reference = f'{s.supplier_id}-{f.supplier_reference}'
	
	
	product_reference_and_volume_and_price_for_100()
	""" Реализация релевантна только для `hb` """

	set_references(f, s)
	
	#
	#
	#	
	#######################################################################################


	f.assist_fields_dict['page_lang'] = d.page_lang
	""" Язык сайта. Так я буду знать с какого языка переводить """


	f.active = field_active() # Совпадает с f.available_for_order
	#f.additional_delivery_times = field_additional_delivery_times()	# [v]  Мое поле. Нахера - не знаю
	f.additional_shipping_cost  = field_additional_shipping_cost() # [v]
	#f.advanced_stock_management = field_advanced_stock_management()
	f.affiliate_short_link =  field_affiliate_short_link() # [v]
	#f.affiliate_summary = field_affiliate_summary()
	#f.affiliate_summary_2 = field_affiliate_summary_2()
	#f.affiliate_text = field_affiliate_text()
	#f.affiliate_image_large = field_affiliate_image_large()
	#f.affiliate_image_medium = field_affiliate_image_medium()
	#f.affiliate_image_small = field_affiliate_image_small()
	#f.available_date = field_available_date()
	f.available_for_order = f.active = field_available_for_order()
	#f.available_later = field_available_later()
	#f.available_now = field_available_now()
	#f.cache_default_attribute = field_cache_default_attribute()
	#f.cache_has_attachments = field_cache_has_attachments()
	#f.cache_is_pack = field_cache_is_pack()
	
	f.condition = field_condition()
	#f.customizable = field_customizable()
	#f.date_add = field_date_add()
	#f.date_upd = field_date_upd()

	###############################  КАРТИНКИ ###############################################
	
	f.assist_fields_dict['default_image_url']: str = d.execute_locator(l["default_image_url"])[0]
	
	_images_urls: List | str = d.execute_locator(l["additional_images_urls"])
	if _images_urls and len(_images_urls) > 0:
		_images_urls: List = [_images_urls] if isinstance(_images_urls, str) else _images_urls
		_images_urls = [url.replace("-100x100", "") for url in _images_urls]
		_images_urls = list(set(_images_urls)	- set(f.assist_fields_dict['default_image_url']))
		
		f.assist_fields_dict['product_images_additional_urls'] = _images_urls

	...
	
	#f.delivery_in_stock = field_delivery_in_stock()	 # [v]	 ##<- доставка
	#f.delivery_out_stock = field_delivery_out_stock()	#   Заметка о доставке, когда товара нет в наличии

	#f.depth = field_depth()
	#f.description = field_description()
	f.description_short = f.description = field_description()
	# f.ean13 = field_ean13()
	# f.ecotax = field_ecotax()
	# f.height = field_height()
	f.how_to_use = field_how_to_use()

	f.id_category_default = field_id_category_default()
	
	############# DEBUG ###########################################################
	#f.associations.update ( field_additional_categories(f.id_category_default, None) )
	...
	f.associations['categories'] = field_additional_categories(f.id_category_default,s.current_scenario['presta_categories']['additional_categories'])  # <- Обновляет словарь категорий `{'categories':...}`
	"""Я могу передавать значения из additional_categories JSON сценария """
	...
	################################################################################
	
	#f.id_default_combination = field_id_default_combination()
	#f.id_default_image = field_id_default_image()
	#f.id_lang = s.locale
	f.id_manufacturer = field_id_manufacturer()
	#f.id_product = field_id_product()
	#f.id_shop_default = field_id_shop_default()   ## <- усранавливается в `product_fields_default_values.json`
	#f.id_supplier = s.supplier_id	# [v] ## <- добывается функцией set_references()
	#f.id_tax = field_id_tax() # [v]
	#f.id_type_redirected = field_id_type_redirected()
	f.images_urls = field_images_urls()	# [v]
	#f.indexed = field_indexed()
	f.ingredients = field_ingredients()

	#f.is_virtual = field_is_virtual()
	#f.isbn = field_isbn()
	#f.link_rewrite = field_link_rewrite()
	#f.location = field_location()
	#f.low_stock_alert = field_low_stock_alert()
	#f.low_stock_threshold = field_low_stock_threshold()
	#f.meta_description = field_meta_description()
	#f.meta_keywords = field_meta_keywords()
	f.meta_title = field_meta_title()
	#f.minimal_quantity = field_minimal_quantity()
	#f.mpn = field_mpn()

	###########################################################################################################
	_name = d.execute_locator (l["name"])[0]	# чтоб два раза не бегать, Я получаю значение локатора в _name
	f.name = field_name(_name)					# а потом использую для f.name
	f.link_rewrite = field_link_rewrite(_name)  # и для f.link_rewrite
	###########################################################################################################	

	#f.online_only = field_online_only()
	f.on_sale = field_on_sale()
	#f.out_of_stock = field_out_of_stock()
	#f.pack_stock_type = field_pack_stock_type()
	#f.position_in_category = field_position_in_category()
	f.price = field_price()
	#f.product_type = field_product_type()
	#f.quantity = field_quantity()
	#f.quantity_discount = field_quantity_discount()
	#f.redirect_type = field_redirect_type()
	#f.reference = field_reference()	# [v]  ## <- устанавливается в функции `set_references()`
	#f.show_condition = field_show_condition()
	#f.show_price = field_show_price()
	#f.state = field_state()
	#f.supplier_reference = field_supplier_reference()  # [v]  ## <- устанавливается в функции `set_references()`
	#f.text_fields = field_text_fields()
	#f.unit_price_ratio = field_unit_price_ratio()		<- см описание поля в базе данных
	#f.unity = field_unity()
	#f.upc = field_upc()
	#f.uploadable_files = field_uploadable_files()
	#f.volume = field_volume()		 ## <- устанавливается в функции `product_reference_and_volume_and_price_for_100()`
	f.visibility = field_visibility()
	#f.weight = field_weight()
	#f.wholesale_price = field_wholesale_price()
	#f.width = field_width()    
	...
	return f
    




def field_additional_shipping_cost():
	"""  
	 стоимость доставки
	@details
	"""
	return d.execute_locator(l["additional_shipping_cost"])




def field_delivery_in_stock():
	"""  
	 Доставка, когда товар в наличии
	@details
	"""
	return str(d.execute_locator(l["delivery_in_stock"]))
	...




def field_active():
	"""  
	
	@details
	"""
	return f.active	 # <-  поставить в зависимость от delivery_out_stock
	...
	
        


def field_additional_delivery_times():
    """  
    
    @details
    """
    return d.execute_locator(l["additional_delivery_times"])
    ...

    


def field_advanced_stock_management():
	"""  
	
	@details
	"""
	return f.advanced_stock_management
	...
	
        

def field_affiliate_short_link():
    """  
    
    @details
    """
    return d.current_url
    ...
    



def field_affiliate_summary():
    """  
    
    @details
    """
    return d.execute_locator(l["affiliate_summary"])
    ...



def field_affiliate_summary_2():
    """  
    
    @details
    """
    return d.execute_locator(l["affiliate_summary_2"])
    ...
        


def field_affiliate_text():
	"""  
	
	@details
	"""
	return d.execute_locator(l["affiliate_text"])
	
    


def field_affiliate_image_large():
	"""  
	
	@details
	"""
	return d.execute_locator(l["affiliate_image_large"])
        


def field_affiliate_image_medium():
	"""  
	
	@details
	"""
	return d.execute_locator(l["affiliate_image_medium"])
        


def field_affiliate_image_small():
	"""  
	
	@details
	"""
	return d.execute_locator(l["affiliate_image_small"])
        

def field_available_date():
    """  
    
    @details
    """
    return f.available_date
    ...
        
    


def field_available_for_order():
	"""  Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
	"""
	available_for_order = d.execute_locator(l["available_for_order"])
	...
	return 1 if available_for_order else 0
	# 	f.available_for_order = 1
	# else:
	# 	f.available_for_order = 0
	...



def field_available_later():
    """  
    
    @details
    """
    return f.available_later
    ...



def field_available_now():
    """  
    
    @details
    """
    return f.available_now
    ...




def field_additional_categories(category_id:list | str, categories_ids:list | str = None) -> Dict:
	"""  Дополнительные категории, восстановленные от целевой к  корнeвой (`2`)
		Возвращаю словарь:
	@code
	{
		"categories":{
			"category":[{'id':`cat_id`}, ...]
		}
	}
	```
	"""
	return f.set_additional_categories(category_id,categories_ids)

	# parents_list: List = c.get_parent_categories_list(category_id)
	
	# if categories_ids:
	# 	for category in categories_ids:
	# 		if not isinstance(category, int):
	# 			...
	# 			continue
			
	# 		parents_list.append(c.get_parent_categories_list(category))
			
	# categories_dict = { 'category': [{'id': cat_id} for cat_id in parents_list] }
	# ...
	# return categories_dict or ''
	

def field_cache_default_attribute():
    """  
    
    @details
    """
    return f.cache_default_attribute
    ...



def field_cache_has_attachments():
    """  
    
    @details
    """
    return f.cache_has_attachments
    ...	
        
                


def field_cache_is_pack():
	"""  
	
	@details
	"""
	return f.cache_is_pack
	...
	


def field_condition():
	"""  
	
	@details
	"""
	return d.execute_locator(l.condition)
        

def field_customizable():
	"""  
	
	@details
	"""
	return f.customizable
	...


def field_date_add():
	"""  
	
	@details
	"""
	return f.date_add
	...
	


def field_date_upd():
	"""  
	
	@details
	"""
	return f.date_upd
	...
	


def field_delivery_in_stock():
	"""  
	 Доставка, когда товар в наличии
	@details
	"""
	return d.execute_locator(l["delivery_in_stock"])
	...
	
        


def field_delivery_out_stock():
	"""  
	 Заметка о доставке, когда товара нет в наличии
	"""
	return f.delivery_out_stock
	...
	
                


def field_depth():
	"""  
	@details
	"""
	return d.execute_locator ( l ["depth"] )
	...
	


def field_description():
	"""  поле полного описания товара 
	@details
	"""
	return d.execute_locator (l["description"] )[0].text or ''
	...


def field_id_category_default():
	"""  Главная категория товара. Берется из сценария	"""
	return s.current_scenario["presta_categories"]["default_category"]
	...
	


def field_ean13():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["ean13"] )  or ''
	...



def field_ecotax():
	"""  
	
	@details
	"""
	return f.ecotax
	...
	
        	
                


def field_height():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["height"] )  or ''
	...
	


def field_how_to_use():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["how_to_use"] ) [0].text	 or ''
	...
	
                	


def field_id_category_default():
	"""  
	
	@details
	"""
	return s.current_scenario["presta_categories"]["default_category"]
	...
	


def field_id_default_combination():
	"""  
	
	@details
	"""
	return f.id_default_combination
	...
	


def field_id_default_image():
	"""  
	
	@details
	"""
	return f.id_default_image
	...
	

def field_id_lang():
	"""  
	
	@details
	"""
	return f.id_lang
	...
	

def field_id_manufacturer():
	"""  ID бренда. Может быть и названием бренда - престашоп сам разберется """
	
	return d.execute_locator(l["id_manufacturer"])
	...
	

def field_id_product():
	"""  
	
	@details
	"""
	return f.id_product
	...

	

def field_id_supplier():
	"""  
	
	@details
	"""
	return d.execute_locator(l["id_supplier"])
	...
	

def field_id_tax():
	"""  
	
	@details
	"""
	return f.id_tax
	...
	

def field_id_type_redirected():
	"""  
	
	@details
	"""
	return f.id_type_redirected
	...


def field_images_urls():
	"""  
	 Вначале я загружу дефолтную картинку
	@details
	"""
	try:
		return d.execute_locator(l["additional_images_urls"])
	except Exception as ex:
		logger.error(f"""Не найден элемент additional_images_urls,
			   {ex}
		url: {d.current_url}""")
		return ''
	...
	


def field_indexed():
	"""  
	
	@details
	"""
	return f.indexed
	...
	
        

def field_ingredients():
	"""  Состав. Забираю с сайта HTML с картинками ингридиентов """
	
	try:
		return d.execute_locator ( l["ingredients"] )[0].text
	except Exception as ex:
		logger.error(f"""Не найден элемент ingredients,
			   {ex}
		url: {d.current_url}""")
		return ''
	



def field_meta_description():
	"""  
	
	@details
	"""
	d.execute_locator ( l['meta_description'] ) or ''
	...
	


def field_meta_keywords():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['meta_keywords'] ) or ''
	...
	
        


def field_meta_title():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['meta_title'] ) or ''
	...
	

	

def field_is_virtual():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['is_virtual'] ) or ''
	...



def field_isbn():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['isbn'] ) or ''
	...
	


def field_link_rewrite(product_name: str) -> str:
	"""  Создается из переменной `product_name` которая содержит значение локатора l["name"] 	"""	
	return StringNormalizer.normalize_link_rewrite ( product_name )
	...
	
	
        


def field_location():
	"""  
	
	@details
	"""
	return f.location
	...
	


def field_low_stock_alert():
	"""  
	
	@details
	"""
	return f.low_stock_alert
	...
	
    


def field_low_stock_threshold():
	"""  
	
	@details
	"""
	return f.low_stock_threshold
	...
	


def field_meta_description():
	"""  
	
	@details
	"""
	...
	


def field_meta_keywords():
	"""  
	
	@details
	"""
	return f.meta_keywords
	...
	



def field_minimal_quantity():
	"""  
	
	@details
	"""
	return f.minimal_quantity
	...



def field_mpn():
	"""  
	
	@details
	"""
	return f.mpn
	...
	


def field_name(name: str):
	"""  Название товара 
	Очищаю поля от лишних параметров, которые не проходят в престашоп 
	"""
	return StringNormalizer.normalize_product_name(name)
	...


def field_online_only():
	"""  	товар только в интернет магазине
	
	@details
	"""
	return d.execute_locator ( l['online_only'] )
	...
	


def field_on_sale():
	"""  	Распродажа	"""
	return d.execute_locator ( l['on_sale'] )
	...
	


def field_out_of_stock():
	"""  Товара нет в наличии """
	return d.execute_locator ( l["out_of_stock"]) 
	...
	


def field_pack_stock_type():
	"""  
	
	@details
	"""
	return f.pack_stock_type
	...
	
	


def field_price():
	"""  
	
	@details
	"""
	return  StringNormalizer.normalize_price (d.execute_locator (l["price"])[0] ) 
	
	


def field_product_type():
	"""  
	
	@details
	"""
	return f.product_type
	...
	

# 
# def field_quantity():
# 	"""  
# 	
# 	@details
# 	"""
# 	return f.quantity
# 	...
	


def field_quantity_discount():
	"""  
	
	@details
	"""
	return f.quantity_discount
	...
	


def field_redirect_type():
	"""  
	
	@details
	"""
	return f.redirect_type
	...
	


def field_reference():
	"""  supplier's SKU """
	return f'{s.supplier_id}-{f.supplier_reference}' 
	...
	


def field_show_condition():
	"""  
	
	@details
	"""
	return f.show_condition
	



def field_show_price():
	"""  
	
	@details
	"""
	return f.show_price
	...



def field_state():
	"""  
	
	@details
	"""
	return f.state
	...




def field_text_fields():
	"""  
	
	@details
	"""
	return f.text_fields
	...
	


def field_unit_price_ratio():
	"""  
	
	@details
	"""
	return f.unit_price_ratio
	...
	


def field_unity():
	"""  
	
	@details
	"""
	return f.unity
	...
	
        


def field_upc():
	"""  
	
	@details
	"""
	return f.upc
	...
	


def field_uploadable_files():
	"""  
	
	@details
	"""
	return f.uploadable_files
	...
	


def field_default_image_url():
	"""  
	
	@details
	"""
	return f.default_image_url
	...
        


def field_visibility():
	"""  
	
	@details
	"""
	return d.execute_locator(l["visibility"])
	...
	


def field_weight():
	"""  
	
	@details
	"""
	return f.weight
	...
	


def field_wholesale_price():
	"""  
	
	@details
	"""
	return f.wholesale_price
	...
	


def field_width():
	"""  
	
	@details
	"""
	return f.width
	...
	
        
                


async def get_price(_d, _l) -> str | float:
	"""  Привожу денюшку через флаг `format` 
	@details к: 
	- [ ] float 
	- [v] str
	"""
	try:
		
		#raw_price = asyncio.run ( _d.execute_locator ( _l ["price"]["new"] )[0])
		raw_price = asyncio.run ( _d.execute_locator ( _l ["price"]["new"] )[0]) if gs.async_run else _d.execute_locator ( _l ["price"]["new"] )[0]
		''' raw_price получаю в таком виде:
		ILS382.00\nILS382\n.\n00
		'''
		raw_price = str (raw_price).split ('\n')[0]
		return StringNormalizer.normalize_price (raw_price)
	except Exception as ex:
		logger.error (ex)
		return
    
    ## price
    # async def cost_price():
    #     _price = _d.execute_locator (_l["price_locator"])        
    #     if not _price or len(_price) < 1:
    #         _price = _d.execute_locator(_l["uniform-banner-box-price"])
    #         ''' цена может быть спрятана баннером. Ищу в баннере'''
    #     _price = StringFormatter.clear_price(_price)
    #     return _price
    




def specification():
    #f["product_specification"] = _d.execute_locator(_l["specification_locator"])
    f["product_specification"] = f["description"]
def summary():
    f["summary"] = f["description"]
def delivery():

    #__ = _l["dynamic_shipping_block"]
    #_d.execute_locator(__l["product_shippihg_locator_button"])
    #''' Открываю панель способов доставки '''
    #shipping_price = _d.execute_locator(__l["dynamic_shipping_titleLayout"])
    #dynamic_shipping_estimated = _d.execute_locator(__l["dynamic_shipping_estimated"])
    #dynamic_tracking_available = _d.execute_locator(__l["dynamic_tracking_available"])
    #close = _d.execute_locator(__l["close"])

    shipping_price = _d.execute_locator(_l["shipping_price_locator"])
    if 'Free Shipping' in shipping_price:
        f["shipping price"] = 0
        return True
    f["shipping price"] = StringFormatter.clear_price(shipping_price)
    return True



def link():
    f["link_to_product"]= _d.current_url.split('?')[0]

## images
def images():

    _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
    _img_name = f'''{f["sku"]}.png'''
    f["img url"] =f'''{_http_server}/{_img_name}'''
    screenshot = _d.execute_locator(_l["main_image_locator"])
    s.save_and_send_viaftp({_img_name:screenshot})

def qty():
    try:
        _qty = _d.execute_locator(_l["qty_locator"])[0]
        f["qty"] = StringFormatter.clear_price(_qty)
        f["tavit im bemlay"] = f["qty"]
        return True
    except Exception as ex: 
        #field["qty"] = None
        logger.error(ex)
        return

def byer_protection():
    try:
        f["product_byer_protection"] = str(_d.execute_locator(_l["byer_protection_locator"]))
        return True
    except Exception as ex: 
        f["product_byer_protection"] = None
        logger.error(ex)
        return


def customer_reviews():
    try:
        f["product_customer_reviews"] = _d.execute_locator(_l["customer_reviews_locator"])
    except Exception as ex:
        f["product_customer_reviews"] = None
        logger.error(ex)
        return



def rewritted_URL():
    '''
    TODO
    получается длинные
    f["Rewritten URL"] = StringFormatter.rewritted_URL(f["title"])
    '''
    f["Rewritten URL"] = f["id"]
    ...



