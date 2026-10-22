def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <=0 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = 0   
    for n in range(1, number):
        if number % n == 0:
            aliquot += n
    if aliquot == number:
        return 'perfect'
    if number < aliquot:
        return 'abundant'
    if number > aliquot:
        return 'deficient'
        
    
