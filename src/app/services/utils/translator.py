from google.cloud import translate_v2


def translate(
    text: str,
    client: translate_v2.Client,
    language: str = "ru",
) -> list[str]:
    lang = client.detect_language(text)

    if lang["language"] == language:
        return text.split("\n")

    splitted = text.split("\n")

    results = client.translate(splitted, target_language=language)

    return [result["translatedText"] for result in results]
