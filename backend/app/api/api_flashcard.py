from fastapi import APIRouter, HTTPException

from database import db_dependency
from schemas.schema_flashcard import FlashcardInfo, FlashcardUpdate
from schemas.schema_word import WordInfo, WordUpdate
from services import sv_flashcard
from services.auth import user_dependency
from starlette import status


router = APIRouter(tags=["Flashcards"], prefix="/flashcard")


# @router.get("/all/", response_model=dict[str, list[FlashcardInfo]])
# async def get_Flashcards(user: user_dependency, db: db_dependency) -> dict[str, list[FlashcardInfo]]:
#     """
#     API Read Flashcard
#     """
#     Flashcards = await sv_flashcard.read_Flashcard(db, user)
#     return {"list": Flashcards}


@router.get("/all/{user_id}", response_model=dict[str, list[FlashcardInfo]])
async def get_Flashcards(user_id: int, db: db_dependency) -> dict[str, list[FlashcardInfo]]:
    """
    API Read Flashcard
    """
    Flashcards = await sv_flashcard.read_Flashcard(db, user_id)
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


@router.post("", response_model=FlashcardInfo, status_code=status.HTTP_201_CREATED)
async def create_Flashcard(Flashcard: FlashcardUpdate, db: db_dependency, user_id: int) -> FlashcardInfo:
    """
    API Create Flashcard
    """
    return await sv_flashcard.create_Flashcard(db, user_id, Flashcard)


@router.put("/{Flashcard_id}", response_model=FlashcardInfo)
async def update_Flashcard(Flashcard_id: int, Flashcard: FlashcardUpdate, db: db_dependency) -> FlashcardInfo:
    """
    API Update Flashcard
    """
    return await sv_flashcard.udpate_flashcard(db, Flashcard_id, Flashcard)

@router.delete("/{Flashcard_id}")
async def delete_Flashcard(Flashcard_id: int, db: db_dependency) -> None:
    """
    API Delete Flashcard
    """
    return await sv_flashcard.delete_Flashcard(db, Flashcard_id)



@router.get("/{flashcard_id}", response_model=dict[str, list[WordInfo]])
async def get_words_of_flashcard(flashcard_id: int, db: db_dependency) -> dict[str, list[WordInfo]]:
    """
    API Read Flashcard
    """
    words = await sv_flashcard.get_words(db, flashcard_id)
    return {"list": words}



@router.post("/{Flashcard_id}/words/", response_model=WordInfo, status_code=status.HTTP_201_CREATED)
async def add_word_to_Flashcard(db: db_dependency,Flashcard_id: int, word: WordUpdate) -> WordInfo:
    """
    API Add word to Flashcard
    """

    return await sv_flashcard.add_word_to_flashcard(db, Flashcard_id, word)



@router.put("/words/{word_id}", response_model=WordInfo)
async def update_word(word_id: int, word: WordUpdate, db: db_dependency) -> WordInfo:
    """
    API Update word
    """
    return await sv_flashcard.update_word(db, word_id, word)



@router.delete("/words/{word_id}")
async def remove_word_from_Flashcard(word_id: int, db: db_dependency):
    """
    API Remove word from Flashcard
    """
    sv_flashcard.remove_word_from_Flashcard(db, word_id)
    return {"message": "word removed from Flashcard",
            "word_id": word_id}
