def rotate_array(array):
    last_elemet = array[-1]

    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    
    array[0] = last_elemet
    return array

print(rotate_array([1,2,3,4,5]))

