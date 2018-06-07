
- 安装
    - pip install websocket-client

- 使用
```python
from websocket import create_connection
import json

src='ws://localhost:8000/ws/chat/labby/'
ws=create_connection(src)

js=json.dumps({'message':'hello'})
ws.send(js)
ws.recv()

js=json.dumps({'message':'hello jlfks'})
ws.send(js)
ws.recv()

```