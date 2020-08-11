import random
import Words


def main():
    hangmanword = random.choice(Words.words)
    character = "abcdefghijklmnopqrstuvwxy"
    word = list(hangmanword)
    finalword = str(word)
    print("The word is", len(hangmanword), "characters is long")
    #print(word)

    playerword = []
    playerstring = ""
    hasguessed = False
    characters = [x for x in word]

    for i in range(len(characters)-1):
        playerword.insert(i, '-')
    used = []

    while hasguessed is False:
        guess = input("Please enter your guess")
        if guess not in characters:
            print("The letter ", guess, "is not in the word")

        if guess in used:
            print("You have already guess the letter ", guess)

        if guess not in character:
            print("Please enter a valid character!")

        if guess in characters and guess not in used:
            for x in range(len(characters)-1):
                if guess == characters[x]:
                    playerword[x] = guess
                    word.remove(guess)
                else:
                    used.append(guess)
        print(str(playerword))
        playerstring = str(playerword)
        #print(playerstring, " ; ", finalword)
        if playerstring == finalword:
            print("Congratulations you have won!")
            break


main()