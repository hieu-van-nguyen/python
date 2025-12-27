def isAnagramV1(s: str, t:str) -> bool:
    # Time Complexity O(nlogn + mlogm)
    # Space Complexity O(1)
    if (len(s) != len(t)):
        return False
    return sorted(s) == sorted(t)

print(isAnagramV1("racecar", "carrace")) # True
print(isAnagramV1("jar", "jam")) # False

def isAnagramV2(s: str, t:str) -> bool:
    # Time Complexity O(n + m)
    # Space Complexity O(1) because we have at most 26 different character
    if (len(s) != len(t)):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    return countS == countT

print(isAnagramV2("racecar", "carrace")) # True
print(isAnagramV2("jar", "jam")) # False