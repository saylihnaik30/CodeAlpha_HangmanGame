
import random

words = ["python", "apple", "tiger", "chair", "cloud"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0

print("Welcome to Hangman!")

while wrong_guesses < 6:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", 6 - wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("You won! The word was:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! The word was:", secret_word)

print("Thanks for playing!")
