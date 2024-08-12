
# Student Management System 📝
![student-management-system](https://github.com/zahariev-webbersof/python-fundamentals-05-2024/assets/68993494/746ccfd8-f414-4714-96f9-e9d704cce587)

The goal of this project is to create a simple student management system using Python. This system will allow users to add, update, delete, and search for student records. Each student record will include information such as name, age, grade, and subjects. 


## ✅ Project Requirements

- Data Types and Variables

- Understand and use different data types including strings, integers, floats, booleans, lists, dictionaries, sets, and tuples.
Tasks to Implement

- Add Student:
Create a function to add a new student record. Each record should include the student's name (string), age (int), grade (float), and subjects (list of strings).
- Update Student:
Create a function to update an existing student record. Allow updating of any of the fields (name, age, grade, subjects).
- Delete Student:
Create a function to delete a student record based on the student's name.
- Search Student:
Create a function to search for a student by name and return their record.
- List All Students:
Create a function to list all student records.

## ✅ Documentation and Comments

Include comments explaining each function and its purpose.
Provide documentation strings for each function, describing the parameters and return values.
User Interaction

Create a main program that prompts the user to choose which task they want to perform.
Use input prompts to gather the necessary data from the user.
Display the results of the chosen task in a clear and user-friendly manner.

## Explanation

    Data Structure:
        The program uses a dictionary students to store student records. Each record contains a dictionary with keys: 'age', 'grade', and 'subjects'.

    Functions:
        add_student: Adds a new student record if the student doesn't already exist.
        update_student: Updates an existing student record by allowing the user to change age, grade, or subjects.
        delete_student: Deletes a student record if it exists.
        search_student: Searches and displays a student record.
        list_all_students: Lists all students in alphabetical order by their name.

    Main Loop:
        The main function provides a loop that prompts the user for actions and calls the corresponding functions based on the user's choice.
        User inputs are validated to ensure that ages are integers and grades are floats.

    Error Handling:
        Error handling is included to manage invalid input types for age and grade using try and except.
        Each function checks for the existence of a student before performing actions like update, delete, or search.

    User Interaction:
        The user interface is text-based and prompts users with clear instructions for each operation.
        Results are displayed in a user-friendly manner with proper formatting.
