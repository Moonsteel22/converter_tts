from app.services.models import Part
from app.services.models import Text


KEY_WORDS = {"ru": ["глава", "часть", "раздел"], "en": ["chapter"]}


def parser(filename: str, text: list[str], language: str = "ru") -> list[Text]:
    if isinstance(text, str):
        text = text.split("\n")

    DELIMITTER_WORDS = KEY_WORDS[language]

    text = list(filter(None, text))
    texts = []

    for i in range(len(text) - 1):
        for j in DELIMITTER_WORDS:
            if j in text[i].lower():
                part = Part(
                    delimitter=text[i].split(" ")[0],
                    text=text[i + 1],
                    chapter=int(text[i].split(" ")[1]),
                )
                i += 1
                texts.append(
                    Text(part=part, name=filename + f"/{j}_{part.chapter}"),
                )
                break
    return texts
