class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # def get_data(self):
    #     return self.data

    # def get_next(self):
    #     return self.next_node

    # def set_next(self, new_next):
    #     self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        if (self.head):
            current = self.head
            while (current.next_node):
                current = current.next_node
            #  new_node.next_node(self.head)
            current.next_node = new_node
        else:
            self.head = new_node
        

    # def size(self, n):
    #     current = self.head
    #     count = 0
    #     while n:
    #         count += 1
    #         current =  current.get_next()
    #     return count

    def listprint(self):
        current = self.head
        while current:
            print(current.data, end='')
            print("->",end='')
            current = current.next_node


list1 = LinkedList()
# list1.size(3)
list1.insert(2)
list1.insert(5)
list1.insert(3)
list1.listprint()