from pydantic import BaseModel


class FlashcardInfo(BaseModel):
    id: int
    name: str
    description: str | None = None
    user_id: int

    class Config:
        from_attributes = True


