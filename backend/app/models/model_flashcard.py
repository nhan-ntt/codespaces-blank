from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from .model_base import BareBase


class Flashcard(BareBase):
    __tablename__ = 'flashcards'

    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


    user = relationship('User', back_populates='flashcards')
    words = relationship('Word', secondary='flashcard_word', back_populates='flashcards')
