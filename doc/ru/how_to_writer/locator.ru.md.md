Как использовать локаторы и их взаимодействие с `executor`
=========================================================================================

Описание
-------------------------
Локаторы — это объекты конфигурации, которые описывают, как найти и взаимодействовать с веб-элементами на странице. Они используются в классе `ExecuteLocator` для выполнения различных действий, таких как клики, ввод текста, извлечение атрибутов. Данная инструкция описывает структуру локаторов и их взаимодействие с `executor`.

Шаги выполнения
-------------------------
1. **Определение локатора**:
   - Локатор представляется в виде словаря (dict) или `SimpleNamespace` объекта, который содержит информацию о том, как найти веб-элемент и какое действие с ним выполнить.
2.  **Ключи локатора**:
    -  `attribute`: Атрибут, который нужно извлечь или установить (может быть `null`, строкой или числом).
    -  `by`: Метод поиска элемента (`XPATH`, `ID`, `VALUE` и т.д.).
    -  `selector`: Селектор для поиска элемента (например, строка XPath).
    -  `if_list`: Правило для обработки списка элементов (`first`, `last`, `all`, `even`, `odd` или индекс элемента).
    -  `use_mouse`: Флаг, указывающий, использовать ли мышь (обычно `false`).
    -  `mandatory`: Флаг, указывающий, является ли действие обязательным (`true` или `false`).
    -  `timeout`: Время ожидания элемента (в секундах, `0` - не ждать).
    -  `timeout_for_event`: Условие ожидания (`presence_of_element_located` и т.д.).
    -  `event`: Событие для выполнения (`click()`, `screenshot()`, `send_keys('text')` и т.д.).
    -  `locator_description`: Описание локатора (необязательно).
3.  **Взаимодействие с `executor`**:
    -  `executor` использует локаторы для выполнения действий в следующем порядке:
        1.  **Парсинг локатора**: Преобразует локатор в `SimpleNamespace`, если это необходимо.
        2.  **Поиск элемента**: Использует `by` и `selector` для поиска элемента на странице.
        3.  **Выполнение события**: Если указан `event`, выполняет соответствующее действие (например, клик).
        4.  **Извлечение атрибута**: Если указан `attribute`, извлекает значение атрибута.
        5.  **Обработка ошибок**: Если элемент не найден, и `mandatory` равно `false`, продолжает выполнение. Если `mandatory` равно `true`, вызывает исключение.
4. **Примеры локаторов**:
    -   **`close_banner`**: Закрытие всплывающего окна.
        - Использует `XPATH` для поиска кнопки по `id` и выполняет `click()`.
        - Необязательное действие.
    -   **`id_manufacturer`**: Возвращает значение атрибута `11290`.
        -  Использует `VALUE` в `by` и возвращает значение `attribute` без поиска элемента.
        - Обязательное действие.
    -   **`additional_images_urls`**: Извлекает URL-адреса дополнительных изображений.
        -  Использует `XPATH` для поиска элементов `img` и извлекает атрибут `src`.
        - Необязательное действие.
    -   **`default_image_url`**: Делает скриншот изображения.
        - Использует `XPATH` для поиска элемента и выполняет `screenshot()`.
        - Обязательное действие.
    -   **`id_supplier`**: Извлекает текст элемента, содержащего SKU.
        -  Использует `XPATH` для поиска элемента и извлекает текст через атрибут `innerText`.
        - Обязательное действие.

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
          "selector": "//button[@id = 'closeXButton']",
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

        # Пример локатора для получения текста элемента
        id_supplier_locator = {
            "attribute": "innerText",
            "by": "XPATH",
            "selector": "//span[@class = 'ltr sku-copy']",
            "if_list": "first",
            "use_mouse": False,
            "mandatory": True,
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "locator_description": "SKU morlevi"
        }

        # Выполнение локатора
        result = await executor.execute_locator(id_supplier_locator)
        print(f"Результат выполнения id_supplier: {result}")
    
        # Закрытие WebDriver
        driver.quit()
        
    if __name__ == "__main__":
        asyncio.run(main())