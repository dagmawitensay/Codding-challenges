from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class UrlMapping(Base):
    """
    Database model for storing URL mappings.
    """
    __tablename__ = "urls"
    
    key = Column(String(7), primary_key=True, index=True, unique=True, nullable=False)
    short_url = Column(String(50), index=True, unique=True, nullable=False)
    long_url = Column(String(150), index=True, nullable=False)
    creation_date = Column(TIMESTAMP, index=True, nullable=False, server_default=func.now())