class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)):
            sliced = haystack[i:i+len(needle)]
            if sliced == needle:
                return i
        return -1