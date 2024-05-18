def can_reach_end(A):
    current_max_reach, last_index = 0, len(A) - 1
    i = 0
    while i <= current_max_reach and current_max_reach < last_index:
        current_max_reach = max(current_max_reach, i + A[i])
        i += 1
    return current_max_reach >= last_index

print(can_reach_end([1, 2, 3, 4])) # True    
print(can_reach_end([1, 0, 3, 4])) # False 