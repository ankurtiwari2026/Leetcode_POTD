# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #make a dummy node to store address of head 
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        for _ in range(n+1):
            first=first.next
        # iterate loop till first is not Null
        while first is not None:
            first=first.next
            second=second.next
        # incerement second two times
        second.next=second.next.next
        return dummy.next        
        