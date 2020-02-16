student = {"name": "Mark", "student_id": 15163, "feedback": None, "lastname": "Kowalski"}

try:
    last_name = student["lastname"]
    print(last_name)
    numbered_last_name = 3 + last_name
except KeyError:
    print("key lastname doesn't exist")
except TypeError as error:
    print("I can't add these 2 together!")
    print(error)
print(student["name"])
print(student.get("name", "student not found"))
print(student.keys())
print(student.values())
