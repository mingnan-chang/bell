# Bell Example Project

This repository demonstrates a simple pipeline for recording audio on a mobile device and uploading it to a PHP server. A Python script downloads the audio, transcribes it with the Vosk speech recognition library, and saves the results. Finally, a small Three.js page displays the transcribed text dropping from the top of the screen.

## Components

- `client/mobile_record.html` – records audio in the browser and uploads it to `server/upload.php`.
- `server/upload.php` – saves uploaded audio files under `server/uploads/`.
- `server/list.php` – lists available uploaded files as JSON.
- `client/pull_transcribe.py` – downloads audio files, converts them with `ffmpeg`, and transcribes them using Vosk.
- `display.html` – loads `transcripts.json` and shows each line of text falling in 3D using Three.js.

To use the Python script you must install `vosk`, `requests`, and `ffmpeg`, and download a Vosk model into a `model/` directory.
