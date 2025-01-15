Как использовать модуль `src.webdriver.firefox`
=========================================================================================

Описание
-------------------------
Модуль `__init__.py` в директории `src.webdriver.firefox` предназначен для импорта и экспорта класса `Firefox` из модуля `firefox.py`. Это упрощает доступ к классу `Firefox` из других частей проекта, позволяя импортировать его напрямую из пакета `src.webdriver.firefox`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте класс `Firefox` из пакета `src.webdriver.firefox`.
   -  Пример: `from src.webdriver.firefox import Firefox`.
   -  Благодаря файлу `__init__.py` импорт класса `Firefox` становится проще, так как нет необходимости указывать путь к файлу `firefox.py`.
2. **Использование класса `Firefox`:**
   -  После импорта класса `Firefox` вы можете создать экземпляр кастомного Firefox WebDriver.
   -  Пример:
       ```python
        from src.webdriver.firefox import Firefox
        
        driver = Firefox(
            profile_name='custom_profile',
            options=['--headless']
        )
       # ... дальнейшие действия с драйвером
       ```
   -   Используйте методы объекта `driver` для управления браузером, навигации, взаимодействия с элементами и т.д.
3.  **Преимущества:**
    - Упрощение импорта: позволяет импортировать класс, не указывая полный путь к файлу `firefox.py`.
    -  Улучшение структуры кода: делает код более организованным и легким для чтения.
    -  Облегчение рефакторинга: изменения в структуре пакета не повлияют на код, импортирующий класс `Firefox`.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.firefox import Firefox
    from selenium.webdriver.common.by import By
    import asyncio
    
    async def main():
         # Создание экземпляра Firefox WebDriver
        driver = Firefox(
           profile_name='custom_profile',
            options=['--headless'],
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