class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum={0:1}
        current_sum=0
        count=0
        for num in nums:
            current_sum+=num
            if current_sum-goal in prefix_sum:
                count+=prefix_sum[current_sum-goal]
            prefix_sum[current_sum]=prefix_sum.get(current_sum,0)+1
        return count        