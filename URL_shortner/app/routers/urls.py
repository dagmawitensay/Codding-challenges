from fastapi import APIRouter, Depends, Request
from app.schemas.request import UrlRequest
from app.crud.url import get_long_url_helper, shorten_url, delete_url_helper
from app.dependencies import get_db

router = APIRouter()

@router.get("/{short_url_key}")
def get_long_url(short_url_key: str, db=Depends(get_db)):
    """
    Redirects to the long URL associated with the given short URL key.
    """
    return get_long_url_helper(db, short_url_key)

@router.post("/shorten")
def shorten_url_endpoint(url_request: UrlRequest, request: Request, db=Depends(get_db),):
    """
    Creates a short URL for the provided long URL and returns the mapping.
    """
    return shorten_url(db, url_request, request)

@router.delete("/{short_url_key}")
def delete_url(short_url_key: str, db=Depends(get_db)):
    """
    Deletes the URL mapping associated with the given short URL key.
    """
    return delete_url_helper(db, short_url_key)
