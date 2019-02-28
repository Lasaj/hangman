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
    location = os.getcwd()
    file_path = os.path.join(location, 'words.txt')
    get_word = RandomWord(file_path)
    word = get_word.random_word()
    original_word = word.copy()

    # create the guessed_word word to fill
    guessed_word = list('_' * len(word))

    # start the game
    guesses = 10
    while guesses > 0:
        print('You have', guesses, 'incorrect guesses left\n')
        print(guessed_word)
        letter = input('Guess a letter: ')
        changed = False
        # find all letters, take from word add to guessed_word
        for i, c in enumerate(word):
            if c == letter:
                changed = True
                guessed_word[i] = letter
                word[i] = '_'
        if not changed: # incorrect guess
            print("'", letter, "' is not in the word")
            guesses -= 1

        # win the game
        if '_' not in guessed_word:
            print('')
            print(guessed_word)
            print('Congratulations, you win!')
            break

    # lose the game
    if '_' in guessed_word:
        print('You lose')
        print('The word was:', original_word)

hangman()
