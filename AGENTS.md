# Voice Assistant

Python Flask web application providing a voice assistant interface powered by OpenAI (`gpt-4o-mini`) and external Watson Speech-to-Text / Text-to-Speech lab APIs.

## Commands

- **Run Dev Server:** `python server.py` (starts Flask server on `http://localhost:8000`)
- **Install Dependencies:** `pip install -r requirements.txt`
- **Docker Build:** `docker build . -t voice-chatapp-powered-by-openai`
- **Docker Run:** `docker run -p 8000:8000 voice-chatapp-powered-by-openai`

## Architecture & Entrypoints

- `server.py`: Main Flask application entrypoint defining routes (`/`, `/speech-to-text`, `/process-message`).
- `worker.py`: Integrates OpenAI client and Watson STT/TTS HTTP APIs (`speech_to_text`, `text_to_speech`, `openai_process_message`).
- Frontend: `templates/index.html`, `static/script.js`, `static/style.css`.
- Models/configs: Subdirectories under `models/` containing service configs and Docker setups for STT/TTS.

## Environment & Gotchas

- Requires `OPENAI_API_KEY` set in the environment for OpenAI chat completions (`gpt-4o-mini`).
- Watson STT/TTS endpoints depend on external lab network availability (`sn-watson-stt.labs.skills.network` / `sn-watson-tts.labs.skills.network`).
