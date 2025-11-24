# Module 1: User Management
students = []

def add_student(name, marks):
    student = {"name": name, "marks": marks}
    students.append(student)
    print(f"✅ Student {name} added successfully!")

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}")
    return students
