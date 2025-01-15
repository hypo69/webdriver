Как использовать модуль Playwright Executor для автоматизации и сбора данных
=========================================================================================

Описание
-------------------------
Модуль предоставляет класс `PlaywrightExecutor`, который обеспечивает выполнение команд на веб-страницах с использованием библиотеки Playwright. Он предназначен для автоматизации взаимодействия с веб-элементами и обработки данных на основе заданных локаторов и событий.

Шаги выполнения
-------------------------
1.  **Импорт модуля:**
    - Импортируйте класс `PlaywrightExecutor` из модуля `src.webdriver.playwright.executor`.
        ```python
        from src.webdriver.playwright.executor import PlaywrightExecutor
        ```
2.  **Инициализация:**
    -   Создайте экземпляр класса `PlaywrightExecutor`, указав тип браузера (по умолчанию `chromium`).
    -   Пример:
        ```python
        executor = PlaywrightExecutor(browser_type='firefox')
        ```
3.  **Запуск браузера:**
    - Используйте метод `start()` для инициализации Playwright и запуска браузера.
    - Пример: `await executor.start()`.
    - Метод запускает браузер в безголовом режиме.
4.  **Остановка браузера:**
    -   Используйте метод `stop()` для закрытия браузера и завершения Playwright.
    - Пример: `await executor.stop()`.
5. **Выполнение локаторов:**
    - Используйте метод `execute_locator(locator, message, typing_speed)` для выполнения действий на основе заданного локатора.
    -   Параметры:
        -   `locator`: словарь или `SimpleNamespace` объект с параметрами локатора (например, `by`, `selector`, `event`, `attribute`).
        - `message` (str, optional): сообщение для отправки (используется с событиями ввода текста).
        - `typing_speed` (float, optional): скорость печати текста (в секундах).
    -  Пример:
         ```python
         locator = {"by": "ID", "selector": "some_id", "event": "click()"}
         result = await executor.execute_locator(locator)
         ```
    -   Метод выполняет действие и возвращает результат.
6.  **Оценка локатора:**
    -  Используйте метод `evaluate_locator(attribute)` для обработки атрибутов локатора.
    -   Пример: `result = await executor.evaluate_locator(attribute='some_attribute')`.
    -  Метод возвращает результат в зависимости от атрибутов.
7. **Получение атрибута:**
   -   Используйте метод `get_attribute_by_locator(locator)` для получения значения атрибута элемента.
   -   Пример: `attribute = await executor.get_attribute_by_locator(locator)`.
8. **Получение элемента:**
   -   Используйте метод `get_webelement_by_locator(locator)` для получения элемента по локатору.
   -   Пример: `element = await executor.get_webelement_by_locator(locator)`.
9.  **Скриншот элемента:**
   - Используйте метод `get_webelement_as_screenshot(locator, webelement)` для получения скриншота элемента (опционально можно передать найденный элемент через параметр `webelement`).
   - Пример: `screenshot = await executor.get_webelement_as_screenshot(locator)`.
10. **Выполнение события:**
    - Используйте метод `execute_event(locator, message, typing_speed)` для выполнения событий (click, ввод текста и т.д.) связанных с элементом, который задан локатором.
    -  Пример: `await executor.execute_event(locator, message='example')`.
11. **Отправка сообщения:**
    -  Используйте метод `send_message(locator, message, typing_speed)` для отправки сообщения в текстовое поле.
    -  Пример: `await executor.send_message(locator, message='example text', typing_speed=0.1)`.
12. **Навигация по URL:**
    -  Используйте метод `goto(url)` для перехода на указанный URL.
    -  Пример: `await executor.goto('https://example.com')`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.playwright.executor import PlaywrightExecutor
    from types import SimpleNamespace

    async def main():
       # Инициализация PlaywrightExecutor
        executor = PlaywrightExecutor(browser_type='chromium')
    
        # Запуск браузера
        await executor.start()
        
       # Пример локатора для клика
        locator = SimpleNamespace(by='ID', selector='some_id', event='click()')
        result = await executor.execute_locator(locator)
        print(f"Результат click: {result}")

        # Пример локатора для ввода текста
        locator_input = SimpleNamespace(by='ID', selector='some_input_id')
        await executor.send_message(locator_input, message="example text")
       
        # Пример локатора для получения атрибута
        locator_attribute = SimpleNamespace(by='ID', selector='some_input_id', attribute="value")
        attribute = await executor.get_attribute_by_locator(locator_attribute)
        print(f"Значение атрибута: {attribute}")
       
        # Пример локатора для скриншота
        locator_screenshot =  SimpleNamespace(by='ID', selector='some_element_id')
        screenshot = await executor.get_webelement_as_screenshot(locator_screenshot)
        if screenshot:
             with open("screenshot.png", "wb") as f:
                  f.write(screenshot)
             print("Скриншот сохранен в screenshot.png")

         # Переход на другую страницу
        await executor.goto("https://example.org")
        
        # Остановка браузера
        await executor.stop()

    if __name__ == "__main__":
        asyncio.run(main())