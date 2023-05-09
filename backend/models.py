from pydantic import BaseModel #type: ignore

class Student(BaseModel):
    id: int
    name: str
    surname1: str
    surname2: str
    phone: str
    age: int
    monthPaid: bool
    nextMonth: bool

class Todo(BaseModel):
    title: str
    desc: str