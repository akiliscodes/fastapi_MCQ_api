from typing import List
from fastapi import FastAPI, HTTPException, Depends, status, Query
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import random
import uvicorn
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.questions import Question
from app.models.users import User

from app.databases import engine
from app.models.schemas import (
    HealthCheck,
    QuestionsRequests,
    ResponseQuestions,
    AddNewQuestion,
    QuestionAdded,
    VerifyUser,
)
from app.utils.helpers import authenticate_user, request_questions, insert_question

security = HTTPBasic()

app = FastAPI(
    openapi_tags=[
        {
            "name": "Health Check",
            "description": "Functions that are used to check API health",
        },
        {
            "name": "Request Questions",
            "description": "Functions that are used to request MCQ questions",
        },
        {
            "name": "Administration",
            "description": "Functions that are used to manage users and questions",
        },
    ],
    title="MCQ questions API",
    description="API to request MCQ questions",
    version="0.0.1",
)


@app.get(
    "/health",
    tags=["Health Check"],
    name="Health Check",
    description="Check wether the API is working",
    response_description="Returns HTTP Status Code 200",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return HealthCheck(status="live")


@app.post(
    "/questions",
    tags=["Request Questions"],
    name="Request questions",
    summary="Request MCQ questions",
    description="This route requests MCQ questions",
    status_code=status.HTTP_200_OK,
    response_model=List[ResponseQuestions],
)
def get_questions(
    questions_requests: QuestionsRequests,
    credentials: HTTPBasicCredentials = Depends(security),
):
    username = credentials.username
    password = credentials.password

    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    filtered_questions = request_questions(questions_requests)
    if not filtered_questions:
        raise HTTPException(status_code=422, detail="Not enough questions available")
    random.shuffle(filtered_questions)
    return filtered_questions


@app.get(
    "/admin/verify",
    tags=["Administration"],
    name="Verify credentials",
    summary="Verify users credentials",
    description="Verify users credentials",
    status_code=status.HTTP_200_OK,
)
def verify_credentials(
    credentials_to_verify: VerifyUser =Depends(VerifyUser),
    credentials: HTTPBasicCredentials = Depends(security),
):
    if not authenticate_user(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not authenticate_user(
        credentials_to_verify.username, credentials_to_verify.password
    ):
        raise HTTPException(
            status_code=401,
            detail=f"User credentials pair ({credentials_to_verify.username}, {credentials_to_verify.password}) are not valid!",
        )
    return {"message": "Credentials are valid"}


@app.post(
    "/admin/add_question",
    tags=["Administration"],
    name="Add question",
    summary="Add new question",
    description="Add new question",
    status_code=status.HTTP_200_OK,
)
def add_question(
    question: AddNewQuestion,
    credentials: HTTPBasicCredentials = Depends(security),
):
    username = credentials.username
    password = credentials.password
    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if username != "admin" or password != "4dm1N":
        raise HTTPException(status_code=403, detail="Permission denied")
    if not insert_question(question):
        raise HTTPException(status_code=500, detail=f"Failed to add question")
    return QuestionAdded(message="Question added successfully")


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
