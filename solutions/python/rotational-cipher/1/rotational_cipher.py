def rotate(text, key):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in text:
        if char.isalpha():
            was_upper = char.isupper()
            position = alphabet.index(char.lower())
            new_position = (position + key) % 26
            result.append(alphabet[new_position].upper() if was_upper else alphabet[new_position])
        else:
            result.append(char)
    return ''.join(result) 
