How to use this code block
=========================================================================================

Description
-------------------------
This `background.js` script is designed for a Chrome extension's background process. It is responsible for listening to browser action clicks and messages from content scripts, and then sending collected data to a server. It acts as a central point for managing extension-wide communication and data submission.

Execution steps
-------------------------
1.  **Set up browser action click listener**: The `chrome.browserAction.onClicked.addListener` function sets up an event listener that activates when the extension's browser action (icon) is clicked.
    - When the icon is clicked, a message with the `action` type `collectData` and the current tab URL is sent to content script of the currently active tab using `chrome.tabs.sendMessage`.
2.  **Set up runtime message listener**: The `chrome.runtime.onMessage.addListener` function sets up a listener that waits for messages from content scripts or other background scripts.
     -  When a message with `action` type `collectData` is received, the script invokes `sendDataToServer` function and passes the URL from the message as an argument.
3. **Send data to the server**: The `sendDataToServer` function handles sending data to the server, it will perform following actions:
    - Retrieves the collected data from Chrome's local storage using `chrome.storage.local.get` with key `'collectedData'`.
    -   If data is available it uses `fetch` method to send a POST request with the collected data to a specified server URL.
    -   It validates the response and logs a success or error message to the console depending on the server response status.
    - If no data is present in the storage, it logs an error message.

Usage example
-------------------------
```javascript
// background.js

// Listener for browser action clicks
chrome.browserAction.onClicked.addListener(tab => {
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
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Replace with your server endpoint
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
- Provided a detailed description of the `background.js` script, including its purpose, methods, and event listeners.
- Outlined clear execution steps of the provided javascript code.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added a detailed explanation on `chrome.browserAction.onClicked.addListener`, `chrome.runtime.onMessage.addListener` and `chrome.storage.local.get` methods and how they function.
- Explained the interaction of the `sendDataToServer` method with external server and how errors are handled.
- Added an explanation about how data from content scripts is used and sent to the server.
- Added an important note about updating `serverUrl` with an actual endpoint.