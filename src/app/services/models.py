from pydantic import BaseModel


class Part(BaseModel):
    text: str
    chapter: int
    delimitter: str

    def __repr__(self):
        return f"{self.delimitter.title()}: {self.chapter} \n{self.text}\n"


class Text(BaseModel):
    part: Part
    name: str
