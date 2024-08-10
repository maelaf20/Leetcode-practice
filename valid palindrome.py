import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        hashset = list()
        for i in s:
            if i.isalnum():
                hashset.append(i)
        "".join(hashset)
        if hashset == hashset[::-1]:
            return True
        return False
        