class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        res=[]
        while i<len(nums1) and j<len(nums2):
            num1=nums1[i]
            num2=nums2[j]
            if num1==num2:
                if not res or res[-1]!=num1:
                    res.append(num1)
                i+=1
                j+=1
            elif num1<num2:
                i+=1
            else:
                j+=1
        return res                

                