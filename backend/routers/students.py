from fastapi import APIRouter, HTTPException, status #type: ignore
from db.models.student import Student
from db.schemas.student import student_schema, students_schema
from db.client import db_client
from bson import ObjectId #type:ignore

router = APIRouter(prefix='/student', tags=['students'])

#students_list = [Student(id=1,
#                         name='Juan',
#                         surname1='Apellido1',
#                         surname2='Apellido2',
#                         phone='666777888',
#                         age=12,
#                         courses=['Curso 1', 'Curso 2'],
#                         monthPaid=True,
#                         nextMonth=False),
#                Student(id=2,
#                         name='Pepe',
#                         surname1='Apellido1',
#                         surname2='Apellido2',
#                         phone='666777888',
#                         age=13,
#                         courses=['Curso 1', 'Curso 2'],
#                         monthPaid=True,
#                         nextMonth=False)]

@router.get('/', response_model=list[Student])
async def students():
    return students_schema(db_client.students.find())


@router.get('/{id}', response_model=Student)
async def get_student(id: str):
    return search_student(id)


@router.post('/', response_model = Student, status_code = status.HTTP_201_CREATED)
async def create_student(student: Student):
    if type(search_student_by_name(student.name, student.surname1, student.surname2)) == Student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Existing user")
    student_dict = dict(student)
    del student_dict['id']
    id = db_client.students.insert_one(student_dict).inserted_id
    new_student = student_schema(db_client.students.find_one({"_id": id}))
    return new_student
    

@router.put('/', response_model = Student)
async def put_student(student: Student):
    student_dict = dict(student)
    del student_dict['id']

    try:
        db_client.students.find_one_and_replace({"_id": ObjectId(student.id)}, student_dict)
    except:
        return search_student(id)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
async def delete_student(id: str):
    found = db_client.students.find_one_and_delete({'_id': ObjectId(id)})
    if not found:
        return {"error": "Not deleted"}


def search_student_by_name(name: str, surname1: str, surname2: str):
    try:
        student = db_client.students.find_one({'name': name, "surname1":surname1, "surname2":surname2})
        return Student(**student_schema(student))
    except:
        return {"error": "No se ha encontrado el usuario"}
    
def search_student(id: str):
    try:
        student = db_client.students.find_one({'_id': ObjectId(id)})
        return Student(**student_schema(student))
    except:
        return {"error": "No se ha encontrado el usuario"}