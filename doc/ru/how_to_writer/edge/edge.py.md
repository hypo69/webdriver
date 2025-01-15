Как использовать модуль кастомного Edge WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль `edge.py` предоставляет кастомный класс `Edge`, расширяющий возможности стандартного `webdriver.Edge` из Selenium. Он позволяет гибко настраивать Edge WebDriver, включая user-agent, профиль браузера и другие параметры, используя файл `edge.json`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   -  Импортируйте класс `Edge` из модуля `src.webdriver.edge.edge`.
   - Пример: `from src.webdriver.edge.edge import Edge`.
2.  **Инициализация WebDriver:**
   -  Создайте экземпляр класса `Edge`, передав необходимые параметры.
   - Пример:
       ```python
       from src.webdriver.edge.edge import Edge
    
       driver = Edge(
           profile_name='my_profile',
           user_agent='Mozilla/5.0...',
           options=['--headless', '--disable-gpu'],
           window_mode='kiosk'
       )
       ```
    - Параметры:
       -   `profile_name` (str, optional): Имя пользовательского профиля Edge.
       -  `user_agent` (str, optional): Пользовательский агент. Если не указан, будет сгенерирован случайный.
       -  `options` (list, optional): Список опций для Edge (например, `--headless`).
       - `window_mode` (str, optional): Режим окна браузера ('windowless', 'kiosk', 'full_window').
    -  Если параметры не переданы, будут использованы значения из файла `edge.json`.
3.  **Настройка профиля пользователя:**
    - Если передан `profile_name`, то используется путь к пользовательскому профилю.
    -  Если в пути профиля встречается переменная окружения `%LOCALAPPDATA%`, то она заменяется на фактический путь.
4. **Настройка режима окна:**
   - Установите режим окна браузера, используя параметр `window_mode`.
   -  Возможные значения:
        -  `kiosk`: полноэкранный режим без интерфейса.
       -  `windowless`: безголовый режим (запуск браузера без видимого окна).
       - `full_window`: обычное окно в полноэкранном режиме.
5.  **Использование WebDriver:**
    - После создания экземпляра класса `Edge` используйте методы Selenium WebDriver.
    -   Примеры:
         - `driver.get(url)`: Загружает URL.
         -   `driver.find_element(By.ID, 'element_id')`: Находит элемент.
        -  `driver.execute_script('...')`: Выполняет JavaScript.
        -  `driver.get_url(url)`: загружает URL, сохраняя куки и предыдущую ссылку (из `src.webdriver.driver.Driver`).
       -  `driver.scroll(scrolls=2, direction='down')`: прокрутка страницы (из `src.webdriver.driver.Driver`).
6.  **Использование `ExecuteLocator` и `JavaScript`:**
    -  Класс `Edge` автоматически инициализирует `ExecuteLocator` и `JavaScript`, предоставляя доступ к их методам через экземпляр класса.
    -   Примеры:
         - `driver.execute_locator(locator)`: выполняет действия с элементом на основе локатора.
        -  `driver.get_webelement_by_locator(locator)`: получает элемент по локатору.
        -   `driver.get_attribute_by_locator(locator)`: получает атрибут элемента по локатору.
       -   `driver.send_message(locator, message)`: отправляет текст элементу.
        -   `driver.get_page_lang()`: возвращает язык страницы.
        - `driver.ready_state`: возвращает статус загрузки страницы.
        -  `driver.unhide_DOM_element(element)`: делает элемент видимым.
        -   `driver.window_focus()`: устанавливает фокус на окно браузера.
7.  **Обработка ошибок:**
    - Модуль логирует ошибки и предупреждения через `logger`.
    -  Отслеживайте логи для поиска ошибок инициализации или работы WebDriver.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.edge.edge import Edge
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

        # Получение заголовка страницы
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')
    
        # Пример с execute_locator для клика
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Результат execute_locator (click): {result}")
    
        # Пример с execute_locator для получения атрибута
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        text = await driver.get_attribute_by_locator(locator)
        if text:
            print(f"Извлеченный текст: {text}")

        # Закрытие браузера
        driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())