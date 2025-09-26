from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/command", methods=["POST"])
def run_command():
    # استقبال الأمر من المستخدم (JSON)
    data = request.get_json()
    cmd = data.get("command") if data else None

    if not cmd:
        return jsonify({"error": "No command provided"}), 400

    try:
        # تنفيذ الأمر
        output = subprocess.check_output(cmd, shell=True)
        # تحويل البايتات لنص مع تجنب المشاكل في الترميز
        return jsonify({"output": output.decode('cp1256', errors='ignore')})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Command failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error: {e}"}), 500

if __name__ == "__main__":
    # تشغيل السيرفر على المنفذ 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
