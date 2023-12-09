def two_positive_numbers(a, b, c):
    if int(a >=0 and b >=0 and c >= 0):
        return  True
    else:
        return False
    
print(two_positive_numbers(5, -5, 20))
print(two_positive_numbers(2,25, 1500))
