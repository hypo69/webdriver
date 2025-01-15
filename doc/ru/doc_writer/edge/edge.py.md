# Документация модуля `src.webdriver.edge`

## Обзор

Модуль `edge.py` предоставляет пользовательский класс `Edge` для работы с WebDriver Microsoft Edge. Он обеспечивает упрощенную конфигурацию и интеграцию с Selenium, используя `fake_useragent` для генерации user-agent и поддерживает гибкую настройку параметров браузера.

## Оглавление

-   [Обзор](#обзор)
-   [Класс `Edge`](#класс-edge)
    -   [`__init__`](#__init__)
    -   [`_payload`](#_payload)
    -   [`set_options`](#set_options)
-   [Пример использования](#пример-использования)

## Класс `Edge`

### Описание

Класс `Edge` представляет собой пользовательский класс WebDriver для Microsoft Edge с расширенными возможностями.

**Атрибуты:**

-   `driver_name` (str): Имя используемого WebDriver, по умолчанию `'edge'`.

### `__init__`

```python
    def __init__(self,  profile_name: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
        """
        Initializes the Edge WebDriver with the specified user agent and options.

        :param user_agent: The user-agent string to be used. If `None`, a random user agent is generated.
        :type user_agent: Optional[str]
        :param options: A list of Edge options to be passed during initialization.
        :type options: Optional[List[str]]
        :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
        :type window_mode: Optional[str]
        """
        self.user_agent = user_agent or UserAgent().random
        settings = j_loads_ns(Path(gs.path.src, 'webdriver', 'edge', 'edge.json'))

        # Initialize Edge options
        options_obj = EdgeOptions()
        options_obj.add_argument(f'user-agent={self.user_agent}')
        
        #  Установка режима окна из конфига
        if hasattr(settings, 'window_mode') and settings.window_mode:
            window_mode = window_mode or settings.window_mode
        #  Установка режима окна из параметров
        if window_mode:
            if window_mode == 'kiosk':
                options_obj.add_argument("--kiosk")
            elif window_mode == 'windowless':
               options_obj.add_argument("--headless")
            elif window_mode == 'full_window':
                 options_obj.add_argument("--start-maximized")


        # Add custom options passed during initialization
        if options:
            for option in options:
                options_obj.add_argument(option)

        # Add arguments from the configuration's options
        if hasattr(settings, 'options') and settings.options:
            for option in settings.options:
                options_obj.add_argument(option)

        # Add arguments from the configuration's headers
        if hasattr(settings, 'headers') and settings.headers:
            for key, value in vars(settings.headers).items():
                options_obj.add_argument(f'--{key}={value}')
        
         # Настройка директории профиля
        profile_directory = settings.profiles.os if settings.profiles.default == 'os' else str(Path(gs.path.src, settings.profiles.internal))

        if profile_name:
             profile_directory = str(Path(profile_directory).parent / profile_name)
        if '%LOCALAPPDATA%' in profile_directory:
              profile_directory = Path(profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA')))
        options_obj.add_argument(f"--user-data-dir={profile_directory}")
        try:
            logger.info('Starting Edge WebDriver')
            edgedriver_path = settings.executable_path.default  # Ensure this is correctly defined in your JSON file
            service = EdgeService(executable_path=str(edgedriver_path))
            super().__init__(options=options_obj, service=service)
            self._payload()
        except WebDriverException as ex:
            logger.critical('Edge WebDriver failed to start:', ex)
            return
        except Exception as ex:
            logger.critical('Edge WebDriver crashed. General error:', ex)
            return
```

**Описание**: Инициализирует Edge WebDriver с заданными user-agent и опциями. Загружает настройки из `edge.json`.

**Параметры**:

-   `profile_name` (Optional[str]): Имя пользовательского профиля Edge.
-   `user_agent` (Optional[str]): Строка user-agent, которая будет использоваться. Если не указано, то будет сгенерирован случайный user-agent.
-   `options` (Optional[List[str]]): Список опций Edge для передачи во время инициализации.
-    `window_mode` (Optional[str]): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)

### `_payload`

```python
    def _payload(self) -> None:
        """
        Load executors for locators and JavaScript scenarios.
        """
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = self.send_key_to_webelement = execute_locator.send_message
```

**Описание**: Загружает исполнителей для локаторов и JavaScript-сценариев.

### `set_options`

```python
    def set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions:  
        """  
        Create and configure launch options for the Edge WebDriver.  

        :param opts: A list of options to add to the Edge WebDriver. Defaults to `None`.  
        :return: Configured `EdgeOptions` object.  
        """  
        options = EdgeOptions()  
        if opts:  
            for opt in opts:  
                options.add_argument(opt)  
        return options
```

**Описание**: Создает и настраивает параметры запуска для Edge WebDriver.

**Параметры**:

- `opts` (Optional[List[str]], optional): Список опций для добавления в Edge WebDriver. По умолчанию `None`.

**Возвращает**:
- `EdgeOptions`: Настроенный объект `EdgeOptions`.

## Пример использования

```python
if __name__ == "__main__":
    driver = Edge(window_mode='full_window')
    driver.get("https://www.example.com")
```