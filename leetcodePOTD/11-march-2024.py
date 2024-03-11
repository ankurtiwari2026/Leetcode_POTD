class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=""
        d={}
        for char in s:
            d[char]=d.get(char,0)+1
        for char in order:
            if char in d:
                res+=char*d[char]
                del d[char]
        for char,count in d.items():
            res+=char*count
        return res        

