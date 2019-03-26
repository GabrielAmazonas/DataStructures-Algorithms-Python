def quick_sort(array):
    # The first call to the helper will pass in the entire array
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, first, last):
    # This method contains the base case cenario
    if first < last:
        splitpoint = partition(array, first, last)

        quick_sort_helper(array, first, splitpoint - 1)
        quick_sort_helper(array, splitpoint + 1, last)


def partition(array, first, last):
    # Initializes the pivot value as the first array element
    pivot_value = array[first]
    leftmark_index = first + 1
    rightmark_index = last

    done = False
    while not done:
        # Both while loops are the base cases: Keep iterating until the values on the right are lower
        # or the values on the left are bigger then the pivot value.
        # While the leftmark_index is before the rightmark_index
        while leftmark_index <= rightmark_index and array[leftmark_index] <= pivot_value:
            # Walk through the array until the left cross the right index
            leftmark_index += 1
        while array[rightmark_index] >= pivot_value and rightmark_index >= leftmark_index:
            rightmark_index -= 1

        if rightmark_index < leftmark_index:
            # they crossed
            done = True
        else:
            # In this case, the marks haven't crossed yet
            # and or the right value is lower then the pivot, or the left one is bigger (last while loops conditions)
            temp = array[leftmark_index]
            array[leftmark_index] = array[rightmark_index]
            array[rightmark_index] = temp

    temp = array[first]
    array[first] = array[rightmark_index]
    array[rightmark_index] = temp
    return rightmark_index


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quick_sort(test))