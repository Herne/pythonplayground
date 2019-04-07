student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

try:
    print(student["lastname"])
except KeyError:
    print("key lastname doesn't exist")
print(student["name"])
print(student.get("name", "student not found"))
print(student.keys())
print(student.values())