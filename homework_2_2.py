def sum_of_divisors(num):
    sum = 0

    for i in range (1, num):
        if num % i == 0:
         sum = sum + i
    return sum

    sum = sum_of_divisors(num)


print (sum_of_divisors(7))