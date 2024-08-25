
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(string):
            holder = []
            for i in string:
                if i != "#":
                    holder.append(i)
                else:
                    if len(holder)>0:
                        holder.pop()
            return "".join(holder)
        return solve(s) == solve(t) 
        
        
