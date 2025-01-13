# The first approach is simple, just sort the array
# The second approach is this:

def move_negative_elements_to_left_of_array(arr):
    left_pointer = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[left_pointer]
            arr[left_pointer] = temp
            left_pointer += 1
    
    return arr

arr = [9,2,13,4,532,124,14,135,-1,3, 7, -2]
print(move_negative_elements_to_left_of_array(arr))
                    