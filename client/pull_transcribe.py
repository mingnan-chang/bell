import os
import json
import requests
import subprocess
import wave
from vosk import Model, KaldiRecognizer

SERVER = "http://yourserver.com/server"  # replace with real server URL
AUDIO_DIR = "downloaded_audio"
TRANS_FILE = "transcripts.json"
MODEL_PATH = "model"  # path to Vosk model


def list_files():
    r = requests.get(f"{SERVER}/list.php")
    r.raise_for_status()
    return r.json()


def download_file(fname):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    local = os.path.join(AUDIO_DIR, os.path.basename(fname))
    if not os.path.exists(local):
        url = f"{SERVER}/{fname}"
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return local


def to_wav(path):
    wav = os.path.splitext(path)[0] + '.wav'
    if not os.path.exists(wav):
        subprocess.run(["ffmpeg", "-y", "-i", path, wav], check=True)
    return wav


def transcribe(wav_path, recognizer):
    with wave.open(wav_path, 'rb') as wf:
        data = wf.readframes(wf.getnframes())
    if recognizer.AcceptWaveform(data):
        res = json.loads(recognizer.Result())
        return res.get('text', '')
    return ''


def main():
    files = list_files()
    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, 16000)
    transcripts = []
    for f in files:
        local = download_file(f)
        wav = to_wav(local)
        text = transcribe(wav, rec)
        transcripts.append({'file': f, 'text': text})
    with open(TRANS_FILE, 'w', encoding='utf-8') as out:
        json.dump(transcripts, out, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
