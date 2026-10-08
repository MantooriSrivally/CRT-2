#876. Middle of the Linked List
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
#solution-1:
class Solution:
    def middleNode(self,head:ListNode|None)->ListNode|None:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next 
        mid_ind=count//2
        temp=head
        for _ in range(mid_ind):
            temp=temp.next
        return temp
#solution-2
class Solution:
    def middleNone(self,head:ListNode|None)->ListNode|None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        return slow
#41
