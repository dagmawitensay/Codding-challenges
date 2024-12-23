from fastapi import HTTPException, Response, Request
from starlette.status import HTTP_404_NOT_FOUND, HTTP_302_FOUND, HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from app.models.url_mapping import UrlMapping
from app.schemas.request import UrlRequest
from app.schemas.response import UrlResponse
from app.utils.hash import shorten_url_helper
from datetime import datetime

def get_long_url_helper(db: Session, short_url_key: str):
    """
    Retrieves the original long URL for a given short URL key and redirects to it.
    """
    record = db.query(UrlMapping).filter(UrlMapping.key == short_url_key).first()
    if not record:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="URL not found")
    return Response(
        headers={"Location": record.long_url},
        status_code=HTTP_302_FOUND,
    )

def shorten_url(db: Session, url_request: UrlRequest, request: Request) -> UrlResponse:
    """
    Shortens a long URL and saves it in the database.
    """
    host_url = str(request.base_url)
    shortend_url = shorten_url_helper(url_request.long_url)
    short_url = f"{host_url}{shortend_url}"
    db_item = UrlMapping(
        key=shortend_url,
        long_url=url_request.long_url,
        short_url=short_url,
        creation_date=datetime.now(),
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return UrlResponse(
        key=shortend_url,
        long_url=db_item.long_url,
        short_url=db_item.short_url
    )

def delete_url_helper(db: Session, short_url_key: str) -> Response:
    """
    Deletes a URL mapping based on the short URL key.
    """
    record = db.query(UrlMapping).filter(UrlMapping.key == short_url_key).first()
    if not record:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="URL not found")

    db.delete(record)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
