from sqlalchemy.orm import Session
from . import models, schemas
import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def create_short_url(db: Session, url_data: schemas.URLBase) -> models.URL:
    if url_data.custom_alias:
        if db.query(models.URL).filter_by(short_code=url_data.custom_alias).first():
            raise ValueError("Custom alias already in use.")
        short_code = url_data.custom_alias
    else:
        short_code = generate_short_code()
        while db.query(models.URL).filter_by(short_code=short_code).first():
            short_code = generate_short_code()

    db_url = models.URL(
    long_url=str(url_data.long_url),  # Convert HttpUrl to str
    short_code=short_code,
    expires_at=url_data.expires_at)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

def increment_click_count(db: Session, url: models.URL):
    url.click_count += 1
    db.commit()
    db.refresh(url)
    return url

