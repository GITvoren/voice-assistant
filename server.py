import base64
import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from worker import speech_to_text, text_to_speech, openai_process_message

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/speech-to-text", methods=["POST"])
def speech_to_text_route():
    audio_binary = request.data
    text = speech_to_text(audio_binary) or ""
    return app.response_class(
        response=json.dumps({"text": text}),
        status=200,
        mimetype="application/json",
    )


@app.route("/process-message", methods=["POST"])
def process_message_route():
    data = request.get_json(silent=True) or {}
    user_message = data.get("userMessage", "")
    voice = data.get("voice", "")
    print("user_message", user_message)
    print("voice", voice)

    # Call openai_process_message function to process the user's message
    openai_response_text = openai_process_message(user_message) or ""

    # Clean the response to remove any empty lines
    openai_response_text = os.linesep.join(
        [line for line in openai_response_text.splitlines() if line.strip()]
    )

    # Convert OpenAI response text to speech audio bytes
    openai_response_speech = text_to_speech(openai_response_text, voice)

    # Encode speech audio as base64 for JSON transport
    speech_base64 = (
        base64.b64encode(openai_response_speech).decode("utf-8")
        if openai_response_speech
        else None
    )

    payload = {
        "openaiResponseText": openai_response_text,
        "openaiResponseSpeech": speech_base64,
    }
    return app.response_class(
        response=json.dumps(payload),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")


# docker build . -t voice-chatapp-powered-by-openai
# docker run -p 8000:8000 voice-chatapp-powered-by-openai
