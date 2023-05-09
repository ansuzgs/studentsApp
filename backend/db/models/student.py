from pydantic import BaseModel #type: ignore
from typing import Optional

class Student(BaseModel):
    id: Optional[str]
    name: str
    surname1: str
    surname2: str
    phone: str
    age: int
    monthPaid: bool
    nextMonth: bool