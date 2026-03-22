"""
Sentence Parser Program - Christopher Alvarez

This program allows the user to enter a paragraph of text.
It uses Python regular expressions to split the paragraph
into individual sentences, including sentences that begin
with numbers. It then displays each sentence and the total
number of sentences.
"""

import re


# This function splits a paragraph into sentences.
# It uses regex with look-ahead and look-behind.
def split_into_sentences(paragraph):

    # (?<=[.!?]) ensures the split happens after sentence-ending punctuation
    # \s+ matches the space between sentences
    # (?=[A-Z0-9]) ensures the next sentence starts with a capital letter or number
    pattern = r'(?<=[.!?])\s+(?=[A-Z0-9])'

    sentences = re.split(pattern, paragraph)

    return sentences


# This function displays each sentence and the total count
def display_sentences(sentences):

    print("\nIndividual Sentences:\n")

    # Loop through each sentence and print it with numbering
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}")

    # Print total number of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")


# Main function that runs the program
def main():

    paragraph = input("Enter a paragraph:\n")

    # Call function to split sentences
    sentences = split_into_sentences(paragraph)

    # Call function to display results
    display_sentences(sentences)


# This runs the program
main()
