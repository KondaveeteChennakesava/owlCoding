#User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s1,s2 ='',''
        while l1:
            s1 += str(l1.data)
            l1 = l1.next
        while l2:
            s2 += str(l2.data)
            l2 = l2.next
        ans = LinkedList()
        s = str(abs(int(s1) - int(s2)))
        if not s:
            return None
        ans = Node(s[0])
        nxt = ans
        for i in s[1:]:
            nxtn = Node(i)
            nxt.next = nxtn
            nxt = nxtn
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends