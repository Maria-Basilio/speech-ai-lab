# Speech AI Lab

**A Python project exploring AI-powered speech recognition and audio generation.**

## About the Project

Speech AI Lab is a Python application built to experiment with generative AI audio workflows using the OpenAI Audio API.

The project explores how spoken language can be converted into text, how written text can be transformed into speech, and how these capabilities can be combined into a complete speech-to-text-to-speech workflow.

It provides a practical environment for experimenting with audio processing and integrating AI capabilities into Python applications.

## Features

- **Speech-to-Text (STT):** Convert spoken audio into written text.
- **Text-to-Speech (TTS):** Generate audio from written text.
- **Speech-to-Text-to-Speech:** Combine transcription and audio generation into a single workflow.
- **Audio Input and Output:** Organize input and generated audio files into dedicated directories.
- **API Integration:** Connect Python applications to OpenAI's audio capabilities.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenAI Python SDK | Integration with OpenAI services |
| OpenAI Audio API | Speech recognition and audio generation |
| python-dotenv | Environment variable management |

## Project Structure

```text
speech-ai-lab/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── input/
├── output/
└── app/
    ├── main.py
    ├── text_to_speech.py
    └── speech_to_text.py
```

## How It Works

The application explores three main audio workflows:

### 1. Speech-to-Text (STT)

Audio input is processed through speech recognition, converting spoken content into text.

### 2. Text-to-Speech (TTS)

Written text is sent for audio generation, producing spoken output.

### 3. Speech-to-Text-to-Speech

This workflow combines both capabilities:

```text
Audio Input
    ↓
Speech Recognition
    ↓
Text Output
    ↓
Text-to-Speech
    ↓
Generated Audio
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- An OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Maria-Basilio/speech-ai-lab.git
```

2. Navigate to the project directory:

```bash
cd speech-ai-lab
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

**Important:** Never commit your `.env` file or expose your API key in the repository.

### Running the Application

Run the main application from the project root:

```bash
python app/main.py
```

## What I Learned

Through this project, I explored:

- Integrating external AI services into Python applications.
- Working with speech recognition and audio generation.
- Building different workflows with the OpenAI Audio API.
- Managing environment variables and API credentials.
- Organizing Python applications into modular components.
- Understanding how speech and text processing can work together.

## Future Improvements

- Add support for more audio formats.
- Improve error handling and input validation.
- Expand the available speech processing workflows.
- Develop a user-friendly interface for audio interactions.

---

**Exploring the connection between language, sound, and artificial intelligence. ♡**
