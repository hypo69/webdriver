Как использовать модуль кастомного Chrome WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию Chrome WebDriver на основе Selenium. Он интегрирует настройки из файла `chrome.json`, такие как user-agent и профили браузера, для гибкого и автоматизированного взаимодействия с браузером.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
    - Убедитесь, что установлены библиотеки `selenium` и `fake_useragent`.
    - Если они не установлены, выполните команду: `pip install selenium fake_useragent`.
2. **Настройка `chrome.json`:**
   - Отредактируйте файл `chrome.json`, чтобы настроить параметры Chrome WebDriver.
   - Основные параметры:
     -   `options`: словарь с параметрами Chrome для изменения поведения браузера:
           - `log-level`: уровень логирования.
           - `disable-dev-shm-usage`: отключение `/dev/shm` (для Docker).
           -  `remote-debugging-port`: порт для удаленной отладки.
           - `arguments`: список аргументов командной строки Chrome (например, `--kiosk`, `--headless`).
      -   `disabled_options`: опции, которые нужно отключить.
      -  `profile_directory`: пути к каталогам профилей пользователя Chrome (для разных окружений).
      -   `binary_location`: пути к исполняемым файлам Chrome и драйвера.
      -   `headers`: пользовательские HTTP-заголовки.
      -   `proxy_enabled`: флаг, указывающий на использование прокси.
3.  **Инициализация Chrome WebDriver:**
    - Создайте экземпляр класса `Chrome`, передав необходимые параметры или используя настройки из `chrome.json`.
    - Пример:
        ```python
        from src.webdriver.chrome import Chrome

        browser = Chrome(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            options=["--headless", "--disable-gpu"]
        )
        ```
    - Класс автоматически загружает настройки из файла `chrome.json`.
    - Параметры:
        - `profile_name` (str, optional): Имя пользовательского профиля Chrome.
        - `chromedriver_version` (str, optional): Версия chromedriver.
        - `user_agent` (str, optional): Пользовательский агент.
        - `proxy_file_path` (str, optional): Путь к файлу с прокси.
        - `options` (list, optional): Список опций Chrome.
        - `window_mode` (str, optional): Режим окна ('windowless', 'kiosk', 'full_window').
4.  **Использование WebDriver:**
    - Используйте методы Selenium WebDriver для навигации и взаимодействия со страницей.
    - Пример:
         ```python
         browser.get("https://www.example.com")
         browser.quit()
         ```
   -   Класс `Chrome` предоставляет методы для управления окном, прокрутки, загрузки URL, и доступа к элементам.
5.  **Настройка прокси:**
    - Если в `chrome.json` установлено `proxy_enabled = true`, то будет использован рабочий прокси из списка, полученного функцией `get_proxies_dict`.
    -   Используется первый рабочий прокси из списка.
6. **Управление режимом окна:**
   -  Установите режим окна с помощью параметра `window_mode` (kiosk, windowless, full_window).
   - `kiosk`: полноэкранный режим без элементов интерфейса.
    -  `windowless`: безголовый режим (Chrome работает в фоновом режиме).
    -   `full_window`: окно на весь экран.
7.  **Работа с `ExecuteLocator` и `JavaScript`:**
   - Класс `Chrome` автоматически инициализирует `ExecuteLocator` и `JavaScript`.
   - Вызывайте методы `execute_locator`, `get_attribute_by_locator` и другие напрямую из объекта класса `Chrome`.
8. **Логирование:**
    -  Модуль использует `logger` для логирования ошибок и сообщений.
    -  Проверяйте логи для отладки.

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

        # Создание экземпляра Chrome Driver с настройками из файла
        driver = Chrome(
             window_mode='full_window'
        )
        if driver.get_url("https://www.example.com"):
            print("Успешно перешли по URL")

        # Получение заголовка страницы
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')

         # Пример использования ExecuteLocator для клика
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Result of execute_locator click: {result}")

        # Пример использования execute_locator для получения атрибута
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        text = await driver.get_attribute_by_locator(locator)
        if text:
            print(f"Извлеченный текст: {text}")

        # Закрытие браузера
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())