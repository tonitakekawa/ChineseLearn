# Flaskベースの音声認識＋TTSサーバーコード

from flask import Flask, request, jsonify, send_file
import whisper
import tempfile
import os
from flask_cors import CORS
from pypinyin import lazy_pinyin, Style
from gtts import gTTS
import uuid

app = Flask(__name__)
CORS(app)
model = whisper.load_model("base")

@app.route("/tts", methods=["POST"])
def tts():
    text = request.json.get("text", "")
    if not text:
        return "No text provided", 400

    filename = f"tts_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang='zh')
    tts.save(filename)
    response = send_file(filename, mimetype="audio/mpeg")
    @response.call_on_close
    def cleanup():
        os.remove(filename)
    return response

@app.route("/odai", methods=["GET"])
def odai():
    text = "你好"
    pin = " ".join([s[0] for s in lazy_pinyin(text, style=Style.TONE)])
    return jsonify({"text": text, "pinyin": pin})

@app.route("/stt", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "音声ファイルがありません"}), 400

    audio_file = request.files["audio"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        audio_file.save(tmp.name)
        result = model.transcribe(tmp.name)
        os.remove(tmp.name)

    text = result["text"]
    pinyin = " ".join(lazy_pinyin(text, style=Style.TONE))
    return jsonify({"text": text, "pinyin": pinyin})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

