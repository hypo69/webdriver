Как использовать модуль `src.webdriver.edge`
=========================================================================================

Описание
-------------------------
Модуль `__init__.py` в директории `src.webdriver.edge` служит для импорта и экспорта класса `Edge` из модуля `edge.py`. Это позволяет упростить импорт класса `Edge` в другие части проекта, предоставляя прямой доступ к нему из пакета `src.webdriver.edge`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте класс `Edge` из пакета `src.webdriver.edge`.
   - Пример: `from src.webdriver.edge import Edge`.
   - Благодаря файлу `__init__.py` импорт класса `Edge` становится проще, так как нет необходимости указывать путь к файлу `edge.py`.
2.  **Использование класса `Edge`:**
    - После импорта класса `Edge` вы можете создать экземпляр кастомного Edge WebDriver.
    -  Пример:
        ```python
        from src.webdriver.edge import Edge
        
        driver = Edge(
           user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
             options=["--headless", "--disable-gpu"]
        )
        # ... дальнейшие действия с драйвером
        ```
    - Далее вы можете использовать методы объекта `driver` для взаимодействия с веб-страницами, навигации, извлечения элементов и т.д.
3. **Преимущества:**
   -  Упрощает импорт: позволяет импортировать класс, не указывая путь к файлу `edge.py`.
    - Улучшает структуру: делает код более организованным и читаемым.
    -  Упрощает рефакторинг: изменения в структуре пакета не повлияют на код, импортирующий `Edge`.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.edge import Edge
    from selenium.webdriver.common.by import By
    import asyncio
    
    async def main():
        # Создание экземпляра Edge WebDriver
        driver = Edge(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
             options=["--headless", "--disable-gpu"],
             window_mode='full_window'
        )
    
        # Навигация по URL
        if driver.get_url("https://www.example.com"):
           print("Успешно перешли по URL")
        
        # Поиск элемента
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')

        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())
```