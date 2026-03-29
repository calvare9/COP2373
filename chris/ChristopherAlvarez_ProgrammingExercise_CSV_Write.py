"""
Write Grades Program - Christopher Alvarez

This program allows an instructor to enter student names
and three exam grades, then stores the data in grades.csv.
"""

import csv


# This function collects student data and writes it to a CSV file
def write_grades():

    num_students = int(input("Enter number of students: "))

    # Open file in write mode
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student
        for i in range(num_students):
            print("\nStudent", i + 1)

            first = input("First name: ")
            last = input("Last name: ")

            exam1 = int(input("Exam 1: "))
            exam2 = int(input("Exam 2: "))
            exam3 = int(input("Exam 3: "))

            # Write student record
            writer.writerow([first, last, exam1, exam2, exam3])


# Run the program
write_grades()
