# Документация модуля `src.webdriver.executor`

## Обзор

Модуль `executor.py` предназначен для выполнения действий с веб-элементами на основе предоставленных конфигураций, известных как "локаторы". Эти конфигурации (или "локаторы") представляют собой словари, содержащие информацию о том, как находить и взаимодействовать с элементами на веб-странице. Модуль обеспечивает следующие функциональные возможности:

1.  **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что обеспечивает гибкое управление данными локаторов.
2.  **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных, модуль может выполнять различные действия, такие как клики, отправка сообщений, выполнение событий и извлечение атрибутов из веб-элементов.
3.  **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы, которые могут иметь нестабильные элементы или требовать особого подхода.
4.  **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, что позволяет идентифицировать и взаимодействовать с одним или несколькими веб-элементами одновременно.

Этот модуль обеспечивает гибкость и универсальность при работе с веб-элементами, позволяя автоматизировать сложные сценарии веб-взаимодействия.

## Оглавление

- [Обзор](#обзор)
- [Класс `ExecuteLocator`](#класс-executelocator)
    - [`__post_init__`](#__post_init__)
    - [`execute_locator`](#execute_locator)
    - [`evaluate_locator`](#evaluate_locator)
    - [`get_attribute_by_locator`](#get_attribute_by_locator)
    - [`get_webelement_by_locator`](#get_webelement_by_locator)
    - [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
    - [`execute_event`](#execute_event)
    - [`send_message`](#send_message)
- [Зависимости](#зависимости)

## Класс `ExecuteLocator`

```python
@dataclass
class ExecuteLocator:
    """Locator handler for web elements using Selenium."""
    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "CLASS_NAME": By.CLASS_NAME,
    })
    mode: str = 'debug'

    def __post_init__(self):
        if self.driver:
            self.actions = ActionChains(self.driver)
```

**Описание**: Класс `ExecuteLocator` является обработчиком локаторов для веб-элементов с использованием Selenium.

**Атрибуты**:

-   `driver` (Optional[object]): Экземпляр Selenium WebDriver.
-   `actions` (ActionChains): Объект `ActionChains` для выполнения сложных действий.
-   `by_mapping` (dict): Словарь, сопоставляющий строковые представления локаторов с константами `By` из Selenium.
-   `mode` (str): Режим работы (по умолчанию `debug`).

### `__post_init__`

```python
    def __post_init__(self):
        if self.driver:
            self.actions = ActionChains(self.driver)
```

**Описание**: Инициализирует объект `ActionChains`, если предоставлен драйвер.

### `execute_locator`

```python
    async def execute_locator( 
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: Optional[float] = 0,
        continue_on_error: Optional[bool] = True,
    ) -> str | list | dict | WebElement | bool:
        """Executes actions on a web element based on the provided locator.

        Args:
            locator: Locator data (dict, SimpleNamespace, or Locator).
            timeout: Timeout for locating the element.
            timeout_for_event: The wait condition ('presence_of_element_located', 'element_to_be_clickable').
            message: Optional message to send.
            typing_speed: Typing speed for send_keys events.
            continue_on_error: Whether to continue on error.

        Returns:
            str | list | dict | WebElement | bool: Outcome based on locator instructions.

        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B --> C{Is locator SimpleNamespace?}
            C -->|Yes| D[Use locator as is]
            C -->|No| E[Convert dict to SimpleNamespace]
            E --> D
            D --> F[Define async function _parse_locator]
            F --> G[Check if locator has event, attribute, or mandatory]
            G -->|No| H[Return None]
            G -->|Yes| I[Try to map by and evaluate attribute]
            I --> J[Catch exceptions and log if needed]
            J --> K{Does locator have event?}
            K -->|Yes| L[Execute event]
            K -->|No| M{Does locator have attribute?}
            M -->|Yes| N[Get attribute by locator]
            M -->|No| O[Get web element by locator]
            L --> P[Return result of event]
            N --> P[Return attribute result]
            O --> P[Return web element result]
            P --> Q[Return final result of _parse_locator]
            Q --> R[Return result of execute_locator]
            R --> S[End]

    ```
        """
```

**Описание**: Выполняет действия с веб-элементом на основе предоставленного локатора.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Данные локатора.
-   `timeout` (Optional[float]): Таймаут для поиска элемента.
-   `timeout_for_event` (Optional[str]): Условие ожидания.
-   `message` (Optional[str]): Сообщение для отправки (если применимо).
-   `typing_speed` (Optional[float]): Скорость печати (если применимо).
-  `continue_on_error` (Optional[bool]): Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.

**Возвращает**:

-   `str | list | dict | WebElement | bool`: Результат выполнения действий с элементом.

### `evaluate_locator`

```python
    async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """Evaluates and processes locator attributes.

        Args:
            attribute (Union[str, List[str], dict]): Attributes to evaluate.

        Returns:
            Union[str, List[str], dict]: Evaluated attributes.

        ```mermaid
                graph TD
            A[Start] --> B[Check if attribute is list]
            B -->|Yes| C[Iterate over each attribute in list]
            C --> D[Call _evaluate for each attribute]
            D --> E[Return gathered results from asyncio.gather]
            B -->|No| F[Call _evaluate for single attribute]
            F --> G[Return result of _evaluate]
            G --> H[End]
            E --> H
            ```
        """
```

**Описание**: Оценивает и обрабатывает атрибуты локатора.

**Параметры**:

-   `attribute` (str | List[str] | dict): Атрибуты для оценки.

**Возвращает**:

-   `Optional[str | List[str] | dict]`: Оцененные атрибуты.

### `get_attribute_by_locator`

```python
    async def get_attribute_by_locator(                                     
        self,
        locator: SimpleNamespace | dict,
        timeout: Optional[float] = 0,
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
    ) ->  WebElement | list[WebElement] | None:
        """ Retrieves attributes from an element or list of elements found by the given locator.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.

        Returns:
            Union[str, list, dict, WebElement | list[WebElement] | None]: The attribute value(s) or dictionary with attributes.

        ```mermaid
                graph TD
            A[Start] --> B[Check if locator is SimpleNamespace or dict]
            B -->|Yes| C[Convert locator to SimpleNamespace if needed]
            C --> D[Call get_webelement_by_locator]
            D --> E[Check if web_element is found]
            E -->|No| F[Log debug message and return]
            E -->|Yes| G[Check if locator.attribute is a dictionary-like string]
            G -->|Yes| H[Parse locator.attribute string to dict]
            H --> I[Check if web_element is a list]
            I -->|Yes| J[Retrieve attributes for each element in list]
            J --> K[Return list of attributes]
            I -->|No| L[Retrieve attributes for a single web_element]
            L --> K
            G -->|No| M[Check if web_element is a list]
            M -->|Yes| N[Retrieve attributes for each element in list]
            N --> O[Return list of attributes or single attribute]
            M -->|No| P[Retrieve attribute for a single web_element]
            P --> O
            O --> Q[End]
            F --> Q
            ```
        """
```

**Описание**: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

**Параметры**:

-   `locator` (SimpleNamespace | dict): Локатор.
-   `timeout` (Optional[float]): Максимальное время ожидания.
-   `timeout_for_event` (str): Тип условия ожидания.
-   `message` (Optional[str]): Сообщение.
-   `typing_speed` (float): Скорость печати.
-   `continue_on_error` (bool): Флаг продолжения при ошибке.

**Возвращает**:

-   `WebElement | list[WebElement] | None`: Значение атрибута(ов) или словарь с атрибутами.

### `get_webelement_by_locator`

```python
    async def get_webelement_by_locator(
        self,
        locator: dict | SimpleNamespace,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located'
    ) -> WebElement | List[WebElement] | None:
        """
        Функция извлекает веб-элемент или список элементов по указанному локатору.
        .. :todo:
            Продумать как передать `timeout_for_event`
        """
```

**Описание**: Извлекает веб-элемент или список элементов по указанному локатору.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Локатор.
-   `timeout` (Optional[float]): Таймаут для поиска элемента.
-   `timeout_for_event` (Optional[str]): Условие ожидания.

**Возвращает**:

-   `WebElement | List[WebElement] | None`: Найденный элемент или список элементов.

### `get_webelement_as_screenshot`

```python
    async def get_webelement_as_screenshot(
        self,                                     
        locator: SimpleNamespace | dict,
        timeout: float = 5, 
        timeout_for_event: str = 'presence_of_element_located',
        message: Optional[str] = None,
        typing_speed: float = 0,
        continue_on_error: bool = True,
        webelement: Optional[WebElement] = None
    ) -> BinaryIO | None:
        """ Takes a screenshot of the located web element.

        Args:
            locator (dict | SimpleNamespace): Locator as a dictionary or SimpleNamespace.
            timeout (float, optional): Max wait time for the element to appear. Defaults to 5 seconds.
            timeout_for_event (str, optional): Type of wait condition. Defaults to 'presence_of_element_located'.
            message (Optional[str], optional): Message to send to the element. Defaults to None.
            typing_speed (float, optional): Speed of typing for send message events. Defaults to 0.
            continue_on_error (bool, optional): Whether to continue in case of an error. Defaults to True.
            webelement (Optional[WebElement], optional): Pre-fetched web element. Defaults to None.

        Returns:
            BinaryIO | None: Binary stream of the screenshot or None if failed.
        """
```

**Описание**: Делает снимок экрана найденного веб-элемента.

**Параметры**:

-   `locator` (SimpleNamespace | dict): Локатор.
-   `timeout` (float): Максимальное время ожидания.
-   `timeout_for_event` (str): Тип условия ожидания.
-   `message` (Optional[str]): Сообщение для отправки.
-   `typing_speed` (float): Скорость печати.
-   `continue_on_error` (bool): Флаг продолжения при ошибке.
-   `webelement` (Optional[WebElement]): Предварительно полученный веб-элемент.

**Возвращает**:

-   `BinaryIO | None`: Бинарный поток снимка экрана или `None` в случае неудачи.

### `execute_event`

```python
    async def execute_event(self,              
                             locator: SimpleNamespace | dict,
                             timeout: float = 5, 
                             timeout_for_event: str = 'presence_of_element_located',
                             message: str = None,
                             typing_speed: float = 0,
                             continue_on_error: bool = True,
    ) -> str | list[str] | bytes | list[bytes] | bool:
        """
        Execute the events associated with a locator.

        Args:
            locator (SimpleNamespace | dict): Locator specifying the element and event to execute.
            timeout: Timeout for locating the element.
            timeout_for_event: Timeout for waiting for the event.
            message (Optional[str], optional): Message to send with the event, if applicable. Defaults to None.
            typing_speed (int, optional): Speed of typing for send_keys events. Defaults to 0.

        Returns:
            bool: Returns True if event execution was successful, False otherwise.
        """
```

**Описание**: Выполняет события, связанные с локатором.

**Параметры**:

-   `locator` (SimpleNamespace | dict): Локатор.
-   `timeout` (float): Таймаут для поиска элемента.
-   `timeout_for_event` (str): Таймаут для ожидания события.
-   `message` (Optional[str]): Сообщение для отправки.
-   `typing_speed` (float): Скорость печати.
-   `continue_on_error` (bool): Флаг продолжения при ошибке.

**Возвращает**:

-   `str | list[str] | bytes | list[bytes] | bool`: Результат выполнения события.

### `send_message`

```python
    async def send_message(self,               
                        locator: SimpleNamespace | dict,
                        timeout:float = 5 , 
                        timeout_for_event: str = 'presence_of_element_located',
                        message: str = None,
                        typing_speed: float = 0,
                        continue_on_error: bool = True,

    ) -> bool:
        """Sends a message to a web element.

        Args:
            self (Driver): The instance of the Driver class.
            locator (dict | SimpleNamespace): Information about the element's location on the page.
                                              It can be a dictionary or a SimpleNamespace object.
            message (Optional[str], optional): The message to be sent to the web element. Defaults to `None`.
            replace_dict (dict, optional): A dictionary for replacing certain characters in the message. Defaults to {";": "SHIFT+ENTER"}.
            typing_speed (float, optional): Speed of typing the message in seconds. Defaults to 0.

        Returns:
            bool: Returns `True` if the message was sent successfully, `False` otherwise.

        Example:
            >>> driver = Driver()
            >>> driver.send_message(locator={"id": "messageBox"}, message="Hello World", typing_speed=0.1)
            True
       

        """
```

**Описание**: Отправляет сообщение веб-элементу.

**Параметры**:

-   `locator` (SimpleNamespace | dict): Локатор.
-   `timeout` (float): Таймаут для поиска элемента.
-   `timeout_for_event` (str): Таймаут для ожидания события.
-    `message` (Optional[str]): Сообщение для отправки.
-   `typing_speed` (float): Скорость печати.
-   `continue_on_error` (bool): Флаг продолжения при ошибке.

**Возвращает**:

-   `bool`: `True`, если сообщение отправлено успешно, `False` в противном случае.

## Зависимости

-   `asyncio`: Для асинхронных операций.
-   `re`: Для работы с регулярными выражениями.
-   `dataclasses`: Для создания классов данных.
-   `enum`: Для создания перечислений.
-   `pathlib`: Для обработки путей к файлам.
-   `types`: Для создания простых пространств имен.
-   `typing`: Для аннотаций типов.
-   `selenium`: Для автоматизации веб-страниц.
-   `header`: Пользовательский модуль.
-   `src.gs`: Пользовательский модуль настроек.
-   `src.logger.logger`: Пользовательский модуль логирования.
-   `src.logger.exceptions`: Пользовательский модуль исключений.
-   `src.utils.jjson`: Пользовательский модуль для работы с JSON.
-   `src.utils.printer`: Пользовательский модуль для печати.
-   `src.utils.image`: Пользовательский модуль для работы с изображениями.