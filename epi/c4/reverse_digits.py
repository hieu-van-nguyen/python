def reverse(x):
    result, remaining = 0, abs(x)
    while remaining:
        result = result * 10 + remaining % 10
        remaining //= 10
    return -result if x < 0 else result

print(reverse(42)) # 24
print(reverse(-314)) # -413
print(reverse(0)) # 0