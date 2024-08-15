class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        letters = set('aeiouAEIOU')
        i,j = 0,len(s)-1
        while i<j:
            if s[i] in letters and s[j] in letters:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in letters :
                i+=1
            elif s[j] not in letters :
                j-=1
            else:
                i+=1
                j-=1
        return "".join(s)