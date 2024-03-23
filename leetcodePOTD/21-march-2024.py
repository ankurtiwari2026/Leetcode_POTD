class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        new=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new    
        