s = "A man, a plan, a canal: Panama"


def isPalindrome(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


print(isPalindrome(s))
