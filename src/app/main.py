import asyncio

from app.services.converter import convert_text
from app.services.converter import preprocessing
from app.services.utils.parser import parser
from app.services.utils.translator import translate
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from google.cloud import texttospeech
from google.cloud import translate_v2
from starlette.responses import FileResponse


app = FastAPI()
converter_client = texttospeech.TextToSpeechClient()
translator_client = translate_v2.Client()


@app.post("/convert", response_class=FileResponse)
async def convert(file: UploadFile = File(...), language: str = "ru"):
    raw_text = await file.read()

    text = raw_text.decode("utf-8")
    text = translate(text=text, client=translator_client, language=language)
    text = parser(filename=file.filename, text=text, language=language)
    voice, audio_config = preprocessing(language_code=language)
    # TODO: refactor to streaming
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        convert_text,
        text,
        converter_client,
        voice,
        audio_config,
    )
    return result.name
