# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using two pointers linkedlist middle
        temp=head
        temp2=head
        while temp2 and temp2.next:
            temp=temp.next
            temp2=temp2.next.next
        return temp    

