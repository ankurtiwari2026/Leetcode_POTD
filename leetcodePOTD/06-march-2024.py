# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l1=head #slow pointer 
        l2=head # fast pointer 
        while l1 and  l1.next:
            l2=l2.next
            #incerement fast one time more than slow 
            l1=l1.next.next
            #if slow and fast equal hai to cycle exixt krege
            if l1==l2:
                return True
        return False        

