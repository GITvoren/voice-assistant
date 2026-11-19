# Voice Assistant

A guided lab project completed as part of the IBM AI Developer Program. This is a Python Flask web application providing a voice assistant interface powered by OpenAI (`gpt-4o-mini`) and external IBM Watson Speech-to-Text and Text-to-Speech lab APIs.

## Features

- Speech-to-Text transcription via Watson STT API
- Natural language processing and response generation via OpenAI (`gpt-4o-mini`)
- Text-to-Speech audio synthesis via Watson TTS API
- Interactive web frontend with audio recording and playback support

## Prerequisites

- Python 3.8+
- OpenAI API Key (`OPENAI_API_KEY` environment variable)
- Access to IBM Skills Network / Watson lab network endpoints for STT/TTS services

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key in your shell environment (the OpenAI SDK automatically picks up the `OPENAI_API_KEY` environment variable; no `.env` file is required):
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```

## Running the Application

### Locally

Start the Flask development server:
```bash
python server.py
```

Open your browser and navigate to `http://localhost:8000`.

### Using Docker

Build the Docker image:
```bash
docker build . -t voice-chatapp-powered-by-openai
```

Run the container:
```bash
docker run -p 8000:8000 -e OPENAI_API_KEY="your-openai-api-key" voice-chatapp-powered-by-openai
```

## Architecture

- `server.py`: Flask application server defining HTTP endpoints (`/`, `/speech-to-text`, `/process-message`).
- `worker.py`: Integration logic for OpenAI and Watson HTTP APIs (`speech_to_text`, `text_to_speech`, `openai_process_message`).
- `templates/` & `static/`: Frontend HTML, JavaScript, and CSS assets.
- `models/`: Service configurations and Docker setups for STT and TTS models.

## License

This project is licensed under the terms included in the LICENSE file.
