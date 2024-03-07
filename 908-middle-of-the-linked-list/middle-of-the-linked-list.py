# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        toto,rab = head,head
        while toto and rab:
            if rab.next == None:
                break
            toto = toto.next
            rab = rab.next.next
        return toto