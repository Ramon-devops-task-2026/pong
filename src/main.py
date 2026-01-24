import os
import time
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)




# Environment variable (from Docker / docker-compose)
ENV_NAME = os.getenv("ENV_NAME", "unknown")

@app.route('/pong', methods=['GET'])
def pong():
    print(f"[{datetime.now()}] Pong request received")

    return jsonify({
        "service": "pong",
        "env": ENV_NAME,
        "message": "pong",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "pong"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
