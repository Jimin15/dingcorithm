class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    def append(self,value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self,index):
        cur = self.head
        count = 0

        while count != index:
            cur = cur.next
            count +=1
        print(cur)

    