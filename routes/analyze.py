from fastapi import APIRouter
from models.schemas import RequestSchema
from services.engine import analyze_case

router = APIRouter()

@router.post("/analyze")
def analyze(data: RequestSchema):
    return analyze_case(data)