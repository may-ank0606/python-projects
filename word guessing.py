import random

def shaktimaan():
    word_list = ["python", "programming", "shaktimaan", "computer", "code"]
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("Welcome to shaktimaan")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong guess!")
            print_shaktimaan(tries)
        else:
            print("Correct guess!")

        word_progress = ""
        for letter in word:
            if letter in guessed_letters:
                word_progress += letter + " "
            else:
                word_progress += "_ "

        print(word_progress)

        if "_" not in word_progress:
            print("Congratulations! You won!")
            break

    if tries == 0:
        print("Sorry, you lost. The word was:", word)

def print_shaktimaan(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[tries])

shaktimaan()
