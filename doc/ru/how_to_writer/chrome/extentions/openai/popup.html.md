Как использовать `popup.html` для интерфейса взаимодействия с OpenAI
=========================================================================================

Описание
-------------------------
Файл `popup.html` представляет собой HTML-страницу для всплывающего окна расширения Chrome, предоставляющего пользовательский интерфейс для взаимодействия с OpenAI. Страница разделена на две основные вкладки: "Chat" для общения с моделью и "Model" для управления обучением и статусом модели. Используются Angular, JQuery, и собственный скрипт `popup.js` для управления интерфейсом.

Шаги выполнения
-------------------------
1. **Структура HTML:**
   -  Файл `popup.html` содержит HTML-структуру всплывающего окна:
       -   Заголовок (`<title>`) и подключение стилей (`style.css`) и скриптов (`angular.min.js`, `jquery-3.5.1.slim.min.js`, `popup.js`).
       -  Контейнер `body` с атрибутами `ng-app="openaiApp"` и `ng-controller="MainController"`, указывающими на использование AngularJS.
   -  Содержит две вкладки:
        - `"Chat"`: для общения с моделью.
        -  `"Model"`: для управления обучением и статусом модели.
2.  **Использование Angular:**
    -   Для динамического управления вкладками, данными и действиями используется AngularJS.
    -  Область приложения `ng-app="openaiApp"` и контроллер `ng-controller="MainController"` настраивают приложение Angular.
3. **Вкладка "Chat":**
    -   Содержит элементы для взаимодействия с моделью чата:
        -  Выпадающий список ассистентов: `<select id="assistants" ng-model="selectedAssistant" ng-options="assistant.name for assistant in assistants track by assistant.id">`.
        -  Поле для ввода сообщения: `<textarea ng-model="message" placeholder="Enter your message"></textarea>`.
        -  Кнопка отправки сообщения: `<button ng-click="sendMessage()">Send</button>`.
        - Область для вывода ответа модели: `<div id="response">`.
4.  **Вкладка "Model":**
    - Содержит элементы для управления обучением модели:
        -  Текстовое поле для ввода данных обучения: `<textarea id="data" ng-model="trainingData" placeholder="Enter training data"></textarea>`.
        -   Кнопка для начала обучения: `<button ng-click="trainModel()">Train</button>`.
        - Область для вывода статуса обучения: `<h3>Training Status:</h3> <p>{{trainingStatus}}</p>`.
5. **Логика работы `popup.js`:**
   -  Скрипт `popup.js` содержит код для управления поведением элементов на странице, отправки сообщений фоновому скрипту и обработки ответов.
     - Обрабатывает переключения вкладок с помощью `ng-click` и функций Angular.
     -   Инициализирует переменные Angular, обрабатывает ввод сообщений, отправляет запросы в фоновый скрипт и т.д.
6.  **Стилизация:**
    -  Файл `style.css` управляет визуальным оформлением страницы.
7.  **Настройка `MODE`:**
    -  Переменная `MODE` предназначена для отладки. Возможные значения: `debug` или `prod`.
    -  Если `MODE="debug"` скрипт может вести себя иначе, чем в production.

Пример использования
-------------------------
.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
       <title>OpenAI Model Interface</title>
       <script src="scripts/angular.min.js"></script>
       <script src="scripts/jquery-3.5.1.slim.min.js"></script>
       <script src="scripts/popup.js"></script>
       <link rel="stylesheet" href="style.css">
    </head>
    <body ng-app="openaiApp" ng-controller="MainController">
       <h1>OpenAI Model Interface</h1>
        
       <!-- Навигационные вкладки -->
       <ul class="tabs">
           <li ng-class="{active: isTabActive('chat')}" ng-click="setActiveTab('chat')">Chat</li>
           <li ng-class="{active: isTabActive('model')}" ng-click="setActiveTab('model')">Model</li>
       </ul>
    
        <!-- Содержимое вкладки 'Chat' -->
        <div ng-show="isTabActive('chat')">
          <h2>Chat with Model</h2>
           <!-- Выпадающий список ассистентов -->
           <label for="assistants">Choose an Assistant:</label>
          <select id="assistants" ng-model="selectedAssistant" ng-options="assistant.name for assistant in assistants track by assistant.id">
                 <option value="">-- Select Assistant --</option>
           </select>
    
          <!-- Поле для ввода сообщения -->
          <textarea ng-model="message" placeholder="Enter your message"></textarea>
           <button ng-click="sendMessage()">Send</button>
    
           <!-- Ответ модели -->
          <div id="response">
            <h3>Response:</h3>
             <p>{{response}}</p>
           </div>
       </div>
    
       <!-- Содержимое вкладки 'Model' -->
       <div ng-show="isTabActive('model')">
          <h2>Model Training and Status</h2>
           <p>Here you can start training or check the status of the model.</p>
    
          <!-- Дополнительный функционал для работы с моделью, как пример: -->
           <label for="data">Training Data:</label>
           <textarea id="data" ng-model="trainingData" placeholder="Enter training data"></textarea>
           <button ng-click="trainModel()">Train</button>
    
           <h3>Training Status:</h3>
            <p>{{trainingStatus}}</p>
        </div>
    </body>
    </html>
    
    <!-- Пример popup.js (minimal example)-->
    <!--
    angular.module('openaiApp', [])
       .controller('MainController', ['$scope', function ($scope) {
            $scope.activeTab = 'chat';

            $scope.isTabActive = function (tab) {
               return $scope.activeTab === tab;
           };

            $scope.setActiveTab = function (tab) {
                 $scope.activeTab = tab;
            };
           $scope.sendMessage = function () {
                alert("Отправка сообщения: " + $scope.message);
            };
            $scope.trainModel = function () {
                 alert("Начало обучения модели с данными: " + $scope.trainingData);
           };
    
            $scope.assistants = [
                { id: 1, name: 'Assistant 1' },
                 { id: 2, name: 'Assistant 2' }
            ];
            $scope.selectedAssistant = null;
       }]);
    -->
```