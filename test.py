import pytest
from fastapi.testclient import TestClient
from app import app  # Adjust the import if your app is in a different module
from database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Test database URL - Change the credentials as needed
TEST_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/anime_db"

# Set up the test database
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database and tables
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Test cases
def test_create_anime():
    response = client.post("/anime/", json={"title": "Naruto", "genre": "Action", "release_date": 2002})
    assert response.status_code == 201
    assert response.json()["title"] == "Naruto"

def test_read_anime():
    # First create an anime
    create_response = client.post("/anime/", json={"title": "Naruto", "genre": "Action", "release_date": 2002})
    anime_id = create_response.json()["id"]  # Get the ID of the created anime

    # Now read it
    response = client.get(f"/anime/{anime_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Naruto"

def test_update_anime():
    # First create an anime
    create_response = client.post("/anime/", json={"title": "Naruto", "genre": "Action", "release_date": 2002})
    anime_id = create_response.json()["id"]  # Get the ID of the created anime

    # Now update it
    response = client.put(f"/anime/{anime_id}", json={"title": "Naruto Shippuden", "genre": "Action", "release_date": 2007})
    assert response.status_code == 200
    assert response.json()["title"] == "Naruto Shippuden"

def test_delete_anime():
    # First create an anime
    create_response = client.post("/anime/", json={"title": "Naruto", "genre": "Action", "release_date": 2002})
    anime_id = create_response.json()["id"]  # Get the ID of the created anime

    # Now delete it
    response = client.delete(f"/anime/{anime_id}")
    assert response.status_code == 204

    # Try to read the deleted anime
    read_response = client.get(f"/anime/{anime_id}")
    assert read_response.status_code == 404
