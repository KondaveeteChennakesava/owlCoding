# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = head
        while temp != None:
            l.append(temp.val)
            temp = temp.next
        l.reverse()
        ans = [l[0]]
        for i in l[1:]:
            if i >= ans[-1]:
                ans.append(i)
        a = ListNode(1)
        flag = a
        ans.reverse()
        for i in ans:
            temp = ListNode(i)
            a.next = temp
            a = temp
        return flag.next