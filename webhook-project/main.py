from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocket

app = FastAPI()

html = """

    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat Application</title>
        </head>
        <body>
            <h1>Welcome to Matthew's Chatting application</h1>
            <h2>Enter an Input to start chatting.</h2>
            <form action="" onsubmit="connectWebhook(event)">
                <input type="text" id="inp"/>
                <button type="submit">Send</button>
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

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)


