Как использовать модуль кастомного Edge WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию Edge WebDriver на основе Selenium. Он интегрирует настройки, определенные в файле `edge.json`, такие как user-agent и профиль браузера, для гибкого и автоматизированного взаимодействия с браузером Edge.

Шаги выполнения
-------------------------
1.  **Установка зависимостей:**
    -   Убедитесь, что установлены библиотеки `selenium` и `fake_useragent`.
    -  Если нет, выполните команду: `pip install selenium fake_useragent`.
    - Убедитесь, что бинарник `msedgedriver` доступен в вашей системе или указан в `edge.json`.
2.  **Настройка конфигурации (`edge.json`):**
    - Отредактируйте файл `edge.json` для настройки Edge WebDriver.
    -  Основные параметры:
       -  `options`: список опций для Edge (например, `--disable-dev-shm-usage`, `--headless`).
       -  `profiles`: пути к каталогам пользовательских профилей:
          -  `os`: для систем Windows.
           - `internal`: для профиля WebDriver.
       -   `executable_path`: путь к бинарнику msedgedriver.
        -   `headers`: пользовательские HTTP-заголовки (например, `User-Agent`, `Accept`).
       -   `proxy_enabled`: флаг для включения/выключения прокси.
3.  **Инициализация Edge WebDriver:**
     - Создайте экземпляр класса `Edge`, передав необходимые параметры.
     -  Пример:
         ```python
         from src.webdriver.edge import Edge
    
         browser = Edge(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            options=["--headless", "--disable-gpu"]
        )
         ```
     -  Параметры:
        -  `profile_name` (str, optional): имя пользовательского профиля Edge.
        -   `user_agent` (str, optional): пользовательский агент. Если не указан, будет сгенерирован случайный.
         -  `options` (list, optional): список опций для Edge.
        -  `window_mode` (str, optional): режим окна браузера ('windowless', 'kiosk', 'full_window').
    -  Класс `Edge` автоматически загружает настройки из файла `edge.json`.
4. **Управление режимом окна:**
    - Установите режим окна браузера, используя параметр `window_mode`:
        -  `kiosk`: полноэкранный режим без элементов интерфейса.
        -   `windowless`: безголовый режим.
        -  `full_window`: обычное окно в полноэкранном режиме.
5. **Использование WebDriver:**
    - Используйте методы Selenium WebDriver для навигации и взаимодействия со страницей.
    -   Примеры:
         -  `browser.get(url)`: Загружает URL.
         -   `browser.find_element(By.ID, 'element_id')`: Находит элемент.
         -   `browser.execute_script('...')`: Выполняет JavaScript.
          -  `browser.get_url(url)`: загружает URL, сохраняя куки и предыдущую ссылку (из `src.webdriver.driver.Driver`).
          -  `browser.scroll(scrolls=2, direction='down')`: прокрутка страницы (из `src.webdriver.driver.Driver`).
6.  **Работа с `ExecuteLocator` и `JavaScript`:**
    -   Класс `Edge` автоматически инициализирует `ExecuteLocator` и `JavaScript`.
    -  Вызывайте методы, такие как `execute_locator`, `get_attribute_by_locator`, `send_message` напрямую из объекта класса `Edge`.
7.  **Логирование:**
    -  Модуль использует `logger` для записи ошибок и предупреждений.
    -   Отслеживайте логи для отладки.
8. **Паттерн Singleton:**
    - Класс `Edge` использует паттерн Singleton, что гарантирует создание только одного экземпляра WebDriver.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.edge import Edge
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs
    
    async def main():
       # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'edge' / 'edge.json'))
        
        # Инициализация Edge WebDriver
        driver = Edge(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
            window_mode='full_window'
        )
    
        if driver.get_url("https://www.example.com"):
            print("Успешно перешли по URL")
        
         # Поиск элемента
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
            print(f'Заголовок страницы: {element.text}')
    
        # Использование execute_locator для клика
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Результат execute_locator (click): {result}")
    
        # Пример использования execute_locator для получения атрибута
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        text = await driver.get_attribute_by_locator(locator)
        if text:
           print(f"Извлеченный текст: {text}")

        # Закрытие браузера
        driver.quit()
    
    if __name__ == "__main__":
        asyncio.run(main())