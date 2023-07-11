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

    pass

print (group([1, 2, 1, 2, 3, 3]))
