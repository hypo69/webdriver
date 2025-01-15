Как использовать модуль `src.webdriver.proxy`
=========================================================================================

Описание
-------------------------
Модуль `proxy.py` предоставляет функции для загрузки, парсинга и проверки списка прокси-серверов. Он загружает текстовый файл с прокси-адресами, распределяет их по категориям (http, socks4, socks5) и проверяет их работоспособность.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте модуль `proxy` в свой проект.
   - Пример: `from src.webdriver import proxy`.
2. **Загрузка списка прокси:**
   - Используйте функцию `download_proxies_list(url, save_path)` для загрузки списка прокси из указанного URL и сохранения его в файл.
   - Пример: `proxy.download_proxies_list()`.
   - По умолчанию используется URL `'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'` и путь `src/webdriver/proxies.txt`.
   - Функция возвращает `True`, если загрузка прошла успешно, иначе `False`.
3. **Парсинг списка прокси:**
   - Используйте функцию `get_proxies_dict(file_path)` для парсинга списка прокси из файла и распределения их по категориям.
   - Пример: `proxies = proxy.get_proxies_dict()`.
   - По умолчанию используется файл `src/webdriver/proxies.txt`.
   - Функция возвращает словарь, где ключи — протоколы (`http`, `socks4`, `socks5`), а значения — списки словарей с данными прокси (`protocol`, `host`, `port`).
4. **Проверка работоспособности прокси:**
   - Используйте функцию `check_proxy(proxy)` для проверки работоспособности отдельного прокси-сервера.
   - Пример: `is_working = proxy.check_proxy(proxy_data)`.
   - Функция принимает словарь с данными прокси (`protocol`, `host`, `port`).
   - Функция возвращает `True`, если прокси работает, иначе `False`.
   - Проверка осуществляется через запрос к `https://httpbin.org/ip`.
5.  **Использование в проекте:**
    - Загрузите список прокси с помощью `download_proxies_list`.
    - Распарсите список прокси с помощью `get_proxies_dict`.
    - Проверьте прокси на работоспособность, используя `check_proxy`.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver import proxy
    from src.logger.logger import logger

    # Загрузка списка прокси
    if proxy.download_proxies_list():
        # Парсинг списка прокси
        proxies = proxy.get_proxies_dict()
    
        # Проверка каждого прокси (пример)
        for protocol, proxy_list in proxies.items():
            logger.info(f"Проверка прокси для протокола: {protocol}")
            for proxy_data in proxy_list:
                if proxy.check_proxy(proxy_data):
                    logger.info(f"Рабочий прокси: {proxy_data}")
                #else:
                 #   logger.info(f"Не рабочий прокси: {proxy_data}")
        logger.info(f'Обработано {sum(len(v) for v in proxies.values())} прокси.')

    else:
        logger.error("Не удалось загрузить список прокси.")