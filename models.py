from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Anime(Base):
    __tablename__ = 'anime'  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    anime_title = Column(String(100), nullable=False)  # Anime title
    anime_genre = Column(String(50))  # Genre of the anime
    anime_release_date = Column(Integer)  # Release year of the anime
