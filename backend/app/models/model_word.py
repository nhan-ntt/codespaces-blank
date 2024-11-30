from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .model_base import BareBase


class Word(BareBase):
    __tablename__ = 'words'

    word = Column(String, index=True, nullable=False)
    meaning = Column(String, index=True, nullable=False)
    kanji = Column(String, index=True)

    flashcards = relationship('Flashcard', secondary='flashcard_word', back_populates='words')
