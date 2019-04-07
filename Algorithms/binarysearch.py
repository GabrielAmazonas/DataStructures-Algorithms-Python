
def binary_search(input_array, value):

    if len(input_array) == 1 and input_array[0] != value:
        return -1

    lower_limit = 0
    upper_limit = len(input_array) - 1
    check_index = len(input_array) // 2

    while upper_limit != lower_limit:

        check_value = input_array[check_index] 
        if check_value == value:
            return check_index
            break
        elif value > check_value:
            #pick the biggest half
            check_index = check_index + ((upper_limit - check_index) // 2) + 1
            lower_limit = check_index - 1
        elif value < check_value:
            upper_limit = upper_limit - (upper_limit - lower_limit)
            check_index = lower_limit + (upper_limit - lower_limit)
    
    if input_array[check_index] == value:
        return check_index
    
    return -1

   

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
