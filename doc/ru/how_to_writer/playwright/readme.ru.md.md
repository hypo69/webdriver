Как использовать модуль Playwright Crawler для автоматизации браузера
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию `PlaywrightCrawler` с именем `Playwrid`, используя библиотеку Crawlee. Он позволяет настраивать параметры запуска браузера, такие как user-agent, прокси-сервер, размер окна и другие опции, определенные в файле `playwrid.json`.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
    - Убедитесь, что установлены библиотеки `playwright` и `crawlee`.
    - Если нет, выполните команду: `pip install playwright crawlee`.
    - Установите браузеры Playwright командой `playwright install`.
2. **Настройка конфигурации (`playwrid.json`):**
    - Отредактируйте файл `playwrid.json` для настройки параметров краулера.
    -  Основные параметры:
       - `browser_type`: Тип браузера ('chromium', 'firefox', 'webkit').
       -   `headless`: Запускать ли браузер без графического интерфейса (`true` или `false`).
      -   `options`: Список параметров командной строки для браузера.
       - `user_agent`: Пользовательский агент.
       -  `proxy`: Настройки прокси-сервера.
        - `viewport`: Размеры окна браузера.
        -  `timeout`: Таймаут для операций.
        - `ignore_https_errors`: Игнорировать ошибки HTTPS.
3. **Инициализация `Playwrid`:**
    -  Создайте экземпляр класса `Playwrid`.
    - Пример:
       ```python
       from src.webdriver.playwright import Playwrid
    
       browser = Playwrid(options=["--headless"])
       ```
    - Параметры:
        -  `user_agent`: Пользовательский агент (необязательный).
       -  `options`: Список опций для Playwright (необязательный).
4. **Запуск краулера и навигация:**
   -  Используйте метод `start(url)` для запуска браузера и перехода по указанному URL.
   - Пример: `browser.start("https://www.example.com")`.
    - Метод запускает браузер, переходит на страницу, и запускает базовый цикл краулинга.
5. **Получение контента страницы:**
    - Используйте метод `get_page_content()` для получения HTML-кода страницы.
    - Пример: `html_content = browser.get_page_content()`.
6. **Получение контента элемента:**
    - Используйте метод `get_element_content(selector)` для извлечения HTML элемента по CSS селектору.
    - Пример: `element_content = await browser.get_element_content("h1")`.
7. **Получение значения элемента по XPath:**
    - Используйте метод `get_element_value_by_xpath(xpath)` для извлечения текстового значения элемента по XPath.
    - Пример: `xpath_value = await browser.get_element_value_by_xpath("//head/title")`.
8. **Клик по элементу:**
    - Используйте метод `click_element(selector)` для клика по элементу с помощью CSS селектора.
    - Пример: `await browser.click_element("button")`.
9. **Выполнение локатора:**
   - Используйте метод `execute_locator(locator)` для выполнения действий на основе локатора.
   - Пример:
      ```python
       locator = {"by": "ID", "selector": "some_id", "event": "click()"}
       result = await browser.execute_locator(locator)
       ```
    -  Параметры локатора определяют, как найти элемент на странице и какие действия выполнить.
10. **Логирование:**
    -  Модуль использует `logger` для логирования ошибок и отладочной информации.
    - Просматривайте логи для отслеживания проблем при работе краулера.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.playwright import Playwrid
    
    async def main():
        # Инициализация краулера
        browser = Playwrid(options=["--headless"])
        
        # Запуск краулера и навигация по URL
        await browser.start("https://www.example.com")
    
        # Получение HTML содержимого страницы
        html_content = browser.get_page_content()
        if html_content:
            print(f"Первые 200 символов HTML контента: {html_content[:200]}...")
        else:
            print("Не удалось получить HTML контент.")
        
        # Получение HTML контента элемента h1
        element_content = await browser.get_element_content("h1")
        if element_content:
           print(f"Содержимое элемента h1: {element_content}")
        else:
          print("Элемент h1 не найден.")
        
        # Получение текста из head/title
        xpath_value = await browser.get_element_value_by_xpath("//head/title")
        if xpath_value:
            print(f"Значение title: {xpath_value}")
        else:
           print("Элемент по XPATH //head/title не найден")
        
        # Выполнение клика по кнопке
        await browser.click_element("button")
        
        # Пример использования execute_locator
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
```