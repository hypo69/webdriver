# Документация модуля `src.webdriver.crawlee_python`

## Обзор

Этот модуль предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные из веб-страниц.

## Оглавление

-   [Обзор](#обзор)
-   [Класс `CrawleePython`](#класс-crawleepython)
    -   [`__init__`](#__init__)
    -   [`setup_crawler`](#setup_crawler)
    -   [`run_crawler`](#run_crawler)
    -   [`export_data`](#export_data)
    -   [`get_data`](#get_data)
    -   [`run`](#run)
-   [Пример использования](#пример-использования)

## Класс `CrawleePython`

### Описание

Класс `CrawleePython` представляет собой пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Атрибуты:**

-   `max_requests` (int): Максимальное количество запросов для выполнения во время сканирования.
-   `headless` (bool): Определяет, запускать ли браузер в безголовом режиме.
-   `browser_type` (str): Тип браузера для использования (`'chromium'`, `'firefox'`, `'webkit'`).
-   `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.

### `__init__`

```python
    def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
        """
        Initializes the CrawleePython crawler with the specified parameters.

        :param max_requests: Maximum number of requests to perform during the crawl.
        :type max_requests: int
        :param headless: Whether to run the browser in headless mode.
        :type headless: bool
        :param browser_type: The type of browser to use ('chromium', 'firefox', 'webkit').
        :type browser_type: str
        :param options: A list of custom options to pass to the browser.
        :type options: Optional[List[str]]
        """
        self.max_requests = max_requests
        self.headless = headless
        self.browser_type = browser_type
        self.options = options or []
        self.crawler = None
```

**Описание**: Инициализирует сканер `CrawleePython` с заданными параметрами.

**Параметры**:

-   `max_requests` (int, optional): Максимальное количество запросов для выполнения во время сканирования. По умолчанию `5`.
-   `headless` (bool, optional): Определяет, запускать ли браузер в безголовом режиме. По умолчанию `False`.
-   `browser_type` (str, optional): Тип браузера для использования (`'chromium'`, `'firefox'`, `'webkit'`). По умолчанию `'firefox'`.
-   `options` (Optional[List[str]], optional): Список пользовательских опций для передачи в браузер. По умолчанию `None`.

### `setup_crawler`

```python
    async def setup_crawler(self):
        """
        Sets up the PlaywrightCrawler instance with the specified configuration.
        """
        self.crawler = PlaywrightCrawler(
            max_requests_per_crawl=self.max_requests,
            headless=self.headless,
            browser_type=self.browser_type,
            launch_options={"args": self.options}
        )

        @self.crawler.router.default_handler
        async def request_handler(context: PlaywrightCrawlingContext) -> None:
            """
            Default request handler for processing web pages.

            :param context: The crawling context.
            :type context: PlaywrightCrawlingContext
            """
            context.log.info(f'Processing {context.request.url} ...')

            # Enqueue all links found on the page.
            await context.enqueue_links()

            # Extract data from the page using Playwright API.
            data = {
                'url': context.request.url,
                'title': await context.page.title(),
                'content': (await context.page.content())[:100],
            }

            # Push the extracted data to the default dataset.
            await context.push_data(data)
```

**Описание**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

### `run_crawler`

```python
    async def run_crawler(self, urls: List[str]):
        """
        Runs the crawler with the initial list of URLs.

        :param urls: List of URLs to start the crawl.
        :type urls: List[str]
        """
        await self.crawler.run(urls)
```

**Описание**: Запускает сканер с начальным списком URL.

**Параметры**:

-   `urls` (List[str]): Список URL для начала сканирования.

### `export_data`

```python
    async def export_data(self, file_path: str):
        """
        Exports the entire dataset to a JSON file.

        :param file_path: Path to save the exported JSON file.
        :type file_path: str
        """
        await self.crawler.export_data(file_path)
```

**Описание**: Экспортирует весь набор данных в JSON-файл.

**Параметры**:

-   `file_path` (str): Путь для сохранения экспортированного JSON-файла.

### `get_data`

```python
    async def get_data(self) -> Dict[str, Any]:
        """
        Retrieves the extracted data.

        :return: Extracted data as a dictionary.
        :rtype: Dict[str, Any]
        """
        data = await self.crawler.get_data()
        return data
```

**Описание**: Извлекает полученные данные.

**Возвращает**:

-   `Dict[str, Any]`: Извлеченные данные в виде словаря.

### `run`

```python
    async def run(self, urls: List[str]):
        """
        Main method to set up, run the crawler, and export data.

        :param urls: List of URLs to start the crawl.
        :type urls: List[str]
        """
        try:
            await self.setup_crawler()
            await self.run_crawler(urls)
            await self.export_data(str(Path(gs.path.tmp / 'results.json')))
            data = await self.get_data()
            logger.info(f'Extracted data: {data.items()}')
        except Exception as ex:
            logger.critical('Crawler failed with an error:', ex)
```

**Описание**: Основной метод для настройки, запуска сканера и экспорта данных.

**Параметры**:

-   `urls` (List[str]): Список URL для начала сканирования.

## Пример использования

```python
if __name__ == '__main__':
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
```