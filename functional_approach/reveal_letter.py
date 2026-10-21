def reveal_letter(target_word, cyphered_word, guessed_letter):
    cyphered_letters = list(cyphered_word)

    for idx, letter in enumerate(target_word):
        if letter == guessed_letter:
            cyphered_letters[idx] = guessed_letter

    return ''.join(cyphered_letters)
