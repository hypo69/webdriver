## Анализ кода модуля `driver.py`

### 1. <алгоритм>
**Описание рабочего процесса:**

Модуль `driver.py` предоставляет класс `Driver`, который является оберткой для веб-драйверов Selenium. Основная цель класса — упростить взаимодействие с веб-драйвером, предоставляя методы для навигации, управления куками, обработки исключений и других операций.

**Блок-схема:**

1.  **Инициализация `Driver`**:
    *   При создании экземпляра `Driver` проверяется, является ли `webdriver_cls` допустимым классом WebDriver.
    *   Создается экземпляр `webdriver_cls`.
    *   Пример: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`

2.  **Инициализация подкласса `Driver`**:
    *   При создании подкласса `Driver` проверяется наличие аргумента `browser_name`.
    *   Пример:
    ```python
    class MyDriver(Driver, browser_name='chrome'):
       def __init__(self, *args, **kwargs):
           super().__init__(Chrome, *args, **kwargs)
    ```

3.  **Доступ к атрибутам драйвера**:
    *   Метод `__getattr__` позволяет обращаться к атрибутам и методам объекта `self.driver`.
    *   Пример: `driver.get('https://example.com')` вызывает `self.driver.get('https://example.com')`

4.  **Прокрутка страницы**:
    *   Функция `scroll` прокручивает страницу на заданное количество раз в указанном направлении.
    *   Пример: `driver.scroll(scrolls=2, direction='down', frame_size=300, delay=0.5)`
        *   Внутренняя функция `carousel` выполняет прокрутку.
        *   `execute_script` используется для выполнения JavaScript, который прокручивает страницу.
        *   Пример: `window.scrollBy(0,600)` прокручивает на 600px вниз
        *   Пример: `window.scrollBy(0,-600)` прокручивает на 600px вверх

5.  **Определение языка страницы**:
    *   Свойство `locale` пытается определить язык страницы, сначала используя мета-тег `Content-Language`, затем JavaScript.
    *   Пример: `language = driver.locale`

6.  **Навигация по URL**:
    *   Метод `get_url` загружает страницу по указанному URL.
    *   Пример: `driver.get_url('https://example.com')`
    *   Перед загрузкой URL сохраняет текущий URL в переменную `_previous_url`.
    *   Вызывает `self.driver.get(url)` для загрузки страницы.
    *   Ждет полной загрузки страницы, проверяя `self.ready_state`.
    *   После загрузки сохраняет куки с помощью `self._save_cookies_localy()`.
    *   Обрабатывает исключения `WebDriverException` и `InvalidArgumentException`, а также общие исключения.

7.  **Открытие нового окна**:
    *   Метод `window_open` открывает новое окно и переключается на него.
    *   Пример: `driver.window_open('https://newtab.com')`

8.  **Ожидание**:
    *   Метод `wait` приостанавливает выполнение на указанное время.
    *   Пример: `driver.wait(1)`

9.  **Сохранение куков**:
    *   Метод `_save_cookies_localy` сохраняет текущие куки в файл.
    *   Пример: `self._save_cookies_localy()`
    *   Использует `pickle` для сериализации и сохранения куков.

10. **Загрузка HTML контента**:
    *   Метод `fetch_html` загружает HTML контент с файла или веб-страницы.
    *   Пример: `driver.fetch_html('https://example.com')` или `driver.fetch_html('file://path/to/file.html')`
        *   Если URL начинается с `file://`, то читает данные из файла.
        *   Если URL начинается с `http://` или `https://`, вызывает `self.get_url(url)`.

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph Driver Class
        A[__init__] --> B{is webdriver_cls valid?}
        B -- Yes --> C[Initialize webdriver]
        B -- No --> D[Raise TypeError]
        C --> E[__init_subclass__]
        E --> F{browser_name?}
        F -- Yes --> G[Set browser_name]
        F -- No --> H[Raise ValueError]
        G --> I[__getattr__]
        I --> J[Proxy attribute access]
        J --> K[scroll]
        K --> L{direction}
        L -- 'forward/down' --> M[carousel('', scrolls, frame_size, delay)]
        L -- 'backward/up' --> N[carousel('-', scrolls, frame_size, delay)]
        L -- 'both' --> O[carousel('', scrolls, frame_size, delay) & carousel('-', scrolls, frame_size, delay)]
        O --> P[execute_script]
        P --> Q[wait]
        Q --> R[locale]
        R --> S{meta tag found?}
        S -- Yes --> T[Return meta tag content]
        S -- No --> U[get_page_lang()]
        U --> V{JS result?}
        V -- Yes --> W[Return JS result]
        V -- No --> X[Return None]
        X --> Y[get_url]
        Y --> Z[Save current URL]
        Z --> AA[Load URL]
        AA --> AB{Page loaded?}
        AB -- Yes --> AC[Save cookies]
        AB -- No --> AA
        AC --> AD[window_open]
        AD --> AE[Open new tab]
        AE --> AF[Switch to new tab]
         AF --> AG{URL?}
        AG -- Yes --> AA
        AG -- No --> AD
        AG --> AH[wait]
        AH --> AI[time.sleep(delay)]
        AI --> AJ[_save_cookies_localy]
        AJ --> AK[Open file]
        AK --> AL[pickle.dump(cookies)]
         AL --> AM[fetch_html]
        AM --> AN{URL start with file://}
         AN -- Yes --> AO[Read file]
         AO --> AP[Set html_content]
        AN -- No --> AQ{URL start with http:// or https://}
        AQ -- Yes --> AR[Get URL]
        AR --> AS[Set page_source]
        AQ -- No --> AT[Unsupported protocol]
        
    end
```

**Объяснение зависимостей `mermaid`:**

*   `Driver Class`: Обозначает основной класс `Driver` и все его методы.
*   `__init__`: Метод инициализации класса `Driver`, проверяет корректность `webdriver_cls`.
*   `__init_subclass__`: Метод инициализации подкласса, проверяет наличие `browser_name`.
*   `__getattr__`: Метод для проксирования доступа к атрибутам драйвера.
*    `scroll`: Метод для прокрутки страницы.
*    `carousel`: Вспомогательная функция для `scroll`.
*   `locale`: Свойство для определения языка страницы.
*   `get_url`: Метод для навигации по URL.
*   `window_open`: Метод для открытия нового окна браузера.
*   `wait`: Метод для приостановки выполнения кода.
*   `_save_cookies_localy`: Метод для сохранения куков в файл.
*   `fetch_html`: Метод для загрузки HTML-контента.
*   `execute_script`: Метод Selenium для выполнения JavaScript.
*   `time.sleep(delay)`: Функция задержки из модуля `time`.
*   `pickle.dump(cookies)`: Функция сохранения данных с помощью `pickle`.
*   Логические блоки: Представлены в виде ромбов.
*   Методы: Представлены в виде прямоугольников.

### 3. <объяснение>
**Импорты:**
*   `selenium.webdriver`: Базовый модуль для управления веб-драйверами.
*   `selenium.common.exceptions.WebDriverException`, `selenium.common.exceptions.InvalidArgumentException`: Исключения, которые могут возникнуть при работе с веб-драйвером.
*   `selenium.webdriver.common.by.By`: Используется для выбора элементов на странице по CSS-селекторам.
*   `time`: Модуль для работы со временем, используется для задержек.
*   `copy`: Модуль для копирования объектов, используется для сохранения предыдущего URL.
*   `pickle`: Модуль для сериализации и десериализации объектов, используется для сохранения куков.
*   `re`: Модуль для работы с регулярными выражениями.
*    `Path` из `pathlib`: Используется для работы с путями к файлам.
*   `Optional` из `typing`: Используется для указания типа, который может быть `None`.
*   `src.logger.logger`: Пользовательский модуль для логирования.
*    `src import gs`:  Импорт глобальных настроек.

**Класс `Driver`:**
*   **Роль:** Обеспечивает унифицированный интерфейс для работы с веб-драйверами Selenium.
*   **Атрибуты:**
    *   `driver`: Экземпляр веб-драйвера.
    *   `previous_url`: Предыдущий URL.
    *   `html_content`: HTML контент страницы.
    *   `browser_name`: Имя браузера.
*   **Методы:**
    *   `__init__(self, webdriver_cls, *args, **kwargs)`: Конструктор класса. Принимает класс веб-драйвера и параметры.
    *    `__init_subclass__(cls, *, browser_name=None, **kwargs)`: Метод для инициализации подклассов `Driver` .
    *   `__getattr__(self, item)`: Проксирует доступ к атрибутам объекта `driver`.
    *   `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3)`: Прокрутка страницы.
    *   `locale(self)`: Свойство для определения языка страницы.
    *   `get_url(self, url: str)`: Навигация по URL.
    *   `window_open(self, url: Optional[str] = None)`: Открытие нового окна.
    *   `wait(self, delay: float = .3)`: Ожидание.
    *   `_save_cookies_localy(self)`: Сохранение куков.
    *   `fetch_html(self, url: str)`: Загрузка HTML-контента.

**Функции:**
*   `carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool`: Вспомогательная функция для `scroll`, выполняет прокрутку.

**Переменные:**
*   `self.driver`: Экземпляр веб-драйвера.
*   `self.previous_url`: Предыдущий URL.
*   `self.html_content`: HTML контент страницы.
*   `webdriver_cls`: Класс веб-драйвера.
*    `browser_name`: Имя браузера.
*   `url`: URL для навигации или загрузки HTML.
*   `scrolls`: Количество прокруток.
*    `frame_size`: Размер прокрутки.
*    `direction`: Направление прокрутки.
*    `delay`: Задержка.

**Потенциальные ошибки и области для улучшения:**
*   Использование `copy.copy(self.current_url)` может вызвать исключение, если `self.current_url` не установлен.
*   Метод `_save_cookies_localy` помечен как `debug`, что может привести к ошибкам, если его не пересмотреть.
*   Обработка исключений в `fetch_html` при работе с локальными файлами может быть более точной.
*   В функции `get_url` ожидание загрузки страницы реализовано через `while self.ready_state != 'complete'`, что может быть ненадежным. Лучше использовать явные ожидания.
*   Отсутствует явная проверка на наличие элемента `meta[http-equiv='Content-Language']` перед обращением к его атрибуту.

**Взаимосвязи с другими частями проекта:**
*   Модуль `logger` используется для логирования ошибок.
*   Модуль `gs` (global settings) используется для получения пути к файлу куков.
*   Может быть интегрирован с другими модулями для веб-скрапинга или автоматизации тестирования.

Это подробное объяснение кода должно помочь понять его функциональность и место в проекте.