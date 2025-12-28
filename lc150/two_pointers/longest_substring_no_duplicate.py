def lengthOfLongestSubstring(s:str) -> int:
    map = {}
    l, res = 0, 0
    for r in range(len(s)):
        if s[r] in map:
            l = max(l, map[s[r]] + 1)
        map[s[r]] = r
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring("zxyzxyz")) # 3 for xyz
print(lengthOfLongestSubstring("xxxx")) # 1 for x