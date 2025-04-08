# Модуль тестирования ThinkingProcessor

## Обзор

Этот модуль содержит тесты для класса `ThinkingProcessor`, который предназначен для обработки текстовых фрагментов, содержащих индикаторы начала и конца процесса мышления (`<think>` и `</think>`). Тесты проверяют корректность разбиения входных данных на фрагменты, определения статуса мышления и возврата ожидаемых результатов. Модуль использует библиотеку `unittest` для организации тестовых случаев.

## Подробней

Модуль тестирует различные сценарии использования `ThinkingProcessor`, включая случаи, когда фрагмент не содержит индикаторов мышления, содержит только начало или конец индикатора, содержит полный цикл (начало и конец), а также случай, когда процесс мышления продолжается.  Тесты проверяют, что `ThinkingProcessor` правильно определяет время начала процесса мышления и возвращает ожидаемые фрагменты текста с соответствующим статусом.

## Классы

### `TestThinkingProcessor`

**Описание**: Класс `TestThinkingProcessor` содержит набор тестов для проверки функциональности класса `ThinkingProcessor`.

**Принцип работы**:
Класс `TestThinkingProcessor` наследует от `unittest.TestCase` и содержит методы, каждый из которых тестирует определенный аспект работы `ThinkingProcessor`. Методы используют `assert` методы для сравнения ожидаемых и фактических результатов.

**Методы**:

- `test_non_thinking_chunk`: Тестирует случай, когда фрагмент не содержит индикаторов мышления.
- `test_thinking_start`: Тестирует случай, когда фрагмент содержит только начало индикатора мышления.
- `test_thinking_end`: Тестирует случай, когда фрагмент содержит только конец индикатора мышления.
- `test_thinking_start_and_end`: Тестирует случай, когда фрагмент содержит полный цикл индикаторов мышления (начало и конец).
- `test_ongoing_thinking`: Тестирует случай, когда процесс мышления продолжается.
- `test_chunk_with_text_after_think`: Тестирует случай, когда фрагмент содержит текст до, между и после индикаторов мышления.

## Функции

### `test_non_thinking_chunk`

```python
def test_non_thinking_chunk(self):
    """
    Тестирует случай, когда входной фрагмент текста не содержит тегов `<think>` или `</think>`.
    
    Args:
        self: Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что при отсутствии индикаторов мышления функция `ThinkingProcessor.process_thinking_chunk` возвращает исходный фрагмент без изменений и время, равное 0.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, не содержащий тегов `<think>` или `</think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` равным 0 и ожидаемый результат `expected_result` как список, содержащий исходный фрагмент.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_non_thinking_chunk(self):
        chunk = "This is a regular text."
        expected_time, expected_result = 0, [chunk]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)
```

### `test_thinking_start`

