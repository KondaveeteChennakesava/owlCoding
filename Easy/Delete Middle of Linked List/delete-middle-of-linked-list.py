#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if head == None or head.next == None:
            return None
        rab = head
        toto = head
        prev = None
        while rab!= None and rab.next!=None and toto != None and toto.next != None:
            prev = toto
            toto = toto.next
            rab = rab.next.next
        prev.next = toto.next
        return head
        #code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        obj = Solution();
        res=obj.deleteMid(ll.head)
        printList(res)
# } Driver Code Ends