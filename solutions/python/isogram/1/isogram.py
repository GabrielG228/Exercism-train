def is_isogram(phrase):
    '''Determine if a word or phrase is an isogram.'''
    clean = phrase.replace(' ', '').lower()
    counter = {}
    for char in clean:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    return all(x==1 for i,x in counter.items() )
            
# def is_isogram(phrase):
#     # Keep only lowercase letters, ignoring spaces and hyphens
#     letters = [char.lower() for char in phrase if char.isalpha()]
    
#     # If unique letters match total letters, no duplicates exist
#     return len(set(letters)) == len(letters)
