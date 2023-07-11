def count_words(arr):
    result = {}

    for elem in arr:
        if elem in result:
           result[elem] = result[elem] + 1
        else:
           result[elem] = 1

        return result    
        pass



print(count_words(["apple", "banana", "apple", "pie"]))