def binary_search(input_array, value):
    lower = 0
    upper = len(input_array)
    while lower<upper:
        mid = (upper+lower)/2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            lower = mid +1
        elif input_array[mid] > value:
            upper = mid
    return -1
