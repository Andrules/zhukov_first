from hangman_game import hangman_game

while True:
    answer = input('Do you want to start new hangman game? y/n : ')

    while answer != 'y' and answer != 'n':
        print('Please use only y/n keys.')
        answer = input('Do you want to start new hangman game? y/n : ')
    if answer == 'y':
        print('Hangman game started!')
        hangman_game()
    elif answer == 'n':
        exit()