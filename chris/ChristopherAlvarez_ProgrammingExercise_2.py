"""
Spam Detection Application - Chris A

This program asks the user to enter an email message.
It checks the message for common spam words and phrases.
Each time a spam phrase appears, the spam score goes up.
At the end, the program tells the user how likely the message is to be spam.
"""

# This is the list of spam words and phrases the program will look for.
SPAM_KEYWORDS = [
    "free", "winner", "win money", "cash prize", "urgent",
    "act now", "limited time", "exclusive deal", "click here",
    "buy now", "risk free", "guaranteed", "congratulations",
    "claim now", "credit card", "lowest price", "million dollars",
    "weight loss", "work from home", "make money fast",
    "earn extra cash", "trial offer", "password",
    "verify your account", "bank account", "lottery",
    "investment opportunity", "cheap meds", "prize", "offer"
]


def calculate_spam_score(message):
    """
    Looks through the email and calculates a spam score
    based on how many spam words are found.

    Returns the total score and a dictionary showing
    which spam words were found and how many times.
    """

    score = 0          # keeps track of total spam points
    found = {}         # stores spam phrases that were found

    # Make everything lowercase so the search isnt case sensitive.
    # strip() removes any extra spaces at the beginning or end.
    message = message.lower().strip()

    # Go through each spam phrase in the list.
    for phrase in SPAM_KEYWORDS:

        # count() checks how many times that phrase appears in the message.
        occurrences = message.count(phrase)

        # If we found the phrase at least once,
        # add to the score and record it in the dictionary.
        if occurrences > 0:
            score += occurrences
            found[phrase] = occurrences

    return score, found


def rate_spam_likelihood(score):
    """
    Decides how spammy the message is
    based on the final spam score.
    """

    if score == 0:
        return "Not likely spam"
    elif score <= 3:
        return "Possibly spam"
    elif score <= 7:
        return "Likely spam"
    else:
        return "Very likely spam"


def main():
    """
    This is where the program starts running.
    """

    print("Spam Detection Program")
    print("----------------------")

    # Ask the user to enter an email message.
    # input() always returns a string.
    email = input("Enter email message:\n")

    # Calculate the spam score using the function above.
    score, found_words = calculate_spam_score(email)

    # Show the results to the user.
    print("\nSpam Score:", score)
    print("Likelihood:", rate_spam_likelihood(score))

    print("\nSpam indicators found:")

    # If any spam words were found, print them.
    if found_words:
        for word in found_words:
            print(word, "-", found_words[word], "time(s)")
    else:
        print("None")


if __name__ == "__main__":
    main()