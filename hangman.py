import random

# List of words
words = ["python", "computer", "science", "developer", "artificial"]

# Choose a random word
word = random.choice(words)

# Create hidden word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect attempts allowed
attempts = 6

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)

# Main game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("Wrong Guess!")

# Final result
print("\n" + "=" * 40)

if "_" not in guessed_word:
    print("🎉 Congratulations!")
    print("You guessed the word:", word.upper())
else:
    print("❌ Game Over!")
    print("The correct word was:", word.upper())

print("=" * 40)