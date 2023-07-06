def to_number(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    return number
    digits = []
    result = to_number(digits)
print (to_number([1,2,3,0,2,3]))