# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        #using stack 
        stack=[]
        while temp:
            stack.append(temp)
            temp=temp.next
        length=len(stack)
        middle=length//2
        for _ in range(middle):
            stack.pop(0)
        return stack.pop(0)        