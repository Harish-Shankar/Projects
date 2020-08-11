import random
import Words


def display_hangman(attempts):
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
    return stages[attempts]


def main():
    randomWord = random.choice(Words.words)
    userWord = "_" * (len(randomWord)-1)
    attempts = 6
    guess = ""
    guessed = False
    guessedLetters = []
    userWordList = list(userWord)

    print("Welcome to Hangman!")
    print("The word is", (len(randomWord)-1), "characters long")
    print(display_hangman(attempts))
    print("\n")

    while not guessed and attempts > 0:
        guess = input("Please guess a letter")
        if len(guess) == 1 and guess.isalpha():
            if guess not in randomWord:
                print("The letter you guessed is not in the word")
                guessedLetters.append(guess)
                attempts -= 1
            elif guess in guessedLetters:
                print("You have already guessed this letter")
            else:
                print("The letter", guess, "is in the word")
                guessedLetters.append(guess)
                userWordList = list(userWord)
                indices = [i for i, letter in enumerate(randomWord) if letter == guess]
                for index in indices:
                    userWordList[index] = guess
                userWord = "".join(userWordList)
                if "_" not in userWord:
                    guessed = True
            print(display_hangman(attempts))
            print(userWord)
            print("\n")
        elif len(guess) > 1:
            print("Please enter only one letter")
        else:
            print("Please enter a letter")

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was "+randomWord+".")
    else:
        print("Congrats! You guessed the word.")


main()
