import random
import os

class RandomWord():
    def __init__(self, filename):
        self.filename = filename
    def random_word(self):
        words = []
        with open(self.filename) as file:
            for line in file:
                words.append(line.strip())
        word =  random.choice(words)
        return list(word)

def hangman():
    # get a word
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'words.txt')
    get_word = RandomWord(file_path)
    word = get_word.random_word()
    original_word = word.copy()

    # create the blank word to fill
    blank = []
    for i in range(len(word)):
       blank.append('_')

    # start the game
    guesses = 10
    while guesses > 0:
        print('You have', guesses, 'incorrect guesses left\n')
        print(blank)
        letter = input('Guess a letter: ')
        if letter in word: # correct guess
            # find all letters, take from word add to blank
            while letter in word:
                location = word.index(letter)
                blank[location] = letter
                word[location] = '_'
        else: # incorrect guess
            print("'", letter, "' is not in the word")
            guesses -= 1

        # win the game
        if '_' not in blank:
            print('')
            print(blank)
            print('Congratulations, you win!')
            break

    # lose the game
    if '_' in blank:
        print('You lose')
        print('The word was:', original_word)

hangman()
