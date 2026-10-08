def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    nrsteps = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        nrsteps += 1
    return nrsteps
        
    
