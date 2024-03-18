class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows=0
        curr_end=float('-inf')
        for start,end in points:
            if start>curr_end:
                arrows+=1
                curr_end=end
        return arrows        
        