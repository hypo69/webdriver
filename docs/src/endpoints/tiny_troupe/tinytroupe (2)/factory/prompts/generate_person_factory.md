# Генерация контекстов для создания описаний персон

## Обзор

Этот документ описывает структуру и назначение запроса, используемого для генерации контекстов, которые в дальнейшем будут использоваться для создания описаний персон. Запрос предназначен для получения широкого контекста с деталями о персонах, которых необходимо сгенерировать (демографические параметры, физические характеристики, поведение, убеждения и т.д.), а затем создания множества других, более специфических контекстов, основанных на исходном.

## Подробней

Этот запрос используется для создания разнообразных и детализированных описаний персон. Он принимает общий контекст и генерирует на его основе несколько более конкретных контекстов, которые затем используются для формирования окончательных описаний персон.

## Функции

### `Генерация контекстов`

```
   Your task is create many contexts that will be used as base to generate a list of persons.
   The idea is receive a broad context, with some  details of persons we want to generate, like demographics parameters, physical characteristics, behaviors, believes, etc; and then create many other contexts, more specifics, but derivaded of the more generic one.
   Your response must be an array in JSON format. Each element of the array must be a context that will be used to generate a person description.

   Example:
     - INPUT:
       Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not
     - OUTPUT:
       ["Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies", "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.", "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."]

```

**Назначение**: Генерация контекстов для создания списка персон.

**Параметры**:
- Нет явных параметров, кроме инструкции в строке запроса. В инструкции указывается широкий контекст с деталями о персонах, которых нужно сгенерировать.

**Возвращает**:
- `array`: Массив в формате JSON, где каждый элемент является контекстом, используемым для генерации описания персоны.

**Вызывает исключения**:
- Не описаны.

**Как работает функция**:
1. Получает широкий контекст с деталями о персонах (демография, физические характеристики, поведение, убеждения и т.д.).
2. Создает множество более специфических контекстов, основанных на исходном.
3. Формирует массив в формате JSON, где каждый элемент представляет собой отдельный контекст для генерации описания персоны.

```
Генерация широкого контекста --> Создание специфических контекстов --> Формирование JSON массива
```

**Примеры**:

**Пример 1**:
- Вход: `Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not`
- Выход: `["Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies", "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.", "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."]`