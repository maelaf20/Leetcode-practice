def isHappy(self, n: int) -> bool:
        s = str(n)
        res = 0
        numbers = {}
        while True:
            for i in s:
                res+=int(i)*int(i)
            if res == 1:
                return True
            if res in numbers:
                return False
            s = str(res)
            numbers[res] = 0 
            res = 0
        return False