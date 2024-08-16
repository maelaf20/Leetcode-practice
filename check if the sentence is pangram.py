import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = list('abcdefghijklmnopqrstuvwxyz')
        final = {}
        for i in sentence:
            if i.isalnum():
                final[i] =1
        if len(final) == 26:
            return True
        return False