"""
NumPy Grades Analysis Program
Christopher Alvarez

This program reads student grade data from a CSV file and uses NumPy
to perform statistical analysis. It calculates statistics for each exam
and overall performance, including pass/fail counts.
"""

import csv
import numpy as np


# This function loads grade data from a CSV file into a NumPy array
def load_grades(filename):

    data = []

    # Open file in read mode
    with open(filename, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header row

        # Loop through each row in file
        for row in reader:
            # Extract exam scores and convert to integers
            exams = [int(row[2]), int(row[3]), int(row[4])]
            data.append(exams)

    # Convert list to NumPy array
    return np.array(data)


# This function performs statistical analysis on the grades
def analyze_grades(grades):

    print("\nFirst few rows of data:")
    print(grades[:5])  # Display first 5 rows

    print("\n--- Statistics Per Exam ---")

    # Loop through each exam column
    for i in range(3):
        column = grades[:, i]

        print(f"\nExam {i + 1}:")
        print("Mean:", np.mean(column))
        print("Median:", np.median(column))
        print("Standard Deviation:", np.std(column))
        print("Minimum:", np.min(column))
        print("Maximum:", np.max(column))

    print("\n--- Overall Statistics ---")

    # Combine all grades into one array
    all_grades = grades.flatten()

    print("Mean:", np.mean(all_grades))
    print("Median:", np.median(all_grades))
    print("Standard Deviation:", np.std(all_grades))
    print("Minimum:", np.min(all_grades))
    print("Maximum:", np.max(all_grades))

    print("\n--- Pass/Fail Per Exam ---")

    # Calculate pass/fail per exam
    for i in range(3):
        column = grades[:, i]

        passed = np.sum(column >= 60)
        failed = np.sum(column < 60)

        print(f"Exam {i + 1}: Passed = {passed}, Failed = {failed}")

    print("\n--- Overall Pass Percentage ---")

    total = all_grades.size
    passed_total = np.sum(all_grades >= 60)

    percent = (passed_total / total) * 100
    print("Pass Percentage:", percent, "%")


# Main function to control program execution
def main():

    # Load grades from CSV file
    grades = load_grades("grades.csv")

    # Process the grades
    analyze_grades(grades)


# Run the program
main()