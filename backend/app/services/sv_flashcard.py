from sqlalchemy import insert, delete
from fastapi import HTTPException
from database import db_dependency
from models import Flashcard, Word
from models.model_base import flashcard_word_association
from schemas.schema_flashcard import FlashcardInfo, FlashcardUpdate
from schemas.schema_word import WordInfo, WordUpdate
from services.auth import user_dependency


# # read all flashcards of user <require authentication>
# async def read_Flashcard(db: db_dependency, user: user_dependency) -> list[FlashcardInfo]:
#     Flashcards = db.query(Flashcard).filter(Flashcard.user_id == user.id).all()
#     return Flashcards


async def read_Flashcard(db: db_dependency, user_id: int) -> list[FlashcardInfo]:
    Flashcards = db.query(Flashcard).filter(Flashcard.user_id == user_id).all()
    return Flashcards


# read flashcard by id
async def read_Flashcard_by_id(db: db_dependency, Flashcard_id: int) -> FlashcardInfo:
    flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    return flashcard


# create flashcard of user
async def create_Flashcard(db: db_dependency, user_id: int, flashcard: FlashcardUpdate) -> FlashcardInfo:
    new_Flashcard = Flashcard(
        name=flashcard.name,
        user_id=user_id,
        description=flashcard.description
    )
    db.add(new_Flashcard)
    db.commit()
    db.refresh(new_Flashcard)
    return new_Flashcard


async def udpate_flashcard(db: db_dependency, Flashcard_id: int, flashcard: FlashcardUpdate) -> FlashcardInfo:
    updating_Flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    if updating_Flashcard is None:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    if flashcard.name is not None:
        updating_Flashcard.name = flashcard.name
    if flashcard.description is not None:
        updating_Flashcard.description = flashcard.description
    db.commit()
    return updating_Flashcard


async def delete_Flashcard(db: db_dependency, Flashcard_id: int) -> None:
    # Fetch and delete associated words
    words = db.query(Word).filter(Word.flashcard_id == Flashcard_id).all()
    for word in words:
        db.delete(word)
    
    # Delete the flashcard
    flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    if flashcard:
        db.delete(flashcard)
    
    db.commit()



# # get all words of flashcard id many to many
# async def get_words(db: db_dependency, Flashcard_id: int) -> list[WordInfo]:
#     # words = db.query(flashcard_word_association).filter(flashcard_word_association.c.Flashcard_id == Flashcard_id).all()
#     words = (db.query(Word)
#              .join(flashcard_word_association)
#              .filter(flashcard_word_association.c.Flashcard_id == Flashcard_id)
#              .all())

#     return words


async def get_words(db: db_dependency, flashcard_id: int) -> list[WordInfo]:
    words = db.query(Word).filter(Word.flashcard_id == flashcard_id).all()
    return words


# # add word to flashcard many to many
# def add_word_to_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
#     stmt = insert(flashcard_word_association).values(Flashcard_id=Flashcard_id, word_id=word_id)
#     db.execute(stmt)
#     db.commit()
#     return None



# add word to flashcard 1 to many
async def add_word_to_flashcard(db: db_dependency, flashcard_id: int, word: WordUpdate) -> WordInfo:
    new_word = Word(
        word=word.word,
        meaning=word.meaning,
        kanji=word.kanji,
        flashcard_id=flashcard_id,
    )
    db.add(new_word)
    db.commit()
    db.refresh(new_word)
    return new_word

# def remove_word_from_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
#     stmt = delete(flashcard_word_association).where(
#         (flashcard_word_association.c.Flashcard_id == Flashcard_id) &
#         (flashcard_word_association.c.word_id == word_id)
#     )
#     db.execute(stmt)
#     db.commit()

async def update_word(db: db_dependency, word_id: int, word: WordUpdate) -> WordInfo:
    updating_word = db.query(Word).filter(Word.id == word_id).first()
    if updating_word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    if word.word is not None:
        updating_word.word = word.word
    if word.meaning is not None:
        updating_word.meaning = word.meaning
    if word.kanji is not None:
        updating_word.kanji = word.kanji
    db.commit()
    return updating_word


async def remove_word_from_Flashcard(db: db_dependency, word_id: int):
    word = db.query(Word).filter(Word.id == word_id).first()
    if word:
        db.delete(word)
        db.commit()
    return None