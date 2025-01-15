Как использовать модуль `src.webdriver.driver`
=========================================================================================

Описание
-------------------------
Модуль `src.webdriver.driver` предоставляет класс `Driver` для взаимодействия с веб-драйверами Selenium. Класс `Driver` обеспечивает унифицированный интерфейс для инициализации драйвера, навигации по URL, прокрутки страницы, определения языка, управления куки и загрузки HTML-контента.

Шаги выполнения
-------------------------
1. **Инициализация драйвера:**
   - Создайте экземпляр класса `Driver`, передав класс веб-драйвера (например, `Chrome`, `Firefox`) и необходимые аргументы.
   - Пример: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
   - Конструктор проверяет, что переданный `webdriver_cls` имеет метод `get`, и создает экземпляр драйвера.
2. **Инициализация подкласса:**
   - При создании подкласса `Driver`, укажите аргумент `browser_name`.
   - Пример: `class CustomDriver(Driver, browser_name='Chrome'): ...`
   - Метод `__init_subclass__` автоматически сохраняет имя браузера в атрибуте `browser_name`.
3. **Доступ к атрибутам драйвера:**
   - Для доступа к атрибутам веб-драйвера используйте атрибуты экземпляра `Driver`.
   - Пример: `driver.current_url` (обращается к `self.driver.current_url`).
   - Метод `__getattr__` перенаправляет запросы к соответствующим атрибутам драйвера.
4. **Прокрутка страницы:**
   - Используйте метод `scroll(scrolls, frame_size, direction, delay)` для прокрутки страницы в заданном направлении.
   - Пример: `driver.scroll(scrolls=3, direction='down', delay=0.5)`.
   - Параметр `scrolls` определяет количество прокруток, `frame_size` - размер прокрутки, `direction` - направление ('forward', 'down', 'backward', 'up', 'both'), `delay` - задержка между прокрутками.
5. **Определение языка страницы:**
   - Получите язык страницы, используя свойство `locale`.
   - Пример: `language = driver.locale`.
   - Свойство пытается определить язык из мета-тега `Content-Language` или с помощью JavaScript (если метод `get_page_lang` реализован).
6. **Навигация по URL:**
   - Используйте метод `get_url(url)` для перехода по указанному URL.
   - Пример: `driver.get_url('https://example.com')`.
   - Метод сохраняет предыдущий URL, ждет загрузки страницы, сохраняет куки и обрабатывает исключения.
7. **Открытие новой вкладки:**
   - Используйте метод `window_open(url)` для открытия новой вкладки и перехода по указанному URL (необязательно).
   - Пример: `driver.window_open('https://newtab.com')`.
8. **Ожидание:**
   - Используйте метод `wait(delay)` для приостановки выполнения на заданное время.
   - Пример: `driver.wait(1)`.
9. **Сохранение куки:**
   - Используйте метод `_save_cookies_localy()` для сохранения куки в локальный файл.
   - Пример: `driver._save_cookies_localy()`.
   - В текущей версии возвращает `True` для отладки. Необходимо использовать `pickle.dump()` для сохранения куки в файл.
10. **Загрузка HTML-контента:**
   - Используйте метод `fetch_html(url)` для загрузки HTML-контента из файла или по URL.
   - Пример: `driver.fetch_html('file:///path/to/local.html')` или `driver.fetch_html('https://example.com')`.
   - Метод поддерживает протоколы `file://`, `http://` и `https://`.

Пример использования
-------------------------
.. code-block:: python

    from selenium.webdriver import Chrome
    from src.webdriver.driver import Driver

    # Инициализация драйвера Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    
    # Переход по URL
    driver.get_url('https://example.com')
    
    # Прокрутка страницы вниз 2 раза с задержкой
    driver.scroll(scrolls=2, direction='down', delay=0.5)
    
    # Получение языка страницы
    language = driver.locale
    print(f"Язык страницы: {language}")

    # Открытие новой вкладки
    driver.window_open('https://newtab.com')
    
    # Получение HTML контента
    if driver.fetch_html('https://example.com'):
        print(f'HTML content: {driver.html_content[:100]}...')

    # Получение заголовка страницы
    print(f'Заголовок страницы: {driver.title}')

    # Ожидание 1 секунду
    driver.wait(1)

    # Закрытие драйвера
    driver.quit()