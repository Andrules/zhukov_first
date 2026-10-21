from constants import FINISH_GAME
from constants import WORDS_POOL, STAGES
from reveal_letter import reveal_letter
from random import choice

def hangman_game():
    mistakes = 0
    max_mistakes = (len(STAGES) - 1)

    is_word_found = False

    target_word, word_suggestion = choice(list(WORDS_POOL.items()))
    cyphered_word = '_' * len(target_word)

    print('Hangman game started!')


    while mistakes < max_mistakes and not is_word_found:
        boilerplate = \
            rf'''
                If you want end game enter {FINISH_GAME}
                {word_suggestion}    {cyphered_word}
                '''

        print(STAGES[mistakes])
        print(boilerplate)

        user_guess = input('Guess a letter: ').upper()

        if user_guess == FINISH_GAME:
            submission = input('Are you sure you want to end game? Press "y" if you sure: ').upper()
            if submission == 'Y' :  break
        elif user_guess not in target_word:
            mistakes += 1
            if mistakes == max_mistakes:
                print(STAGES[-1])

        elif user_guess in target_word:
            if cyphered_word == target_word:
                is_word_found = True
                print('Congratulations! You won!')

            cyphered_word = reveal_letter(cyphered_word, target_word, user_guess)

