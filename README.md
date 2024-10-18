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

## Setup

Follow these steps to set up and run the application:

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

```bash
http://0.0.0.0:8000
```
