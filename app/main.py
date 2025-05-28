from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from starlette.status import HTTP_404_NOT_FOUND
from .utils import get_cached_url, set_cached_url
import time
from sqlalchemy.exc import OperationalError

# Wait for the database to be ready
for i in range(10):
    try:
        models.Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        print("⏳ Waiting for DB to be ready...")
        time.sleep(2)
        
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to the URL Shortener API! Visit /docs for Swagger UI."}
    
@app.post("/shorten", response_model=schemas.URLInfo)
def create_url(url_data: schemas.URLBase, db: Session = Depends(get_db)):
    try:
        return crud.create_short_url(db, url_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    # Check Redis first
    cached_url = get_cached_url(short_code)
    if cached_url:
        return RedirectResponse(url=cached_url, status_code=302)

    # Fallback to DB
    db_url = crud.get_url_by_code(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    # Cache and redirect
    set_cached_url(short_code, db_url.long_url)
    crud.increment_click_count(db, db_url)
    return RedirectResponse(url=db_url.long_url, status_code=302)

@app.get("/stats/{short_code}", response_model=schemas.URLInfo)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_code(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url
    
    crud.increment_click_count(db, db_url)
    return RedirectResponse(url=db_url.long_url, status_code=302)




