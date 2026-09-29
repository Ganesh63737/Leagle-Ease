from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.generator import generate_answer

router = APIRouter()


class LegalQuestion(BaseModel):
    question: str


@router.post("/ask")
def ask_question(data: LegalQuestion):
    answer = generate_answer(data.question)

    return {
        "question": data.question,
        "answer": answer
    }