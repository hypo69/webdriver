# Модуль Crawlee Python для автоматизации и сбора данных

Этот модуль предоставляет кастомную реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать данные из них. Конфигурация управляется через файл `crawlee_python.json`.

## Оглавление

-   [Обзор](#обзор)
-   [Класс `Playwrid`](#класс-playwrid)
    -   [`__init__`](#__init__)
    -   [`_set_launch_options`](#_set_launch_options)
    -   [`start`](#start)
    -   [`current_url`](#current_url)
    -   [`get_page_content`](#get_page_content)
    -   [`get_element_content`](#get_element_content)
    -   [`get_element_value_by_xpath`](#get_element_value_by_xpath)
    -   [`click_element`](#click_element)
    -   [`execute_locator`](#execute_locator)
-  [Пример использования](#пример-использования)

## Обзор

Этот модуль предоставляет кастомную реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать данные из них. Конфигурация управляется через файл `crawlee_python.json`.

## Класс `Playwrid`

### Описание

Класс `Playwrid` является подклассом `PlaywrightCrawler` и предоставляет дополнительные возможности, такие как настройка параметров запуска браузера, пользовательского агента и упрощенная работа с локаторами.

**Атрибуты:**

-   `driver_name` (str): Имя драйвера, по умолчанию `'playwrid'`.
-   `base_path` (Path): Путь к каталогу модуля.
-   `config` (SimpleNamespace): Настройки, загруженные из файла `playwrid.json`.
-   `context` (Optional): Контекст сканирования Playwright.

### `__init__`

```python
    def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs) -> None:
        """
        Initializes the Playwright Crawler with the specified launch options, settings, and user agent.
        """
        launch_options = self._set_launch_options(user_agent, options)
        self.executor = PlaywrightExecutor()
        # Pass launch_options to PlaywrightCrawler if it accepts them
        # Otherwise, remove launch_options from the parameters
        super().__init__(
            browser_type=self.config.browser_type,
            # launch_options=launch_options,  # Remove or adjust if not accepted
            **kwargs
        )
        # If PlaywrightCrawler does not accept launch_options, set them separately
        if hasattr(self, 'set_launch_options'):
            self.set_launch_options(launch_options)
        else:
            # Handle launch options differently if needed
            pass
```

**Описание**: Инициализирует сканер `Playwrid` с заданными параметрами запуска, настройками и пользовательским агентом.

**Параметры**:

-   `user_agent` (Optional[str], optional): Строка user-agent, которая будет использоваться. По умолчанию `None`.
-   `options` (Optional[List[str]], optional): Список опций Playwright, передаваемых при инициализации. По умолчанию `None`.
-    `*args`: Произвольные позиционные аргументы, передаваемые родительскому классу.
-   `**kwargs`: Произвольные ключевые аргументы, передаваемые родительскому классу.

### `_set_launch_options`

```python
    def _set_launch_options(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Configures the launch options for the Playwright Crawler.

        :param settings: A SimpleNamespace object containing launch settings.
        :type settings: SimpleNamespace
        :param user_agent: The user-agent string to be used.
        :type user_agent: Optional[str]
        :param options: A list of Playwright options to be passed during initialization.
        :type options: Optional[List[str]]
        :returns: A dictionary with launch options for Playwright.
        :rtype: Dict[str, Any]
        """
        launch_options = {
            "headless": self.config.headless if hasattr(self.config, 'headless') else True,
            "args": self.config.options if hasattr(self.config, 'options') else []
        }

        # Add custom user-agent if provided
        if user_agent:
            launch_options['user_agent'] = user_agent

        # Merge custom options with default options
        if options:
            launch_options['args'].extend(options)

        return launch_options
```

**Описание**: Настраивает параметры запуска для Playwright Crawler.

**Параметры**:

-   `user_agent` (Optional[str]): Строка user-agent, которая будет использоваться.
-   `options` (Optional[List[str]]): Список опций Playwright, передаваемых во время инициализации.

**Возвращает**:

-   `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

### `start`

```python
    async def start(self, url: str) -> None:
        """
        Starts the Playwrid Crawler and navigates to the specified URL.

        :param url: The URL to navigate to.
        :type url: str
        """
        try:
            logger.info(f"Starting Playwright Crawler for {url}")
            await self.executor.start()  # Start the executor
            await self.executor.goto(url) # Goto url
            super().run(url) # run crawler
            # получаем контекст
            self.context = self.crawling_context
        except Exception as ex:
            logger.critical('Playwrid Crawler failed with an error:', ex)
```

**Описание**: Запускает сканер `Playwrid` и переходит по указанному URL.

**Параметры**:

-   `url` (str): URL для перехода.

### `current_url`

```python
    @property
    def current_url(self) -> Optional[str]:
        """
        Returns the current URL of the browser.

        :returns: The current URL.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            return self.context.page.url
        return None
```

**Описание**: Возвращает текущий URL браузера.

**Возвращает**:

-   `Optional[str]`: Текущий URL.

### `get_page_content`

```python
    def get_page_content(self) -> Optional[str]:
        """
        Returns the HTML content of the current page.

        :returns: HTML content of the page.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            return self.context.page.content()
        return None
```

**Описание**: Возвращает HTML-контент текущей страницы.

**Возвращает**:

-   `Optional[str]`: HTML-контент страницы.

### `get_element_content`

```python
    async def get_element_content(self, selector: str) -> Optional[str]:
        """
        Returns the inner HTML content of a single element on the page by CSS selector.

        :param selector: CSS selector for the element.
        :type selector: str
        :returns: Inner HTML content of the element, or None if not found.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(selector)
                return await element.inner_html()
            except Exception as ex:
                logger.warning(f"Element with selector '{selector}' not found or error during extraction: {ex}")
                return None
        return None
```

**Описание**: Возвращает внутренний HTML-контент одного элемента на странице по CSS-селектору.

**Параметры**:

-   `selector` (str): CSS-селектор элемента.

**Возвращает**:

-   `Optional[str]`: Внутренний HTML-контент элемента или `None`, если элемент не найден.

### `get_element_value_by_xpath`

```python
    async def get_element_value_by_xpath(self, xpath: str) -> Optional[str]:
        """
        Returns the text value of a single element on the page by XPath.

        :param xpath: XPath of the element.
        :type xpath: str
        :returns: The text value of the element, or None if not found.
        :rtype: Optional[str]
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(f'xpath={xpath}')
                return await element.text_content()
            except Exception as ex:
                logger.warning(f"Element with XPath '{xpath}' not found or error during extraction: {ex}")
                return None
        return None
```

**Описание**: Возвращает текстовое значение одного элемента на странице по XPath.

**Параметры**:

-   `xpath` (str): XPath элемента.

**Возвращает**:

-   `Optional[str]`: Текстовое значение элемента или `None`, если элемент не найден.

### `click_element`

```python
    async def click_element(self, selector: str) -> None:
        """
        Clicks a single element on the page by CSS selector.

        :param selector: CSS selector of the element to click.
        :type selector: str
        """
        if self.context and self.context.page:
            try:
                element = self.context.page.locator(selector)
                await element.click()
            except Exception as ex:
                logger.warning(f"Element with selector '{selector}' not found or error during click: {ex}")
```

**Описание**: Кликает по одному элементу на странице по CSS-селектору.

**Параметры**:

-   `selector` (str): CSS-селектор элемента для клика.

### `execute_locator`

```python
    async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
        """
        Executes locator through executor

        :param locator: Locator data (dict or SimpleNamespace).
        :type locator: dict | SimpleNamespace
        :param message: Optional message for events.
        :type message: Optional[str]
        :param typing_speed: Optional typing speed for events.
        :type typing_speed: float
        :returns: Execution status.
        :rtype: str | List[str] | bytes | List[bytes] | bool
        """
        return await self.executor.execute_locator(locator, message, typing_speed)
```

**Описание**: Выполняет локатор через исполнитель.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Данные локатора.
-   `message` (Optional[str]): Сообщение для событий.
-   `typing_speed` (float): Скорость печати для событий.

**Возвращает**:

-   `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

## Пример использования

```python
if __name__ == "__main__":
    async def main():
        browser = Playwrid(options=["--headless"])
        await browser.start("https://www.example.com")
        
        # Получение HTML всего документа
        html_content = browser.get_page_content()
        if html_content:
            print(html_content[:200])  # Выведем первые 200 символов для примера
        else:
            print("Не удалось получить HTML-контент.")
        
        # Получение HTML элемента по селектору
        element_content = await browser.get_element_content("h1")
        if element_content:
            print("
Содержимое элемента h1:")
            print(element_content)
        else:
            print("
Элемент h1 не найден.")
        
        # Получение значения элемента по xpath
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
             print(f"
Значение элемента по XPATH //head/title: {xpath_value}")
        else:
             print("
Элемент по XPATH //head/title не найден")

        # Нажатие на кнопку (при наличии)
        await browser.click_element("button")

        locator_name = {
        "attribute": "innerText",
        "by": "XPATH",
        "selector": "//h1",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "mandatory": True,
        "locator_description": "Название товара"
        }

        name = await browser.execute_locator(locator_name)
        print("Name:", name)

        locator_click = {
        "attribute": None,
        "by": "CSS",
        "selector": "button",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "mandatory": True,
        "locator_description": "название товара"
        }
        await browser.execute_locator(locator_click)
        await asyncio.sleep(3)
    asyncio.run(main())