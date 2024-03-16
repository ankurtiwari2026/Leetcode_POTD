class Solution:
    def findMaxLength(self, nums: List[int]) -> int:    
        max_length = 0
        count = 0
        sum_to_index = {0: -1}  # Initialize a dictionary to store cumulative sum and its index

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in sum_to_index:
                max_length = max(max_length, i - sum_to_index[count])
            else:
                sum_to_index[count] = i

        return max_length 
        