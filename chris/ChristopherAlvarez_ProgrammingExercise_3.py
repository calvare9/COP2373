"""
Monthly Expense Analyzer - Christopher Alvarez

This program asks the user to enter their monthly expenses.
The user will input the type of expense and the amount.
The program stores this information in a list and uses
the reduce() function to calculate the total expense,
as well as find the highest and lowest expenses.
"""

from functools import reduce


# This function collects all of the user's expenses.
# It stores each expense as a tuple inside a list.
def get_expenses():

    expenses = []   # this list will store all expense types and amounts

    while True:

        # Ask the user to enter the type of expense.
        expense_type = input(
            "Enter the type of expense (or type 'done' to finish): "
        )

        # If the user types done, stop asking for expenses.
        if expense_type.lower() == "done":
            break

        try:
            # Ask for the amount of the expense.
            amount = float(input("Enter the amount for this expense: "))

            # Add the expense type and amount together as a tuple.
            expenses.append((expense_type, amount))

        except ValueError:
            # If the user enters something that isnt a number.
            print("Please enter a valid number.")

    return expenses


# This function uses reduce() to add up all the expenses.
def calculate_total(expenses):

    # reduce() goes through each expense and adds the amounts together.
    return reduce(lambda total, expense: total + expense[1], expenses, 0)


# This function finds the highest expense.
def get_highest(expenses):

    # reduce() compares each expense and keeps the larger one.
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


# This function finds the lowest expense.
def get_lowest(expenses):

    # reduce() compares each expense and keeps the smaller one.
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)


def main():

    print("Monthly Expense Analyzer")
    print("------------------------")

    # Get the list of expenses from the user.
    expenses = get_expenses()

    # Check if the user entered anything.
    if len(expenses) == 0:
        print("No expenses entered.")
        return

    # Calculate the total expenses.
    total = calculate_total(expenses)

    # Find the highest and lowest expenses.
    highest = get_highest(expenses)
    lowest = get_lowest(expenses)

    # Display the results.
    print("\nTotal Expenses: $", total)
    print("Highest Expense:", highest[0], "-", highest[1])
    print("Lowest Expense:", lowest[0], "-", lowest[1])


if __name__ == "__main__":
    main()