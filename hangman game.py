
# Hangman body parts
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """,
]

def clear_screen():
    """Clears the console screen."""

def get_word():
    """Player 1 enters the secret word and an optional clue."""
    print("Player 1: Enter the word for Player 2 to guess (no spaces).")
    word = input("Word: ").strip().lower()
    clue = input("Enter a clue (optional): ").strip()
    clear_screen()
    return word, clue

def display_progress(word, guessed_letters, attempts):
    """Displays the hangman stage and current word progress."""
    print(HANGMAN_STAGES[attempts])
    progress = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print("\nWord: ", progress)

def hangman():
    word, clue = get_word()
    guessed_letters = set()
    attempts = 0  # Starts with no body parts drawn (max 6 attempts)

    print("Player 2: Start guessing the word!")
    if clue:
        print(f"Clue: {clue}")

    while attempts < len(HANGMAN_STAGES) - 1:
        display_progress(word, guessed_letters, attempts)
        guess = input("\nGuess a letter: ").strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts += 1
            print(f"Wrong guess! You have {6 - attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            display_progress(word, guessed_letters, attempts)
            print("\n🎉 Congratulations! You guessed the word correctly! 🎉")
            return

    print(HANGMAN_STAGES[attempts])
    print("\n💀 Game Over! The full body was drawn. You lost.")
    print(f"The correct word was: {word}")

# Run the game
hangman()
