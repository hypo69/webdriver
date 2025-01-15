# Документация модуля `chrome.runtime.onInstalled.addListener`

## Обзор

Этот модуль представляет собой JavaScript-код, который устанавливает слушатель для события `chrome.runtime.onInstalled`. Это событие срабатывает, когда расширение Chrome устанавливается или обновляется.

## Оглавление

-   [Обзор](#обзор)
-   [Функции](#функции)
    -   [Слушатель события `onInstalled`](#слушатель-события-oninstalled)

## Функции

### Слушатель события `onInstalled`

```javascript
chrome.runtime.onInstalled.addListener(() => {
    console.log('OpenAI Model Interface Extension Installed');
});
```

**Описание**: Этот код добавляет слушатель для события `chrome.runtime.onInstalled`. Когда расширение устанавливается или обновляется, этот слушатель срабатывает и выводит сообщение `'OpenAI Model Interface Extension Installed'` в консоль.

**Описание работы:**

1.  `chrome.runtime.onInstalled.addListener()`: Устанавливает слушатель на событие `onInstalled`, которое срабатывает при установке или обновлении расширения.
2.  `() => { ... }`: Анонимная функция, которая выполняется при наступлении события.
3.  `console.log('OpenAI Model Interface Extension Installed');`: Выводит сообщение в консоль, подтверждая успешную установку или обновление расширения.