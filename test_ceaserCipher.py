from ceaserCypher import encrypt, decrypt
from random import choice, randint
import string

wordlist = []
for i in range(15):
    word = ''
    for i in range(5):
        word += choice(string.ascii_letters)
    wordlist.append(word)

def test_lowercase_encrypt():
    assert encrypt(3, "keag") == "nhdj"

def test_lowercase_decrypt():
    assert decrypt(3, "nhdj") == "keag"

def test_encrypt_wrapping():
    assert encrypt(3, 'x') == 'a'
    assert encrypt(20, 'g') == 'a'

def test_encrypt_mixed_case():
    assert encrypt(3, 'Keag') == "Nhdj"

def test_lowercase_bidirectional():
    for word in wordlist:
        step = randint(1, 26)
        assert word == decrypt(step, encrypt(step, word))
    