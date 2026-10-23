def is_valid(isbn):
    '''Check if valid isbn'''
    isbn = isbn.strip()
    clean = isbn.replace('-', '')

    if len(clean)!=10:
        return False
        
    # First 9 characters gotta be digits
    if not clean[:9].isdigit():
        return False
        
    # Last character may be digit OR X
    if not (clean[-1].isdigit() or clean[-1] == "X"):
        return False
    
    total = 0
    for ind,num in enumerate(reversed(clean), start = 1):
        value = 10 if num == 'X' else int(num)
        total += value*ind
        
    if total % 11 == 0:
        return True
    return False
    
