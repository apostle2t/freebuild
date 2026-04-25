from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """

    <!DOCTYPE html>
    <html>
        <head>
            <title><Chat Application/title>
        </head>
        <body>
            <h1>Welcome to Matthew's Chatting application</h1>
            <h2>Enter an Input to start chatting<h2>
            <form action="" onsubmit="connectWebhook(event)">
                <input type="text" id="inp"/>
                <button type="submit"/>
            </form>
            <ul id="messages"></ul>
            <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            }
            
            function connectWebhook(event) {
                var input = document.getElementById('inp');
                ws.send(input.value);
                input.value = "";
                event.preventDefault();
            }
            </script>
        </body>
    </html>

"""