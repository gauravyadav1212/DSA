# Approach 1, create a temp array
def reverse_array(og_arr):
    length_og_array = len(og_arr)
    temp_array = [0] * length_og_array

    for current_index in range(length_og_array):
        temp_array[current_index] = og_arr[length_og_array - current_index -1]
    
    return temp_array

array = [1,2,3,4,5,6,7]
print(reverse_array(array))


# Two pointer approach
def reverse_array_two_pointer(og_arr):
    if len(og_arr) < 2:
        return og_arr
    
    left_most_pointer = 0
    right_most_pointer = len(og_arr) - 1

    while right_most_pointer > left_most_pointer:
        temp = og_arr[left_most_pointer]
        og_arr[left_most_pointer] = og_arr[right_most_pointer]
        og_arr[right_most_pointer] = temp
        left_most_pointer += 1
        right_most_pointer -= 1
    
    return og_arr

array = [1,2,3,4,5,6,7]
print(reverse_array_two_pointer(array))