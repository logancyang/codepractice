"""
Caesar cipher encryptor

Given nonempty string of lowercase letters, and nonnegative integer `key`,
encode the string by shifting the letters by k

a shift 1 is b
z shift 1 is a
"""

def caesarCipherEncryptor(string, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    pos_dict = {char: alphabets.index(char) for char in alphabets}
    new_letters = []
    for char in string:
        new_char_ind = (pos_dict[char] + key) % 26
        new_char = alphabets[new_char_ind]
        new_letters.append(new_char)
    return ''.join(new_letters)
