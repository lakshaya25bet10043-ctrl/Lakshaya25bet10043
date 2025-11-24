# Module 2: Data Processing
def calculate_average(students):
    if not students:
        print("⚠️ No students available to calculate average.")
        return None
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print(f"📊 Average Marks: {avg:.2f}")
    return avg
