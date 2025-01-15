# Модуль `src.webdriver.driver`

## Обзор

Модуль `driver.py` предоставляет класс `Driver` для взаимодействия с веб-драйверами Selenium. В этом документе подробно описан принцип работы модуля.

## Оглавление

- [Обзор](#обзор)
- [Алгоритм работы модуля `driver.py`](#алгоритм-работы-модуля-driverpy)
    - [Инициализация (`__init__`)](#инициализация-__init__)
    - [Инициализация подкласса (`__init_subclass__`)](#инициализация-подкласса-__init_subclass__)
    - [Проксирование атрибутов (`__getattr__`)](#проксирование-атрибутов-__getattr__)
    - [Прокрутка страницы (`scroll`)](#прокрутка-страницы-scroll)
    - [Определение языка страницы (`locale`)](#определение-языка-страницы-locale)
    - [Навигация по URL (`get_url`)](#навигация-по-url-get_url)
    - [Открытие новой вкладки (`window_open`)](#открытие-новой-вкладки-window_open)
    - [Ожидание (`wait`)](#ожидание-wait)
    - [Сохранение куки локально (`_save_cookies_localy`)](#сохранение-куки-локально-_save_cookies_localy)
    - [Получение HTML контента (`fetch_html`)](#получение-html-контента-fetch_html)
- [Диаграмма Mermaid](#диаграмма-mermaid)
    - [Объяснение диаграммы Mermaid](#объяснение-диаграммы-mermaid)
- [Детальное объяснение](#детальное-объяснение)
    - [Импорты](#импорты)
    - [Классы](#классы)
    - [Функции](#функции)
    - [Переменные](#переменные)
    - [Потенциальные ошибки и области для улучшения](#потенциальные-ошибки-и-области-для-улучшения)
    - [Связи с другими частями проекта](#связи-с-другими-частями-проекта)

## Алгоритм работы модуля `driver.py`

Модуль `driver.py` предоставляет класс `Driver` для взаимодействия с веб-драйверами Selenium. Вот пошаговое объяснение того, как работает этот модуль:

### Инициализация (`__init__`)

1.  Класс `Driver` создается с `webdriver_cls` (например, `Chrome`, `Firefox`) и необязательными аргументами (`*args`, `**kwargs`).
2.  **Пример**: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`
3.  Конструктор проверяет, есть ли у предоставленного `webdriver_cls` метод `get`, и вызывает `TypeError`, если его нет, гарантируя, что это допустимый класс Selenium WebDriver.
4.  Если проверка пройдена, объект драйвера инициализируется: `self.driver = webdriver_cls(*args, **kwargs)`.

### Инициализация подкласса (`__init_subclass__`)

1.  Когда создается подкласс `Driver`, этот метод вызывается автоматически.
2.  **Пример**: `class CustomDriver(Driver, browser_name='Chrome'): ...`
3.  Проверяет, был ли указан `browser_name` при создании подкласса, и вызывает `ValueError`, если он отсутствует.
4.  Атрибут `browser_name` сохраняется в подклассе для будущего использования: `cls.browser_name = browser_name`.

### Проксирование атрибутов (`__getattr__`)

1.  При доступе к атрибуту экземпляра `Driver`, который не определен непосредственно в классе `Driver`, вызывается метод `__getattr__`.
2.  **Пример**: Доступ к `driver.page_source` вызывает `self.driver.page_source`, где `driver` является экземпляром класса `Driver`.
3.  Этот метод проксирует доступ к атрибутам базовому Selenium WebDriver: `return getattr(self.driver, item)`.

### Прокрутка страницы (`scroll`)

1.  Метод `scroll` вызывается с параметрами `scrolls`, `frame_size`, `direction` и `delay` для прокрутки страницы в указанном направлении.
2.  **Пример**: `driver.scroll(scrolls=2, direction='down')`
3.  Используется вложенная функция `carousel`, которая использует `execute_script` для выполнения прокрутки. Она ждет заданной задержки между прокрутками, используя метод `wait()`.
4.  Направление может быть `'forward'`/`'down'`, `'backward'`/`'up'` или `'both'`, определяя направление прокрутки.

### Определение языка страницы (`locale`)

1.  Свойство `locale` пытается извлечь язык страницы из тега `<meta>` или с помощью метода JavaScript (`get_page_lang()`, который не реализован в этом коде).
2.  **Пример**: `lang = driver.locale`
3.  Используется `find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")` для поиска тега `<meta>`, а затем извлекается его атрибут `content`.
4.  Если тег `<meta>` не удается найти или метод JavaScript не срабатывает, возвращается `None`.

### Навигация по URL (`get_url`)

1.  Метод `get_url` переходит по заданному URL, вызывая `self.driver.get(url)`.
2.  **Пример**: `driver.get_url('https://example.com')`
3.  Перед навигацией сохраняет копию `current_url`, используя `copy.copy(self.current_url)`.
4.  Он ждет, пока страница полностью загрузится, используя цикл `while self.ready_state != 'complete':`.
5.  Обновляет предыдущий URL `self.previous_url`, если новый URL отличается от предыдущего.
6.  Сохраняет куки локально с помощью `self._save_cookies_localy()` после загрузки страницы.
7.  Обрабатывает `WebDriverException`, `InvalidArgumentException` и общие `Exception`.

### Открытие новой вкладки (`window_open`)

1.  Метод `window_open` открывает новую вкладку и переключает фокус на нее.
2.  **Пример**: `driver.window_open('https://newtab.com')`
3.  Используется `execute_script('window.open();')` для открытия новой вкладки, затем `switch_to.window(self.window_handles[-1])` для переключения на эту новую вкладку. Если предоставлен URL, новая вкладка откроет этот URL, используя метод `get()`.

### Ожидание (`wait`)

1.  Метод `wait` приостанавливает выполнение на указанное количество времени.
2.  **Пример**: `driver.wait(2)`
3.  Вызывается `time.sleep(delay)` для введения задержки.

### Сохранение куки локально (`_save_cookies_localy`)

1.  Метод `_save_cookies_localy` сохраняет куки в файл, определенный в `gs.cookies_filepath`.
2.  **Пример**: `driver._save_cookies_localy()`
3.  Использует `pickle.dump()` для сохранения куки.
4.  В настоящее время метод заглушен с помощью `return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`.

### Получение HTML контента (`fetch_html`)

1.  Метод `fetch_html` получает HTML-контент из указанного URL (локального файла или HTTP/HTTPS).
2.  **Пример**: `driver.fetch_html('file:///path/to/local.html')` или `driver.fetch_html('https://example.com')`
3.  Проверяется, является ли URL локальным файлом или веб-адресом.
4.  Для локального файла открывается файл и считывается его содержимое и сохраняется в `self.html_content`.
5.  Для веб-адреса выполняется переход по URL, вызывая `get_url()`, и получается `page_source`.
6.  Обрабатывает исключения и регистрирует ошибки, если не удается прочитать или загрузить страницу.

## Диаграмма Mermaid

```mermaid
flowchart TD
    Start[Start] --> InitDriver[Initialize Driver: <br><code>Driver(webdriver_cls, *args, **kwargs)</code>]
    InitDriver --> CheckWebDriver[Check if <br><code>webdriver_cls</code> is valid]
    CheckWebDriver -- Yes --> CreateWebDriver[Create driver instance <br><code>self.driver = webdriver_cls(*args, **kwargs)</code>]
    CheckWebDriver -- No --> TypeError[Raise TypeError]
    CreateWebDriver --> SubclassInit[Subclass Initialization: <br><code>__init_subclass__</code>]
    SubclassInit --> CheckBrowserName[Check if <br><code>browser_name</code> is specified]
    CheckBrowserName -- Yes --> SetBrowserName[Set browser name: <br><code>cls.browser_name = browser_name</code>]
    CheckBrowserName -- No --> ValueError[Raise ValueError]
    SetBrowserName --> AttributeProxy[Access Attribute: <br><code>__getattr__(self, item)</code>]
    AttributeProxy --> GetDriverAttribute[Get attribute from <br><code>self.driver</code>]
    GetDriverAttribute --> ScrollPage[Scroll Page: <br><code>scroll(self, scrolls, frame_size, direction, delay)</code>]
    ScrollPage --> CarouselFunction[<code>carousel(direction, scrolls, frame_size, delay)</code>]
    CarouselFunction --> ExecuteScript[Execute scroll by script:<br><code>execute_script(window.scrollBy(0,{direction}{frame_size}))</code>]
    ExecuteScript --> WaitAfterScroll[Wait for a while:<br><code>wait(delay)</code>]
    WaitAfterScroll -->  ScrollLoop[Loop if <br><code>scrolls</code> remain ]
    ScrollLoop -- Yes --> ExecuteScript
    ScrollLoop -- No --> ScrollComplete[Scroll operation complete]
    ScrollComplete --> GetLocale[Get Page Locale:<br><code>locale</code>]
    GetLocale --> GetMetaTag[Get <br><code>meta</code> tag]
     GetMetaTag -- Success --> GetContent[Get <br><code>content</code> attribute]
     GetContent --> ReturnLocale[Return language code]
     GetMetaTag -- Fail --> TryJavaScript[Try JavaScript <br><code>get_page_lang()</code>]
    TryJavaScript -- Success --> ReturnLocale
    TryJavaScript -- Fail --> ReturnNone[Return None]
    ReturnLocale --> NavigateToURL[Navigate to URL: <br><code>get_url(self, url)</code>]
    ReturnNone --> NavigateToURL
    NavigateToURL --> GetCurrentURL[Get current URL]
     GetCurrentURL -- Success --> SavePreviousURL[Save to <br><code>previous_url</code> if changed]
     GetCurrentURL -- Fail -->  ReturnFalse1[Return False]
    SavePreviousURL --> LoadURL[Load URL: <br><code>self.driver.get(url)</code>]
    LoadURL --> WaitForComplete[Wait until <br><code>readyState == 'complete'</code>]
    WaitForComplete -- Yes --> SaveCookies[Save Cookies: <br><code>_save_cookies_localy()</code>]
    WaitForComplete -- No --> WaitForComplete
    SaveCookies --> ReturnTrue[Return True]
    LoadURL -- Fail --> CatchWebDriverError[Catch <br><code>WebDriverException</code>]
     CatchWebDriverError --> LogWebDriverError[Log error]
     LogWebDriverError --> ReturnFalse2[Return False]
    LoadURL -- Fail --> CatchInvalidArgError[Catch <br><code>InvalidArgumentException</code>]
     CatchInvalidArgError --> LogInvalidArgError[Log error]
    LogInvalidArgError --> ReturnFalse3[Return False]
      LoadURL -- Fail --> CatchAnyError[Catch other exceptions]
    CatchAnyError --> LogAnyError[Log error]
    LogAnyError --> ReturnFalse4[Return False]
    ReturnFalse1 --> End[End]
    ReturnFalse2 --> End
    ReturnFalse3 --> End
    ReturnFalse4 --> End
    ReturnTrue --> End
    End --> OpenNewTab[Open New Tab: <br><code>window_open(self, url)</code>]
    OpenNewTab --> ExecuteNewTabScript[Execute: <br><code>execute_script('window.open();')</code>]
    ExecuteNewTabScript --> SwitchToNewTab[Switch to new tab]
    SwitchToNewTab --> LoadURLinNewTab[Load URL if specified]
    LoadURLinNewTab --> End1[End]
   End1 --> WaitTime[Wait Time: <br><code>wait(self, delay)</code>]
   WaitTime --> SleepTime[<code>time.sleep(delay)</code>]
   SleepTime --> End2[End]
   End2 --> SaveCookiesLocally[Save Cookies Locally: <br><code>_save_cookies_localy(self)</code>]
   SaveCookiesLocally --> OpenCookieFile[Open cookie file in <br><code>gs.cookies_filepath</code>]
    OpenCookieFile --> DumpCookies[Save cookies using <br><code>pickle.dump()</code>]
    DumpCookies -->  ReturnTrueDebug[Return True for debugging]
    SaveCookiesLocally -- Fail --> LogErrorSaveCookies[Log error saving cookies]
    LogErrorSaveCookies --> End3[End]
    ReturnTrueDebug --> End3
  End3 --> FetchHTML[Fetch HTML: <br><code>fetch_html(self, url)</code>]
    FetchHTML --> CheckURLType[Check if url starts with file, http or https]
    CheckURLType -- File --> ExtractFilePath[Extract File path]
    ExtractFilePath --> CheckFileExists[Check if file exists]
     CheckFileExists -- Yes --> ReadFile[Read the file content]
    ReadFile --> SetHTMLContent[Set html content as `self.html_content`]
       SetHTMLContent --> ReturnTrue4[Return True]
    CheckFileExists -- No -->  LogFileNotFound[Log "Local file not found"]
    LogFileNotFound --> ReturnFalse5[Return False]
    CheckURLType -- HTTP/HTTPS --> NavigateAndGetHTML[Call <br><code>get_url(url)</code>]
    NavigateAndGetHTML -- Success --> GetPageSource[Get the page source]
    GetPageSource --> SetHTMLContent
    NavigateAndGetHTML -- Fail --> LogErrorFetchingURL[Log error fetching URL]
    LogErrorFetchingURL --> ReturnFalse6[Return False]
    CheckURLType -- Other --> LogUnsupportedProtocol[Log unsupported protocol error]
    LogUnsupportedProtocol --> ReturnFalse7[Return False]
     ReturnFalse5 --> End4[End]
    ReturnFalse6 --> End4
    ReturnFalse7 --> End4
   ReturnTrue4 --> End4
```

### Объяснение диаграммы Mermaid

**Зависимости:**

*   **`time`**: Используется в методе `wait` для приостановки выполнения на заданное время с помощью `time.sleep(delay)`. Это стандартная библиотека Python для работы со временем.
*   **`copy`**: Используется в методе `get_url` для создания копии текущего URL перед навигацией с помощью `copy.copy(self.current_url)`. Модуль `copy` предоставляет операции поверхностного и глубокого копирования.
*   **`pickle`**: Используется в методе `_save_cookies_localy` для сериализации куки и сохранения их в файл с помощью `pickle.dump(self.driver.get_cookies(), cookiesfile)`. Модуль `pickle` используется для сериализации и десериализации объектов Python.
*   **`pathlib`**: Используется в методе `fetch_html` для работы с путями файлов с помощью `Path(match.group(0))`. Это стандартная библиотека Python.
*   **`re`**: Используется в методе `fetch_html` для извлечения пути к файлу с помощью регулярного выражения `re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)`. Это стандартная библиотека Python.
*   **`gs`**: Глобальные настройки, импортированные из файла проекта (скорее всего, `src.config.settings`). Модуль предоставляет доступ к глобальным настройкам проекта, включая пути к файлам, такие как `gs.cookies_filepath`.
*   **`logger`**: Функции логирования из `src.logger.logger`. Используется для обработки ошибок и отладки.
*   **`selenium.webdriver`**: Используется для взаимодействия с веб-драйверами. Аргумент `webdriver_cls` класса `Driver` является экземпляром `selenium.webdriver`.
*   **`selenium.webdriver.common.by`**: Используется для поиска элементов на веб-странице с помощью CSS-селекторов (`By.CSS_SELECTOR`).
*   **`selenium.common.exceptions`**: Используется для обработки исключений, специфичных для веб-драйверов selenium. `WebDriverException` и `InvalidArgumentException`.

## Детальное объяснение

### Импорты

*   `time`: Используется для реализации задержек в методе `wait`, позволяя скрипту приостановить выполнение.
*   `copy`: Используется для создания копии текущего URL в методе `get_url`, сохраняя его перед навигацией.
*   `pickle`: Используется для сериализации и сохранения куки веб-драйвера в локальный файл в методе `_save_cookies_localy` для постоянного хранения.
*   `pathlib.Path`: Используется в `fetch_html` для манипуляций с путями к файлам, например, для проверки наличия файла.
*    `re`: Используется для извлечения пути к файлу из URL в методе `fetch_html`.
*   `src.config.settings as gs`: Импортирует глобальные настройки из модуля `src.config.settings`, специально для доступа к пути к файлу cookie (`gs.cookies_filepath`).
*   `src.logger.logger as logger`: Импортирует модуль логирования для обработки ошибок, предупреждений и информационных сообщений в классе.
*   `selenium.webdriver`: Импортирует основные классы для работы с веб-драйверами Selenium (например, `Chrome`, `Firefox`).
*   `selenium.webdriver.common.by.By`: Предоставляет способы поиска элементов на веб-странице.
*   `selenium.common.exceptions.WebDriverException`, `selenium.common.exceptions.InvalidArgumentException`: Импортирует исключения из Selenium для обработки специфических ошибок, связанных с веб-драйвером.

### Классы

*   `Driver`:
    *   **Назначение**: Предоставляет высокоуровневый интерфейс для управления веб-драйверами Selenium, инкапсулируя инициализацию, навигацию, прокрутку и управление куки.
    *   **Атрибуты**:
        *   `self.driver`: Хранит фактический экземпляр Selenium WebDriver.
        *   `self.html_content`: Хранит полученный HTML-контент из URL или файла.
        *   `self.previous_url`: Хранит предыдущий посещенный URL.
    *   **Методы**:
        *   `__init__(self, webdriver_cls, *args, **kwargs)`: Инициализирует экземпляр `Driver`, создавая объект WebDriver, гарантирует передачу допустимого класса драйвера и вызывает `TypeError`, если это не так.
        *   `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Вызывается при создании подкласса, требует предоставления `browser_name`.
        *   `__getattr__(self, item)`: Проксирование атрибутов, извлекает атрибуты, не определенные непосредственно в экземпляре `Driver`.
        *   `scroll(self, scrolls, frame_size, direction, delay)`: Прокручивает веб-страницу в указанном направлении и использует вложенную функцию с именем `carousel` для прокрутки с помощью метода `execute_script`.
        *   `locale(self)`: Свойство, которое пытается определить язык страницы. Сначала пытается получить язык из метатегов, если не удается найти метатег, пытается использовать вызов JavaScript `get_page_lang()` (который не реализован в предоставленном коде).
        *   `get_url(self, url)`: Переходит к URL с помощью веб-драйвера Selenium, обрабатывает исключения, такие как `WebDriverException`, `InvalidArgumentException`, и сохраняет куки и предыдущий URL.
        *   `window_open(self, url)`: Открывает новую вкладку и переключается на нее с помощью инъекции JavaScript и загружает URL, если он предоставлен.
        *   `wait(self, delay)`: Вводит задержку на указанное количество времени с помощью `time.sleep`.
        *   `_save_cookies_localy(self)`: Сохраняет куки локально с помощью `pickle`.
        *    `fetch_html(self, url)`: Получает HTML-контент из локального файла или URL, поддерживает протоколы `file://`, `http://` и `https://`.

### Функции

*   `__init__(self, webdriver_cls, *args, **kwargs)`:
    *   **Аргументы**:
        *   `webdriver_cls` (`type`): Класс WebDriver (например, `Chrome`, `Firefox`).
        *   `*args`: Позиционные аргументы для конструктора WebDriver.
        *   `**kwargs`: Именованные аргументы для конструктора WebDriver.
    *   **Назначение**: Инициализирует новый экземпляр класса `Driver`, создавая базовый Selenium WebDriver и проверяя `webdriver_cls`.
    *   **Возврат**: `None`.
*   `__init_subclass__(cls, *, browser_name=None, **kwargs)`:
    *   **Аргументы**:
        *   `cls` (`type`): Инициализируемый класс (подкласс).
        *   `browser_name` (`Optional[str]`): Название браузера.
        *   `**kwargs`: Дополнительные именованные аргументы.
    *   **Назначение**: Устанавливает атрибут имени браузера в подклассе, гарантируя, что он указан во время создания подкласса.
    *   **Возврат**: `None`.
*   `__getattr__(self, item)`:
    *   **Аргументы**:
        *   `item` (`str`): Имя атрибута для доступа.
    *   **Назначение**: Проксирует доступ к атрибутам базового драйвера Selenium.
    *   **Возврат**: Атрибут из базового драйвера.
*   `scroll(self, scrolls, frame_size, direction, delay)`:
    *   **Аргументы**:
        *   `scrolls` (`int`): Количество прокруток.
        *   `frame_size` (`int`): Размер кадра прокрутки в пикселях.
        *   `direction` (`str`): Направление прокрутки, может быть `'forward'`, `'down'`, `'backward'`, `'up'` или `'both'`.
        *   `delay` (`float`): Задержка между прокрутками в секундах.
    *   **Назначение**: Прокручивает страницу.
    *   **Возврат**: `bool`.
*   `locale(self)`:
    *   **Аргументы**:
        *   `self` (`Driver`): Экземпляр класса `Driver`.
    *   **Назначение**: Пытается определить язык страницы, используя метатеги или JavaScript.
    *   **Возврат**: `Optional[str]`, код языка, если найден, иначе `None`.
*   `get_url(self, url)`:
    *   **Аргументы**:
        *   `url` (`str`): URL для перехода.
    *   **Назначение**: Переходит к заданному URL, ждет завершения загрузки страницы, сохраняет куки и обрабатывает исключения.
    *   **Возврат**: `bool`.
*   `window_open(self, url)`:
    *   **Аргументы**:
        *   `url` (`Optional[str]`): URL для загрузки в новой вкладке.
    *   **Назначение**: Открывает новую вкладку и загружает URL, если он предоставлен.
    *   **Возврат**: `None`.
*   `wait(self, delay)`:
    *   **Аргументы**:
        *   `delay` (`float`): Продолжительность задержки в секундах.
    *   **Назначение**: Вводит задержку в выполнении скрипта.
    *   **Возврат**: `None`.
*   `_save_cookies_localy(self)`:
    *   **Аргументы**:
        *   `self` (`Driver`): Экземпляр класса `Driver`.
    *   **Назначение**: Сохраняет куки веб-драйвера в локальный файл с помощью `pickle`.
    *   **Возврат**: `None`.
*   `fetch_html(self, url)`:
    *   **Аргументы**:
        *   `url` (`str`): URL для получения HTML (файл, http, https).
    *   **Назначение**: Извлекает и сохраняет HTML-контент из указанного URL, поддерживает локальные пути к файлам, HTTP и HTTPS URL.
    *   **Возврат**: `Optional[bool]`.

### Переменные

*   `self.driver`: Хранит экземпляр Selenium WebDriver.
*   `self.html_content`: Хранит содержимое страницы после навигации.
*   `self.previous_url`: Хранит ранее посещенный URL.
*   `gs.cookies_filepath`: Путь к файлу для хранения куки, загруженный из `src.config.settings`.
*   `logger`: Экземпляр логгера для регистрации ошибок.

### Потенциальные ошибки и области для улучшения

*   **`get_page_lang()`**: Метод `get_page_lang()` упоминается, но не реализован. Его необходимо реализовать для полной функциональности.
*   **Сохранение куки**: Метод `_save_cookies_localy()` в настоящее время заглушен для отладки (`return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug`), что препятствует сохранению куки. Это должно быть заменено правильным кодом, использующим `pickle.dump()` с обработкой ошибок.
*   **Обработка исключений**: Обработка ошибок может быть улучшена с помощью более конкретного логирования.
*   **Метод прокрутки**: Вложенный метод `carousel` можно упростить.
*   **Чтение файлов**: Чтение файлов можно улучшить, используя функцию `read_text_file` из модуля `src.utils.file` для согласованности.

### Связи с другими частями проекта

*   **`src.config.settings`**: Модуль импортирует `gs` из `src.config.settings` для доступа к глобальным настройкам проекта, в частности к пути к файлу, где хранятся куки. Этот модуль должен предоставлять путь к файлу cookie.
*   **`src.logger.logger`**: Этот модуль использует функциональность логирования из модуля `src.logger.logger` для регистрации ошибок и отладочной информации. Этот модуль должен быть реализован для логирования.
*   **`selenium`**: Модуль использует библиотеку `selenium` для взаимодействия с веб-драйверами, поэтому `selenium` является зависимостью.
*   **`src.utils.file`**: Этот модуль может выиграть от использования функций модуля `src.utils.file` (например, функции `read_text_file`), но в настоящее время не используется.

Этот исчерпывающий анализ дает подробное представление о модуле `driver.py` и о том, как он вписывается в более широкий проект.