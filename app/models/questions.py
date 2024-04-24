from sqlalchemy import Column, Integer, String
from app.databases import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    subject = Column(String, index=True)
    correct = Column(String)
    use = Column(String, index=True)
    responseA = Column(String)
    responseB = Column(String)
    responseC = Column(String)
    responseD = Column(String, nullable=True)