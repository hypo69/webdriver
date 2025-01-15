How to use this code block
=========================================================================================

Description
-------------------------
This `background.js` script is designed to be used as a background script for a Chrome extension. It handles communication between the extension's popup or content scripts and sends collected data to a server. It listens for browser action clicks and messages from content scripts, then sends the collected data to a predefined server endpoint.

Execution steps
-------------------------
1. **Set up a listener for browser action clicks**: The `chrome.action.onClicked.addListener` function sets up an event listener that triggers when the extension's browser action icon is clicked.
   -   When the icon is clicked, it sends a message to the content script running on the active tab using `chrome.tabs.sendMessage`. This message includes an action called `'collectData'` and the current tab URL.
2. **Set up a message listener**: The `chrome.runtime.onMessage.addListener` function sets up an event listener that listens for messages sent from the extension's content scripts or other parts of the extension.
     - When a message with the action `collectData` is received, it calls `sendDataToServer` function passing the URL from the message as an argument.
3. **Send data to the server**: The `sendDataToServer` function is responsible for sending collected data to a server:
     -  It retrieves collected data from Chrome local storage using `chrome.storage.local.get`, using the key `'collectedData'`.
    -   If data is found, it sends a POST request to the defined server URL using the fetch method, including the collected data as JSON.
    -   If the server response is not successful, it logs an error in the console.
    -   If data is sent successfully, the console will show a message.
    -   If there is no data, an error message is logged to the console.

Usage example
-------------------------
```javascript
// background.js

// Listener for browser action clicks
chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});

// Listener for messages from content scripts
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});

// Function to send data to the server
function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php'; // Replace with your server endpoint
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
```

## Changes
- Added a detailed description of the `background.js` script, explaining its purpose, methods, and event listeners.
- Outlined clear execution steps of the provided javascript code.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added explanations for what happens when the browser action icon is clicked and how messages are sent between the extension parts.
- Improved descriptions of functions for handling collected data and sending it to a server.
-  Added a note that the `serverUrl` must be replaced with actual server endpoint for the script to work.