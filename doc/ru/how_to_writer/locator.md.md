Как использовать локаторы и их взаимодействие с `executor`
=========================================================================================

Описание
-------------------------
Локаторы - это конфигурационные объекты, описывающие, как найти и взаимодействовать с веб-элементами на странице. Они передаются классу `ExecuteLocator` для выполнения различных действий, таких как клики, отправка сообщений, извлечение атрибутов и т.д. В этом документе подробно рассматриваются примеры локаторов, их ключи и взаимодействие с `executor`.

Шаги выполнения
-------------------------
1. **Определение локатора**:
   - Локатор представляет собой словарь с ключами, описывающими, как найти веб-элемент и какое действие с ним выполнить.
2. **Ключи локатора**:
   - `attribute`: Атрибут, который нужно извлечь или установить. Может быть `null` или строкой, или числом.
   - `by`: Метод поиска элемента (`XPATH`, `ID`, `VALUE` и т.д.).
   - `selector`: Селектор для поиска элемента.
   - `if_list`: Правило для обработки списка элементов (`first`, `last`, `all`, `even`, `odd` или индекс элемента).
   - `use_mouse`: Флаг, указывающий, использовать ли мышь (обычно `false`).
   - `mandatory`: Флаг, указывающий, является ли действие обязательным.
   - `timeout`: Время ожидания элемента (в секундах).
   - `timeout_for_event`: Условие ожидания (`presence_of_element_located` и т.д.).
   - `event`: Событие, которое нужно выполнить (`click()`, `screenshot()` и т.д.).
   - `locator_description`: Описание локатора (необязательно).
3.  **Взаимодействие с `executor`**:
    - `executor` принимает локатор и выполняет действия в следующем порядке:
       1. **Парсинг локатора**: Преобразует локатор в объект `SimpleNamespace` для удобства использования.
       2. **Поиск элемента**: Использует `by` и `selector` для поиска элемента.
       3. **Выполнение события**: Если указано `event`, выполняет соответствующее действие.
       4. **Извлечение атрибута**: Если указано `attribute`, извлекает значение атрибута.
       5. **Обработка ошибок**: Если элемент не найден и `mandatory` имеет значение `false`, продолжает выполнение, иначе вызывает ошибку.
4. **Примеры локаторов**:
    - **`close_banner`**: Закрывает баннер (всплывающее окно).
      -  Использует `XPATH` для поиска кнопки по `id`, выполняет `click()`. Если элемент не найден, выполнение продолжится.
    -  **`id_manufacturer`**: Возвращает значение атрибута (11290).
      - `by` установлен в `VALUE`, `executor` не ищет элемент, а возвращает значение `attribute`.
    - **`additional_images_urls`**: Извлекает URL дополнительных изображений.
      -  Использует `XPATH` для поиска элементов `img`, извлекает `src` атрибут. Если элемент не найден, выполнение продолжится.
    - **`default_image_url`**: Делает скриншот основного изображения.
      -  Использует `XPATH` для поиска элемента, выполняет `screenshot()`. Если элемент не найден, вызовет ошибку.
    -  **`id_supplier`**: Извлекает текст элемента SKU.
      -  Использует `XPATH` для поиска элемента, извлекает текст через `innerText`. Если элемент не найден, вызовет ошибку.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver.executor import ExecuteLocator
    import asyncio
    
    async def main():
        # Инициализация WebDriver
        driver = webdriver.Chrome()
    
        # Инициализация ExecuteLocator
        executor = ExecuteLocator(driver=driver)
    
        # Пример локатора для закрытия баннера
        close_banner_locator = {
          "attribute": None,
          "by": "XPATH",
          "selector": "//button[@id = \'closeXButton\']",
          "if_list": "first",
          "use_mouse": False,
          "mandatory": False,
          "timeout": 0,
          "timeout_for_event": "presence_of_element_located",
          "event": "click()",
          "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
        }
    
        # Выполнение локатора
        result = await executor.execute_locator(close_banner_locator)
        print(f"Результат выполнения close_banner: {result}")
        
    
        # Пример локатора для получения id_manufacturer
        id_manufacturer_locator = {
          "attribute": 11290,
          "by": "VALUE",
          "selector": None,
          "if_list": "first",
          "use_mouse": False,
          "mandatory": True,
          "timeout": 0,
          "timeout_for_event": "presence_of_element_located",
          "event": None,
          "locator_description": "id_manufacturer"
        }
        # Выполнение локатора
        result = await executor.execute_locator(id_manufacturer_locator)
        print(f"Результат выполнения id_manufacturer: {result}")
    
        # Закрытие WebDriver
        driver.quit()
        
    if __name__ == "__main__":
        asyncio.run(main())