Как использовать модуль `src.webdriver.bs`
=========================================================================================

Описание
-------------------------
Модуль `src.webdriver.bs` предоставляет класс `BS` для парсинга HTML-контента с использованием библиотек BeautifulSoup и XPath. Модуль позволяет загружать HTML как из локальных файлов, так и по URL, а также извлекать элементы по XPath.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
    - Убедитесь, что у вас установлены необходимые библиотеки: `beautifulsoup4`, `lxml`, `requests`.
    - Установите их с помощью `pip install beautifulsoup4 lxml requests`.
2.  **Настройка конфигурации:**
    -   Настройте параметры парсера в файле `bs.json`.
    -   Основные параметры:
        -   `default_url`: URL по умолчанию для загрузки HTML.
        -  `default_file_path`: путь к локальному файлу HTML.
        - `default_locator`: локатор по умолчанию для извлечения элементов:
            -  `by`: тип локатора (ID, CSS, TEXT).
            - `attribute`: атрибут для поиска (например, id).
            -   `selector`: XPath селектор.
        - `logging`: настройки логирования.
        -  `proxy`: настройки прокси.
        - `timeout`: таймаут для запросов (в секундах).
        -   `encoding`: кодировка для чтения файлов или запросов.
3. **Инициализация класса `BS`:**
   - Создайте экземпляр класса `BS` без параметров для использования дефолтных настроек из `bs.json`, или с параметром URL для немедленной загрузки HTML.
   - Пример:
      ```python
      from src.webdriver.bs import BS
      from src.utils.jjson import j_loads_ns
      from pathlib import Path
      
      settings_path = Path('path/to/bs.json') # Укажите свой путь к bs.json
      settings = j_loads_ns(settings_path)
    
      parser = BS(url=settings.default_url)
      ```
   -  Или без URL: `parser = BS()`.
4.  **Загрузка HTML-контента:**
    -   Используйте метод `get_url(url)` для загрузки HTML-контента из файла или URL.
    - Пример: `parser.get_url('https://example.com')` или `parser.get_url('file://path/to/local.html')`.
    - Метод обрабатывает протоколы `file://` и `https://`.
    -  HTML-код сохраняется в атрибуте `html_content` экземпляра класса `BS`.
    -   Метод возвращает `True` при успешной загрузке, `False` в противном случае.
5.  **Выполнение локатора:**
    -   Создайте локатор, используя `SimpleNamespace` или `dict`.
        -   `by`: метод поиска (ID, CSS, TEXT, XPATH).
        -  `attribute`: атрибут для поиска.
        -   `selector`: XPath селектор.
    -  Используйте метод `execute_locator(locator, url)` для выполнения XPath запроса.
    -  Пример:
        ```python
        from types import SimpleNamespace
        locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
        elements = parser.execute_locator(locator)
        ```
    - `url` - необязательный параметр, используйте если нужно переопределить URL.
    - Метод возвращает список элементов, соответствующих XPath.
6.  **Обработка результатов:**
    -   Проверьте, что список элементов не пустой.
    -   Итерируйте по списку, извлекая нужную информацию (текст, атрибуты).
    -   Пример:
         ```python
         if elements:
             for element in elements:
                 print(element.text)
         ```
7.  **Логирование:**
    -   Модуль использует `logger` для логирования ошибок, предупреждений и информационных сообщений.
    -   Логи записываются в файл, указанный в настройках (`bs.json`).

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

    # Создание экземпляра парсера с настройками по умолчанию
    parser = BS(url=settings.default_url)
    
    # Создание локатора для поиска элемента по ID
    locator_id = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
    elements_id = parser.execute_locator(locator_id)
    
    if elements_id:
        print("Найдено элементов (ID):")
        for element in elements_id:
           print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены (ID).")
        
    # Создание локатора для поиска элемента по CSS классу
    locator_css = SimpleNamespace(by='CSS', attribute='example-class', selector='//*[contains(@class, "example-class")]')
    elements_css = parser.execute_locator(locator_css)

    if elements_css:
        print("Найдено элементов (CSS):")
        for element in elements_css:
           print(element.text if hasattr(element, 'text') else element)
    else:
       print("Элементы не найдены (CSS).")
    
    # Создание локатора для поиска текстового поля
    locator_text = SimpleNamespace(by='TEXT', attribute='text', selector='//input[@type="text"]')
    elements_text = parser.execute_locator(locator_text)
    if elements_text:
        print("Найдено текстовых полей:")
        for element in elements_text:
            print(element.text if hasattr(element, 'text') else element)
    else:
        print("Текстовые поля не найдены.")
    
    # Пример загрузки HTML из файла
    parser.get_url('file://src/webdriver/bs/example.html') # замените на корректный путь
    elements_file = parser.execute_locator(locator_id)
    
    if elements_file:
       print("Найдено элементов (из файла):")
       for element in elements_file:
            print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены (из файла).")