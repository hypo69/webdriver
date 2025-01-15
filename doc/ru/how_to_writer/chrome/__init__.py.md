Как использовать модуль `src.webdriver.chrome`
=========================================================================================

Описание
-------------------------
Модуль `__init__.py` в директории `src.webdriver.chrome` предназначен для импорта и экспорта класса `Chrome` из модуля `chrome.py`. Это позволяет упростить импорт класса `Chrome` в другие части проекта, предоставляя прямой доступ к нему из пакета `src.webdriver.chrome`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте класс `Chrome` из пакета `src.webdriver.chrome`.
   - Пример: `from src.webdriver.chrome import Chrome`.
   - Благодаря файлу `__init__.py` импорт класса `Chrome` становится проще, так как нет необходимости указывать путь к файлу `chrome.py`.
2.  **Использование класса `Chrome`:**
   - После импорта класса `Chrome` вы можете создать экземпляр кастомного Chrome WebDriver.
   -  Пример:
        ```python
        from src.webdriver.chrome import Chrome

        driver = Chrome(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            options=["--headless", "--disable-gpu"]
        )
        ```
   - Далее вы можете использовать методы объекта `driver` для взаимодействия с веб-страницами, навигации, извлечения элементов и т.д.
3.  **Преимущества:**
    -   Упрощает импорт: позволяет импортировать класс, не указывая путь к файлу `chrome.py`.
    -  Улучшает структуру: обеспечивает более чистый и организованный код, делая использование класса более наглядным.
    -   Упрощает рефакторинг: изменения в структуре пакета могут быть сделаны без изменения кода, импортирующего класс `Chrome`.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.chrome import Chrome
    from selenium.webdriver.common.by import By
    import asyncio
    
    async def main():
        # Создание экземпляра Chrome WebDriver
        driver = Chrome(
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