# Документация модуля `src.webdriver.js`

## Обзор

Модуль `js.py` предоставляет утилиты JavaScript для взаимодействия с веб-страницами. Этот модуль разработан для расширения возможностей Selenium WebDriver путем добавления общих функций на основе JavaScript для взаимодействия с веб-страницами, включая управление видимостью, извлечение информации о странице и управление фокусом браузера.

## Оглавление

- [Обзор](#обзор)
- [Основные возможности](#основные-возможности)
- [Класс `JavaScript`](#класс-javascript)
    - [`__init__`](#__init__)
    - [`unhide_DOM_element`](#unhide_dom_element)
    - [`ready_state`](#ready_state)
    - [`window_focus`](#window_focus)
    - [`get_referrer`](#get_referrer)
    - [`get_page_lang`](#get_page_lang)

## Основные возможности

1.  Делает невидимые элементы DOM видимыми для взаимодействия.
2.  Извлекает метаданные, такие как состояние готовности документа, реферер или язык страницы.
3.  Управляет фокусом окна браузера программно.

## Класс `JavaScript`

### `__init__`

```python
    def __init__(self, driver: WebDriver):
        """Initializes the JavaScript helper with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
        """
        self.driver = driver
```

**Описание**: Инициализирует помощника JavaScript с экземпляром Selenium WebDriver.

**Параметры**:

-   `driver` (WebDriver): Экземпляр Selenium WebDriver для выполнения JavaScript.

### `unhide_DOM_element`

```python
    def unhide_DOM_element(self, element: WebElement) -> bool:
        """Makes an invisible DOM element visible by modifying its style properties.

        Args:
            element (WebElement): The WebElement object to make visible.

        Returns:
            bool: True if the script executes successfully, False otherwise.
        """
        script = """
        arguments[0].style.opacity = 1;
        arguments[0].style.transform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.MozTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.WebkitTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.msTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].style.OTransform = 'translate(0px, 0px) scale(1)';
        arguments[0].scrollIntoView(true);
        return true;
        """
        try:
            self.driver.execute_script(script, element)
            return True
        except Exception as ex:
            logger.error('Error in unhide_DOM_element: %s', ex)
            return False
```

**Описание**: Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

**Параметры**:

-   `element` (WebElement): Объект WebElement, который нужно сделать видимым.

**Возвращает**:

-   `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

### `ready_state`

```python
    @property
    def ready_state(self) -> str:
        """Retrieves the document loading status.

        Returns:
            str: 'loading' if the document is still loading, 'complete' if loading is finished.
        """
        try:
            return self.driver.execute_script('return document.readyState;')
        except Exception as ex:
            logger.error('Error retrieving document.readyState: %s', ex)
            return ''
```

**Описание**: Извлекает статус загрузки документа.

**Возвращает**:

-   `str`: `'loading'`, если документ все еще загружается, `'complete'`, если загрузка завершена.

### `window_focus`

```python
    def window_focus(self) -> None:
        """Sets focus to the browser window using JavaScript.

        Attempts to bring the browser window to the foreground.
        """
        try:
            self.driver.execute_script('window.focus();')
        except Exception as ex:
            logger.error('Error executing window.focus(): %s', ex)
```

**Описание**: Устанавливает фокус на окно браузера с помощью JavaScript.

### `get_referrer`

```python
    def get_referrer(self) -> str:
        """Retrieves the referrer URL of the current document.

        Returns:
            str: The referrer URL, or an empty string if unavailable.
        """
        try:
            return self.driver.execute_script('return document.referrer;') or ''
        except Exception as ex:
            logger.error('Error retrieving document.referrer: %s', ex)
            return ''
```

**Описание**: Извлекает URL-адрес реферера текущего документа.

**Возвращает**:

-   `str`: URL-адрес реферера или пустую строку, если он недоступен.

### `get_page_lang`

```python
    def get_page_lang(self) -> str:
        """Retrieves the language of the current page.

        Returns:
            str: The language code of the page, or an empty string if unavailable.
        """
        try:
            return self.driver.execute_script('return document.documentElement.lang;') or ''
        except Exception as ex:
            logger.error('Error retrieving document.documentElement.lang: %s', ex)
            return ''
```

**Описание**: Извлекает язык текущей страницы.

**Возвращает**:

-   `str`: Код языка страницы или пустую строку, если он недоступен.