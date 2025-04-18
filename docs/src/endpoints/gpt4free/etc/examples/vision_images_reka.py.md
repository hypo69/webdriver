# Модуль для работы с Image Chat Reka

## Обзор

Модуль предоставляет пример использования чат-бота Reka для анализа изображений. Он демонстрирует, как загрузить изображение и отправить запрос для получения описания содержимого изображения.
Для корректной работы требуется быть залогиненым в chat.reka.ai и иметь сохраненные cookies.

## Подробней

Данный код является примером использования библиотеки `g4f` для взаимодействия с моделью `reka-core`. Он показывает, как отправить изображение в чат-бот и получить описание содержимого изображения.
Код предполагает, что изображение `test.png` находится в той же директории, что и скрипт.

## Функции

### `chat.completions.create`

```python
completion = client.chat.completions.create(
    model = "reka-core",
    messages = [
        {
            "role": "user",
            "content": "What can you see in the image ?"
        }
    ],
    stream = True,
    image = open("docs/images/cat.jpeg", "rb") # open("path", "rb"), do not use .read(), etc. it must be a file object
)
```

**Назначение**: Отправляет запрос в чат-бот Reka для получения описания содержимого изображения.

**Параметры**:
- `model` (str): Указывает модель, которую нужно использовать ("reka-core").
- `messages` (list): Список сообщений для отправки в чат-бот. В данном случае содержит одно сообщение с вопросом "What can you see in the image ?".
- `stream` (bool): Указывает, нужно ли возвращать ответ в режиме потока (True).
- `image` (file object): Объект файла изображения, который нужно проанализировать. Открывается в режиме чтения байтов ("rb").

**Возвращает**:
- `completion` (Generator): Генератор, который выдает чанки ответа от чат-бота.

**Вызывает исключения**:
- Отсутствуют явные обработки исключений в данном коде.

**Как работает функция**:

1.  **Инициализация клиента**: Создается экземпляр класса `Client` из библиотеки `g4f` для взаимодействия с чат-ботом Reka.
2.  **Формирование запроса**: Формируется запрос к чат-боту с указанием модели, сообщения и изображения.
3.  **Отправка запроса**: Запрос отправляется в чат-бот с использованием метода `chat.completions.create`.
4.  **Получение ответа**: Ответ от чат-бота возвращается в виде генератора, который выдает чанки ответа.

```
Инициализация клиента
     ↓
Формирование запроса (модель, сообщение, изображение)
     ↓
Отправка запроса
     ↓
Получение ответа в виде генератора
```

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import Reka

client = Client(
    provider = Reka # Optional if you set model name to reka-core
)

completion = client.chat.completions.create(
    model = "reka-core",
    messages = [
        {
            "role": "user",
            "content": "What can you see in the image ?"
        }
    ],
    stream = True,
    image = open("docs/images/cat.jpeg", "rb") # open("path", "rb"), do not use .read(), etc. it must be a file object
)

for message in completion:
    print(message.choices[0].delta.content or "")
```

### Вывод результата

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Выводит в консоль полученные от чат-бота сообщения.

**Параметры**:
- `message` (str): Сообщение от чат-бота.

**Возвращает**:
- Ничего. Функция просто выводит сообщения в консоль.

**Как работает функция**:

1.  **Итерация по ответам**: Цикл `for` итерируется по чанкам ответа, полученным от чат-бота.
2.  **Извлечение содержимого**: Из каждого чанка извлекается текстовое содержимое сообщения с помощью `message.choices[0].delta.content`.
3.  **Вывод в консоль**: Полученное содержимое выводится в консоль. Если содержимое отсутствует, выводится пустая строка.

```
Итерация по ответам
     ↓
Извлечение содержимого
     ↓
Вывод в консоль
```

**Примеры**:

```python
for message in completion:
    print(message.choices[0].delta.content or "")