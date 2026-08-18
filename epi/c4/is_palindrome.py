def is_palindrome_number(n):
    if n <= 0:
        return n == 0
    reverted_num = 0
    while n > reverted_num:
        reverted_num = reverted_num * 10 + n % 10
        n //= 10
    
    return n == reverted_num or n == reverted_num // 10

print(is_palindrome_number(12321)) # True
print(is_palindrome_number(1221)) # True
print(is_palindrome_number(12341)) # False
    