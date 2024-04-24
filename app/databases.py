from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.exc import IntegrityError

# Define database connection URL
DATABASE_URL = "sqlite:///./data/qcm_database.db"

# Create DB engine
engine = create_engine(DATABASE_URL)

# Create DB session
SessionLocal = Session(bind=engine)

Base = declarative_base()