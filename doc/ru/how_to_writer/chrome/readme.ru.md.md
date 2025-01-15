Как использовать модуль кастомной реализации Chrome WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль предоставляет класс `Chrome`, который является кастомной реализацией Chrome WebDriver на основе Selenium. Он позволяет настраивать браузер Chrome с помощью параметров, заданных в файле `chrome.json`, включая user-agent, профили и другие опции.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   - Убедитесь, что установлены библиотеки `selenium` и `fake_useragent`.
   - Если нет, выполните команду: `pip install selenium fake_useragent`.
   - Убедитесь, что `chromedriver` доступен в системе (путь должен быть указан в `chrome.json`).
2. **Настройка конфигурации:**
   - Отредактируйте файл `chrome.json` для настройки параметров Chrome WebDriver.
   - Параметры:
     - `options`: словарь параметров Chrome для изменения поведения браузера:
       -  `log-level`: уровень логирования.
       -  `disable-dev-shm-usage`: отключение `/dev/shm` в Docker.
       - `remote-debugging-port`: порт для отладки.
       - `arguments`: список аргументов Chrome (например, `"--kiosk"`, `"--headless"`).
     -  `disabled_options`: список опций, которые нужно отключить, например,  `"headless": ""` чтобы браузер запускался в обычном режиме.
     -  `profile_directory`: пути к каталогам профилей пользователя: `os` - для систем Windows, `internal` - внутренний путь WebDriver.
     -   `binary_location`: пути к исполняемым файлам Chrome, драйвера и Chromium: `os`, `exe`, `binary`, `chromium`.
     -   `headers`: пользовательские HTTP заголовки (`User-Agent`, `Accept` и т.д.).
     -  `proxy_enabled`: флаг, указывающий на использование прокси.
3. **Инициализация WebDriver:**
   - Создайте экземпляр класса `Chrome`, передав необходимые параметры или используя дефолтные значения из `chrome.json`.
   - Пример:
      ```python
      from src.webdriver.chrome import Chrome
      
      browser = Chrome(
          user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
           options=["--headless", "--disable-gpu"]
      )
      ```
    -  Параметры:
       -   `profile_name` (str, optional): имя пользовательского профиля Chrome.
        - `chromedriver_version` (str, optional): версия ChromeDriver.
       -   `user_agent` (str, optional): пользовательский агент. Если не указан, будет сгенерирован случайный.
       -   `proxy_file_path` (str, optional): путь к файлу с прокси.
       -   `options` (list, optional): список опций для Chrome.
       -   `window_mode` (str, optional): режим окна ('windowless', 'kiosk', 'full_window').
4.  **Использование WebDriver:**
    -  Используйте методы Selenium WebDriver для навигации и взаимодействия со страницей.
    -  Пример:
       ```python
        browser.get("https://www.example.com")
        browser.quit()
        ```
5.  **Управление прокси:**
    -  Если `proxy_enabled` установлен в `true` в `chrome.json`, будет автоматически выбран рабочий прокси из файла.
6.  **Управление режимом окна:**
    -  Используйте параметр `window_mode` при инициализации:
       - `kiosk`: полноэкранный режим без элементов интерфейса.
       - `windowless`: безголовый режим.
       -  `full_window`: окно на весь экран.
7.  **Логирование:**
    - Модуль использует `logger` для логирования ошибок и предупреждений. Проверяйте логи для отладки.
8.  **Использование `ExecuteLocator` и `JavaScript`:**
    - Класс `Chrome` инициализирует `ExecuteLocator` и `JavaScript` и предоставляет их методы через экземпляр класса.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.chrome import Chrome
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs

    async def main():
        # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'chrome' / 'chrome.json'))

        # Инициализация Chrome WebDriver
        driver = Chrome(
           #chromedriver_version='111',
            #profile_name='my_profile',
           # user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
           #proxy_file_path='path/to/proxy.txt',
            #options=['--headless', '--disable-gpu'],
            window_mode='full_window'
        )
        if driver.get_url("https://www.example.com"):
           print("Успешно перешли по URL")

        # Поиск заголовка страницы
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')

         # Использование ExecuteLocator для клика
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Результат execute_locator (click): {result}")

        # Пример использования get_attribute_by_locator
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        text = await driver.get_attribute_by_locator(locator)
        if text:
           print(f"Извлеченный текст: {text}")

        # Закрытие браузера
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())