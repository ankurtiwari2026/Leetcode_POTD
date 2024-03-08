from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count = [0] * 101  # List to store frequency of numbers
        max_freq = 0
        
        for num in nums:
            count[num] += 1
            max_freq = max(max_freq, count[num])
        
        result = 0
        for i in range(101):
            if count[i] == max_freq:
                result += max_freq
        
        return result