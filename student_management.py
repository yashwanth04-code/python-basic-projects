student_management.py
students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    students[roll] = name
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for roll, name in students.items():
            print(f"Roll: {roll}, Name: {name}")

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
