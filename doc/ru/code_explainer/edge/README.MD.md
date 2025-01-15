## Анализ модуля Edge WebDriver для Selenium

### 1. <алгоритм>

**Описание рабочего процесса:**

Этот документ описывает модуль, предоставляющий кастомную реализацию Edge WebDriver с использованием Selenium. Он предназначен для интеграции настроек из файла `edge.json`, таких как пользовательский агент и профиль браузера, для автоматизации взаимодействия с браузером Edge.

**Блок-схема:**

1.  **Инициализация `Edge`**:
    *   Создается экземпляр класса `Edge` с параметрами (профиль, user-agent, опции, режим окна).
    *   **Пример**: `driver = Edge(profile_name='myprofile', user_agent='myagent', options=["--disable-gpu"], window_mode='kiosk')` или `driver = Edge()`
    *   Загружает настройки из `edge.json`, используя `j_loads_ns`.
    *   Устанавливает пользовательский агент, если он задан, или генерирует случайный.
    *   Создает объект `EdgeOptions`.
    *  Устанавливает режим окна (kiosk, windowless, full_window).
    *   Добавляет пользовательские опции, переданные при инициализации.
    *   Добавляет опции из файла конфигурации.
    *   Добавляет заголовки из файла конфигурации.
    *    Определяет путь к профилю пользователя.
    *   Создается экземпляр `EdgeService`.
    *  Инициализирует `WebDriver` с заданными опциями и сервисом.
    *   Вызывает `_payload()` для инициализации инструментов для работы с локаторами и JavaScript.
    *   Ловит исключения `WebDriverException` и общие исключения.

2.  **Инициализация инструментов (`_payload`)**:
    *   Метод `_payload` создает экземпляры `JavaScript` и `ExecuteLocator` и связывает их с текущим экземпляром `Edge`.
    *   **Пример**: `self._payload()`
    *   Создает экземпляр `JavaScript` и связывает его методы с методами экземпляра `Edge`.
    *  Создает экземпляр `ExecuteLocator` и связывает его методы с методами экземпляра `Edge`.

3.  **Создание опций (`set_options`)**:
    *   Метод `set_options` принимает список опций.
    *   **Пример**: `options = self.set_options(opts=["--disable-gpu"])`
    *   Создает объект `EdgeOptions`.
    *   Добавляет переданные опции в объект `EdgeOptions`.
    *   Возвращает объект `EdgeOptions`.

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Start] --> InitEdge[Initialize Edge Driver: <br><code>Edge(...)</code>]
    InitEdge --> LoadSettings[Load settings from <code>edge.json</code>]
    LoadSettings --> SetUserAgent[Set user agent]
    SetUserAgent --> InitOptions[Initialize Edge Options]
    InitOptions --> SetWindowModeFromConfig{Is window_mode in config?}
     SetWindowModeFromConfig -- Yes --> SetWindowModeFromConfig1[Set window mode from config]
        SetWindowModeFromConfig1 --> SetWindowModeArgs{Is window_mode in init args?}
        SetWindowModeArgs -- Yes --> SetWindowModeFromArgs[Set window mode from args]
        SetWindowModeArgs -- No --> CheckForModeSet[Check for window mode, if not set pass]
    CheckWindowMode -- No --> SetWindowModeArgs
       CheckForModeSet --> AddOptionsFromFile[Add options from config file]
      AddOptionsFromFile --> AddCustomOptions[Add custom options from init args]
    AddCustomOptions --> AddHeaders[Add headers from config file]
     AddHeaders --> SetUserProfile[Set user profile directory]
    SetUserProfile --> CreateWebDriverInstance[Create WebDriver instance]
    CreateWebDriverInstance --> Payload[Call Payload Method: <br><code>_payload()</code>]
     Payload --> InitJavaScript[Initialize JavaScript helper]
    InitJavaScript --> SetJavaScriptMethods[Set JavaScript methods in the instance]
    SetJavaScriptMethods --> InitExecuteLocator[Initialize ExecuteLocator]
    InitExecuteLocator --> SetExecutorMethods[Set ExecuteLocator methods in the instance]
    SetExecutorMethods --> ReturnDriverInstance[Return Edge Driver Instance]
    ReturnDriverInstance --> End[End]
```

```mermaid
flowchart TD
    Start --> Header[<code>header.py</code><br> Determine Project Root]
    Header --> import[Import Global Settings: <br><code>from src import gs</code>]
