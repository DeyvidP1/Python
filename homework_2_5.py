def contains_digit(number):

    result = str(number)

    if len(result) == 1:
        return True
    else:
        return False
    print (result)
    
print(contains_digit(123, 4))