How to use this code block
=========================================================================================

Description
-------------------------
This `background.js` script is designed for a Chrome extension's background process. It manages the communication flow between the extension's browser action, content scripts, and an external server. The script listens for browser action clicks and messages from content scripts, and sends the collected data to a server endpoint.

Execution steps
-------------------------
1. **Set up browser action click listener**: The `chrome.browserAction.onClicked.addListener` function sets up an event listener that triggers when the extension's browser action icon is clicked.
    - When the icon is clicked, it sends a message using `chrome.tabs.sendMessage` to the content script running in the active tab with `action` set to `'collectData'` and including the active tab's URL.
2.  **Set up runtime message listener**: The `chrome.runtime.onMessage.addListener` sets up a listener to handle messages sent from the content scripts or other parts of the extension using `chrome.runtime.sendMessage`.
    -  When a message with the action `'collectData'` is received, it calls the `sendDataToServer` function, passing the message's URL as an argument.
3.  **Send data to the server**: The `sendDataToServer` function handles sending data to an external server.
     - It retrieves data from Chrome local storage by calling `chrome.storage.local.get` with key `'collectedData'`.
    -  If data is available, it sends a POST request to the defined server URL with the collected data as a JSON payload using `fetch` method.
    - If the server response is not successful, it throws an error and catches it.
    - If the request is successful, it logs a message, and if not it logs an error message to the browser console.
    -  If there is no data in local storage, an error message is logged to the console.

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
- Provided a detailed description of the `background.js` script and its components, explaining the purpose, logic, and actions performed by this code block.
- Outlined clear execution steps performed by the javascript code.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanations for the usage of `chrome.browserAction.onClicked.addListener`, `chrome.runtime.onMessage.addListener`, `chrome.storage.local.get` and `fetch` methods.
- Clarified the role of each part of the script in Chrome extension.
- Added a note about updating `serverUrl` with an actual endpoint.