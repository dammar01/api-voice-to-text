# API Audio to Text dengan Vosk

Aplikasi API ini memungkinkan pengguna untuk mengunggah file audio dan mengonversinya menjadi teks menggunakan Vosk, sebuah pustaka pengenalan suara.

## Fitur

- Upload file audio dalam berbagai format (MP3, WAV, dll.)
- Konversi audio menjadi teks menggunakan model Vosk
- Mendukung autentikasi melalui header

## Prerequisites

Sebelum memulai, pastikan Anda memiliki hal-hal berikut:

- **Docker**: Pastikan Docker dan Docker Compose telah terinstal di sistem Anda. [Ikuti petunjuk pemasangan Docker di sini.](https://docs.docker.com/get-docker/)
- **FFmpeg**: Pastikan FFmpeg terinstal untuk mengonversi format audio. Jika menggunakan Docker, FFmpeg sudah termasuk dalam image yang digunakan.

## Setup

Ikuti langkah-langkah berikut untuk mengatur dan menjalankan aplikasi:

### 1. Clone Repository

Clone repositori ini ke dalam direktori lokal Anda:

```bash
git clone <repository-url>
cd <repository-name>
docker-compose up --build
```
