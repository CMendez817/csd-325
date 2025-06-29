#Cameron Mendez
#06/28/2025
#Module 8.2

import json
import os

try:
    file_path = os.path.join(os.getcwd(), "students.json")
    print(f"Opening file: {file_path}")

    with open(file_path, 'r') as file:
        student_list = json.load(file)

    def print_students(students):
        for student in students:
            first = student.get('F_Name', 'Unknown')
            last = student.get('L_Name', 'Unknown')
            sid = student.get('Student_ID', 'N/A')
            email = student.get('Email', 'N/A')
            print(f"{last}, {first} : ID = {sid} , Email = {email}")

    print("\nOriginal Student List:")
    print_students(student_list)

    # Add your info - match the key names exactly
    new_student = {
        "F_Name": "Cameron",
        "L_Name": "Mendez",
        "Student_ID": 99999,
        "Email": "camendez@my365.bellevue.edu"
    }

    student_list.append(new_student)

    print("\nUpdated Student List:")
    print_students(student_list)

    with open(file_path, 'w') as file:
        json.dump(student_list, file, indent=4)

    print("\n The student.json file has been updated.")

except Exception as e:
    print("\n An error occurred:")
    print(e)

input("\nPress Enter to exit...")
