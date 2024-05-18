def delete_duplicate(arr):
    if not arr:
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if (arr[write_index - 1] != arr[i]):
            arr[write_index] = arr[i]
            write_index += 1

    return write_index

print(delete_duplicate([2, 3, 5, 5, 7, 11, 11, 11, 13, 13])) # 6