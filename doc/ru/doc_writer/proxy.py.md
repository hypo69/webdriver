# Документация модуля `src.webdriver.proxy`

## Обзор

Модуль `proxy.py` предназначен для работы с прокси. Он определяет функции для загрузки и парсинга списка прокси, загружает текстовый файл с прокси-адресами и распределяет их по категориям.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`download_proxies_list`](#download_proxies_list)
    - [`get_proxies_dict`](#get_proxies_dict)
    - [`check_proxy`](#check_proxy)
- [Переменные](#переменные)
    -   [`url`](#url)
    -   [`proxies_list_path`](#proxies_list_path)

## Функции

### `download_proxies_list`

```python
def download_proxies_list(url: str = url, save_path: Path = proxies_list_path) -> bool:
    """
    Загружает файл по указанному URL и сохраняет его в заданный путь.

    :param url: URL файла для загрузки.
    :param save_path: Путь для сохранения загруженного файла.
    :return: Успешность выполнения операции.
    """
    try:
        # Отправка запроса на загрузку файла
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Генерирует исключение для ошибок HTTP

        # Сохранение файла
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        logger.info(f'Файл успешно загружен и сохранён в {save_path}')
        return True
    except Exception as ex:
        logger.error('Ошибка при загрузке файла: ', ex)
        ...
        return False
```

**Описание**: Загружает файл по указанному URL и сохраняет его в заданный путь.

**Параметры**:

-   `url` (str): URL файла для загрузки. По умолчанию используется значение переменной `url`.
-   `save_path` (Path): Путь для сохранения загруженного файла. По умолчанию используется значение переменной `proxies_list_path`.

**Возвращает**:

-   `bool`: `True`, если загрузка и сохранение прошли успешно, `False` в случае ошибки.

### `get_proxies_dict`

```python
def get_proxies_dict(file_path: Path = proxies_list_path) -> Dict[str, List[Dict[str, Any]]]:
    """
    Парсит файл с прокси-адресами и распределяет их по категориям.

    :param file_path: Путь к файлу с прокси.
    :return: Словарь с распределёнными по типам прокси.
    """

    download_proxies_list()

    proxies: Dict[str, List[Dict[str, Any]]] = {
        'http': [],
        'socks4': [],
        'socks5': []
    }

    try:
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(http|socks4|socks5)://([\d\.]+):(\d+)', line.strip())
                if match:
                    protocol, host, port = match.groups()
                    proxies[protocol].append({'protocol':protocol, 'host': host, 'port': port})
    except FileNotFoundError as ex:
        logger.error('Файл не найден: ', ex)
        ...
    except Exception as ex:
        logger.error('Ошибка при парсинге прокси: ', ex)
        ...

    return proxies
```

**Описание**: Парсит файл с прокси-адресами и распределяет их по категориям (http, socks4, socks5).

**Параметры**:

-   `file_path` (Path): Путь к файлу с прокси. По умолчанию используется значение переменной `proxies_list_path`.

**Возвращает**:

-   `Dict[str, List[Dict[str, Any]]]`: Словарь, где ключи — это типы прокси (`'http'`, `'socks4'`, `'socks5'`), а значения — списки словарей, содержащих информацию о прокси (`'protocol'`, `'host'`, `'port'`).

### `check_proxy`

```python
def check_proxy(proxy: dict) -> bool:
    """
    Проверяет работоспособность прокси-сервера.
    
    :param proxy: Словарь с данными прокси (host, port, protocol).
    :return: True, если прокси работает, иначе False.
    """
    try:
        # Попытка сделать запрос через прокси
        response = requests.get("https://httpbin.org/ip", proxies={proxy['protocol']: f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"}, timeout=5)
        # Проверка кода ответа
        if response.status_code == 200:
            logger.info(f"Прокси найден: {proxy['host']}:{proxy['port']}")
            return True
        else:
            logger.warning(f"Прокси не работает: {proxy['host']}:{proxy['port']} (Статус: {response.status_code})", None, False)
            return False
    except (ProxyError, RequestException) as ex:
        logger.warning(f"Ошибка подключения через прокси {proxy['host']}:{proxy['port']}:",ex)
        return False
```

**Описание**: Проверяет работоспособность прокси-сервера, отправляя запрос к `https://httpbin.org/ip` через прокси.

**Параметры**:

-   `proxy` (dict): Словарь с данными прокси, содержащий ключи `'protocol'`, `'host'`, `'port'`.

**Возвращает**:

-   `bool`: `True`, если прокси работает, `False` в противном случае.

## Переменные

### `url`

```python
url: str = 'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt'
```

**Описание**: URL-адрес источника списка прокси.

**Тип**: `str`

### `proxies_list_path`

```python
proxies_list_path: Path = gs.path.src / 'webdriver' / 'proxies.txt'
```

**Описание**: Путь к файлу для сохранения списка прокси.

**Тип**: `Path`