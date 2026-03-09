"""
Input Validation Program - Christopher Alvarez

This program asks the user to enter a phone number,
social security number, and zip code. It uses Python
regular expressions to check if each input follows
the correct format and tells the user if it is valid.
"""

import re


# This function checks if a phone number is valid.
# Format required: 123-456-7890
def validate_phone(phone):

    pattern = r'^\d{3}-\d{3}-\d{4}$'

    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


# This function checks if a social security number is valid.
# Format required: 123-45-6789
def validate_ssn(ssn):

    pattern = r'^\d{3}-\d{2}-\d{4}$'

    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False


# This function checks if a zip code is valid.
# Formats allowed: 12345 or 12345-6789
def validate_zip(zipcode):

    pattern = r'^\d{5}(-\d{4})?$'

    if re.fullmatch(pattern, zipcode):
        return True
    else:
        return False


# Main function that asks the user for input
def main():

    phone = input("Enter a phone number (123-456-7890): ")
    ssn = input("Enter a social security number (123-45-6789): ")
    zipcode = input("Enter a zip code (12345 or 12345-6789): ")

    # Check phone number
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Check SSN
    if validate_ssn(ssn):
        print("Social security number is valid.")
    else:
        print("Social security number is invalid.")

    # Check ZIP code
    if validate_zip(zipcode):
        print("Zip code is valid.")
    else:
        print("Zip code is invalid.")


# This runs the program
main()