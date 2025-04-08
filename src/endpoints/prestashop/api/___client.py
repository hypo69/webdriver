## \file /src/endpoints/prestashop/api/___client.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop.api 
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
  
""" module: src.endpoints.prestashop.api """



""" Класс клиента PrestaShop"""
...
import os
import asyncio
import importlib
from pathlib import Path
from typing import List, Dict
...
from src import gs
from src.utils.printer import  pprint
from .api_adaptor import  PrestaAPIV
from src.utils import  save_image_from_url
from src.logger.logger import logger
from src.logger.exceptions import PrestaShopException


class PrestaShop(PrestaAPIV):
    """
    @param client_api_credentials: dict
    """
    
    api_credentials: dict = {}
    
    
    def __init__(self, api_credentials, *args,**kwards):
        """ 
        
        @details
        @param self `object` : description
        @returns None
        """
        self.api_credentials = api_credentials
        super().__init__( api_credentials, *args,**kwards)
        ...
    
    def remove_file(self, file_path):
        try:
            os.remove(file_path)
            
        except Exception as e:
            logger.error(f"Ошибка при удалении файла {file_path}: {e}")   
            
        
    def get_apis(self):
        """ Возвращает список все доступных API """
        ...
        return super().get()
    
    
    def get_languages_schema(self) -> dict:
        """ 
        
        @details
        @param self `object` : description
        @returns None
        @todo плохое решение. Лучше получить схему сразу при запуске потсавщика и не дергать
        API. Хорошо при тестировании нагрузки моего сервера
        """
        ...
        try:
            responce = super().get('languages', display='full',  io_format='JSON')
            ...
            return  responce
        except Exception as ex:
            logger.error(f"Ошибка {ex}")
            ...
            return
        ...
        
        
    def get(self,
            resource: str = None,
            resource_id: int | str = None,
            resource_ids: List = None, 
            search_filter:dict | str = None, 
            display:str = None,  
            sort:str= None, 
            limit:str = None,
            schema:str = None,
            io_format:str = 'JSON'):
        """ Возвращает ответ PrestaShop.
                @param resource: str = None,
                @param resource_id: int | str = None,
                @param resource_ids: List = None, 
                @param search_filter:dict | str = None, 
                @param display:str = None,  
                @param sort:str= None, 
                @param limit:str = None,
                @param schema:str = None,
                @param io_format:str = 'JSON'
        """
        ...
        return super().get(resource,
                           resource_id,
                            resource_ids, 
                            search_filter, 
                            display,  
                            sort, 
                            limit,
                            schema,
                            io_format)
    ...
    
    def add(self,resource:str = None,
            data:dict = None,
            resource_id: int | str = None,
            resource_ids: int | str | List[str, tuple] = None, 
            search_filter:dict = None, 
            display:str | list = 'full',  
            io_format:str = 'JSON') :        
        """ Добавляет сущность в PrestaShop и возвращает ответ.
                @param resource: str = None,
                @param resource_id: int | str = None,
                @param resource_ids: List = None, 
                @param search_filter:dict | str = None, 
                @param display:str = None,  
                @param sort:str= None, 
                @param limit:str = None,
                @param schema:str = None,
                @param io_format:str = 'JSON'
        """

        ...
        return super().add(resource = resource,
                        data = data,
                        resource_id = resource_id,
                        resource_ids = resource_ids, 
                        display = display,  
                        io_format = io_format)
    
        

        # 7.
    ...
    
    async def upload_image_async(self, resource, resource_id:int , img_url:str, img_name:str = None) -> object | None:
        """
        Загружаю картинку, получаю или id_image или False
        
        @param image_url `str`  :  source url
        @paramlocal_file_path `str`  :  имя файла для PrestaShop. Если на указано (`default.png`) - 
        @returns id_image `int`  :  id_image from src.endpoints.PrestaShop db if success else False

        """
        ...
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id)+f'_{img_name}.{extension}'
        png_file_path = save_image_from_url(img_url, filename)
        response = super().upload_image(resource, resource_id, png_file_path)
        self.remove_file(png_file_path)
        ...
        return response

    def upload_image(self, resource, resource_id:int , img_url:str, img_name:str = None) -> object | None:
        """
        Загружаю картинку, получаю или id_image или False
        
        @param image_url `str`  :  source url
        @paramlocal_file_path `str`  :  имя файла для PrestaShop. Если на указано (`default.png`) - 
        @returns id_image `int`  :  id_image from src.endpoints.PrestaShop db if success else False

        """
        ...
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id)+f'_{img_name}.{extension}'
        png_file_path = save_image_from_url(img_url, filename)
        response = super().upload_image(resource, resource_id, png_file_path)
        self.remove_file(png_file_path)
        ...
        return response      

    
    def get_product_images(self, product_id):
        """ """
        ...
        img = super().get_image_product(product_id)
        ...
        return imgg