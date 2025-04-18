# Модуль beeper

## Обзор

Модуль `beeper.py` предназначен для генерации звуковых сигналов, оповещающих о различных событиях в системе. Он использует библиотеку `winsound` для воспроизведения звуков на платформе Windows и предоставляет функциональность для управления звуковыми сигналами на основе заданных уровней важности событий.
В частности, данный модуль определяет различные уровни звуковых оповещений (например, SUCCESS, INFO, ERROR), каждый из которых связан с определенной мелодией или частотой звука. Это позволяет визуально и аудиально различать разные типы событий, происходящих в системе.

## Подробней

Модуль `beeper` предоставляет классы и функции для генерации звуковых сигналов, соответствующих различным уровням событий (например, успех, информация, предупреждение, ошибка). Он использует библиотеку `winsound` для воспроизведения звуков на платформе Windows. Этот модуль позволяет разработчикам интегрировать звуковые оповещения в свои приложения для улучшения восприятия и информирования пользователей о происходящих событиях.

## Классы

### `BeepLevel`

**Описание**: Класс-перечисление, определяющий различные типы событий, которым соответствуют разные мелодии.

**Как работает класс**:
Класс `BeepLevel` является перечислением (`Enum`), которое определяет набор возможных уровней событий, таких как `SUCCESS`, `INFO`, `ATTENTION`, `WARNING`, `DEBUG`, `ERROR`, `LONG_ERROR`, `CRITICAL` и `BELL`. Каждому уровню события соответствует список кортежей, где каждый кортеж содержит ноту и длительность звука. Это позволяет воспроизводить различные мелодии в зависимости от типа события.

**Методы**:
- Нет

**Параметры**:
- Нет

**Примеры**
```python
from src.logger.beeper import BeepLevel

# Пример использования BeepLevel
success_level = BeepLevel.SUCCESS
print(success_level.value)  # Вывод: [('D5', 100), ('A5', 100), ('D6', 100)]
```

### `BeepHandler`

**Описание**: Класс для обработки записей логов и воспроизведения соответствующих звуковых сигналов.

**Как работает класс**:
Класс `BeepHandler` предназначен для обработки записей логов и воспроизведения соответствующих звуковых сигналов. Он имеет метод `emit`, который вызывается для каждой записи лога. В методе `emit` определяется уровень события из записи лога и вызывается метод `play_sound` для воспроизведения соответствующего звука. Если уровень события не соответствует ни одному из предопределенных, вызывается метод `play_default_sound`.

**Методы**:
- `emit(self, record)`: Метод для обработки записи лога и воспроизведения соответствующего звукового сигнала.
- `beep(self, level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000)`:  Вызывает метод `beep` класса `Beeper` для воспроизведения звукового сигнала.
- `play_sound(self, frequency: int, duration: int)`: Воспроизводит звуковой сигнал с заданной частотой и длительностью.
- `play_default_sound(self)`: Воспроизводит звук по умолчанию

**Параметры**:
- Нет

**Примеры**

```python
from src.logger.beeper import BeepHandler

# Пример использования BeepHandler
handler = BeepHandler()
handler.play_sound(440, 500)  # Воспроизведение звука с частотой 440 Гц и длительностью 500 мс
```

### `Beeper`

**Описание**: Класс для управления звуковыми сигналами.

**Как работает класс**:
Класс `Beeper` предоставляет статический метод `beep` для воспроизведения звуковых сигналов. Он также содержит переменную `silent`, которая позволяет отключать звуковые сигналы. Метод `beep` принимает уровень события, частоту и длительность звука в качестве параметров. В зависимости от уровня события воспроизводится соответствующая мелодия.

**Методы**:
- `beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000)`: Статический метод для воспроизведения звукового сигнала.

**Параметры**:
- `silent`: Флаг, указывающий, включен ли беззвучный режим. По умолчанию `False`.

**Примеры**
```python
from src.logger.beeper import Beeper, BeepLevel

# Пример использования Beeper
Beeper.silent = True  # Включение беззвучного режима
Beeper.beep(level=BeepLevel.ERROR)  # Воспроизведение звукового сигнала для ошибки (если беззвучный режим выключен)
```

## Функции

### `silent_mode`

```python
def silent_mode(func):
    """
     Функция-декоратор для управления режимом "беззвучия".
    
    @details Принимает один аргумент - функцию, которую нужно декорировать.
    
    @param func: Функция для декорирования.
    
    @return: Обернутая функция, добавляющая проверку режима "беззвучия".
    """
    def wrapper(*args, **kwargs):
        """
         Внутренняя функция-обертка для проверки режима "беззвучия" перед выполнением функции.
        
        @details Если режим "беззвучия" включен, выводит сообщение о пропуске воспроизведения звука и завершает выполнение функции beep.\n
        В противном случае вызывает оригинальную функцию, переданную как аргумент (func(*args, **kwargs)).
        
        @param args: Позиционные аргументы, переданные в оборачиваемую функцию.
        @param kwargs: Именованные аргументы, переданные в оборачиваемую функцию.
        
        @return: Результат выполнения оборачиваемой функции или None, если режим "беззвучия" включен.
        """
        if Beeper.silent:
            print("Silent mode is enabled. Skipping beep.")
            return
        return func(*args, **kwargs)
    return wrapper
```

**Описание**: Функция-декоратор для управления режимом "беззвучия".

**Как работает функция**:
Функция `silent_mode` является декоратором, который принимает функцию в качестве аргумента и возвращает обертку вокруг этой функции. Обертка проверяет, включен ли режим "беззвучия" (переменная `Beeper.silent`). Если режим "беззвучия" включен, функция выводит сообщение о пропуске воспроизведения звука и завершает выполнение. В противном случае вызывается оригинальная функция.

**Параметры**:
- `func` (function): Функция, которую нужно декорировать.

**Возвращает**:
- function: Обернутая функция, добавляющая проверку режима "беззвучия".

**Примеры**:
```python
from src.logger.beeper import Beeper, silent_mode

@silent_mode
def my_beep_function():
    """
    Функция для воспроизведения звукового сигнала.
    """
    print("Beep!")

Beeper.silent = True
my_beep_function()  # Вывод: Silent mode is enabled. Skipping beep.

Beeper.silent = False
my_beep_function()  # Вывод: Beep!