from pydantic import BaseModel

class UrlRequest(BaseModel):
    long_url: str