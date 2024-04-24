from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.users import User
from app.models.questions import Question
from app.databases import Base, SessionLocal, engine
import pandas as pd

questions_data_df = pd.read_csv("./data/questions.csv").drop(columns=["remark"])
questions_data = questions_data_df.to_dict(orient="records")

users_data = [
    {"id": 1, "username": "alice", "password": "wonderland"},
    {"id": 2, "username": "bob", "password": "builder"},
    {"id": 3, "username": "clementine", "password": "mandarine"},
    {"id": 4, "username": "admin", "password": "4dm1N"},
]

# Tables creation
Base.metadata.create_all(bind=engine)
# Data ingestion in both tables (Question & User)
def ingest_data():
    try:
        for question_data in questions_data:
            question = Question(**question_data)
            SessionLocal.add(question)
        
        for user_data in users_data:
            user = User(**user_data)
            SessionLocal.add(user)

        SessionLocal.commit()
        print("Data ingested successfully.")
    except IntegrityError as e:
        SessionLocal.rollback()
        print(f"Error ingesting data: {e}")
    finally:
        SessionLocal.close()


if __name__ == "__main__":
    ingest_data()