```python
def test_thinking_start(self):
    """
    Тестирует случай, когда входной фрагмент текста содержит только открывающий тег `<think>`.

    Args:
        self: Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что при наличии только открывающего тега `<think>` функция `ThinkingProcessor.process_thinking_chunk` возвращает время, близкое к текущему, и разбивает фрагмент на части, включая объекты `Reasoning` с соответствующим статусом.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, содержащий только открывающий тег `<think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` как текущее время, ожидаемый результат `expected_result` как список, содержащий части фрагмента и объекты `Reasoning` с соответствующим статусом.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertAlmostEqual` и `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_start(self):
        chunk = "Hello <think>World"
        expected_time = time.time()
        expected_result = ["Hello ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("World")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertAlmostEqual(actual_time, expected_time, delta=1)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

### `test_thinking_end`

```python
def test_thinking_end(self):
    """
    Тестирует случай, когда входной фрагмент текста содержит только закрывающий тег `</think>`.

    Args:
        self: Экземпляр класса TestThinkingProcessor.
        
    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что при наличии только закрывающего тега `</think>` функция `ThinkingProcessor.process_thinking_chunk` возвращает время, равное 0, и разбивает фрагмент на части, включая объекты `Reasoning` с соответствующим статусом.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, содержащий только закрывающий тег `</think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` равным 0, ожидаемый результат `expected_result` как список, содержащий части фрагмента и объекты `Reasoning` с соответствующим статусом.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk` и временем начала `start_time`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_end(self):
        start_time = time.time()
        chunk = "token</think> content after"
        expected_result = [Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, 0)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

### `test_thinking_start_and_end`

```python
def test_thinking_start_and_end(self):
    """
    Тестирует случай, когда входной фрагмент текста содержит одновременно открывающий и закрывающий теги `<think>` и `</think>`.

    Args:
        self: Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что при наличии обоих тегов `<think>` и `</think>` функция `ThinkingProcessor.process_thinking_chunk` возвращает время, равное 0, и разбивает фрагмент на части, включая объекты `Reasoning` с соответствующим статусом для обоих тегов.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, содержащий одновременно открывающий и закрывающий теги `<think>` и `</think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` равным 0, ожидаемый результат `expected_result` как список, содержащий части фрагмента и объекты `Reasoning` с соответствующим статусом для обоих тегов.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk` и временем начала `start_time`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_start_and_end(self):
        start_time = time.time()
        chunk = "<think>token</think> content after"
        expected_result = [Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, 0)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
        self.assertEqual(actual_result[3], expected_result[3])
```

### `test_ongoing_thinking`

```python
def test_ongoing_thinking(self):
    """
    Тестирует случай, когда процесс мышления продолжается и входной фрагмент текста не содержит тегов `<think>` или `</think>`.

    Args:
        self: Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что при отсутствии тегов `<think>` и `</think>`, но при активном процессе мышления, функция `ThinkingProcessor.process_thinking_chunk` возвращает исходное время начала и фрагмент, обернутый в объект `Reasoning`.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, не содержащий теги `<think>` или `</think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` как исходное время начала `start_time`, ожидаемый результат `expected_result` как список, содержащий фрагмент, обернутый в объект `Reasoning`.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk` и временем начала `start_time`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_ongoing_thinking(self):
        start_time = time.time()
        chunk = "Still thinking..."
        expected_result = [Reasoning("Still thinking...")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, start_time)
        self.assertEqual(actual_result, expected_result)
```

### `test_chunk_with_text_after_think`

```python
def test_chunk_with_text_after_think(self):
    """
    Тестирует случай, когда входной фрагмент текста содержит текст до, между и после тегов `<think>` и `</think>`.

    Args:
        self: Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактическое время или результат не совпадают с ожидаемыми.
    """
```

**Назначение**: Проверяет, что функция `ThinkingProcessor.process_thinking_chunk` правильно обрабатывает фрагмент с текстом до, между и после тегов `<think>` и `</think>`, корректно разбивая его на части и добавляя объекты `Reasoning` с соответствующим статусом.

**Параметры**:

- `self`: Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если фактическое время или результат не совпадают с ожидаемыми.

**Как работает функция**:

1. **Определение входных данных**: Определяется входной фрагмент текста `chunk`, содержащий текст до, между и после тегов `<think>` и `</think>`.
2. **Определение ожидаемых результатов**: Устанавливается ожидаемое время `expected_time` равным 0, ожидаемый результат `expected_result` как список, содержащий части фрагмента и объекты `Reasoning` с соответствующим статусом для обоих тегов.
3. **Вызов тестируемой функции**: Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом `chunk`.
4. **Сравнение результатов**: Сравниваются фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями с использованием `self.assertEqual`.

**Примеры**:

```python
import unittest
import time

from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_chunk_with_text_after_think(self):
        chunk = "Start <think>Middle</think>End"
        expected_time = 0
        expected_result = ["Start ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("Middle"), Reasoning(status="Finished", is_thinking="</think>"), "End"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)
```