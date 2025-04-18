
### Настройка политик безопасности PowerShell (только для Windows)

В Windows политика безопасности PowerShell может ограничивать выполнение скриптов. Если вы столкнулись с проблемами при запуске скриптов проекта, выполните следующие действия для настройки политики безопасности:

1.  **Запустите PowerShell от имени администратора.**

2.  **Выполните следующую команду для разрешения выполнения скриптов в текущей директории и всех поддиректориях:**

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```

    *   `Set-ExecutionPolicy`: Команда для изменения политики выполнения скриптов.
    *   `-ExecutionPolicy RemoteSigned`: Устанавливает политику, разрешающую выполнение локально созданных скриптов и скриптов, подписанных доверенным издателем.
    *   `-Scope Process`: Указывает, что политика применяется только к текущему процессу PowerShell. Это наиболее безопасный вариант, так как изменения не сохраняются глобально.

    **Внимание:** Если требуется более широкая область действия, можно использовать `-Scope CurrentUser` или `-Scope LocalMachine`, но это может снизить безопасность системы.

    После выполнения команды вам может быть предложено подтвердить изменения. Введите `Y` (Да) и нажмите Enter.

    **❗Важно:** Изменение политики безопасности PowerShell может повлиять на безопасность вашей системы. Будьте внимательны и используйте только необходимые параметры.

### Инструкция по установке зависимостей

Для запуска модуля `webdriver` проекта `hypotez` необходимо установить все необходимые зависимости 
для работы модуля

Выполните следующие команды в командной строке или терминале:

1.  **Обновление `pip` (рекомендуется):**

    ```bash
    python.exe -m pip install --upgrade pip
    ```
    Эта команда обновит установленный менеджер пакетов `pip` до последней версии.
2.  **Установка зависимостей проекта:**

    ```bash
    pip install jupyter selenium pandas json-repair reportlab A4 fake-useragent aiofiles aiohttp beautifulsoup4 lxml Pillow pydantic
    ```

    Эта команда установит все необходимые пакеты, перечисленные в списке:

    *   `jupyter`: Для создания и запуска Jupyter Notebooks.
    *   `selenium`: Для автоматизации веб-браузеров.
    *   `pandas`: Для анализа и обработки данных.
    *   `json-repair`: Для восстановления поврежденных JSON.
    *   `reportlab`: Для создания PDF-документов.
    *   `A4`: Определения размера бумаги A4
    *   `fake-useragent`: Для генерации поддельных User-Agent.
    *   `aiofiles`: Для асинхронной работы с файлами.
    *   `aiohttp`: Для асинхронных HTTP-запросов.
    *   `beautifulsoup4`: Для парсинга HTML и XML.
    *   `lxml`: Для быстрой обработки XML и HTML.
    *   `Pillow`: Для работы с изображениями.
    *   `pydantic`: Для валидации данных и настроек.

**Альтернативный способ установки (если есть файл `requirements.txt`):**

```bash
pip install -r requirements.txt
```

#### Обзор файлов в директории `src`:

Директория `src` содержит исходный код проекта `hypotez`. 

❗**Важно:** Для разработки собственного кода и экспериментов рекомендуется создать отдельную директорию в папке `SANDBOX`.
Подробней 👉 [Как начать разработку в `Sandbox`](https://github.com/hypo69/webdriver/blob/master/SANDBOX/README.MD)

1.  **`header.py`**:

    *   **Назначение**: Содержит функцию `set_project_root`, которая определяет корневую директорию проекта.
    *   **Функциональность**: Функция ищет маркерные файлы (например, `__root__` или `.git`) в родительских директориях, чтобы определить корень проекта. Добавляет корень проекта в `sys.path`, чтобы обеспечить возможность импорта модулей из любой части проекта.
    *   **Пути**: Определяет и экспортирует переменную `__root__`, содержащую путь к корневой директории проекта.
2.  **`__init__.py`**:

    *   **Назначение**: Инициализирует пакет `src` и определяет, откуда загружать секреты (API-ключи и т.д.).
    *   **Логика**:
        *   Определяет переменную `USE_ENV:bool`, которая управляет способом загрузки секретов.
        *   Если `USE_ENV` равно `True`, импортирует модуль `gs` из `gs.py` и загружает секреты из файлов `.env`.
        *   Если `USE_ENV` равно `False`, импортирует модуль `gs` из `credentials.py` и загружает секреты из объекта `gs` (например, `token = gs.path.telegram.kazarinov_bot`).
        *   Вызывает функцию `check_latest_release` для проверки наличия новой версии проекта на GitHub.
3.  **`check_release.py`**:

    *   **Назначение**: Содержит функцию `check_latest_release`, которая проверяет наличие новой версии проекта на GitHub.
    *   **Функциональность**: Функция делает запрос к API GitHub для получения информации о последнем релизе и возвращает его версию. В случае ошибки логирует сообщение об ошибке.
4.  **`config.json`**:

    *   **Назначение**: Файл конфигурации в формате JSON, содержащий основные настройки проекта (хост, репозиторий, пути к различным директориям и т.д.).
    *   **Структура**:
        *   `host`: Хост для запуска приложения.
        *   `git`: Название репозитория.
        *   `git_user`: Имя пользователя GitHub.
        *   `current_release`: Текущая версия релиза.
        *   `path`: Объект, содержащий пути к различным директориям (внешнее хранилище, Google Drive, логи, временные файлы).
        *   `timestamp_format`: Формат временной метки.
5.  **`gs.py`**:

    *   **Назначение**: Загружает параметры программы, если флаг `USE_ENV` установлен в `True`.
    *   **Функциональность**: Загружает конфигурацию из файла `config.json` и создает объект `gs`, аналогичный тому, который создается в `credentials.py`, но без параметров учетных данных. Используется, когда не требуется полная загрузка параметров из KeePass.

#### Как настроить пути в файле конфигурации (`config.json`):

Файл `config.json` содержит объект `path`, который определяет пути к различным директориям проекта. Важно правильно настроить эти пути, чтобы обеспечить корректную работу приложения.

Пример конфигурации путей:

```json
"path": {
    "external_storage": "E:\\hypo69\\data",
    "google_drive": "H:\\My Drive\\hypotez\\data",
    "log": "E:\\hypo69\\log",
    "tmp": "E:\\hypo69\\tmp"
}
```

*   `external_storage`: Путь к внешнему хранилищу данных.
*   `google_drive`: Путь к локальной директории Google Drive.
*   `log`: Путь к директории для хранения логов.
*   `tmp`: Путь к директории для хранения временных файлов.

**Рекомендации по настройке путей:**

*   Укажите абсолютные пути, чтобы избежать проблем с относительными путями.
*   Убедитесь, что директории, указанные в `config.json`, существуют на вашей системе.
*   Настройте пути в соответствии с вашей структурой хранения данных и логов.
*   Учитывайте особенности операционной системы (например, используйте `\` в Windows и `/` в Unix).

### Клонирование репозитория `webdriver` с GitHub

Если вам необходимо клонировать репозиторий `webdriver` с GitHub, выполните следующие действия:

1.  **Установите Git:**

    Если у вас еще не установлен Git, скачайте и установите его с официального сайта: [https://git-scm.com/downloads](https://git-scm.com/downloads)

2.  **Откройте командную строку или терминал.**

3.  **Перейдите в директорию, куда хотите клонировать репозиторий.**

    Например:

    ```bash
    cd /path/to/your/projects
    ```

4.  **Выполните команду клонирования:**

    ```bash
    git clone https://github.com/hypo69/webdriver.git
    ```

    Эта команда клонирует репозиторий `webdriver` в локальную директорию.

    **Примечание:** Замените `https://github.com/hypo69/webdriver.git` на фактический URL репозитория, если он отличается.

5.  **Перейдите в директорию клонированного репозитория:**

    ```bash
    cd webdriver
    ```

### Разработка собственных модулей в папке `SANDBOX`

Для разработки собственного кода и экспериментов рекомендуется создать отдельную директорию в папке `SANDBOX`. 
Подробные инструкции смотрите в файле [`README.md`](https://github.com/hypo69/webdriver/blob/master/SANDBOX/README.MD) в директории `SANDBOX`.

