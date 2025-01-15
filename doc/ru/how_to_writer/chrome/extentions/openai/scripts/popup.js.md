Как использовать AngularJS контроллер для взаимодействия с OpenAI
=========================================================================================

Описание
-------------------------
Этот JavaScript-код представляет собой AngularJS контроллер `MainController`, предназначенный для управления пользовательским интерфейсом, который взаимодействует с OpenAI. Он отвечает за загрузку списка ассистентов, отправку сообщений выбранному ассистенту и отображение ответов от сервера.

Шаги выполнения
-------------------------
1.  **Инициализация AngularJS приложения:**
    - Код начинает с инициализации AngularJS приложения `openaiApp` с помощью `angular.module('openaiApp', []);`.
    -  Это создает новый модуль Angular без зависимостей.
2.  **Создание контроллера:**
     -  Создается контроллер `MainController` с помощью `app.controller('MainController', function ($scope, $http) { ... });`.
        -   Контроллер принимает зависимости `$scope` для работы с данными и `$http` для отправки HTTP-запросов.
3.  **Инициализация переменных:**
    -   В контроллере инициализируются переменные:
        -  `$scope.message`: для хранения сообщения, введенного пользователем.
        -  `$scope.response`: для хранения ответа от сервера.
         -   `$scope.assistants`: для хранения списка доступных ассистентов.
         -  `$scope.selectedAssistant`: для хранения выбранного ассистента.
4. **Загрузка списка ассистентов:**
   -  Функция `loadAssistants()`:
        -   Выполняет HTTP GET-запрос к адресу `http://localhost:8000/assistants`.
        -   При успешном запросе присваивает полученные данные (список ассистентов) переменной `$scope.assistants`.
        - При возникновении ошибки логирует ее в консоль.
5.  **Инициализация при запуске:**
    -   Функция `loadAssistants()` вызывается сразу после создания контроллера, чтобы получить список доступных ассистентов при загрузке страницы.
6.  **Отправка сообщения модели:**
    -  Функция `$scope.sendMessage()`:
        -  Создает объект `data`, включающий:
            - `message`: сообщение пользователя из `$scope.message`.
            - `system_instruction`: системную инструкцию для модели.
            -   `assistant_id`: идентификатор выбранного ассистента.
        - Выполняет HTTP POST запрос к адресу `http://localhost:8000/ask` и передает объект `data`.
         - При успешном запросе присваивает полученный ответ от сервера переменной `$scope.response`.
         -  В случае ошибки логирует ее в консоль и выводит сообщение об ошибке.
7.  **Использование в HTML:**
    - Этот контроллер предназначен для работы с HTML, который включает AngularJS директивы для отображения и управления данными.
    -  В HTML должны быть элементы для ввода сообщения, выбора ассистента, а также для отображения ответа от сервера.

Пример использования
-------------------------
.. code-block:: javascript

    // JavaScript
    
    // Инициализируем Angular приложение
    const app = angular.module('openaiApp', []);
    
    // Контроллер для обработки логики
    app.controller('MainController', function ($scope, $http) {
        $scope.message = '';
        $scope.response = '';
        $scope.assistants = [];
        $scope.selectedAssistant = null;
        
        // Функция для получения списка ассистентов
        function loadAssistants() {
             const url = 'http://localhost:8000/assistants';  // Создай новый endpoint для получения списка ассистентов
            alert("ASST")
            $http.get(url)
                .then(function (response) {
                  $scope.assistants = response.data;  // Список ассистентов
                })
                .catch(function (error) {
                    console.error('Ошибка загрузки ассистентов:', error);
               });
       }
    
        // Загружаем список ассистентов при инициализации
        loadAssistants();
    
        // Функция для отправки сообщения модели
        $scope.sendMessage = function () {
            const url = 'http://localhost:8000/ask';  // Адрес FastAPI сервера
    
            const data = {
                message: $scope.message,
                system_instruction: "You are a helpful assistant.",
                assistant_id: $scope.selectedAssistant.id  // Добавляем ID ассистента
           };
        
           // Отправка POST-запроса через $http (AJAX)
           $http.post(url, data)
                .then(function (response) {
                    $scope.response = response.data.response;  // Ответ от сервера
                })
               .catch(function (error) {
                   console.error('Ошибка:', error);
                  $scope.response = 'Произошла ошибка. Попробуйте позже.';
              });
       };
    });

   
    
    
   // HTML
    
    
    <!DOCTYPE html>
    <html>
    <head>
       <title>OpenAI Model Interface</title>
       <script src="scripts/angular.min.js"></script>
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
```