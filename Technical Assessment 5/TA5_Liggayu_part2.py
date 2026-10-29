
# Function to count happy words in a sentence
def number_happy(sentence):

    # List of happy words
    happy_words = [
        "happy", "joy", "love", "great", "excellent",
        "wonderful", "excited", "amazing", "glad", "fun"
    ]

    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()

    # Initialize the happy word counter
    count = 0

    # Check each word in the sentence
    for word in words:

        # Remove punctuation marks from the word
        word = word.strip(".,!?;:")

        # Check if the word is in the happy words list
        if word in happy_words:
            count += 1

    # Return the total number of happy words
    return count


# Function to count sad words in a sentence
def number_sad(sentence):

    # List of sad words
    sad_words = [
        "sad", "unhappy", "cry", "hate", "terrible",
        "awful", "miserable", "depressed", "lonely", "bad"
    ]

    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()

    # Initialize the sad word counter
    count = 0

    # Check each word in the sentence
    for word in words:

        # Remove punctuation marks from the word
        word = word.strip(".,!?;:")

        # Check if the word is in the sad words list
        if word in sad_words:
            count += 1

    # Return the total number of sad words
    return count


# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Count the happy and sad words in the sentence
happy = number_happy(sentence)
sad = number_sad(sentence)

# Display the number of happy and sad words
print("Number of happy words:", happy)
print("Number of sad words:", sad)

# Compare the number of happy and sad words
if happy > sad:

    # More happy words means a positive tone
    print("Tone: Happy (Positive)")

elif sad > happy:

    # More sad words means a negative tone
    print("Tone: Sad (Negative)")

else:

    # Equal counts mean a neutral tone
    print("Tone: Neutral")
