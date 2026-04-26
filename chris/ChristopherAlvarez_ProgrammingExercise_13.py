"""
Population Database Program - Christopher Alvarez

This program creates a population database, stores Florida city population
data, simulates population growth and decline for 20 years, and graphs the
population trend for the city chosen.
"""

import matplotlib.pyplot as plt


# This is the database called population_CA
population_CA = []


# This function creates the population table and inserts 2025 data
def create_database():
    # Each record has city, year, and population
    cities = [
        ("Miami", 2025, 455000),
        ("Tampa", 2025, 410000),
        ("Orlando", 2025, 330000),
        ("Jacksonville", 2025, 990000),
        ("St. Petersburg", 2025, 265000),
        ("Tallahassee", 2025, 205000),
        ("Fort Lauderdale", 2025, 185000),
        ("Cape Coral", 2025, 225000),
        ("Gainesville", 2025, 150000),
        ("Sarasota", 2025, 60000)
    ]

    # Insert each record into the population table
    for record in cities:
        population_CA.append(record)


# This function simulates population growth and decline for 20 years
def simulate_population():
    # Different rates are used so the graph does not become a straight line
    rates = [0.015, -0.005, 0.02, 0.01, -0.01]

    # Save only the original 2025 data before adding new years
    original_data = population_CA[:]

    # Go through each city
    for city, year, population in original_data:
        current_population = population

        # Create population data from 2026 to 2045
        for i in range(20):
            new_year = 2026 + i

            # Choose a different rate each year
            rate = rates[i % len(rates)]

            # Calculate new population
            current_population = int(current_population * (1 + rate))

            # Insert the new record into the population table
            population_CA.append((city, new_year, current_population))


# This function lets the user choose a city and displays the graph
def show_population_graph():
    cities = [
        "Miami", "Tampa", "Orlando", "Jacksonville", "St. Petersburg",
        "Tallahassee", "Fort Lauderdale", "Cape Coral", "Gainesville", "Sarasota"
    ]

    # Show city options
    print("Choose one of these Florida cities:")
    for city in cities:
        print(city)

    chosen_city = input("Enter city name: ")

    years = []
    populations = []

    # Search the population table for the chosen city
    for record in population_CA:
        city = record[0]
        year = record[1]
        population = record[2]

        if city == chosen_city:
            years.append(year)
            populations.append(population)

    # If the city was not found, tell the user
    if len(years) == 0:
        print("City not found.")
    else:
        # Plot the city population data
        plt.plot(years, populations)
        plt.title("Population Growth and Decline for " + chosen_city)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()


# This function runs the program
def main():
    create_database()
    simulate_population()
    show_population_graph()


main()