Как использовать модуль `src.webdriver.playwright`
=========================================================================================

Описание
-------------------------
Модуль `__init__.py` в директории `src.webdriver.playwright` служит для импорта и экспорта класса `Playwrid` из модуля `playwrid.py`. Это позволяет упростить импорт класса `Playwrid` в другие части проекта, предоставляя прямой доступ к нему из пакета `src.webdriver.playwright`.

Шаги выполнения
-------------------------
1.  **Импорт модуля:**
    - Импортируйте класс `Playwrid` из пакета `src.webdriver.playwright`.
    - Пример: `from src.webdriver.playwright import Playwrid`.
    - Благодаря файлу `__init__.py` импорт класса `Playwrid` становится проще, так как нет необходимости указывать путь к файлу `playwrid.py`.
2.  **Использование класса `Playwrid`:**
    -  После импорта класса `Playwrid` вы можете создать экземпляр кастомного Playwright краулера.
    -  Пример:
         ```python
         from src.webdriver.playwright import Playwrid
         import asyncio

         async def main():
              browser = Playwrid(options=["--headless"])
              # ...
         ```
    - Далее вы можете использовать методы объекта `browser` для настройки и запуска краулинга, как описано в инструкции к модулю `playwrid.py`.
3. **Преимущества:**
   -  Упрощает импорт: позволяет импортировать класс, не указывая путь к файлу `playwrid.py`.
    -   Улучшает структуру: обеспечивает более чистый и организованный код.
   - Облегчает рефакторинг: изменения в структуре пакета не повлияют на код, импортирующий класс `Playwrid`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.playwright import Playwrid
    
    async def main():
       # Инициализация краулера
        browser = Playwrid(
             options=["--headless"]
        )

       # Запуск краулера и навигация
        await browser.start("https://www.example.com")
    
        # Получение HTML контента
        html_content = browser.get_page_content()
        if html_content:
            print(f'Первые 100 символов контента: {html_content[:100]}...')
        else:
            print("Не удалось получить HTML контент.")
   
    if __name__ == "__main__":
        asyncio.run(main())