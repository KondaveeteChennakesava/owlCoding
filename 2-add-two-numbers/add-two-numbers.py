# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        carry,x = 0,0
        while l1 and l2:
            k = self.add(l1.val,l2.val) + x
            x = 0
            if k > 9:
                x = k//10
                k = k%10
            t = ListNode(k)
            curr.next = t
            curr = t
            l1 = l1.next
            l2 = l2.next
            # print(k,x)
        while l1:
            k = l1.val + x
            x = 0
            if k > 9:
                x = k // 10
                k = k % 10
            t1 = ListNode(k)
            curr.next = t1
            curr = t1
            l1 = l1.next
            # print(k,x)
        while l2:
            k = l2.val + x
            x = 0
            if k > 9:
                x = k // 10
                k = k % 10
            t2 = ListNode(k)
            curr.next = t2
            curr = t2
            l2 = l2.next
            # print(k,x)

        if x:
            tt = ListNode(x)
            curr.next = tt
        return ans.next
    def add(self,a,b):
        if a == None:return b
        if b == None:return a
        return a+b