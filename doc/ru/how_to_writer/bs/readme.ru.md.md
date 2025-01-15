Как использовать модуль парсера BeautifulSoup и XPath
=========================================================================================

Описание
-------------------------
Модуль предоставляет класс `BS` для парсинга HTML-контента с использованием библиотек BeautifulSoup и lxml (для XPath). Он позволяет загружать HTML из файлов или URL-адресов, парсить его и извлекать элементы с помощью XPath-локаторов.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   - Убедитесь, что установлены библиотеки `beautifulsoup4`, `lxml` и `requests`.
   - Если они не установлены, выполните команду: `pip install beautifulsoup4 lxml requests`.
2. **Настройка конфигурации:**
   -  Настройте параметры парсера в файле `bs.json`.
   -   Основные параметры конфигурации:
       -   `default_url`: URL для загрузки HTML-контента по умолчанию.
       -   `default_file_path`: путь к файлу для загрузки HTML-контента по умолчанию.
       -   `default_locator`: локатор по умолчанию для извлечения элементов:
           -  `by`: метод поиска элемента (`ID`, `CSS`, `TEXT`, `XPATH`).
           -  `attribute`: атрибут для поиска.
           - `selector`: XPath-селектор.
       -   `logging`: настройки логирования (`level` - уровень логирования, `file` - путь к файлу).
       -  `proxy`: настройки прокси (`enabled`, `server`, `username`, `password`).
       -   `timeout`: таймаут для запросов (в секундах).
       -   `encoding`: кодировка.
3.  **Инициализация парсера:**
    -  Создайте экземпляр класса `BS`, указав (опционально) URL для загрузки HTML.
    - Пример:
        ```python
        from src.webdriver.bs import BS
        from src.utils.jjson import j_loads_ns
        from pathlib import Path
    
        settings_path = Path('path/to/bs.json') # Укажите правильный путь к файлу
        settings = j_loads_ns(settings_path)
    
        parser = BS(url=settings.default_url)
        ```
       - Или без URL: `parser = BS()`.
4. **Загрузка HTML:**
    -   Используйте метод `get_url(url)` для загрузки HTML-контента.
    -   Примеры:
        -  `parser.get_url('https://example.com')` для загрузки HTML с веб-страницы.
        -   `parser.get_url('file://path/to/your/file.html')` для загрузки HTML из локального файла.
    -   Метод возвращает `True`, если загрузка успешна, `False` — в противном случае.
5. **Извлечение элементов:**
   -  Создайте объект локатора (`SimpleNamespace` или `dict`).
   -  Определите тип локатора `by`, атрибут `attribute` и XPath-селектор `selector`.
   -  Используйте метод `execute_locator(locator)` для извлечения элементов из HTML.
   -   Пример:
       ```python
        from types import SimpleNamespace
    
        locator = SimpleNamespace(
            by='ID',
            attribute='element_id',
            selector='//*[@id="element_id"]'
        )
        elements = parser.execute_locator(locator)
       ```
    -   Метод возвращает список найденных элементов.
6.  **Обработка результатов:**
    - Проверьте, что список найденных элементов не пуст.
    - Итерируйте по списку, извлекая нужную информацию (текст, атрибуты).
7. **Логирование:**
    -  Модуль использует `logger` для логирования ошибок и сообщений.
    - Настройте уровень логирования и путь к файлу в `bs.json`.
    - Просматривайте логи для отладки и отслеживания проблем.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.bs import BS
    from types import SimpleNamespace
    from src.utils.jjson import j_loads_ns
    from pathlib import Path

    # Путь к файлу конфигурации
    settings_path = Path('src/webdriver/bs/bs.json')
    settings = j_loads_ns(settings_path)

    # Инициализация парсера
    parser = BS(url = settings.default_url)

    # Локатор для поиска по ID
    locator_id = SimpleNamespace(
        by='ID',
        attribute='element_id',
        selector='//*[@id="element_id"]'
    )

    elements = parser.execute_locator(locator_id)
    if elements:
        print("Найдено элементов по ID:")
        for element in elements:
            print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены по ID.")

    # Локатор для поиска по CSS классу
    locator_css = SimpleNamespace(
        by='CSS',
        attribute='class_name',
        selector='//*[contains(@class, "class_name")]'
    )
    elements_css = parser.execute_locator(locator_css)

    if elements_css:
        print("Найдено элементов по CSS:")
        for element in elements_css:
           print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены по CSS.")
    
    # Локатор для поиска текстового поля
    locator_text = SimpleNamespace(
        by='TEXT',
        attribute='text',
        selector='//input[@type="text"]'
    )
    elements_text = parser.execute_locator(locator_text)
    
    if elements_text:
        print("Найдено текстовых полей:")
        for element in elements_text:
             print(element.text if hasattr(element, 'text') else element)
    else:
        print("Текстовые поля не найдены.")

    # Пример с локальным файлом
    parser.get_url('file://src/webdriver/bs/example.html') # замените на корректный путь
    elements_file = parser.execute_locator(locator_id)
    if elements_file:
       print("Найдено элементов по ID (из файла):")
       for element in elements_file:
            print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены (из файла).")