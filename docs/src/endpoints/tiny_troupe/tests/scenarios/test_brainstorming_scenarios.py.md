# Модуль тестирования сценария мозгового штурма

## Обзор

Модуль содержит функцию `test_brainstorming_scenario`, которая тестирует сценарий мозгового штурма с использованием агентов `TinyPerson` для генерации идей по улучшению Microsoft Word с помощью AI.

## Подробней

Этот модуль предназначен для проверки работоспособности системы мозгового штурма в контексте разработки новых функций для Microsoft Word. Он использует агентов `TinyPerson` для генерации идей, а затем извлекает и анализирует результаты. Тесты проверяют, соответствуют ли сгенерированные идеи заданным критериям.

## Функции

### `test_brainstorming_scenario`

```python
def test_brainstorming_scenario(setup, focus_group_world):
    """ Функция тестирует сценарий мозгового штурма с использованием агентов TinyPerson.
    Args:
        setup: Настройка тестовой среды.
        focus_group_world: Объект мира для проведения мозгового штурма.

    Returns:
        None

    Raises:
        AssertionError: Если сгенерированные результаты не соответствуют ожидаемым.
    """
```

**Как работает функция**:

1.  **Инициализация мира**: Функция начинает с инициализации мира на основе переданного объекта `focus_group_world`.
2.  **Рассылка сообщения**: Функция рассылает сообщение участникам мозгового штурма с заданием сгенерировать идеи для новых AI-функций в Microsoft Word.
3.  **Запуск мира**: Функция запускает мир на один шаг (`world.run(1)`), чтобы агенты могли взаимодействовать и генерировать идеи.
4.  **Получение агента**: Функция получает агента `TinyPerson` по имени "Lisa Carter".
5.  **Активация агента**: Агент прослушивает и действует, запрашивая обобщение идей, предложенных группой.
6.  **Извлечение результатов**: Функция использует класс `ResultsExtractor` для извлечения результатов из ответов агента.
7.  **Анализ результатов**: Извлеченные результаты анализируются для проверки соответствия заданным критериям.
8.  **Проверка утверждения**: Функция проверяет, содержит ли извлеченный текст идеи для новых функций продукта или совершенно новые продукты, используя функцию `proposition_holds`. Если утверждение не выполняется, тест завершается с ошибкой.

```
Начало -> Инициализация мира
↓
Рассылка сообщения -> Установка задачи для мозгового штурма
↓
Запуск мира -> Агенты взаимодействуют и генерируют идеи
↓
Получение агента -> Выбор агента "Lisa Carter"
↓
Активация агента -> Запрос обобщения идей
↓
Извлечение результатов -> Анализ ответов агента
↓
Проверка утверждения -> Подтверждение соответствия результатов ожиданиям
↓
Конец
```

**Примеры**:

```python
# Пример вызова функции с настроенным миром и агентами
test_brainstorming_scenario(setup_fixture, world_fixture)