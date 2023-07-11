def sum_of_numbers(string):
    current_number = " "
    total_sum = 0

    for char in string:
        if char.isdigit():
            current_number = current_number + char
        elif current_number != " ":
            total_sum = total_sum + int(current_number)
            current_number = " "

    
    if current_number != " ":
        total_sum = total_sum + int(current_number)

    return total_sum

print(sum_of_numbers("1abc33xyz22"))