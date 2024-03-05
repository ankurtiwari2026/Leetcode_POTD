class Solution:
    def minimumLength(self, s: str) -> int:
        #taking two pointers to track the length of string
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1
