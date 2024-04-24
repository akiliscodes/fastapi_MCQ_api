from pydantic import BaseModel
from typing import List, Annotated, Union
from fastapi import Query
from typing import Optional
from pydantic import Field


class HealthCheck(BaseModel):
    status: str = "live"

class VerifyUser(BaseModel):
    username: str = Field(None, example="alice", description="Username")
    password: str = Field(None, example="wonderland", description="Username")

class QuestionAdded(BaseModel):
    message: str = "Question added successfully"

class QuestionsRequests(BaseModel):
    use: str = Field(None, example="Test de positionnement", description="Type of MCQ")
    subjects: Optional[List[str]] = Field(
        None, example=["BDD"], description="Question category"
    )
    num_questions: int = Field(
        None, example=3, description="Number of questions to return"
    )

class AddNewQuestion(BaseModel):
    question: str = Field(
        None,
        example="Cassandra et HBase sont des bases de données",
        description="Type of MCQ",
    )
    subject: str = Field(None, example="BDD", description="")
    use: str = Field(None, example="Test de positionnement", description="")
    responseA: str = Field(
        None, example="relationnelles", description="Avalaible option for the question"
    )
    responseB: str = Field(
        None, example="orientées objet", description="Avalaible option for the question"
    )
    responseC: str = Field(
        None,
        example="orientées colonne",
        description="Avalaible option for the question",
    )
    responseD: Optional[str] = Field(
        None,
        example="orientées graphe",
        description="Avalaible option for the question",
        nullable=True,
    )
    correct: str = Field(None, example="C", description="Identifies the correct answer")


class ResponseQuestions(AddNewQuestion):
    id: int = Field(None, example=1, description="Identifier of the question")

class ResponseQuestionsValidationError(BaseModel):
    pass
