from app.database import Base, engine
from app.models.url_mapping import UrlMapping

print("Creating database table")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
