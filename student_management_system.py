# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    if name in students:
        print(f"Student '{name}' already exists.")
    else:
        students[name] = {
            'age': age,
            'grade': grade,
            'subjects': subjects
        }
        print(f"Student '{name}' added successfully.")


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    if name not in students:
        print(f"Student '{name}' does not exist.")
    else:
        age = input("Enter new age (leave blank to keep current): ")
        grade = input("Enter new grade (leave blank to keep current): ")
        subjects = input("Enter new subjects (comma-separated, leave blank to keep current): ")

        if age:
            students[name]['age'] = int(age)
        if grade:
            students[name]['grade'] = float(grade)
        if subjects:
            students[name]['subjects'] = subjects.split(',')

        print(f"Student '{name}' updated successfully.")


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    if name not in students:
        print(f"Student '{name}' does not exist.")
    else:
        del students[name]
        print(f"Student '{name}' deleted successfully.")


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    if name not in students:
        print(f"Student '{name}' does not exist.")
    else:
        student = students[name]
        print(f"Name: {name}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print(f"Subjects: {', '.join(student['subjects'])}")


def list_all_students():
    """
    List all student records.
    """
    if not students:
        print("No student records available.")
    else:
        for name, details in sorted(students.items()):
            print(f"Name: {name}")
            print(f"Age: {details['age']}")
            print(f"Grade: {details['grade']}")
            print(f"Subjects: {', '.join(details['subjects'])}")
            print("-" * 20)


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            try:
                age = int(input("Enter student's age: "))
                grade = float(input("Enter student's grade: "))
            except ValueError:
                print("Invalid input for age or grade. Please enter valid numbers.")
                continue
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
