
from flask import Flask, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "service": "VC Backend",
        "message": "Backend is running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "online",
        "service": "VC Backend",
        "connected": True,
        "time": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify({
        "status": "online",
        "vc_engine": "not_configured",
        "total_sessions": 0,
        "message": "Backend API is ready"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Route not found"
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
