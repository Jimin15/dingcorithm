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

    def add_node(self,index,value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        index_minus_1_node = self.get_node(index-1)
        next_node = index_minus_1_node.next
        index_minus_1_node.next = new_node
        new_node.next = next_node

    def delete_node(self,index):
        if index == 0:
            self.head = self.head.next
            return

        prev = self.get_node(index-1)
        index_node = self.get_node(index)
        prev.next = index_node.next