import socket

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    container_id=socket.gethostname()
    return f"Response from Server: <b>{container_id}</b>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

