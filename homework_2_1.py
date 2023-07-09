def sum_of_min_and_max(arr):
    minNum = 0
    maxNum = 0

    for num in arr:
        if maxNum < num:
            minNum = num

        if minNum > num:
            maxNum = num
            
    return maxNum, minNum


print (sum_of_min_and_max([1,2,3,4,5,6,8,9]))