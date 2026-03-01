students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")
        print()


def search_student():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student["roll"] == roll:
            print(f"Found: {student}")
            return
    print("Student not found.\n")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
