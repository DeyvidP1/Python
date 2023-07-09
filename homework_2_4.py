def is_int_palindrome(number):
    result = str(number)
    
    reversed_result = (result[::-1])
    return result == reversed_result

    if string == reversed_result:
        print(True)
    else:
        print(False)
    



print(is_int_palindrome(22))