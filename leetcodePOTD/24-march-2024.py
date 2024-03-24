class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        watched_element=set()
        for num in nums:
            if num in watched_element:
                return num
            watched_element.add(num)    