Как использовать модуль `src.webdriver.excutor`
=========================================================================================

Описание
-------------------------
Модуль `executor.py` предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Он обеспечивает гибкий и универсальный интерфейс для поиска, взаимодействия и извлечения информации из веб-элементов на основе конфигураций, называемых "локаторами".

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
   - Используйте метод `execute_locator(locator, timeout, timeout_for_event, message, typing_speed, continue_on_error)` для выполнения действий, определенных в локаторе.
   - Пример: `result = await executor.execute_locator(locator, timeout=10, message="example text")`.
   - Метод обрабатывает локатор, определяет тип локатора и вызывает соответствующие методы для выполнения действий и возвращает результат.
   - `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию 0.
   - `timeout_for_event` (str, optional): Условие ожидания элемента. По умолчанию 'presence_of_element_located'.
   - `message` (str, optional): Сообщение для отправки. По умолчанию None.
   - `typing_speed` (float, optional): Скорость печати текста. По умолчанию 0.
   - `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при ошибке. По умолчанию True.
4. **Оценка локатора:**
   - Используйте метод `evaluate_locator(attribute)` для обработки атрибутов локатора.
   - Пример: `evaluated_attribute = await executor.evaluate_locator(attribute="some attribute")`.
   - Метод возвращает результат обработки атрибутов.
5. **Получение атрибута по локатору:**
    - Используйте метод `get_attribute_by_locator(locator, timeout, timeout_for_event)` для получения атрибута веб-элемента.
    - Пример: `attribute_value = await executor.get_attribute_by_locator(locator, timeout=5)`.
   -  `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию 0.
   - `timeout_for_event` (str, optional): Условие ожидания элемента. По умолчанию 'presence_of_element_located'.
6. **Получение веб-элемента по локатору:**
   - Используйте метод `get_webelement_by_locator(locator, timeout, timeout_for_event)` для извлечения веб-элемента.
   - Пример: `element = await executor.get_webelement_by_locator(locator, timeout=5)`.
   -  `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию 0.
   - `timeout_for_event` (str, optional): Условие ожидания элемента. По умолчанию 'presence_of_element_located'.
7. **Получение скриншота элемента:**
    - Используйте метод `get_webelement_as_screenshot(locator, timeout, timeout_for_event, message, typing_speed, continue_on_error, webelement)` для получения скриншота элемента.
    - Пример: `screenshot = await executor.get_webelement_as_screenshot(locator, timeout=5)`.
    - Метод возвращает бинарный поток изображения.
    - `webelement` (WebElement, optional): Веб-элемент для снятия скриншота. По умолчанию None.
8. **Выполнение событий:**
   - Используйте метод `execute_event(locator, timeout, timeout_for_event, message, typing_speed, continue_on_error)` для выполнения событий, определенных в локаторе.
   - Пример: `await executor.execute_event(locator, timeout=5, message="some text")`.
   - Метод обрабатывает такие события, как клик, пауза, загрузка медиа, скриншот, очистка поля, отправка клавиш и ввод текста.
    - `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию 5.
   - `timeout_for_event` (str, optional): Условие ожидания элемента. По умолчанию 'presence_of_element_located'.
   - `message` (str, optional): Сообщение для отправки. По умолчанию None.
   - `typing_speed` (float, optional): Скорость печати текста. По умолчанию 0.
   - `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при ошибке. По умолчанию True.
9. **Отправка сообщения:**
    - Используйте метод `send_message(locator, timeout, timeout_for_event, message, typing_speed, continue_on_error)` для отправки сообщения в веб-элемент.
    - Пример: `await executor.send_message(locator, message="Hello World", typing_speed=0.1)`.
    - `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию 5.
   - `timeout_for_event` (str, optional): Условие ожидания элемента. По умолчанию 'presence_of_element_located'.
   - `message` (str, optional): Сообщение для отправки. По умолчанию None.
   - `typing_speed` (float, optional): Скорость печати текста. По умолчанию 0.
   - `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при ошибке. По умолчанию True.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    import asyncio

    async def main():
        # Инициализация WebDriver
        driver = webdriver.Chrome()
        
        # Инициализация класса ExecuteLocator
        executor = ExecuteLocator(driver=driver)
        
        # Определение локатора
        locator = {
            "by": "ID",
            "selector": "login",
            "event": "click()"
        }
        
        # Выполнение локатора
        result = await executor.execute_locator(locator, timeout=10)
        print(f"Result of execution: {result}")

        # Определение локатора для input
        locator_input = {
             "by": "ID",
            "selector": "user-name",
        }
         # Отправка сообщения в input
        await executor.send_message(locator_input, message="example_username", typing_speed=0.1)

        # Определение локатора для получения атрибута
        locator_attribute = {
            "by": "ID",
             "selector": "user-name",
            "attribute": "value"
        }
        # Получение значения атрибута
        attribute_value = await executor.get_attribute_by_locator(locator_attribute)
        print(f"Attribute value: {attribute_value}")

         # Take screenshot of element
        screenshot = await executor.get_webelement_as_screenshot(locator_attribute, timeout=5)
        if screenshot:
            with open("screenshot.png", "wb") as f:
                f.write(screenshot)
            print(f"Screenshot save to screenshot.png")

        # Закрытие WebDriver
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())