```

**Объяснение зависимостей `mermaid`:**

*   **`os`**: Используется для доступа к переменным окружения.
*   **`pathlib`**: Используется для работы с путями к файлам.
*   **`selenium.webdriver`**: Используется для управления веб-драйвером Edge.
*    **`selenium.webdriver.edge.options`**: Используется для настройки опций Edge.
*   **`selenium.webdriver.edge.service`**: Используется для управления сервисом EdgeDriver.
*   **`selenium.common.exceptions`**: Используется для обработки исключений, связанных с Selenium.
*   **`src`**: Используется для импорта глобальных настроек `gs`.
*  **`src.webdriver.executor`**: Используется для управления взаимодействиями с элементами.
*   **`src.webdriver.js`**: Используется для выполнения JavaScript на странице.
*    **`fake_useragent`**: Используется для генерации случайных user-agent.
*   **`src.utils.jjson`**: Используется для загрузки JSON-конфигураций.
*    **`src.logger.logger`**: Используется для логирования.

### 3. <объяснение>

**Импорты:**

*   `os`: Используется для работы с операционной системой (например, для доступа к переменным окружения).
*   `pathlib.Path`: Используется для работы с путями к файлам и директориям.
*    `typing.Optional`, `typing.List`: Используются для аннотации типов.
*   `selenium.webdriver.Edge`: Используется как базовый класс для создания кастомного драйвера.
*  `selenium.webdriver.edge.service.Service`: Используется для управления процессом EdgeDriver.
*   `selenium.webdriver.edge.options.Options`: Используется для настройки опций Edge.
*   `selenium.common.exceptions.WebDriverException`: Используется для обработки исключений, связанных с WebDriver.
*   `src`: Используется для импорта глобальных настроек `gs`.
*   `src.webdriver.executor.ExecuteLocator`: Используется для управления взаимодействиями с элементами.
*   `src.webdriver.js.JavaScript`: Используется для выполнения JavaScript-кода на странице.
*  `fake_useragent.UserAgent`: Используется для генерации случайных User-Agent.
*   `src.logger.logger`: Используется для логирования.
*  `src.utils.jjson.j_loads_ns`: Используется для загрузки JSON-конфигурации.

**Классы:**

*   `Edge(WebDriver)`:
    *   **Роль**: Расширяет функциональность `selenium.webdriver.Edge`, добавляя загрузку настроек из JSON, установку пользовательского агента и т.д.
    *   **Атрибуты**:
        *   `driver_name`: (`str`) - Имя драйвера (всегда "edge").
    *   **Методы**:
        *   `__init__(...)`: Инициализирует драйвер, загружает настройки, устанавливает user-agent, профиль и опции.
        *  `_payload(self) -> None`: Загружает инструменты для работы с локаторами и JavaScript.
        *    `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`: Настраивает опции Edge.

**Функции:**

*   `__init__(...)`:
    *   **Аргументы**:
        * `profile_name`: (`Optional[str]`) - Имя профиля пользователя.
        *    `user_agent`: (`Optional[str]`) - User-Agent.
        *   `options`: (`Optional[List[str]]`) - Список опций для Edge.
        *    `window_mode`: (`Optional[str]`) - Режим окна браузера.
        *   `*args`, `**kwargs`: Дополнительные параметры для WebDriver.
    *   **Назначение**: Инициализирует Edge WebDriver, загружая настройки из `edge.json`, устанавливая user-agent, опции, профиль и режим окна.
    *   **Возвращает**: `None`.
*   `_payload(self) -> None`:
    *    **Аргументы**:
          *  `self` (`Edge`): Экземпляр класса `Edge`.
    *   **Назначение**: Инициализирует инструменты для работы с локаторами и JavaScript.
    *    **Возвращает**: `None`.
*   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`:
    *   **Аргументы**:
        *    `opts`: (`Optional[List[str]]`) - Список опций.
    *   **Назначение**: Создает объект `EdgeOptions` и добавляет в него опции.
    *   **Возвращает**: `EdgeOptions` - объект с настроенными опциями.

**Переменные:**

*  `self.driver_name`: (`str`) - Имя драйвера.
*   `self.user_agent`: (`str`) - User-Agent.
*   `settings`: (`SimpleNamespace`) - Настройки из `edge.json`.
*   `options_obj`: (`EdgeOptions`) - Объект для настройки опций Edge.
*   `profile_directory`: (`str`) - Путь к профилю пользователя.
*   `j`: Экземпляр класса `JavaScript`.
*  `execute_locator`: Экземпляр класса `ExecuteLocator`.
*   `edgedriver_path`:  (`str`) - Путь к edgedriver.
*    `service`: (`EdgeService`) - Сервис для управления драйвером.
*   `opts`: (`Optional[List[str]]`) - Список опций для `set_options`.

**Потенциальные ошибки и области для улучшения:**

*   Обработка исключений может быть более специфичной.
*   Можно добавить логику выбора прокси, если она будет использоваться.
*   Можно добавить валидацию конфигурационных данных.
*    Можно упростить логику установки режима окна.
*    В методе `_payload` можно добавить проверки на наличие объектов `JavaScript` и `ExecuteLocator`.
* Можно улучшить логику установки профиля.

**Взаимосвязи с другими частями проекта:**

*   Использует `header` для определения корня проекта.
*   Использует глобальные настройки `gs` из пакета `src`.
*   Использует `src.webdriver.executor` для выполнения действий по локаторам.
*   Использует `src.webdriver.js` для выполнения JavaScript.
*   Использует `fake_useragent` для генерации User-Agent.
*   Использует `src.utils.jjson` для загрузки JSON-конфигураций.
*   Использует `src.logger.logger` для логирования.
*    Является частью веб-драйверного фреймворка и предоставляет конкретную реализацию для Edge.

Этот анализ предоставляет полное представление о работе модуля `edge.py`, его структуре, зависимостях и возможностях.