from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "message": "Flask backend is running"})

if __name__ == "__main__":
    app.run(debug=True)