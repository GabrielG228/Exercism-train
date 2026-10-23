def square_root(number):
    '''Integer square root (binary search)'''
    if number <= 0:
        raise ValueError("Number must be positive")
    
    low = 0
    up = number + 1

    while low != up-1:
        mid = (low + up) // 2
        if mid * mid <= number:
            low = mid
        else:
            up = mid
            
    if low * low == number: ### check for returning a positive integer
        return low

    return None
    
