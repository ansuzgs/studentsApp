from motor.motor_asyncio import AsyncIOMotorClient #type: ignore
from models import Student
from models import Todo

client = AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.BibiApp2
collection = database.students

async def fetch_one_student(id: int):
    document = await collection.find_one({'id': id})
    return document

async def fetch_all_students():
    students = []
    cursor = collection.find({})
    async for document in cursor:
        students.append(Student(**document))
    return students

async def create_todo(todo: Todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def create_student(student: Student):
    document = student
    result = await collection.insert_one(document)
    return document

async def update_student(student: Student):
    await collection.update_one(student)
    document = await collection.find_one({"id": student.id})
    return document

async def remove_student(id: int):
    await collection.delete_one({'id': id})
    return True