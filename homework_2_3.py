def is_prime(num):
    sum = 0
    
    for i in range(1, num):
         if num % i == 0:
            sum = sum + i
            return True
    else:
            return False


print (is_prime(2))