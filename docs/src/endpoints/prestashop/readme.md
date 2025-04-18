# Документация для модуля управления PrestaShop

## Обзор

Данный файл `README.md` предоставляет информацию о структуре и использовании веб-сайтов PrestaShop, а также о хранении и использовании ключей API.

## Подробней

Этот файл содержит информацию о том, как управлять веб-сайтами PrestaShop, включая информацию о ключах API. В нем описывается, как безопасно хранить ключи API и как использовать их для взаимодействия с различными параметрами и функциями веб-сайтов.

## Содержание

- [Веб-сайты](#веб-сайты)
- [Хранение ключей API](#хранение-ключей-api)
- [Пример использования API](#пример-использования-api)
  - [Пример запроса API](#пример-запроса-api)
  - [Пример вызова API](#пример-вызова-api)
- [Рекомендации по безопасности](#рекомендации-по-безопасности)
- [Дополнительные ресурсы](#дополнительные-ресурсы)

## Веб-сайты

Ваши веб-сайты PrestaShop:

1. [e-cat.co.il](https://e-cat.co.il)
2. [emil-design.com](https://emil-design.com)
3. [sergey.mymaster.co.il](https://sergey.mymaster.co.il)

Каждый из этих веб-сайтов использует API для взаимодействия с различными параметрами и функциями.

## Хранение ключей API

Ключи API для каждого веб-сайта хранятся в файле `credentials.kdbx`. Этот файл представляет собой защищенную базу данных паролей и содержит следующие данные для каждого веб-сайта:

- URL веб-сайта
- Ключ API
- Дополнительные метаданные (если необходимо)

Для работы с ключами из файла используйте менеджер паролей, поддерживающий формат `.kdbx`, например, [KeePass](https://keepass.info/) или [KeePassXC](https://keepassxc.org/).

## Пример использования API

Чтобы подключиться к API одного из ваших веб-сайтов, следуйте шаблону ниже:

### Пример запроса API

**Шаблон запроса API:**

```bash
curl -X GET 'https://<SITE_URL>/api/<endpoint>' \\\
-H 'Authorization: Basic <base64(API_KEY)>'
```

**Описание параметров:**

- `<SITE_URL>` — адрес веб-сайта, например, `e-cat.co.il`.
- `<endpoint>` — API endpoint (например, `products`, `customers`).
- `<API_KEY>` — ключ API, закодированный в Base64.

### Пример вызова API

Чтобы получить список продуктов из `e-cat.co.il`:

```bash
curl -X GET 'https://e-cat.co.il/api/products' \\\
-H 'Authorization: Basic <base64(API_KEY)>'
```

## Рекомендации по безопасности

- Никогда не передавайте файл `credentials.kdbx` другим лицам. ❗
- Убедитесь, что файл хранится в безопасном месте, доступном только вам. (Папка `secrets` в корне проекта исключена из `git`).
- Регулярно обновляйте свои ключи API и пароли к базе данных.

## Дополнительные ресурсы

Если у вас возникнут какие-либо проблемы или вопросы о подключении к API, обратитесь к [официальной документации PrestaShop API](https://devdocs.prestashop.com/), в которой представлена информация о доступных endpoints и о том, как с ними взаимодействовать.