from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)
VERSION = os.getenv('APP_VERSION', '1.0.0')

@app.route('/')
def index():
    return jsonify({
        'app': 'FormaTech',
        'version': VERSION,
        'host': socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': VERSION}), 200

@app.route('/version')
def version():
    return jsonify({'version': VERSION}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
