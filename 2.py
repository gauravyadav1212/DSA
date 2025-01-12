# Approach 1, make 2 functions to find the minimum and maximum values
def find_minimum(arr):
    positive_inf = float('inf')
    for number in arr:
        if number < positive_inf:
            positive_inf = number
    return positive_inf

def find_maxinum(arr):
    negative_inf = float('-inf')
    for number in arr:
        if number > negative_inf:
            negative_inf = number
    return negative_inf

arr = [3,5,7,1,2,4,1,5,6,7]
minimum_number = find_minimum(arr)
maximum_number = find_maxinum(arr)
print("Min: ", minimum_number,"Max: ", maximum_number)


# Approach 2, sort the array and return the results
def find_minimum_and_maximum(arr):
    arr.sort()
    minimum_number = arr[0]
    maximum_number = arr[len(arr)-1]
    return minimum_number, maximum_number

arr = [3,5,7,1,2,4,1,5,6,7]
min_number, max_number = find_minimum_and_maximum(arr)
print("Min: ", min_number, "Max: ", maximum_number)