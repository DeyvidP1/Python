def group(lst):
    result = []
    temporary_result = []
    for n in lst:
        if temporary_result == []:
            temporary_result.append(n)
        elif n in temporary_result:
            temporary_result.append(n)
        else:
            result.append(temporary_result)
            temporary_result = []
            temporary_result.append(n)

    result.append(temporary_result)
    return result

def max_consectuive(items):
    max_num = 1
    current_num = 1

    for item in range (1, len(items)):
        if items[item] == items [item -1]:
            current_num = current_num + 1

        if current_num > max_num:
            max_num = current_num
        
        else:
            current_num = 1

    return max_num

    pass

print (group([1, 2, 1, 2, 3, 3]))
print (max_consectuive([1, 2, 3, 3, 3, 3, 4, 3, 3]))