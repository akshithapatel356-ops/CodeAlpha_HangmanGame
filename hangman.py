import random

words = ["python", "laptop", "garden", "planet", "silver"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== Hangman Game =====")
print("Guess the word one letter at a time.\n")

while attempts > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if "_" not in display_word:
        print("\nYou guessed the word successfully.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Letter already used.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess.\n")
    else:
        attempts -= 1
        print("Incorrect guess.")
        print("Remaining attempts:", attempts, "\n")

if attempts == 0:
    print("Game Over")
    print("The correct word was:", secret_word)