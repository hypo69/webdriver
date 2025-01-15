Как использовать модуль `src.webdriver`
=========================================================================================

Описание
-------------------------
Модуль `src.webdriver` предоставляет набор инструментов для автоматизации взаимодействия с веб-страницами с использованием Selenium WebDriver. Он включает классы для управления браузером, выполнения действий над элементами, обработки JavaScript и управления куками.

Шаги выполнения
-------------------------
1. **Инициализация драйвера:**
   - Создайте экземпляр класса `Driver`, указав класс браузера (например, `Chrome`).
   - Пример: `chrome_driver = Driver(Chrome)`.
   - Можно передать дополнительные параметры в конструктор, например, пользовательский User-Agent: `custom_chrome_driver = Driver(Chrome, user_agent=user_agent)`.
2. **Навигация по URL:**
   - Используйте метод `get_url(url)` для перехода по указанному URL.
   - Пример: `if chrome_driver.get_url("https://www.example.com"): ...`.
   - Метод загружает указанный URL и сохраняет предыдущий URL и куки.
3. **Извлечение домена:**
   - Используйте метод `extract_domain(url)` для извлечения домена из URL.
   - Пример: `domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")`.
   - Метод возвращает доменное имя.
4. **Сохранение куки:**
   - Используйте метод `_save_cookies_localy()` для сохранения куки в локальный файл.
   - Пример: `success = chrome_driver._save_cookies_localy()`.
   - Метод сохраняет куки текущего сеанса браузера.
5. **Обновление страницы:**
   - Используйте метод `page_refresh()` для обновления текущей страницы.
   - Пример: `if chrome_driver.page_refresh(): ...`.
   - Метод перезагружает текущую страницу.
6. **Прокрутка страницы:**
   - Используйте метод `scroll(scrolls, direction, frame_size, delay)` для прокрутки страницы в указанном направлении.
   - Пример: `if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1): ...`.
   - Параметры: `scrolls` - количество прокруток, `direction` - направление прокрутки (`forward`, `backward`, `both`), `frame_size` - размер прокрутки, `delay` - задержка между прокрутками.
7. **Определение языка страницы:**
   - Используйте свойство `locale` для определения языка текущей страницы.
   - Пример: `page_language = chrome_driver.locale`.
   - Метод пытается определить язык из мета-тега или с помощью JavaScript.
8. **Поиск элемента:**
   - Используйте метод `find_element(by, selector)` для поиска элемента на странице.
   - Пример: `element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')`.
   - Параметры: `by` - метод поиска (например, `By.CSS_SELECTOR`, `By.XPATH`), `selector` - селектор.
9.  **Получение текущего URL:**
    - Используйте свойство `current_url` для получения URL текущей страницы.
    - Пример: `current_url = chrome_driver.current_url`.
10. **Фокус окна браузера:**
    - Используйте метод `window_focus()` для перевода фокуса на окно браузера.
    - Пример: `chrome_driver.window_focus()`.
11. **Использование `ExecuteLocator`:**
    - Создайте экземпляр `ExecuteLocator`, передав ему экземпляр WebDriver.
    - Пример: `executor = ExecuteLocator(driver=chrome_driver)`.
    - Используйте метод `execute_locator(locator)` для выполнения действий, описанных в локаторе.
    - Пример: `result = await executor.execute_locator(locator)`.
12. **Извлечение атрибутов:**
    - Используйте метод `get_attribute_by_locator(locator)` для извлечения атрибутов.
    - Пример: `attribute_value = await executor.get_attribute_by_locator(locator)`.
13. **Отправка сообщения:**
    - Используйте метод `send_message(locator, message)` для отправки текста в элемент.
    - Пример: `await executor.send_message(locator, message='example_text')`.
14. **Скриншоты элементов:**
    - Используйте метод `get_webelement_as_screenshot(locator)` для создания скриншота элемента.
    - Пример: `screenshot = await executor.get_webelement_as_screenshot(locator)`.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.driver import Driver, Chrome
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator

    async def main():
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
        
        # Example 11: Using ExecuteLocator for click action
        executor = ExecuteLocator(driver=chrome_driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Result of execute_locator click: {result}")
        
        #Example 12: Using ExecuteLocator for send message
        locator_input = {"by": "ID", "selector": "some_input_id"}
        result = await executor.send_message(locator_input, message='example_text')
        print(f'Result of send_message: {result}')
        
        #Example 13: Using ExecuteLocator for getting attribute
        locator_attribute = {"by": "ID", "selector": "some_input_id", 'attribute': "value"}
        attribute_value = await executor.get_attribute_by_locator(locator_attribute)
        print(f"Attribute value: {attribute_value}")

        #Example 14: Using ExecuteLocator for taking screenshot
        locator_screenshot = {"by": "ID", "selector": "some_element_id"}
        screenshot = await executor.get_webelement_as_screenshot(locator_screenshot)
        if screenshot:
            with open("screenshot.png", "wb") as f:
                f.write(screenshot)
            print(f"Screenshot saved to screenshot.png")

        chrome_driver.quit()

    if __name__ == "__main__":
       asyncio.run(main())