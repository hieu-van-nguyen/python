def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if (A[i]) != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

print(plus_one([1, 5, 3])) # [1, 5, 4]        
print(plus_one([1, 5, 9])) # [1, 6, 0]
print(plus_one([9, 9, 9])) # [1, 0, 0, 0]