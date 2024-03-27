class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        product=1
        count=left=0
        for right,value in enumerate(nums):
            product*=value
            while product>=k:
                product/=nums[left]
                left+=1
            count+=right-left+1
        return count        
