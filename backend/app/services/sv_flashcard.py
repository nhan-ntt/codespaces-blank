from sqlalchemy import insert, delete

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
    Flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    return Flashcard


# create flashcard of user
async def create_Flashcard(db: db_dependency, user: user_dependency, flashcard: FlashcardUpdate) -> FlashcardInfo:
    new_Flashcard = Flashcard(
        name=flashcard.name,
        user_id=user.id,
        description=flashcard.description
    )
    db.add(new_Flashcard)
    db.commit()
    db.refresh(new_Flashcard)
    return new_Flashcard


async def delete_Flashcard(db: db_dependency, Flashcard_id: int):
    Flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    db.delete(Flashcard)
    db.commit()
    return


# get all words of flashcard id 
async def get_words(db: db_dependency, Flashcard_id: int) -> list[WordInfo]:
    # words = db.query(flashcard_word_association).filter(flashcard_word_association.c.Flashcard_id == Flashcard_id).all()
    words = (db.query(Word)
             .join(flashcard_word_association)
             .filter(flashcard_word_association.c.Flashcard_id == Flashcard_id)
             .all())

    return words


# # add word to flashcard many to many
# def add_word_to_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
#     stmt = insert(flashcard_word_association).values(Flashcard_id=Flashcard_id, word_id=word_id)
#     db.execute(stmt)
#     db.commit()
#     return None


# add word to flashcard 1 to many
def add_word_to_flashcard(db: db_dependency, flashcard_id: int, word: WordUpdate) -> WordInfo:
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

def remove_word_from_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
    stmt = delete(flashcard_word_association).where(
        (flashcard_word_association.c.Flashcard_id == Flashcard_id) &
        (flashcard_word_association.c.word_id == word_id)
    )
    db.execute(stmt)
    db.commit()
