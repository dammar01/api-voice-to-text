from fastapi import Header, File, FastAPI, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv
from pydub import AudioSegment
import os, shutil, subprocess, json

app = FastAPI()
model_path = "./app/vosk" if os.path.exists("./app/vosk") else "./app/app/vosk"
model = Model(model_path, lang="en-us")
if os.path.exists("./tmp"):
    shutil.rmtree("./tmp")
os.makedirs("tmp", exist_ok=True)

SAMPLE_RATE = 16000
recognizer = KaldiRecognizer(model, SAMPLE_RATE)


def auth(authorization: str = Header(None)):
    api_key = os.getenv("API_KEY")
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    if authorization != f"Bearer {api_key}":
        raise HTTPException(status_code=403, detail="Invalid API Key")


@app.on_event("startup")
async def startup_event():
    load_dotenv()


@app.post("/")
async def main(file: UploadFile = File(...), authorization: str = Header(None)):
    auth(authorization)
    audio_file_path = f"tmp/{file.filename}"
    with open(audio_file_path, "wb") as buffer:
        buffer.write(await file.read())

    wav_file_path = "tmp/temp_audio.wav"
    try:
        audio = AudioSegment.from_file(audio_file_path)
        audio = audio.set_frame_rate(SAMPLE_RATE).set_channels(1)
        audio.export(wav_file_path, format="wav")
    except Exception as e:
        os.remove(audio_file_path)
        return {"error": f"Failed to convert audio: {str(e)}"}

    rec = KaldiRecognizer(model, SAMPLE_RATE)
    try:
        with subprocess.Popen(
            [
                "ffmpeg",
                "-loglevel",
                "quiet",
                "-i",
                wav_file_path,
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-f",
                "s16le",
                "-",
            ],
            stdout=subprocess.PIPE,
        ) as process:

            results = []
            while True:
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    results.append(result)

            final_result = rec.FinalResult()
            results.append(final_result)
    except Exception as e:
        os.remove(audio_file_path)
        os.remove(wav_file_path)
        return {"error": f"Error processing audio: {str(e)}"}

    os.remove(audio_file_path)
    os.remove(wav_file_path)
    transcription = [json.loads(res)["text"] for res in results]
    return JSONResponse(content={"transcription": transcription})
