# Модуль `product_translator`

## Обзор

Модуль `product_translator` предназначен для управления переводами товаров, обеспечивая связь между словарем полей товара, таблицей переводов и различными сервисами перевода. Он предоставляет функции для получения, вставки и перевода записей о товарах, используя базу данных PrestaShop и AI-модели для перевода.

## Подробней

Этот модуль является ключевым компонентом системы, отвечающим за автоматизацию процесса перевода информации о товарах. Он интегрируется с базой данных PrestaShop для извлечения существующих переводов и использует AI-модели для генерации новых переводов. Это позволяет поддерживать мультиязычность в интернет-магазине, предоставляя пользователям информацию о товарах на их родном языке.

## Функции

### `get_translations_from_presta_translations_table`

```python
def get_translations_from_presta_translations_table(product_reference: str, i18n: str = None) -> list:
    """Функция возвращает словарь переводов полей товара."""
```

**Описание**: Получает переводы полей товара из таблицы переводов PrestaShop.

**Как работает функция**:
1. Инициализирует менеджер для работы с базой данных переводов.
2. Формирует фильтр поиска по референсу продукта.
3. Извлекает запись о переводе продукта из базы данных.

**Параметры**:
- `product_reference` (str): Уникальный идентификатор товара.
- `i18n` (str, optional): Локаль перевода (например, 'en_US'). По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей, содержащих переводы полей товара.

**Примеры**:
```python
product_translations = get_translations_from_presta_translations_table('12345')
if product_translations:
    print(f'Найдены переводы: {product_translations}')
else:
    print('Переводы не найдены')
```

### `insert_new_translation_to_presta_translations_table`

```python
def insert_new_translation_to_presta_translations_table(record: dict):
    """Функция для вставки новых переводов в таблицу переводов PrestaShop."""
```

**Описание**: Добавляет новую запись перевода в таблицу переводов PrestaShop.

**Как работает функция**:
1. Инициализирует менеджер для работы с базой данных переводов.
2. Вставляет предоставленную запись перевода в базу данных.

**Параметры**:
- `record` (dict): Словарь, содержащий данные для вставки (например, переведенные поля товара).

**Примеры**:
```python
new_translation = {
    'product_reference': '67890',
    'locale': 'fr_FR',
    'name': 'Nouveau Produit'
}
insert_new_translation_to_presta_translations_table(new_translation)
```

### `translate_record`

```python
def translate_record(record: dict, from_locale: str, to_locale: str) -> dict:
    """Функция для перевода полей товара."""
```

**Описание**: Переводит поля товара с использованием AI-модели.

**Как работает функция**:
1. Вызывает функцию `translate` из модуля `src.ai.openai` для выполнения перевода.
2. Обрабатывает переведенную запись (в текущей версии кода отсутствует конкретная реализация обработки).

**Параметры**:
- `record` (dict): Словарь с полями товара для перевода.
- `from_locale` (str): Исходная локаль (например, 'en_US').
- `to_locale` (str): Целевая локаль (например, 'fr_FR').

**Возвращает**:
- `dict`: Словарь с переведенными полями товара.

**Примеры**:
```python
record = {
    'name': 'Product Name',
    'description': 'Product Description'
}
translated_record = translate_record(record, 'en_US', 'fr_FR')
print(f'Переведенная запись: {translated_record}')