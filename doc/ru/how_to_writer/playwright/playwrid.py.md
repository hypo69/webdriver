Как использовать модуль Playwright Crawler для автоматизации и сбора данных
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию `PlaywrightCrawler` с именем `Playwrid` с использованием библиотеки Crawlee. Он расширяет функционал стандартного краулера, добавляя возможность настройки браузера, профилей и параметров запуска. Управление конфигурацией происходит через файл `playwrid.json`.

Шаги выполнения
-------------------------
1.  **Установка зависимостей:**
    -  Убедитесь, что установлены библиотеки `crawlee` и `playwright`.
    -   Если они не установлены, выполните `pip install crawlee playwright`.
    -   Установите браузеры Playwright с помощью команды `playwright install`.
2. **Импорт модуля:**
    -  Импортируйте класс `Playwrid` из модуля `src.webdriver.playwright.playwrid`.
       ```python
        from src.webdriver.playwright.playwrid import Playwrid
        ```
3.  **Настройка конфигурации (playwrid.json):**
    -  Отредактируйте файл `playwrid.json` для настройки параметров браузера.
    - Основные параметры:
        -  `max_requests`: максимальное количество запросов (не используется в текущей реализации `start()`).
        -   `headless`: запускать ли браузер в безголовом режиме (по умолчанию `true`).
        -   `browser_type`: тип браузера ('chromium', 'firefox', 'webkit').
        -  `options`: список параметров командной строки для запуска браузера.
        - `user_agent`: строка пользовательского агента.
        - `proxy`: настройки прокси (не используются в текущей реализации).
         - `viewport`: размеры окна браузера.
         -   `timeout`: таймаут (в миллисекундах).
        - `ignore_https_errors`: игнорировать ошибки HTTPS (по умолчанию `false`).
4.  **Инициализация `Playwrid`:**
     - Создайте экземпляр класса `Playwrid`, передав опциональные параметры.
     -  Пример:
          ```python
          from src.webdriver.playwright.playwrid import Playwrid
    
          browser = Playwrid(options=["--headless"])
          ```
     -  Параметры:
        - `user_agent`: пользовательский агент (опционально).
        - `options`: дополнительные опции для запуска браузера (опционально).
       - Все остальные параметры загружаются из `playwrid.json`.
5.  **Запуск краулера и навигация:**
    - Используйте метод `start(url)` для запуска краулера и перехода по URL.
    - Пример: `await browser.start('https://www.example.com')`.
   -    Метод инициализирует Playwright, запускает браузер, переходит на указанный URL, и затем запускает базовый краулер.
6. **Получение текущего URL:**
    - Используйте свойство `current_url` для получения URL текущей страницы.
    - Пример: `current_url = browser.current_url`.
7.  **Получение HTML контента страницы:**
    -  Используйте метод `get_page_content()` для получения HTML-контента.
    -  Пример: `html_content = browser.get_page_content()`.
8.  **Получение HTML контента элемента по CSS селектору:**
    - Используйте метод `get_element_content(selector)` для получения HTML контента элемента.
    -  Пример: `element_content = await browser.get_element_content('h1')`.
9.  **Получение значения элемента по XPath:**
    -  Используйте метод `get_element_value_by_xpath(xpath)` для получения текста элемента.
    -  Пример: `text = await browser.get_element_value_by_xpath('//head/title')`.
10. **Выполнение клика по элементу:**
    - Используйте метод `click_element(selector)` для выполнения клика по элементу.
    -  Пример: `await browser.click_element('button')`.
11. **Выполнение локатора:**
   -  Используйте метод `execute_locator(locator, message, typing_speed)` для выполнения действий на основе заданного локатора.
    -   Пример:
        ```python
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await browser.execute_locator(locator)
        ```
   -   Возвращает результат операции.
12. **Логирование:**
    -  Модуль использует `logger` для логирования ошибок и предупреждений.
    - Просматривайте логи для отладки.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.playwright.playwrid import Playwrid
    from types import SimpleNamespace
    
    async def main():
        # Инициализация Playwrid с опциями
        browser = Playwrid(options=["--headless"])
        await browser.start("https://www.example.com")
    
        # Получение HTML всего документа
        html_content = browser.get_page_content()
        if html_content:
            print(f"Первые 200 символов HTML: {html_content[:200]}...")
        else:
            print("Не удалось получить HTML-контент.")
    
        # Получение HTML элемента по селектору
        element_content = await browser.get_element_content("h1")
        if element_content:
            print(f"Содержимое элемента h1: {element_content}")
        else:
            print("Элемент h1 не найден.")
    
        # Получение значения элемента по XPATH
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
            print(f"Значение элемента по XPATH //head/title: {xpath_value}")
        else:
            print("Элемент по XPATH //head/title не найден")
    
        # Нажатие на кнопку
        await browser.click_element("button")
        
        # Использование execute_locator
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
            "locator_description": "кнопка"
            }
        await browser.execute_locator(locator_click)
        await asyncio.sleep(3)
   
    if __name__ == "__main__":
        asyncio.run(main())