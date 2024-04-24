from fastapi import HTTPException
from sqlalchemy import select, func

from app.databases import SessionLocal
from app.models.users import User
from app.models.questions import Question
from app.models.schemas import QuestionsRequests, AddNewQuestion

def authenticate_user(username: User, password: User):
    session = SessionLocal
    try:
        user = session.execute(select(User).filter(User.username == username)).scalar()

        if user and user.password == password:
            return True
        else:
            print("Invalid username or password.")
            return False
    except Exception as e:
        print(f"Error verifying user credentials: {e}")


def request_questions(questions_requests: QuestionsRequests):
    session = SessionLocal
    try:
        use = questions_requests.use
        subjects = questions_requests.subjects
        num_questions = questions_requests.num_questions
        stmt = (
            select(Question)
            .where(func.lower(Question.use) == use.lower())
            .where(func.lower(Question.subject).in_([x.lower() for x in subjects]))
            .limit(num_questions)
        )
        filtered_questions = session.execute(stmt).scalars().all()
        if len(filtered_questions) < num_questions:
            return False
        return filtered_questions
    except Exception as e:
        print("An error has occured")

def insert_question(question: AddNewQuestion):
    session = SessionLocal
    try:
        question = question.model_dump()
        new_question = Question(**question)
        session.add(new_question)
        session.commit()
        session.refresh(new_question) 
        return True
    except Exception as e:
        session.rollback()
        return False


