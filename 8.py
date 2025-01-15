# [2,3,-1,8,-12,10] -> 

# Find maximum subarray
def find_maximum_subarray_bf(arr):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(0, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


print(find_maximum_subarray_bf([2,3,-1,8,-12,10]))