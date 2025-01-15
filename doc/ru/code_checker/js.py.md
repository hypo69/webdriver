## Анализ кода модуля `src.webdriver.js`

**Качество кода**
7
- Плюсы
    - Код предоставляет набор JavaScript-утилит для работы с веб-страницами.
    - Присутствует документация в формате reStructuredText (RST).
    - Код выполняет распространенные задачи, такие как изменение видимости элемента, получение состояния загрузки страницы и языка, управление фокусом окна.
    - Используется логирование для отслеживания ошибок.
    - Код достаточно структурирован.
- Минусы
    -  Отсутствует импорт необходимых библиотек.
    -  Не все методы имеют описание типов для параметров и возвращаемых значений.
    -  Комментарии в docstring не соответствуют стандарту reStructuredText (RST) в части описания параметров и возвращаемых значений.
    -  В блоках `try-except` используется форматирование строк в стиле `%s`, а не `f-string`.
    -  Метод `window_focus` не возвращает значение.
    - Импорт `header` не используется и должен быть удален.
    - Присутствует дублирование кода при обработке ошибок.

**Рекомендации по улучшению**

1.  Добавить необходимые импорты, такие как `typing`.
2.  Удалить импорт `header`, так как он не используется.
3.  Добавить описание типов для параметров и возвращаемых значений во всех функциях и методах.
4.  Переписать комментарии в docstring в соответствии со стандартом reStructuredText (RST) в части описания параметров и возвращаемых значений.
5.  Использовать f-строки для форматирования сообщений в блоках `try-except`.
6.  Изменить метод `window_focus` чтобы он возвращал `bool`.
7.  Устранить дублирование кода при обработке ошибок путем вынесения в отдельную функцию.
8.   Переписать комментарии в соответствии с форматом reStructuredText (RST).
9.   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
.. module::  src.webdriver.js
    :platform: Windows, Unix
    :synopsis: Provides JavaScript utility functions for interacting with a web page.

    This module is designed to extend the capabilities of Selenium WebDriver by adding common JavaScript-based
    functions for interacting with web pages, including visibility manipulations, retrieving page information,
    and managing browser focus.

    Key Features:
        1. Make invisible DOM elements visible for interaction.
        2. Retrieve metadata like document ready state, referrer, or page language.
        3. Manage browser window focus programmatically.
"""

from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from src.logger.logger import logger


class JavaScript:
    """Provides JavaScript utility functions for interacting with a web page."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует JavaScript хелпер с экземпляром Selenium WebDriver.

        :param driver: Экземпляр Selenium WebDriver для выполнения JavaScript.
        :type driver: WebDriver
        """
        self.driver = driver

    def _execute_script(self, script: str, *args: WebElement) -> Optional[Any]:
        """
        Выполняет JavaScript код.

        :param script: JavaScript код для выполнения.
        :type script: str
        :param args: Аргументы для JavaScript.
        :type args: WebElement
        :return: Результат выполнения JavaScript кода или None в случае ошибки.
        :rtype: Optional[Any]
        """
        try:
            return self.driver.execute_script(script, *args)
        except Exception as ex:
            logger.error(f'Ошибка при выполнении скрипта: {script}', exc_info=ex)
            return None

    def unhide_DOM_element(self, element: WebElement) -> bool:
        """
        Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

        :param element: Веб-элемент, который нужно сделать видимым.
        :type element: WebElement
        :return: True, если скрипт выполнен успешно, иначе False.
        :rtype: bool
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
        return bool(self._execute_script(script, element))

    @property
    def ready_state(self) -> str:
        """
        Получает статус загрузки документа.

        :return: 'loading', если документ еще загружается, 'complete', если загрузка завершена.
        :rtype: str
        """
        return self._execute_script('return document.readyState;') or ''


    def window_focus(self) -> bool:
        """
        Устанавливает фокус на окно браузера с помощью JavaScript.

        :return: True, если фокус установлен, иначе False.
        :rtype: bool
        """
        return bool(self._execute_script('window.focus();'))


    def get_referrer(self) -> str:
        """
        Получает URL-адрес отправителя текущего документа.

        :return: URL-адрес отправителя или пустая строка, если он недоступен.
        :rtype: str
        """
        return self._execute_script('return document.referrer;') or ''


    def get_page_lang(self) -> str:
        """
        Получает язык текущей страницы.

        :return: Языковой код страницы или пустая строка, если он недоступен.
        :rtype: str
        """
        return self._execute_script('return document.documentElement.lang;') or ''
```

**Изменения**

1.  Добавлен импорт `typing`.
2.  Удален импорт `header`.
3.  Добавлены описания типов для параметров и возвращаемых значений во всех функциях и методах.
4.  Переписаны комментарии в docstring в соответствии со стандартом reStructuredText (RST) в части описания параметров и возвращаемых значений.
5.  Использованы f-строки для форматирования сообщений в блоках `try-except`.
6.  Изменен метод `window_focus`, чтобы он возвращал `bool`.
7.  Устранено дублирование кода при обработке ошибок путем вынесения в отдельную функцию `_execute_script`.
8. Переписаны комментарии в соответствии с форматом reStructuredText (RST).
9. Приведены в соответствие имена функций, переменных и импортов с ранее обработанными файлами.