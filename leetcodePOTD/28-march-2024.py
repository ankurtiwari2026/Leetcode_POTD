from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        left=0
        max_length=0
        counts=Counter()
        for right, num in enumerate(nums):
            counts[num]+=1
            while counts[num]>k:
                counts[nums[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length        