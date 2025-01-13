# Approach 1, make 3 arrays:

def sort012(arr):
    # code here
    hash_map = {
        "zero": 0,
        "one": 0,
        "two": 0
    }

    for element in arr:
        if element == 0:
            hash_map["zero"] = hash_map["zero"] + 1
        elif element == 1:
            hash_map["one"] = hash_map["one"] + 1
        else:
            hash_map["two"] = hash_map["two"] + 1

    arr_zero = [0] * hash_map["zero"]
    arr_one = [1] * hash_map["one"]
    arr_two = [2] * hash_map["two"]
    arr_final = []
    arr_final.extend(arr_zero)
    arr_final.extend(arr_one)
    arr_final.extend(arr_two)

    return arr_final

arr = [1,1,2,0]
print(sort012(arr))