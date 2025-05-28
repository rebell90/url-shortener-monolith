from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLBase(BaseModel):
    long_url: HttpUrl
    expires_at: Optional[datetime] = None
    custom_alias: Optional[str] = None

class URLInfo(BaseModel):
    id: int
    long_url: HttpUrl
    short_code: str
    created_at: datetime
    expires_at: Optional[datetime]
    click_count: int

    class Config:
        from_attributes = True  # Pydantic v2
