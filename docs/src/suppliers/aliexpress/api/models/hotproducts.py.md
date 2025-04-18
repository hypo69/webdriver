# Модуль `hotproducts`

## Обзор

Модуль `hotproducts` содержит классы для представления ответа API, содержащего список популярных товаров с AliExpress. Он включает класс `HotProductsResponse`, который хранит информацию о текущей странице, количестве записей на странице, общем количестве записей и список товаров, представленных классом `Product` из модуля `product`.

## Подробней

Модуль предназначен для обработки данных, возвращаемых API AliExpress при запросе популярных товаров. Он структурирует полученные данные в удобный для использования формат, что упрощает дальнейшую обработку и отображение информации о товарах.

## Классы

### `HotProductsResponse`

**Описание**: Класс представляет ответ API, содержащий список популярных товаров.

**Принцип работы**:
Класс агрегирует информацию о текущей странице, количестве товаров на странице, общем количестве товаров и список экземпляров класса `Product`. Это позволяет удобно представить и обрабатывать данные, полученные от API AliExpress.

**Аттрибуты**:

- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список объектов `Product`, представляющих товары.

**Методы**:
Отсутствуют.

## Функции
В данном модуле отсутствуют функции.