class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num=[]
        for i in range(len(nums)):
            x=abs(nums[i])
            num.append(x)
        num.sort()    
        n=[]
        for i in range(len(num)):
            y=(num[i]*num[i])
            n.append(y)
        return n    

        