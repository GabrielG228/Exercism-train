def is_pangram(sentence):
    modified = sentence.lower().replace(' ', '')
    counter = 0
    letters = ''
    for char in modified:
        if char not in letters and char.isalpha():
            letters += char
            counter += 1
    if counter == 26:
        return True
    return False
