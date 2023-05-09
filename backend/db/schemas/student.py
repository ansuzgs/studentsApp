def student_schema(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "surname1": student["surname1"],
        "surname2": student["surname2"],
        "phone": student["phone"],
        "age": student["age"],
        "monthPaid": student["monthPaid"],
        "nextMonth": student["nextMonth"]        
    }

def students_schema(students) -> list:
    return [student_schema(student) for student in students]