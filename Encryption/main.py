from sanic import Sanic
from sanic_cors import CORS
from crypto import encrypt, decrypt

app = Sanic(name='encryption')
app.add_route(encrypt, '/encrypt', methods=['POST', 'OPTIONS'])
app.add_route(decrypt, '/decrypt', methods=['POST', 'OPTIONS'])
# app.config.CORS_ORIGINS = "http://127.0.0.1:8112,http://localhost:8112"
app.config.CORS_ALLOW_HEADERS = '*'
# Extend(app)

if __name__ == '__main__':
    CORS(app)
    app.run(host="127.0.0.1", port=8111)

