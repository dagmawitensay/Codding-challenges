from pydantic import BaseModel

class UrlResponse(BaseModel):
    key: str
    long_url: str
    short_url: str