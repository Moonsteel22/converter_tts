import tarfile
from io import BytesIO

from app.services.models import Text
from google.cloud import texttospeech


LANGUAGES = {"en": "en-GB", "ru": "ru-RU"}


class SettingsNotFound(Exception):
    pass


async def convert_all():
    pass


def preprocessing(
    language_code: str = "ru",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    speaking_rate: float = 0.82,
):
    language_code = LANGUAGES[language_code]
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=ssml_gender,
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate,
    )

    return voice, audio_config


def convert_text(
    text: list[Text],
    client: texttospeech.TextToSpeechClient,
    voice: texttospeech.VoiceSelectionParams,
    audio_config: texttospeech.AudioConfig,
) -> tarfile.TarFile:
    t = tarfile.open("temptar.tar.gz", mode="w:gz")
    for i in text:
        synthesis_input = texttospeech.SynthesisInput(text=i.part.text)

        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config,
        )
        audio = BytesIO(response.audio_content)
        dfinfo = tarfile.TarInfo(i.name + ".mp3")
        dfinfo.size = len(audio.getvalue())
        audio.seek(0)

        t.addfile(dfinfo, audio)
    t.close()
    return t
