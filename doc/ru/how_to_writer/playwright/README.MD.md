Как использовать модуль Playwright Crawler для автоматизации и сбора данных
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию `PlaywrightCrawler` с именем `Playwrid` с использованием библиотеки Crawlee. Он позволяет настраивать параметры запуска браузера, такие как user-agent, прокси, размер окна и другие опции, определенные в файле `playwrid.json`.

Шаги выполнения
-------------------------
1.  **Установка зависимостей:**
    -   Убедитесь, что установлены библиотеки `playwright` и `crawlee`.
    -  Если нет, выполните: `pip install playwright crawlee`.
    - Установите браузеры Playwright с помощью команды `playwright install`.
2.  **Настройка конфигурации:**
    - Отредактируйте файл `playwrid.json`, чтобы настроить параметры краулера.
    - Основные параметры:
        -  `browser_type`: тип браузера (`chromium`, `firefox`, `webkit`).
        -  `headless`: запускать ли браузер в безголовом режиме (`true` или `false`).
        -  `options`: список дополнительных параметров командной строки для браузера.
        -   `user_agent`: строка user-agent.
        -  `proxy`: настройки прокси (включено/выключено, сервер, логин, пароль).
        -  `viewport`: размеры окна (`width`, `height`).
        - `timeout`: таймаут (в миллисекундах).
        -   `ignore_https_errors`: игнорировать ошибки HTTPS (`true` или `false`).
3.  **Инициализация `Playwrid`:**
    -  Создайте экземпляр класса `Playwrid`, передав дополнительные параметры или используя настройки из `playwrid.json`.
    - Пример:
        ```python
        from src.webdriver.playwright import Playwrid
    
        browser = Playwrid(options=["--headless"])
        ```
    -   Параметры:
        - `user_agent`: пользовательский агент (опционально).
        -  `options`: список параметров командной строки для браузера (опционально).
4.  **Запуск краулера и навигация:**
     - Используйте метод `start(url)` для запуска краулера и перехода на указанный URL.
    - Пример:
       ```python
        await browser.start("https://www.example.com")
        ```
      -   Метод инициализирует Playwright, запускает браузер, переходит по URL и запускает базовый краулер.
5. **Получение HTML контента:**
   - Используйте метод `get_page_content()` для получения HTML контента.
   -  Пример: `html = browser.get_page_content()`
6. **Получение HTML контента элемента:**
    -  Используйте метод `get_element_content(selector)` для извлечения HTML контента элемента по CSS селектору.
    -   Пример: `html = await browser.get_element_content(selector="h1")`.
7.  **Получение текста элемента по XPath:**
    - Используйте метод `get_element_value_by_xpath(xpath)` для извлечения текста элемента по XPath.
    - Пример: `text = await browser.get_element_value_by_xpath("//h1")`.
8. **Клик по элементу:**
    - Используйте метод `click_element(selector)` для клика по элементу.
    - Пример: `await browser.click_element("button")`.
9.  **Выполнение локатора:**
    -  Используйте метод `execute_locator(locator, message, typing_speed)` для выполнения действий, основанных на локаторе.
    -   Пример: `await browser.execute_locator(locator)`.
10. **Логирование:**
     -  Модуль использует `logger` для логирования ошибок и предупреждений.
     - Проверяйте логи для отладки и отслеживания ошибок.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.playwright import Playwrid

    async def main():
       # Инициализация краулера
        browser = Playwrid(options=["--headless"])
        await browser.start("https://www.example.com")
    
        # Получение HTML контента страницы
        html_content = browser.get_page_content()
        if html_content:
            print(f"HTML контент (первые 200 символов): {html_content[:200]}...")
        else:
            print("Не удалось получить HTML контент.")
    
        # Получение HTML контента элемента
        element_content = await browser.get_element_content("h1")
        if element_content:
            print(f"Содержимое элемента h1: {element_content}")
        else:
            print("Элемент h1 не найден.")
    
        # Получение значения элемента по XPATH
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
            print(f"Значение элемента по XPath //head/title: {xpath_value}")
        else:
            print("Элемент по XPath //head/title не найден.")
    
        # Клик по кнопке
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
           "locator_description": "Заголовок"
        }

        name = await browser.execute_locator(locator_name)
        print("Заголовок:", name)

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