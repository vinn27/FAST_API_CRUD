from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from anime_crud import get_anime, get_anime_by_id, create_anime, update_anime, delete_anime
from models import Anime

app = FastAPI()

# Get all anime
@app.get("/anime/")
def read_anime(db: Session = Depends(get_db)):
    return get_anime(db)

# Get anime by ID
@app.get("/anime/{anime_id}")
def read_anime_by_id(anime_id: int, db: Session = Depends(get_db)):
    anime = get_anime_by_id(db, anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime

# Create new anime
@app.post("/anime/")
def create_anime_entry(title: str, genre: str, release_date: int, db: Session = Depends(get_db)):
    return create_anime(db, title, genre, release_date)

# Update anime
@app.put("/anime/{anime_id}")
def update_anime_entry(anime_id: int, title: str, genre: str, release_date: int, db: Session = Depends(get_db)):
    return update_anime(db, anime_id, title, genre, release_date)

# Delete anime
@app.delete("/anime/{anime_id}")
def delete_anime_entry(anime_id: int, db: Session = Depends(get_db)):
    return delete_anime(db, anime_id)
