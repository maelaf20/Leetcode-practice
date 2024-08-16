class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        for i in range(0,max(len(word1),len(word2))):
            if i<=len(word1)-1:
                final += word1[i]
            if i<=len(word2)-1:
                final += word2[i]
        return final
        