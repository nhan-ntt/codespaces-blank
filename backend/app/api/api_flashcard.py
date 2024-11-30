from fastapi import APIRouter, HTTPException

from database import db_dependency
from schemas.schema_flashcard import FlashcardInfo
from schemas.schema_word import WordInfo
from services import sv_flashcard
from services.auth import user_dependency

router = APIRouter(tags=["Flashcards"], prefix="/flashcard")


@router.get("all/", response_model=dict[str, list[FlashcardInfo]])
async def get_Flashcards(user: user_dependency, db: db_dependency) -> dict[str, list[FlashcardInfo]]:
    """
    API Read Flashcard
    """
    Flashcards = await sv_flashcard.read_Flashcard(db, user)
    return {"list": Flashcards}


@router.get("/{Flashcard_id}", response_model=FlashcardInfo)
async def get_Flashcard_by_id(Flashcard_id: int, db: db_dependency) -> FlashcardInfo:
    """
    API Read Flashcard by id
    """
    Flashcard = await sv_flashcard.read_Flashcard_by_id(db, Flashcard_id)
    if Flashcard is None:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return Flashcard


@router.post("", response_model=FlashcardInfo)
async def create_Flashcard(Flashcard: FlashcardInfo, db: db_dependency, user: user_dependency) -> FlashcardInfo:
    """
    API Create Flashcard
    """
    return await sv_flashcard.create_Flashcard(db, user, Flashcard)


@router.delete("/{Flashcard_id}")
async def delete_Flashcard(Flashcard_id: int, db: db_dependency, user: user_dependency) -> None:
    """
    API Delete Flashcard
    """
    return await sv_flashcard.delete_Flashcard(db, Flashcard_id)


@router.get("/{Flashcard_id}/words", response_model=dict[str, list[WordInfo]])
async def get_words(Flashcard_id: int, db: db_dependency) -> dict[str, list[WordInfo]]:
    """
    API Get words
    """
    words = await sv_flashcard.get_words(db, Flashcard_id)
    return {"list": words}


@router.post("/{Flashcard_id}/words/{word_id}")
async def add_word_to_Flashcard(Flashcard_id: int, word_id: int, db: db_dependency):
    """
    API Add word to Flashcard
    """

    sv_flashcard.add_word_to_Flashcard(db, Flashcard_id, word_id)
    return {"message": "word added to Flashcard",
            "Flashcard_id": Flashcard_id,
            "word_id": word_id}


@router.delete("/{Flashcard_id}/words/{word_id}")
async def remove_word_from_Flashcard(Flashcard_id: int, word_id: int, db: db_dependency):
    """
    API Remove word from Flashcard
    """
    sv_flashcard.remove_word_from_Flashcard(db, Flashcard_id, word_id)
    return {"message": "word removed from Flashcard",
            "Flashcard_id": Flashcard_id,
            "word_id": word_id}
