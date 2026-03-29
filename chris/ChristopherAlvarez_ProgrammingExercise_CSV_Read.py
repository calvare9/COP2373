"""
Read Grades Program - Christopher Alvarez

This program reads the grades.csv file and displays
the student data in a tabular format.
"""

import csv


# This function reads the CSV file and displays formatted output
def read_grades():

    print("\nStudent Grades:\n")

    # Open file in read mode
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Read header
        header = next(reader)

        # Print header in table format
        print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(
            header[0], header[1], header[2], header[3], header[4]
        ))

        print("-" * 60)

        # Print each row formatted
        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(
                row[0], row[1], row[2], row[3], row[4]
            ))


# Run the program
read_grades()