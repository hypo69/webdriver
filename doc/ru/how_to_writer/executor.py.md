Как использовать модуль `src.webdriver.excutor`
=========================================================================================

Описание
-------------------------
Модуль `executor.py` предназначен для выполнения действий над веб-элементами на основе предоставленных конфигураций, называемых "локаторами". Модуль обеспечивает гибкость и универсальность при работе с веб-элементами, позволяя автоматизировать сложные сценарии взаимодействия.

Шаги выполнения
-------------------------
1. **Инициализация `ExecuteLocator`:**
   - Создайте экземпляр класса `ExecuteLocator`, передав экземпляр Selenium WebDriver.
   - Пример: `executor = ExecuteLocator(driver=driver)`.
   - При инициализации создается объект `ActionChains`, если драйвер предоставлен.
2. **Определение локатора:**
   - Локатор может быть словарем или объектом `SimpleNamespace`, содержащим информацию о том, как найти веб-элемент.
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
   - `selector`: Значение локатора.
   - `event`: Событие для выполнения (например, "click()", "send_keys('text')").
   - `attribute`: Атрибут для извлечения.
3. **Выполнение локатора:**
   - Используйте метод `execute_locator(locator, timeout, timeout_for_event, message, typing_speed, continue_on_error)` для выполнения действий, определенных в локаторе.
   - Пример: `result = await executor.execute_locator(locator, timeout=10, message="some text")`.
   - Метод определяет тип локатора, вызывает соответствующие методы для выполнения действий и возвращает результат.
   - `timeout`: Максимальное время ожидания элемента.
   - `timeout_for_event`: Тип ожидания элемента.
   - `message`: Сообщение для отправки.
   - `typing_speed`: Скорость печати текста.
   - `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение при ошибке.
4. **Оценка локатора:**
   - Используйте метод `evaluate_locator(attribute)` для обработки атрибутов локатора.
   - Метод поддерживает строковые атрибуты или список атрибутов и возвращает результат обработки.
5. **Получение атрибута по локатору:**
   - Используйте метод `get_attribute_by_locator(locator, timeout, timeout_for_event)` для получения атрибута веб-элемента.
   - Пример: `attribute_value = await executor.get_attribute_by_locator(locator, timeout=5)`.
   - `timeout`: Время ожидания.
   - `timeout_for_event`: Тип ожидания элемента.
6. **Получение веб-элемента по локатору:**
   - Используйте метод `get_webelement_by_locator(locator, timeout, timeout_for_event)` для извлечения веб-элемента или списка элементов.
   - Пример: `element = await executor.get_webelement_by_locator(locator, timeout=5)`.
   - `timeout`: Время ожидания.
   - `timeout_for_event`: Тип ожидания элемента.
7.  **Получение скриншота элемента:**
    - Используйте метод `get_webelement_as_screenshot(locator, timeout, timeout_for_event, webelement)` для получения скриншота элемента.
    - Пример: `screenshot = await executor.get_webelement_as_screenshot(locator, timeout=5)`.
    - Метод возвращает бинарный поток изображения.
    - `webelement`: Переопределенный веб-элемент.
8. **Выполнение событий:**
   - Используйте метод `execute_event(locator, timeout, timeout_for_event, message, typing_speed)` для выполнения событий, определенных в локаторе.
     - Пример: `await executor.execute_event(locator, timeout=5, message="some text")`.
   - Метод обрабатывает такие события, как клик, пауза, загрузка медиа, скриншот, очистка поля, отправка клавиш и ввод текста.
9. **Отправка сообщения:**
   - Используйте метод `send_message(locator, timeout, timeout_for_event, message, typing_speed)` для отправки сообщения в веб-элемент.
   - Пример: `await executor.send_message(locator, message="Hello World", typing_speed=0.1)`.
   - Метод разбивает сообщение на слова и символы для эмуляции ввода текста.

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
        result = await executor.execute_locator(locator, timeout=10)
        print(f"Result of execution: {result}")

        # Define locator for input
        locator_input = {
             "by": "ID",
            "selector": "user-name",
        }
         # Send message to input
        await executor.send_message(locator_input, message="example_username", typing_speed=0.1)

        # Define locator to retrieve attribute
        locator_attribute = {
            "by": "ID",
             "selector": "user-name",
            "attribute": "value"
        }
        # Get attribute value
        attribute_value = await executor.get_attribute_by_locator(locator_attribute)
        print(f"Attribute value: {attribute_value}")

        # Take screenshot of element
        screenshot = await executor.get_webelement_as_screenshot(locator_attribute)
        if screenshot:
            with open("screenshot.png", "wb") as f:
                f.write(screenshot)
            print(f"Screenshot save to screenshot.png")

        # Close the WebDriver
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())