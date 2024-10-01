from sqlalchemy.orm import Session
from models import Anime

# Get all Anime entries
def get_anime(db: Session):
    return db.query(Anime).all()

# Get Anime by ID
def get_anime_by_id(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()

# Create a new Anime entry
def create_anime(db: Session, title: str, genre: str, release_date: int):
    db_anime = Anime(anime_title=title, anime_genre=genre, anime_release_date=release_date)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

# Update Anime entry
def update_anime(db: Session, anime_id: int, title: str, genre: str, release_date: int):
    db_anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if db_anime:
        db_anime.anime_title = title
        db_anime.anime_genre = genre
        db_anime.anime_release_date = release_date
        db.commit()
        db.refresh(db_anime)
    return db_anime

# Delete Anime entry
def delete_anime(db: Session, anime_id: int):
    db_anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if db_anime:
        db.delete(db_anime)
        db.commit()
    return db_anime
