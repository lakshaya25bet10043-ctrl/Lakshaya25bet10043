# Module 3: Reporting
def generate_report(students, average):
    print("\n=== Student Report ===")
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {average:.2f}" if average else "No data available")
    print("Performance:")
    for s in students:
        status = "Pass" if s["marks"] >= 40 else "Fail"
        print(f"{s['name']} - {status}")
