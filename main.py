from scaffold.build_scaffold import build_scaffold

answer = input('Do you want to start new hangman game? y/n : ')

while answer != 'y' and answer != 'n':
    print('Please use only y/n keys.')
    answer = input('Do you want to start new hangman game? y/n : ')

if answer == 'y':
    print('Hangman game started!')
    build_scaffold()
elif answer == 'n':
    exit()