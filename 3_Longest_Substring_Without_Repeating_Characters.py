def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
        print(charSet)
        print(res, r, l)
    return res


myset = set()
myset.add("ab")
myset.add("c")
myset.add("d")
# print(myset)

print(lengthOfLongestSubstring("pwwkew"))
