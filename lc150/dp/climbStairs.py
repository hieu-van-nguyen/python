# Time complexity: O(n)
# Space complexity: O(n)
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbStairs(3)) # 3

# Time complexity: O(n)
# Space complexity: O(1)
def climbStairsV2(n: int) -> int:
    f0, f1 = 1, 1
    for i in range(n - 1):
        temp = f1
        f1 = f0 + f1
        f0 = temp
    return f1

print(climbStairsV2(3)) # 3
