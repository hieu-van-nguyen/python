def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

A = [1, 0, 2, 0, 0, 1, 1, 2, 0, 1, 2]
pivot_index = 0

dutch_flag_partition(pivot_index, A)
print(A) # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]