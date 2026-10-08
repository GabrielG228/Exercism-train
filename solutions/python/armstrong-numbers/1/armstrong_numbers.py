def is_armstrong_number(number):
    digits = []
    temp = number
    for x in range(len(str(number))):
        digits.append(temp % 10)
        temp = temp // 10
    return number == sum(y**len(digits) for y in digits)
    
        
    
