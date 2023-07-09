def biggest_difference(arr):
    min_num = min(arr)
    max_num = max(arr)

    difference1 = max_num - min_num
    difference2 = min_num - max_num

    biggest_difference_between_numbers = max (difference1, difference2)
    return biggest_difference_between_numbers
    pass


print (biggest_difference([1,2]))