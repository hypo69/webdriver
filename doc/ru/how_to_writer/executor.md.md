Как использовать модуль `src.webdriver.excutor`
=========================================================================================

Описание
-------------------------
Модуль `executor.py` предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Он предоставляет гибкий и универсальный фреймворк для поиска, взаимодействия и извлечения информации из веб-элементов на основе конфигураций, называемых "локаторами".

Шаги выполнения
-------------------------
1. **Инициализация `ExecuteLocator`:**
   - Создайте экземпляр класса `ExecuteLocator`, передав экземпляр Selenium WebDriver.
   - Пример: `executor = ExecuteLocator(driver=driver)`.
   - При инициализации создается объект `ActionChains`, если передан драйвер.
2. **Определение локатора:**
   - Локатор представляет собой словарь или `SimpleNamespace` объект с информацией о том, как найти веб-элемент.
   - Пример:
     ```python
     locator = {
         "by": "ID",
         "selector": "some_element_id",
         "event": "click()",
         "attribute": "value"
     }
     ```
   - `by`: Тип локатора (например, "ID", "CSS_SELECTOR", "XPATH").
   - `selector`: Значение локатора (например, "some_element_id").
   - `event`: Событие для выполнения (например, "click()", "send_keys('text')").
   - `attribute`: Атрибут для извлечения (например, "value", "text").
3. **Выполнение локатора:**
   - Используйте метод `execute_locator(locator)` для выполнения действий, определенных в локаторе.
   - Пример: `result = await executor.execute_locator(locator)`.
   - Метод определяет тип локатора и вызывает соответствующие методы для выполнения действий.
4. **Оценка локатора:**
   - Используйте метод `evaluate_locator(locator)` для обработки и извлечения атрибутов из веб-элемента.
   - Метод возвращает результат в зависимости от атрибутов локатора.
5. **Получение атрибута по локатору:**
    - Используйте метод `get_attribute_by_locator(locator)` для получения атрибута веб-элемента.
    - Пример: `attribute_value = await executor.get_attribute_by_locator(locator)`.
6. **Получение веб-элемента по локатору:**
   - Используйте метод `get_webelement_by_locator(locator)` для извлечения веб-элемента.
   - Пример: `element = await executor.get_webelement_by_locator(locator)`.
7. **Получение скриншота элемента:**
    - Используйте метод `get_webelement_as_screenshot(locator)` для получения скриншота элемента.
    - Метод возвращает путь к файлу со скриншотом.
8. **Выполнение событий:**
   - Используйте метод `execute_event(locator)` для выполнения событий, определенных в локаторе.
   - Пример: `await executor.execute_event(locator)`.
9. **Отправка сообщения:**
    - Используйте метод `send_message(locator, message)` для отправки сообщения в веб-элемент.
    - Пример: `await executor.send_message(locator, 'example text')`

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    import asyncio

    async def main():
        # Initialize the WebDriver
        driver = webdriver.Chrome()
        
        # Initialize the ExecuteLocator class
        executor = ExecuteLocator(driver=driver)
        
        # Define a locator
        locator = {
            "by": "ID",
            "selector": "login",
            "event": "click()"
        }
        
        # Execute the locator
        result = await executor.execute_locator(locator)
        print(f"Result of execution: {result}")

        # Define locator for input
        locator_input = {
             "by": "ID",
            "selector": "user-name",
        }
         # Send message to input
        await executor.send_message(locator_input, "example_username")

        # Define locator to retrieve attribute
        locator_attribute = {
            "by": "ID",
             "selector": "user-name",
            "attribute": "value"
        }
        # Get attribute value
        attribute_value = await executor.get_attribute_by_locator(locator_attribute)
        print(f"Attribute value: {attribute_value}")

        # Close the WebDriver
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())