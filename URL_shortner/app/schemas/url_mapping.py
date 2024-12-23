from pydantic import BaseModel
from datetime import datetime

class UrlMapping(BaseModel):
    key: str
    short_url: str
    long_url: str
    creation_date: datetime

    class Config:
        orm_mode = True
