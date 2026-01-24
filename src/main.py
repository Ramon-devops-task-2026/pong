import os
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Environment variable
ENV_NAME = os.getenv("ENV_NAME", "unknown")

print(f"[{datetime.now()}] 🚀 PONG service started | ENV_NAME={ENV_NAME}")

@app.route('/pong', methods=['GET'])
def pong():
    print(f"[{datetime.now()}] 🔁 PONG({ENV_NAME}) received request")

    return jsonify({
        "service": "pong",
        "env": ENV_NAME,
        "message": "pong",
        "timestamp": datetime.now().isoformat()
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "service": "pong",
        "env": ENV_NAME,
        "status": "healthy"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
