# api_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

latest_command = None
latest_output = None

@app.route("/send_command", methods=["POST"])
def send_command():
    global latest_command
    data = request.get_json()
    latest_command = data.get("command")
    return jsonify({"status": "command received"})

@app.route("/get_command", methods=["GET"])
def get_command():
    global latest_command
    return jsonify({"command": latest_command})

@app.route("/send_output", methods=["POST"])
def send_output():
    global latest_output
    data = request.get_json()
    latest_output = data.get("output")
    return jsonify({"status": "output received"})

@app.route("/get_output", methods=["GET"])
def get_output():
    global latest_output
    # حفظ القيمة مؤقتًا
    output = latest_output
    # تصفيرها بعد الإرسال
    latest_output = None
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
