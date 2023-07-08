def get_all_num(num):
    result = []

    for iter in range(0, 4):
        result.append(num%10) 
        num = num // 10


def sum_of_digits_in_list(my_list):
        result = 0

        for elem in my_list:
            result = result + elem

        return result
            

def is_number_balanced(num):
    digits = get_all_num(num)
    half_of_digits = len(digits)/2


    left_part = sum_of_digits_in_list(digits[0:int(half_of_digits)])
    right_part = sum_of_digits_in_list(digits[int(half_of_digits):])

    return left_part == right_part


print(is_number_balanced(4518))