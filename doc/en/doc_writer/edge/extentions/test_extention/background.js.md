# Background Script Documentation (`background.js`)

This document provides an overview of the `background.js` script, focusing on its role in listening for messages, collecting data, and sending it to a server.

## Table of Contents

1.  [Overview](#overview)
2.  [Event Listeners](#event-listeners)
    -   [`chrome.browserAction.onClicked.addListener`](#chromebrowseractiononclickedaddlistener)
    -   [`chrome.runtime.onMessage.addListener`](#chromeruntimeonmessageaddlistener)
3.  [Functions](#functions)
    -   [`sendDataToServer`](#senddatatoserver)

## Overview

The `background.js` script is a core component of a browser extension that operates in the background. It sets up event listeners to react to specific actions within the browser and provides functions to handle those events. Its primary responsibilities include capturing specific messages from other parts of the extension and forwarding data to a designated server.

## Event Listeners

### `chrome.browserAction.onClicked.addListener`

```javascript
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});
```

**Description**: This event listener is triggered when the browser extension's icon is clicked.

-   It sends a message to the currently active tab using `chrome.tabs.sendMessage`.
-   The message includes an `action` property set to `'collectData'` and the `url` of the tab.

### `chrome.runtime.onMessage.addListener`

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});
```

**Description**: This event listener is triggered when a message is sent to the background script using `chrome.runtime.sendMessage()`.

-   It checks if the received message has an `action` property set to `'collectData'`.
-  If the condition is met, it calls the `sendDataToServer()` function, passing the URL from the message as an argument.

## Functions

### `sendDataToServer`

```javascript
function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Change to your server endpoint
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to send data to server');
                    }
                    console.log('Data sent to server successfully');
                })
                .catch(error => {
                    console.error('Error sending data to server:', error);
                });
        } else {
            console.error('No collected data found');
        }
    });
}
```

**Description**: This function sends collected data to a specified server endpoint.

**Parameters**:

-   `url`: The URL of the page from which the data was collected.

**Functionality**:

-   It defines the `serverUrl` to where the data will be sent (`http://127.0.0.1/hypotez.online/api/`).
-   Retrieves stored data from `chrome.storage.local` using the key `collectedData`.
-   If `collectedData` exists, it sends a POST request to the `serverUrl` with the data, setting the `Content-Type` header to `application/json`.
-   Logs a success message if the server receives the data successfully.
-   Logs an error message if the server request fails or no collected data is found.

This document provides a comprehensive overview of the `background.js` script, detailing its event listeners and functions, which is essential for developers working with this extension.