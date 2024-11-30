from pydantic import BaseModel


class WordInfo(BaseModel):
    id: int
    word: str 
    meaning: str 
    kanji: int | None = None

    class Config:
        from_attributes = True


