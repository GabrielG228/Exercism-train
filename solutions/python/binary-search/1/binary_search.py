def find(search_list, value):
    if not search_list:
        raise ValueError('value not in array')
    ind = len(search_list)//2
    middle = search_list[ind]
    if value == middle:
        return ind
    if value < middle:
        return find(search_list[:ind], value)
    if value > middle:
        return ind + 1 + find(search_list[ind+1:], value)
        
    
        
