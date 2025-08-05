from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import spotipy_client as spc
from spotipy_client import sp, auth_manager

load_dotenv()
app = Flask(__name__)

# App API routes
@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        auth_manager.get_access_token(code)
    return "<h1>Authorization successful, you can close this tab and return to the app.</h1>"

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "message": "Flask backend is running"})


# Spotipy API routes
@app.route('/api/me')
def me():
    return jsonify(spc.get_current_user())

@app.route('/api/playlists')
def playlists():
    return jsonify(spc.get_user_playlists())


if __name__ == "__main__":
    app.run(debug=True)