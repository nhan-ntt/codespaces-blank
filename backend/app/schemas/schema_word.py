from pydantic import BaseModel


class WordInfo(BaseModel):
    id: int
    word: str 
    meaning: str 
    flashcard_id: int
    kanji: str | None = None

    class Config:
        from_attributes = True


class WordUpdate(BaseModel):
    word: str 
    meaning: str 
    kanji: str | None = None

    class Config:
        from_attributes = True
