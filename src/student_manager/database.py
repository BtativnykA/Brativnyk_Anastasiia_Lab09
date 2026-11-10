"""Database connection and session management."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# База даних буде зберігатися у файлі students.db
DATABASE_URL = "sqlite:///students.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)