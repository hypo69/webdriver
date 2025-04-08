## \file /src/endpoints/prestashop/api/____core.py
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



""" PrestaShop API connector """


import os, sys
from enum import Enum
from csv import excel
from http.client import HTTPConnection
from venv import logger
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError
from requests import Session
from requests.models import PreparedRequest
from typing import Dict, List
from pathlib import Path

from src import gs
from src.utils import save_text_file
from src.utils import dict2xml, xml2dict, base64_to_tmpfile
from src.utils.printer import pprint
from src.logger.logger import logger
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError



class Format(Enum):
    """Data types return (JSON,XML)
    @param Enum (int): 1 => JSON, 2 => XML
    @deprecated - я предпочитаю JSON 👍 :))
    """
    # JSON = 1
    # XML = 2
    JSON = 'JSON'
    XML = 'XML'


class PrestaShop():
    """ Interact with PrestaShop webservice API, using JSON and XML for message

    Raises:
        PrestaShopAuthenticationError: Authentication error.
        when: wrong api key or api key not exist.
        PrestaShopException: Generic PrestaShop WebServices error .

    Example:

    from PrestaShop import PrestaShop, Format

    api = PrestaShop(
        API_DOMAIN = "https://myPrestaShop.com",
        API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        default_lang=1,
        debug=True,
        data_format='JSON',
    )

    api.ping()

    data = {
        'tax':{
            'rate' : 3.000,
            'active': '1',
            'name' : {
                'language' : {
                    'attrs' : {'id' : '1'},
                    'value' : '3% tax'
                }
            }
        }
    }

    # create tax record
    rec = api.create('taxes',data)

    # update the same tax record

    update_data = {
        'tax':{
            'id' : str(rec['id']),
            'rate' : 3.000,
            'active': '1',
            'name' : {
                'language' : {
                    'attrs' : {'id' : '1'},
                    'value' : '3% tax'
                }
            }
        }
    }

    update_rec = api.write('taxes',update_data)

    # remove this tax
    api.unlink('taxes',str(rec['id']))

    # search the first 3 taxes with 5 in the name 
    import pprint
    recs = api.search('taxes',filter='[name]=%[5]%',limit='3')

    for rec in recs:
        pprint(rec)

    # create binary (product image)

    api.create_binary('images/products/22','img.jpeg','image')
    # or
    api.create_binary('images/products/22','img.jpeg','image')
    """
    API_KEY = ''
    API_DOMAIN = ''
    client: Session = Session()
    debug = True
    lang = None
    data_format = 'JSON'
    session: Session = None
    #params: dict = {}
    ps_version = ''
    
    
    def __init__(self,
                 API_DOMAIN:str, 
                 API_KEY:str, 
                 data_format = 'JSON', 
                 default_lang:int = 1,
                 debug:bool = True) -> None:
        """ PrestaShop class
        @param API_DOMAIN (str): API_DOMAIN of your shop (https://myPrestaShop.com)
        @param API_KEY (str): api key generate from PrestaShop 
        @param https://devdocs.PrestaShop-project.org/8/webservice/tutorials/creating-access/
        @param data_format (Format, optional): default data format ('JSON' or Format.XML). Defaults to 'JSON'.
        @param default_lang (str, optional): default language id (1). Defaults to None.
        @param session (Session, optional): requests.Session() for old sessing. Defaults to None.
        @param debug (bool, optional): activate debug mode. Defaults to False.
        """
        
        self.API_DOMAIN = API_DOMAIN
        self.API_KEY = API_KEY
        self.debug = debug
        self.language = default_lang
        self.data_format = data_format


        # fix API_DOMAIN 
        if not self.API_DOMAIN.endswith('/'):
            self.API_DOMAIN += '/'
        if not self.API_DOMAIN.endswith('/api/'):
            self.API_DOMAIN += 'api/'

        if not self.client.auth:
            self.client.auth = (API_KEY , '')
        
        
        response = self.client.request(
            method = 'HEAD',
            url = API_DOMAIN
        )

        self.ps_version = response.headers.get('psws-version')
        
    
    def ping(self) -> bool:
        """ Test if webservice work perfectly else raise error

        Returns:
            bool: Result of ping test
        """
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        content = {
            "errors": [
                {
                    "code": 0,
                    "message": "Ping not working "
                }
            ]
        }

        #return self._check_response(response.status_code,content)
        return self._check_response(response.status_code,response)
    
    
    def _check_response(self, status_code, response, method=None, url=None, headers=None, data=None) -> bool:
        """ Обработчик ответов (`response`).
        Объект `response` получает ответ от сервера.
        Коды 200,201 - ответ вернулся без ошибки.

        @returns `True`, если код 200 или 201, иначе `False`
        """

        if status_code in (200, 201):
            return True

        else:
            self._parse_response_error(response, method, url, headers, data )
            """ Сюда падают ошибки престашоп 
            @todo организовать логирование """
            # raise PrestaShopException(
            #     message_by_code.get(status_code,'Unknown error'),
            #     status_code,
            #     ps_check_response_msg=ps_check_response_msg,
            #     ps_check_response_code=ps_check_response_code,
            # )
            return
        
    
    def _parse_response_error(self,response, method=None, url=None, headers=None, data=None):
        """
               
        message_by_code = {
            100: 'Continue',
            101: 'Switching Protocols',
            102: 'Processing',
            103: 'Early Hints',
            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            207: 'Multi-Status',
            208: 'Already Reported',
            226: 'IM Used',
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            305: 'Use Proxy',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect',
            400: 'Bad Request',
            401: 'Unauthorized',
            402: 'Payment Required',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Method Not Allowed',
            406: 'Not Acceptable',
            407: 'Proxy Authentication Required',
            408: 'Request Timeout',
            409: 'Conflict',
            410: 'Gone',
            411: 'Length Required',
            412: 'Precondition Failed',
            413: 'Payload Too Large',
            414: 'URI Too Long',
            415: 'Unsupported Media Type',
            416: 'Range Not SatiStringFormatteriable',
            417: 'Expectation Failed',
            418: "I'm a teapot",
            421: 'Misdirected Request',
            422: 'Unprocessable Entity',
            423: 'Locked',
            424: 'Failed Dependency',
            425: 'Too Early',
            426: 'Upgrade Required',
            428: 'Precondition Required',
            429: 'Too Many Requests',
            431: 'Request Header Fields Too Large',
            451: 'Unavailable For Legal Reasons',
            500: 'Internal Server Error',
            501: 'Not Implemented',
            502: 'Bad Gateway',
            503: 'Service Unavailable',
            504: 'Gateway Timeout',
            505: 'HTTP Version Not Supported',
            506: 'Variant Also Negotiates',
            507: 'Insufficient Storage',
            508: 'Loop Detected',
            510: 'Not Extended',
            511: 'Network Authentication Required',
        }
        """
        # JSON responce
        if self.data_format == 'JSON':
            parced_message: str = ''
            status_code = response.status_code
            if not status_code in (200,201):
                logger.critical(f"""response status code: {status_code}
                    url: {response.request.url}
                    --------------
                    headers: {response.headers}
                    --------------
                    response text {response.text}""")

                ...
            return response 

            # code = content['errors'][0]['code']
            # msg = content['errors'][0]['message']
            #return (code, msg)
                
        # XML responce
        error_answer = self._parse(response)
        if isinstance(error_answer, dict):
            error_content = (error_answer
                             .get('PrestaShop', {})
                             .get('errors', {})
                             .get('error', {})
                             )
            if isinstance(error_content, list):
                error_content = error_content[0]
            code = error_content.get('code')
            message = error_content.get('message')
        elif isinstance(error_answer, type(ElementTree.Element(None))):
            error = error_answer.find('errors/error')
            code = error.find('code').text
            message = error.find('message').text
        logger.error(f"XML response error:{message} \n {code}")
        return (code, message)
    
    
    def _prepare(self, url, params):
        req = PreparedRequest()
        req.prepare_url(url , params)
        return req.url

    
    def _exec(self,
              resource: str,   ## <- `products`, `categories`, etc.
              resource_id: int |  str = None,  
              resource_ids:list | tuple = None,
              method: str ='GET',   ## <-  'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE' | 'HEAD' 
              data: dict = None,      ## <- словарь сущности  
              headers: dict = {},  ## <- дополнительные заголовки
              search_filter = None,    ## <- фильтр f.e. `filer[reference] = [reference]` | `{'filer[reference]':'reference'}`
              display: str('full') | str | list = 'full',   ## <- размер кадра выводимых данных (`full` | `id` | [`id`,`name`])
              schema: str('blank') | str('synopsis') = None,   ## <- схема выводимых данных (базовая, полная)
              sort = None,
              limit = None,
              language = None,
              io_format = 'JSON'  ) -> HTTPConnection.request | None:

        params: dict = {}

        if search_filter:
            """ Я могу передать фильтр, как строку `filter[id] = [5]`
            и как словарь `{'filter[id]':'[5]'}
            """ 
            if isinstance(search_filter, str):     ## <- `'filter[id]' = '[5]'`
                """ если пришла строка - преобразую ее в словарь """
                lst = search_filter.split('=',1)
                key = lst[0]
                params.update({key : lst[1]})
            elif isinstance(search_filter, dict):  ## <- `{'filter[id]' : '[5]'}`
                params.update(search_filter)


            
        ##########################################################################################
        #
        #           param filter
        #    
        
        if io_format == 'JSON':
            #params.update ({'io_format' : io_format , 'output_format' : io_format}) 
            params.update ({'io_format' : io_format }) 
            """@todo  почему два раза задается формат данных? """
            
        if self.language:
            params.update ({'language' : self.language })

        
        if display:
            params.update ({'display' : display})
                
        if sort:
            params.update ({'sort' : sort})

        if limit:
            params.update ({'limit' : limit})
            
        if schema:
            params.update ({'schema' : schema})

        
        """ @todo проверить поведение   `resource_ids` """                                          
        if isinstance (resource_ids, (list, tuple)):  ## <- может быть несколько ID в поисковом запросе
            """ @todo проверить поведение """
            params.update ({'ids' : resource_ids})
   

        if resource_id:
            _API_DOMAIN = f'{self.API_DOMAIN}{resource}/{resource_id}'
        else:
            _API_DOMAIN = f'{self.API_DOMAIN}{resource}'

        #
        #
        #
        #################################################################################### 
        
        
        url = self._prepare (_API_DOMAIN, params)
        
        ########################################################################################
        #
        #       headers
        #
        if io_format == 'JSON':
            """ Данные в формате `JSON` """
            headers.update({'Content-Type': 'application/json'})
        else:
            """ Данные в формате `XML` """
            headers.update({'Content-Type': 'text/xml'})
        #
        #
        ##########################################################################################       


        if self.debug:
            HTTPConnection.debuglevel = 0
        #HTTPConnection.debuglevel = 0

        # Сбрасываю лог в файл
        """ @todo Сделать через декоратор    """

        #1. Open the log file in append mode
        log_file_path = str(Path(gs.dir_log, 'http_debug.log'))
        with open(log_file_path, 'a+') as f:
            original_stderr = sys.stderr
            sys.stderr = f  # Redirect stderr to the log file
    
            #2. Perform HTTP request
            try:
                response = self.client.request(
                    method=method,
                    url=url,
                    data=data,
                    headers=headers,
                )
                response_log_message:str = f"""Response: {str(self._parse_response_error(response))}
                    method={method},
                    url={url},
                    headers={headers}
                """
                # Log debug information if needed
                # logger.success(f"""Response executed: 
                #                {response_log_message}""")
            except Exception as e:
                # Log any exceptions that occur during the request
                logger.critical(f"""Response failed: {self._parse_response_error(response)}""",e)
                print("Exception occurred during HTTP request:", e, file=f)
                ...

            #3. Flush the file to ensure data is written immediately
            f.flush()
            sys.stderr = original_stderr  # Restore stderr 


        
        if self._check_response(response.status_code, response, method, url, headers, data):
            """  Вернулся валидный ответ """
            return response.json()
        else:
            
            return
        
    
    def _parse(self, content):
        """ Parse the response of the webservice.
        @param content: response from the webservice
        @returns: an ElementTree of the content
        """
        if not content:
            raise PrestaShopException('HTTP response is empty')

        if isinstance(content, dict):
            return content

        try:
            parsed_content = ElementTree.fromstring(content)
        except ExpatError as e:
            raise PrestaShopException(
                'HTTP XML response is not parsable : %s' % (e,)
            )
        except ElementTree.ParseError as e:
            raise PrestaShopException(
                'HTTP XML response is not parsable : %s. %s' %
                (e, content[:512])
            )

        return parsed_content
    
    
    def search(self,
            resource: str = None,
            resource_id: int | str = None,
            resource_ids: int | str | list[int] = None, 
            search_filter:dict | str = None, 
            display:str = None,  
            sort:str= None, 
            limit:str = None,
            schema:str = None,
            io_format:str = 'JSON') -> dict | None:
        """ Search from PrestaShop with options, for more details check the official doc \n
        https://devdocs.PrestaShop-project.org/1.7/webservice/tutorials/advanced-use/additional-list-parameters/

        Args:
            @param resource `str`: resource to search ( taxes,customers,products ...)
            List of API resources:
            ...
            @param resource_ids `int, str, List[str], Tuple(str)` фильтр запроса. `resource_ids=[5,6]`, `resource_ids=4`
            @param display (str, optional): display parameter (full | [field1,field2]). Defaults to 'full'.
            @param filter (str, optional): filter parameter ([id]=[1|5] , [name]=[app]%). Defaults to None.
            @param sort (str, optional): sort parameter ([{fieldname}_{ASC|DESC}] ,[lastname_ASC,id_DESC] ). Defaults to None.
            @param limit (str, optional): limit parameter ('offset,limit' , '9,2' , '5'). Defaults to None.

        Returns:
            dict : result of search
        """

        return self._exec(
            resource=resource, 
            resource_ids = resource_ids, 
            method='GET', 
            search_filter=search_filter, 
            display=display,  
            sort=sort,
            limit=limit)

    
    
    def get(self,
            resource: str = None,
            resource_id:str = None, 
            resource_ids:list | tuple = None,
            search_filter:dict | str = None, 
            display:str = None,  
            sort:str= None, 
            limit:str = None,
            schema:str = None,
            io_format:str = 'JSON') -> dict | None:
        """ get one result from PrestaShop with options .
        for more details check the official doc \n
        https://devdocs.PrestaShop-project.org/8/webservice/tutorials/advanced-use/additional-list-parameters/

            @param resource (str): resource to search ( taxes,customers,products ...)
            @param resource_ids (list[int] | tuple(int) | str): list|tuple|str of ids to remove. ([1,3,9] , [9] , '3')
            @param display (str, optional): display parameter (full | [field1,field2]). Defaults to 'full'.

            @returns dict : result of get request
        """


        # if version.parse(self.ps_version)  <= version.parse('1.7.6.8') :
        #     """ Нижняя версия престашоп. 
        #     На самом деле я думаю, что будет работать в более раних версиях, не проверял."""
        #     display = None

        return self._exec(resource = resource ,
                        resource_id = resource_id,
                        resource_ids = resource_ids,
                        method='GET', 
                        search_filter = search_filter, 
                        display = display, 
                        sort = sort, 
                        limit = limit,
                        schema = schema,
                        io_format = io_format)
    
    
    def unlink(self, resource:str, resource_ids:list | tuple | str ) -> bool:
        """remove one or multiple records
            @param resource (str): resource to search ( taxes,customers,products ...)
            @param resource_ids (list[int] | tuple(int) | str): list|tuple|str of ids to remove. ([1,3,9] , [9] , '3')

            @returns boolean: result of remove (True,False)
            @todo переименовать функцию в `del`
        """
        if isinstance(resource_ids , (tuple,list)):
            resource_ids = ','.join([str(id) for id in resource_ids])
            resource_ids = '[{}]'.format(resource_ids)
            return self._exec(resource = resource ,resource_ids = resource_ids, method='DELETE' , display=None)
            
        else:
            return self._exec(resource = resource ,resource_ids = resource_ids, method='DELETE', display=None)
    

    def add(self, resource:str, data:dict) -> dict:
        """ create record 
            @param resource (str): resource to search ( taxes,customers,products ...).
            @param data (dict): data in dict format (
                    data = {
                        'tax':{
                            'rate' : 3.000,
                            'active': '1',
                            'name' : {
                                'language' : {
                                    'attrs' : {'id' : '1'},
                                    'value' : '3% tax'
                                }
                            }
                        }
                    }
        )

        @returns:
            dict: record added.
        """


        data  = {'PrestaShop' : data}
        # for key in data.keys():
        #     if isinstance(data[key],(int,float)):
        #        data[key] = str (data[key]) 
        
        ############################# debug 
        # filename = Path(gs.dir_tmp, f"{data['PrestaShop']['product']['reference']}.xml")
        # save_text_file (dict2xml(data), filename)
        # j_dumps()
        ############################ /debug
        
        try:data = dict2xml(data)  ## <- конвертер json - xml
        except Exception as e: 
            logger.error(f""" Проверь валидность словаря {data}""", e, True)
            ...
            
            
        return self._exec(resource = resource, 
                            data = data,
                            method='POST', 
                            display='full',
                            io_format = 'JSON')
        """@todo попробовать реализовать отправку JSON"""
        
    
    def create_binary(self, resource:str, resource_id:int, file_local_path:str, _type:str = 'image', file_name=None, params: Dict = {}) -> dict | None:
        """ create binary record
            @param `resource` (str): resource to add file f.e.  'images/products/22' ...
            @param `file_local_path` (str):  a path of file ('image.png', 'image.jpg') or binary.
            @param `_type` (str, optional): a type of file (image,pdf ...) Default to 'image'
            @param `file_name` (str, optinal): name of file in case of base64. Default to None
            @param `params`
        """

        #params.update({'display' : '[id]'})
        
        # if self.language:
        #     params.update({'language' : self.language})
        
        # if self.data_format == 'JSON':
        #     params.update({'io_format' : 'JSON' , 'output_format' : 'JSON'})
    

        _API_DOMAIN = fr'{self.API_DOMAIN}images/{resource}/{resource_id}'
        API_DOMAIN = self._prepare(_API_DOMAIN,params)


        if os.path.exists(file_local_path):
            _file = {_type : open(file_local_path,'rb')}

        elif isinstance(file_local_path ,str):
            _file = {_type : open(base64_to_tmpfile(file_local_path,file_name),'rb') }
            """ @todo проверить поведение """
        else:
            raise PrestaShopException('File not found',404)

        try:
            response = self.client.post(
                url = API_DOMAIN,
                files = _file
            )
        except Exception as ex:
            logger.error(f"""
                Ошибка загрузки файла на сервер 
                status_code: {response.status_code} 
                url: {response.url} 
                response headers: {response.headers}
                {response.content}
                        """)
        ...
        
        """ Мне надо получить `ID` загруженной картинки """
        if response.status_code == 200:
            return xml2dict(response.text)['PrestaShop']['image']
        else:
            logger.error(f"""response.request: {response.request} 
                        response.status_code: {response.status_code}
                        response.reason: {response.reason}
                        response.text: {
                            pprint(xml2dict(response.text))
                            }
                        """)
        

        """locator_description У меня упал в 400, когда я вытирал товар и загружал картинку """
        return
    
    def get_image_product(self, resource_id:int, image_id:int, params: Dict = {}):
        """ get product image from PrestaShop
        
            @param resource_id (int): the id of product
            @param image_id (int): the id of image
            
            @returns binary: image of product
        
        Raise:
            PrestaShopException: 'This image id does not exist'
        """
        

        if self.language:
            params.update ( {'language' : self.language} )

        if self.data_format == 'JSON':
            params.update ( {'io_format' : 'JSON' , 'output_format' : 'JSON'} ) 

        _API_DOMAIN = f'{self.API_DOMAIN}images/products/{resource_id}'   # /api/images/products/{ID}
        if image_id:
            _API_DOMAIN += f'/{image_id}'
        
        _API_DOMAIN = self._prepare (_API_DOMAIN, params)
        
        response = self.client.request(
            method='GET',
            url = _API_DOMAIN,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            return response.content
        
        self._check_response(response.status_code,response.json())
        return response.json())