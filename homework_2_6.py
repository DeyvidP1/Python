def contains_digits(number, digits):
    result = str(number)

    for digit in digits:
        if str(digit) not in result:
            return False
        else:
            return True
    

print(contains_digits(402123, [0, 3, 4]))
