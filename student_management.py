import json
import os

FILE_NAME = "students.json"

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")

# View students
def view_students(students):
    if not students:
        print("No student records found.")
    else:
        print("\n===== STUDENT RECORDS =====")
        for student in students:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print("-" * 30)

# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["marks"] = input("Enter new marks: ")

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")

# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")

# Main program
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

main()