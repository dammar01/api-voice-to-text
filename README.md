# Audio to Text API with Vosk

This API application allows users to upload audio files and convert them into text using Vosk, a speech recognition library.

## Features

- Upload audio files in various formats (MP3, WAV, etc.)
- Convert audio to text using the Vosk model
- Supports authentication through headers

## Prerequisites

Before getting started, ensure you have the following:

- **Docker**: Make sure Docker and Docker Compose are installed on your system. [Follow the installation guide for Docker here.](https://docs.docker.com/get-docker/)
- **FFmpeg**: Ensure FFmpeg is installed for converting audio formats. If using Docker, FFmpeg is already included in the image used.
- **.env File**: Copy .env.example to .env and input your backend API_KEY. This API_KEY is used to restrict access to the application, ensuring that it can only be accessed from authorized servers (You can use custom generated API key or random text).

## Setup

Follow these steps to set up and run the application:

## Using Docker

### 1. Clone the Repository

```bash
git clone https://github.com/dammar01/api-audio-to-text.git
cd api-audio-to-text
```

### 2. Build the Docker Image

```bash
docker-compose up --build
```

### 3. Access the API
using postman or
```bash
curl -X POST http://0.0.0.0:8000/upload-audio \
-H "Authorization: Bearer API_KEY" \
-F "file=@path_to_your_audio_file"
```

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dammar01/api-audio-to-text.git
cd api-audio-to-text
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Access the API
using postman or
```bash
curl -X POST http://0.0.0.0:8000/upload-audio \
-H "Authorization: Bearer API_KEY" \
-F "file=@path_to_your_audio_file"
```
