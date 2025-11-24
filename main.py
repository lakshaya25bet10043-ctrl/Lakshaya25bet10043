# Main file to run all modules
from user_management import add_student, list_students
from data_processing import calculate_average
from reporting import generate_report

def main():
    # Adding students
    add_student("mami", 60)
    add_student("Lakshaya", 95)
    add_student("sri", 72)
    add_student("hachu", 100)

    # Listing students
    students = list_students()

    # Processing data
    average = calculate_average(students)

    # Generating report
    generate_report(students, average)

if __name__ == "__main__":
    main()
