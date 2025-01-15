# Обзор модуля: Исполнитель через WebDriver

## Описание

Модуль предоставляет основу для выполнения навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий с веб-элементами.

## Оглавление

- [Обзор](#обзор)
- [Основные возможности](#основные-возможности)
- [Функциональность](#функциональность)
    - [Обработка локаторов](#обработка-локаторов)
    - [Скриншоты](#скриншоты)
    - [Действие клика](#действие-клика)
    - [Оценка локатора](#оценка-локатора)
- [Обработка ошибок](#обработка-ошибок)
- [Использование](#использование)
- [Зависимости](#зависимости)
- [Примеры использования классов и методов](#примеры-использования-классов-и-методов)
    - [Примеры](#примеры)
- [Примечания](#примечания)
- [WebDriver Executor](#webdriver-executor)
    - [Обзор](#обзор-1)
    - [Основные возможности](#основные-возможности-1)
    - [Общая структура и назначение](#общая-структура-и-назначение)
        - [Основное назначение](#основное-назначение)
        - [Основные компоненты](#основные-компоненты)
        - [Импорты и зависимости](#импорты-и-зависимости)
        - [Класс `ExecuteLocator`](#класс-executelocator-1)
            - [Атрибуты класса](#атрибуты-класса)
            - [Методы класса](#методы-класса)
        - [Примеры локаторов](#примеры-локаторов-1)
        - [Примеры KEY](#примеры-key)
    - [WebDriver Executor](#webdriver-executor-1)
        - [Обзор](#обзор-2)
        - [Основные возможности](#основные-возможности-2)
        - [Использование](#использование-1)
        - [Зависимости](#зависимости-1)
        - [Примеры использования](#примеры-использования)

## Основные возможности

-   Выполняет алгоритмы навигации, указанные в файлах скриптов.
-   Выполняет алгоритмы взаимодействия со страницей, указанные в файлах локаторов.

## Функциональность

### Обработка локаторов

-   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
-   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локатора, который содержит информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
-   **Получение элемента:** Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
-   **Получение атрибута:** Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с использованием локатора. Он поддерживает как одиночные, так и множественные элементы.
-   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод веб-элементам. Он поддерживает имитацию печати с настраиваемой скоростью печати и дополнительным взаимодействием с мышью.

### Скриншоты

-   **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде PNG-изображения. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

### Действие клика

-   **Клик по элементу:** Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удается.

### Оценка локатора

-   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

## Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или время ожидания истекло.

## Использование

-   **Инициализация:** Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.
-   **Выполнение локатора:** Вызовите метод `execute_locator` со словарем локатора для выполнения действий или получения данных из веб-элементов.
-   **Обработка результатов:** Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

## Зависимости

-   Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Примеры использования классов и методов

### Примеры

-   **Создание экземпляра Chrome драйвера и навигация по URL:**

    ```python
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")
    ```
-   **Извлечение домена из URL:**

    ```python
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")
    ```
-   **Сохранение cookies в локальный файл:**

    ```python
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")
    ```
-   **Обновление текущей страницы:**

    ```python
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")
    ```
-   **Прокрутка страницы вниз:**

    ```python
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")
    ```
-   **Получение языка текущей страницы:**

    ```python
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")
    ```
-   **Установка кастомного User-Agent для Chrome драйвера:**

    ```python
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")
    ```
-   **Поиск элемента по CSS селектору:**

    ```python
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    ```
-   **Получение текущего URL:**

    ```python
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")
    ```
-   **Фокусировка окна, чтобы убрать фокус с элемента:**

    ```python
    chrome_driver.window_focus()
    print("Focused the window")
    ```

## Примечания

-   Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
-   Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

## WebDriver Executor

### Обзор

Модуль WebDriver Executor предоставляет основу для выполнения навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий с веб-элементами.

### Основные возможности

-   **Обработка локаторов**
    -   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локатора, который содержит информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Получение элемента:** Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    -   **Получение атрибута:** Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с использованием локатора. Он поддерживает как одиночные, так и множественные элементы.
    -   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод веб-элементам. Он поддерживает имитацию печати с настраиваемой скоростью печати и дополнительным взаимодействием с мышью.
-   **Скриншоты**
    -   **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде PNG-изображения. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
-   **Действие клика**
    -   **Клик по элементу:** Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удается.
-   **Оценка локатора**
    -   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

### Общая структура и назначение

#### Основное назначение

Класс `ExecuteLocator` предназначен для выполнения навигационных алгоритмов и взаимодействия с веб-страницами на основе данных конфигурации, предоставленных в виде словарей локаторов.

#### Основные компоненты

1.  **Импорты и зависимости**

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import NoSuchElementException, TimeoutException

    from src import gs 
    from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
    
    from src.logger.logger import logger
    from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
    ```

    Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами и внутренние модули для настроек, логирования и обработки исключений.

2.  **Класс `ExecuteLocator`**

    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов. Рассмотрим его методы и атрибуты более подробно.

#### Атрибуты класса

-   **`driver`**: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
-   **`actions`**: Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
-   **`by_mapping`**: Словарь, который сопоставляет строковые представления локаторов с объектами `By` Selenium.

#### Методы класса

1.  **`__init__(self, driver, *args, **kwargs)`**

    Конструктор класса инициализирует WebDriver и `ActionChains`:

    ```python
    def __init__(self, driver, *args, **kwargs):
        self.driver = driver
        self.actions = ActionChains(driver)
    ```

2.  **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

    Основной метод для выполнения действий на основе локатора:

    ```python
    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        ...
    ```

    -   **`locator`**: Словарь с параметрами для выполнения действий.
    -   **`message`**: Сообщение для отправки, если необходимо.
    -   **`typing_speed`**: Скорость печати для отправки сообщений.
    -   **`continue_on_error`**: Флаг, указывающий, следует ли продолжать выполнение, если произошла ошибка.

    Этот метод выбирает, какие действия выполнять на основе конфигурации локатора.

3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

    Извлекает элементы, найденные на странице на основе локатора:

    ```python
    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
        ...
    ```

4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

    Извлекает атрибут из элемента на основе локатора:

    ```python
    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
        ...
    ```

5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

    Вспомогательный метод для получения атрибута из веб-элемента:

    ```python
    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
        ...
    ```

6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

    Отправляет сообщение веб-элементу:

    ```python
    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        ...
    ```

7.  **`evaluate_locator(self, attribute: str | list | dict) -> str`**

    Оценивает атрибут локатора:

    ```python
    def evaluate_locator(self, attribute: str | list | dict) -> str:
        ...
    ```

8.  **`_evaluate(self, attribute: str) -> str | None`**

    Вспомогательный метод для оценки одиночного атрибута:

    ```python
    def _evaluate(self, attribute: str) -> str | None:
        ...
    ```

9.  **`get_locator_keys() -> list`**

    Возвращает список доступных ключей локатора:

    ```python
    @staticmethod
    def get_locator_keys() -> list:
        ...
    ```

#### Примеры локаторов

Файл также включает примеры различных локаторов, которые можно использовать для тестирования:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },
  ...
}
```

#### Примеры KEY

```
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },

  "pagination": {
    "ul": {
      "attribute": null,
      "by": "xpath",
      "selector": "//ul[@class='pagination']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
    },
    "->": {
      "attribute": null,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
      "if_list":"first","use_mouse": false
    }
  }

}
"description": {
  "attribute": [
    null,
    null
  ],
  "by": [
    "xpath",
    "xpath"
  ],
  "selector": [
    "//a[contains(@href, '#tab-description')]",
    "//div[@id = 'tab-description']//p"
  ],
  "timeout":0,"timeout_for_event":"presence_of_element_located","event": [
    "click()",
    null
  ],
  "if_list":"first","use_mouse": [
    false,
    false
  ],
  "mandatory": [
    true,
    true
  ],
  "locator_description": [
    "Clicking on the tab to open the description field",
    "Reading data from div"
  ]
}
```

1.  `KEY.NULL`: Представляет нулевой ключ.
2.  `KEY.CANCEL`: Представляет ключ отмены.
3.  `KEY.HELP`: Представляет ключ помощи.
4.  `KEY.BACKSPACE`: Представляет ключ backspace.
5.  `KEY.TAB`: Представляет ключ tab.
6.  `KEY.CLEAR`: Представляет ключ clear.
7.  `KEY.RETURN`: Представляет ключ return.
8.  `KEY.ENTER`: Представляет ключ enter.
9.  `KEY.SHIFT`: Представляет ключ shift.
10. `KEY.CONTROL`: Представляет ключ control.
11. `KEY.ALT`: Представляет ключ alt.
12. `KEY.PAUSE`: Представляет ключ pause.
13. `KEY.ESCAPE`: Представляет ключ escape.
14. `KEY.SPACE`: Представляет ключ пробела.
15. `KEY.PAGE_UP`: Представляет ключ page up.
16. `KEY.PAGE_DOWN`: Представляет ключ page down.
17. `KEY.END`: Представляет ключ end.
18. `KEY.HOME`: Представляет ключ home.
19. `KEY.LEFT`: Представляет ключ левой стрелки.
20. `KEY.UP`: Представляет ключ верхней стрелки.
21. `KEY.RIGHT`: Представляет ключ правой стрелки.
22. `KEY.DOWN`: Представляет ключ нижней стрелки.
23. `KEY.INSERT`: Представляет ключ insert.
24. `KEY.DELETE`: Представляет ключ delete.
25. `KEY.SEMICOLON`: Представляет ключ точки с запятой.
26. `KEY.EQUALS`: Представляет ключ равно.
27. `KEY.NUMPAD0` - `KEY.NUMPAD9`: Представляют клавиши цифровой клавиатуры от 0 до 9.
28. `KEY.MULTIPLY`: Представляет ключ умножения.
29. `KEY.ADD`: Представляет ключ сложения.
30. `KEY.SEPARATOR`: Представляет ключ разделителя.
31. `KEY.SUBTRACT`: Представляет ключ вычитания.
32. `KEY.DECIMAL`: Представляет ключ десятичной точки.
33. `KEY.DIVIDE`: Представляет ключ деления.
34. `KEY.F1` - `KEY.F12`: Представляют функциональные клавиши от F1 до F12.
35. `KEY.META`: Представляет ключ meta.

## WebDriver Executor

### Обзор

Модуль WebDriver Executor предоставляет основу для выполнения навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий с веб-элементами.

### Основные возможности

-   **Обработка локаторов**
    -   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локатора, который содержит информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Получение элемента:** Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    -   **Получение атрибута:** Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с использованием локатора. Он поддерживает как одиночные, так и множественные элементы.
    -   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод веб-элементам. Он поддерживает имитацию печати с настраиваемой скоростью печати и дополнительным взаимодействием с мышью.
-   **Скриншоты**
    -   **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде PNG-изображения. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
-   **Действие клика**
    -   **Клик по элементу:** Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удается.
-   **Оценка локатора**
    -   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

### Использование

#### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

#### Выполнение локатора

Вызовите метод `execute_locator` со словарем локатора для выполнения действий или получения данных из веб-элементов.

#### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

### Зависимости

Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

### Примеры использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Main function to demonstrate usage examples for Driver and Chrome 

    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

[Driver explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Executor explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Locator explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.md)