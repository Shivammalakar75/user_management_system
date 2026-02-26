from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from urllib.parse import quote_plus
password = quote_plus(settings.DB_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:"
    f"{password}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)
# print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

