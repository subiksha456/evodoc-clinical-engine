from pydantic import BaseModel
from typing import List

class PatientHistory(BaseModel):
    current_medications: List[str]
    allergies: List[str]
    conditions: List[str]
    age: int
    weight: float

class RequestSchema(BaseModel):
    medications: List[str]
    patient_history: PatientHistory