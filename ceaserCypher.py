from string import ascii_lowercase as lwc


def encrypt(step, word):
    newWord = ''
    for letter in word:
        letterIndex = lwc.find(letter)
        letterIndex += step
        if letterIndex > 25:
            letterIndex -= 26
        newWord += lwc[letterIndex]
    return newWord

def decrypt(step, word):
    newWord = ''
    for letter in word:
        letterIndex = lwc.find(letter)
        letterIndex -= step
        newWord += lwc[letterIndex]
    return newWord