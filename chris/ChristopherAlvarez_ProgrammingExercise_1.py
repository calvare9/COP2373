"""
Cinema Ticket Pre-Sale Application

This program sells a limited number of cinema tickets.
Each buyer can purchase up to 4 tickets, and no more than
20 tickets can be sold total.
"""


MAX_TICKETS = 10
MAX_PER_BUYER = 4


def get_ticket_request(remaining_tickets):
    """
    Prompt the user for the number of tickets they want to buy.

    Args:
        remaining_tickets (int): Number of tickets still available.

    Returns:
        int: Valid number of tickets requested by the buyer.
    """
    while True:
        try:
            requested = int(input(
                f"How many tickets would you like to buy (1-{MAX_PER_BUYER})? "
            ))

            if requested < 1 or requested > MAX_PER_BUYER:
                print("You can only buy between 1 and 4 tickets.")
            elif requested > remaining_tickets:
                print("Not enough tickets remaining.")
            else:
                return requested
        except ValueError:
            print("Please enter a valid number.")


def sell_tickets():
    """
    Manage the ticket-selling process and display final results.
    """
    remaining_tickets = MAX_TICKETS
    total_buyers = 0

    while remaining_tickets > 0:
        print(f"\nTickets remaining: {remaining_tickets}")
        requested = get_ticket_request(remaining_tickets)

        remaining_tickets -= requested
        total_buyers += 1

        print(f"Purchase successful! Tickets left: {remaining_tickets}")

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")


def main():
    """Run the cinema ticket application."""
    sell_tickets()


if __name__ == "__main__":
    main()
