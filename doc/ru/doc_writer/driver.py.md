# Модуль `src.webdriver.driver`

## Обзор

Модуль `src.webdriver.driver` предназначен для работы с веб-драйверами Selenium. Основной целью класса `Driver` является предоставление унифицированного интерфейса для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера, навигации, управления куками, обработки исключений и других операций.

## Оглавление

- [Обзор](#обзор)
- [Класс `Driver`](#класс-driver)
    - [Инициализация (`__init__`)](#инициализация-__init__)
    - [Инициализация подкласса (`__init_subclass__`)](#инициализация-подкласса-__init_subclass__)
    - [Проксирование атрибутов (`__getattr__`)](#проксирование-атрибутов-__getattr__)
    - [Прокрутка страницы (`scroll`)](#прокрутка-страницы-scroll)
    - [Определение языка страницы (`locale`)](#определение-языка-страницы-locale)
    - [Переход по URL (`get_url`)](#переход-по-url-get_url)
    - [Открытие новой вкладки (`window_open`)](#открытие-новой-вкладки-window_open)
    - [Ожидание (`wait`)](#ожидание-wait)
    - [Сохранение куки локально (`_save_cookies_localy`)](#сохранение-куки-локально-_save_cookies_localy)
    - [Извлечение HTML-контента (`fetch_html`)](#извлечение-html-контента-fetch_html)

## Класс `Driver`

### Инициализация (`__init__`)

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    .. method:: __init__(self, webdriver_cls, *args, **kwargs)
    
    Инициализирует экземпляр класса Driver.

    :param webdriver_cls: Класс WebDriver, например Chrome или Firefox.
    :type webdriver_cls: type
    :param args: Позиционные аргументы для драйвера.
    :param kwargs: Ключевые аргументы для драйвера.

    Пример:
        >>> from selenium.webdriver import Chrome
        >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """
    if not hasattr(webdriver_cls, 'get'):
        raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
    self.driver = webdriver_cls(*args, **kwargs)
```

**Описание**: Инициализирует экземпляр класса `Driver`.

**Параметры**:

-   `webdriver_cls` (type): Класс WebDriver, например, `Chrome` или `Firefox`.
-   `*args`: Позиционные аргументы для драйвера.
-   `**kwargs`: Ключевые аргументы для драйвера.

**Вызывает исключения**:

-   `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver.

### Инициализация подкласса (`__init_subclass__`)

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    """
    .. method:: __init_subclass__(cls, *, browser_name=None, **kwargs)

    Автоматически вызывается при создании подкласса `Driver`.

    :param browser_name: Имя браузера.
    :type browser_name: str
    :param kwargs: Дополнительные аргументы.

    Исключение:
        ValueError: Если browser_name не указан.
    """
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
    cls.browser_name = browser_name
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:

-   `browser_name` (str): Имя браузера.
-   `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:

-   `ValueError`: Если `browser_name` не указан.

### Проксирование атрибутов (`__getattr__`)

```python
def __getattr__(self, item):
    """
    .. method:: __getattr__(self, item)

    Прокси для доступа к атрибутам драйвера.

    :param item: Имя атрибута.
    :type item: str

    Пример:
        >>> driver.current_url
    """
    return getattr(self.driver, item)
```

**Описание**: Проксирует доступ к атрибутам драйвера.

**Параметры**:

-   `item` (str): Имя атрибута.

**Возвращает**:

-   Значение атрибута драйвера.

### Прокрутка страницы (`scroll`)

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    .. method:: scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)

    Прокручивает страницу в указанном направлении.

    :param scrolls: Количество прокруток, по умолчанию 1.
    :type scrolls: int
    :param frame_size: Размер прокрутки в пикселях, по умолчанию 600.
    :type frame_size: int
    :param direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
    :type direction: str
    :param delay: Задержка между прокрутками, по умолчанию 0.3.
    :type delay: float
    :return: True, если успешно, иначе False.
    :rtype: bool

    Пример:
        >>> driver.scroll(scrolls=3, direction='down')
    """
    def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
        """
        .. method:: carousel(direction='', scrolls=1, frame_size=600, delay=.3)

        Локальный метод для прокрутки экрана.

        :param direction: Направление ('down', 'up').
        :type direction: str
        :param scrolls: Количество прокруток.
        :type scrolls: int
        :param frame_size: Размер прокрутки.
        :type frame_size: int
        :param delay: Задержка между прокрутками.
        :type delay: float
        :return: True, если успешно, иначе False.
        :rtype: bool
        """
        try:
            for _ in range(scrolls):
                self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                self.wait(delay)
            return True
        except Exception as ex:
            logger.error('Ошибка при прокрутке', exc_info=ex)
            return False

    try:
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
    except Exception as ex:
        logger.error('Ошибка в функции прокрутки', ex)
        return False
```

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:

-   `scrolls` (int): Количество прокруток, по умолчанию 1.
-   `frame_size` (int): Размер прокрутки в пикселях, по умолчанию 600.
-   `direction` (str): Направление прокрутки ('both', 'down', 'up'), по умолчанию 'both'.
-   `delay` (float): Задержка между прокрутками, по умолчанию 0.3.

**Возвращает**:

-   `bool`: `True`, если успешно, иначе `False`.

### Определение языка страницы (`locale`)

```python
@property
def locale(self) -> Optional[str]:
    """
    .. method:: locale(self)

    Определяет язык страницы на основе мета-тегов или JavaScript.

    :return: Код языка, если найден, иначе None.
    :rtype: Optional[str]

    Пример:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' или None
    """
    try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
    except Exception as ex:
        logger.debug('Не удалось определить язык сайта из META', ex)
        try:
            return self.get_page_lang()
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из JavaScript', ex)
            return
```

**Описание**: Определяет язык страницы на основе мета-тегов или JavaScript.

**Возвращает**:

-   `Optional[str]`: Код языка, если найден, иначе `None`.

### Переход по URL (`get_url`)

```python
def get_url(self, url: str) -> bool:
    """
    Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

    Args:
        url (str): URL для перехода.

    Возвращает:
        bool: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

    Исключения:
        WebDriverException: Если возникает ошибка с WebDriver.
        InvalidArgumentException: Если URL некорректен.
        Exception: Для любых других ошибок при переходе.
    """
    try:
        _previous_url = copy.copy(self.current_url)
    except Exception as ex:
        logger.error("Ошибка при получении текущего URL", ex)
        #return False
    
    try:
        self.driver.get(url)
        
        while self.ready_state != 'complete':
            """ Ожидаем завершения загрузки страницы """

        if url != _previous_url:
            self.previous_url = _previous_url

        self._save_cookies_localy()
        return True
        
    except WebDriverException as ex:
        logger.error('WebDriverException', ex)
        return False

    except InvalidArgumentException as ex:
        logger.error(f"InvalidArgumentException {url}", ex)
        return False
    except Exception as ex:
        logger.error(f'Ошибка при переходе по URL: {url}\
', ex)
        return False
```

**Описание**: Переходит по указанному URL, сохраняет текущий и предыдущий URL, а также куки.

**Параметры**:

-   `url` (str): URL для перехода.

**Возвращает**:

-   `bool`: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

**Вызывает исключения**:

-   `WebDriverException`: Если возникает ошибка с WebDriver.
-   `InvalidArgumentException`: Если URL некорректен.
-   `Exception`: Для любых других ошибок при переходе.

### Открытие новой вкладки (`window_open`)

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url (Optional[str]): URL to open in the new tab. Defaults to `None`.
    """
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Описание**: Открывает новую вкладку в текущем окне браузера и переключается на нее.

**Параметры**:

-   `url` (Optional[str]): URL для открытия в новой вкладке. По умолчанию `None`.

### Ожидание (`wait`)

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное количество времени.

    Args:
        delay (float, optional): Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
    time.sleep(delay)
```

**Описание**: Ожидает указанное количество времени.

**Параметры**:

-   `delay` (float, optional): Время задержки в секундах. По умолчанию 0.3.

### Сохранение куки локально (`_save_cookies_localy`)

```python
def _save_cookies_localy(self) -> None:
    """
    Сохраняет текущие куки веб-драйвера в локальный файл.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении куки.
    """
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Ошибка при сохранении куки:', ex)
```

**Описание**: Сохраняет текущие куки веб-драйвера в локальный файл.

**Вызывает исключения**:

-   `Exception`: Если возникает ошибка при сохранении куки.

### Извлечение HTML-контента (`fetch_html`)

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Извлекает HTML-контент из файла или веб-страницы.

    Args:
        url (str): Путь к файлу или URL для извлечения HTML-контента.

    Returns:
        Optional[bool]: Возвращает `True`, если контент успешно получен, иначе `None`.

    Raises:
        Exception: Если возникает ошибка при извлечении контента.
    """
    if url.startswith('file://'):
        cleaned_url = url.replace('file://', '')
        match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
        if match:
            file_path = Path(match.group(0))
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.html_content = file.read()
                    return True
                except Exception as ex:
                    logger.error('Ошибка при чтении файла:', ex)
                    return False
            else:
                logger.error('Локальный файл не найден:', file_path)
                return False
        else:
            logger.error('Некорректный путь к файлу:', cleaned_url)
            return False
    elif url.startswith('http://') or url.startswith('https://'):
        try:
            if self.get_url(url):
                self.html_content = self.page_source
                return True
        except Exception as ex:
            logger.error(f"Ошибка при получении {url}:", ex)
            return False
    else:
        logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
        return False
```

**Описание**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:

-   `url` (str): Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:

-   `Optional[bool]`: `True`, если контент успешно получен, иначе `None`.

**Вызывает исключения**:

-   `Exception`: Если возникает ошибка при извлечении контента.