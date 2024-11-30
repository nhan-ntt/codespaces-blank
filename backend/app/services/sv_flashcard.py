from sqlalchemy import insert, delete

from database import db_dependency
from models import Flashcard, Word
from models.model_base import flashcard_word_association
from schemas.schema_flashcard import FlashcardInfo
from schemas.schema_word import WordInfo
from services.auth import user_dependency


# read all flashcards of user
async def read_Flashcard(db: db_dependency, user: user_dependency) -> list[FlashcardInfo]:
    Flashcards = db.query(Flashcard).filter(Flashcard.user_id == user.id).all()
    return Flashcards


# read flashcard by id
async def read_Flashcard_by_id(db: db_dependency, Flashcard_id: int) -> FlashcardInfo:
    Flashcard = db.query(Flashcard).filter(Flashcard.id == Flashcard_id).first()
    return Flashcard


# create flashcard of user
async def create_Flashcard(db: db_dependency, user: user_dependency, Flashcard: FlashcardInfo) -> FlashcardInfo:
    new_Flashcard = Flashcard(
        name=Flashcard.name,
        user_id=user.id,
        description=Flashcard.description
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


# add word to flashcard
def add_word_to_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
    stmt = insert(flashcard_word_association).values(Flashcard_id=Flashcard_id, word_id=word_id)
    db.execute(stmt)
    db.commit()
    return None


def remove_word_from_Flashcard(db: db_dependency, Flashcard_id: int, word_id: int):
    stmt = delete(flashcard_word_association).where(
        (flashcard_word_association.c.Flashcard_id == Flashcard_id) &
        (flashcard_word_association.c.word_id == word_id)
    )
    db.execute(stmt)
    db.commit()
