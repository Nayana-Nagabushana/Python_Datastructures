def missing_element(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        print(num)
        result ^= num
    return result

missing_element([5,5,7,7],[5,7,7])