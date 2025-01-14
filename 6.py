# Union and intersection of two arrays
# Union - Hashmap approach
def union(array1, array2):
    # [2,3,1,4,5]
    # [1,2,3]
    hash_map = {}
    for element in array1:
        hash_map[element] = True

    for element in array2:
        hash_map[element] = True
    
    return len(hash_map)

print(union([2,3,1,4,5], [1,2,3]))


# Intersection - sorting and two pointer approach
def intersection(array1, array2):
    array_containing_common_elements = []
    array1.sort()
    array2.sort()
    array_1_pointer = 0
    array_2_pointer = 0

    while ((array_1_pointer < len(array1)) and (array_2_pointer<len(array2))):

        if array1[array_1_pointer] == array2[array_2_pointer]:
            array_containing_common_elements.append(array1[array_1_pointer])
            
        if array1[array_1_pointer] > array2[array_2_pointer]:
            array_2_pointer += 1
        elif array1[array_1_pointer] < array2[array_2_pointer]:
            array_1_pointer += 1
        else:
            array_1_pointer +=1
            array_2_pointer +=1
    
    return len(array_containing_common_elements)

print(intersection([2,3,1,1,4,5], [1,1,2,3]))


# Intersection - Brute force
def intersection_using_brute_force(array1, array2):
    new_array = []

    for element in array2:
        if element in array1:
            new_array.append(element)
    return len(new_array)

print(intersection_using_brute_force([2,3,1,1,4,5], [1,1,2,3]))



