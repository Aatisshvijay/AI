# Hangman Stages (Visual Representation)
stages = ['''
+---+
|   |
O   |
/|\  |
/ \  |
    |
=========
''', '''
+---+
|   |
O   |
/|\  |
/    |
    |
=========
''', '''
+---+
|   |
O   |
/|\  |
     |
    |
=========
''', '''
+---+
|   |
O   |
/|   |
     |
    |
=========
''', '''
+---+
|   |
O   |
 |   |
     |
    |
=========
''', '''
+---+
|   |
O   |
     |
     |
    |
=========
''', '''
+---+
|   |
    |
     |
     |
    |
=========
''']

# Main Hangman Game Function
def hangman():
    print("\n-------------Welcome to 2-Player Hangman-------------\n")
    
    # Player 1 chooses the secret word
    print("Player 1: Choose a secret word for Player 2 to guess.")
    chosen_word = input("Enter the secret word: ").lower()
    
    # Hide the word with enough newlines for secrecy
    print("\n" * 50)
    print("Word is set. Player 2, get ready to guess!")
    
    # Prepare the display with underscores
    display = ["_"] * len(chosen_word)
    end_of_loop = False
    lives = 6
    guessed_letters = set()
    
    print("Guess the word:- ", end=" ")
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")
    
    while not end_of_loop:
        guess = input("Player 2, Guess a Letter: ").lower()

        # Check if the guess was already made
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        guessed_letters.add(guess)
        
        # Incorrect guess
        if guess not in chosen_word:
            lives -= 1
            print("Wrong guess. You lost a life.")
        else:
            # Correct guess
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess

        # Display the current game status
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")
        print(stages[6 - lives])  # Display corresponding hangman stage

        # Check for win or lose condition
        if "_" not in display:
            print("🎉 Player 2 Wins! Congratulations!")
            end_of_loop = True
        elif lives == 0:
            print("💀 Player 2 Loses! Better luck next time.")
            print(f"The word was: {chosen_word}")
            end_of_loop = True

# Game Loop to allow replaying
end_of_game = False
while not end_of_game:
    ask = input("\nDo you want to play 2-Player Hangman? (y/n): ").lower()
    if ask in ('y', 'yes'):
        hangman()
    elif ask in ('n', 'no'):
        print("Program Exit Successful. Goodbye!")
        end_of_game = True
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
