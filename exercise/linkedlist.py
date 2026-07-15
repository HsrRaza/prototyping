class Node:
    def __init__(self , data):
        self.data = data
        self.next =None
    
class LinkedList:
    def __init__(self):
        self.head =None

    # insert at end
    def append(self , data):
        new_node = Node(data)

        if self.head is None:
            self.head =new_node
            return
        current = self.head

        while current.next is not None:
            current =current.next
        current.next = new_node
        
    
    # display all  nodes
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    # insert at beginning

    def prepend(self , data):
        new_node = Node(data)

        new_node.next =self.head
        self.head =new_node

    # search for value
    def search_value(self ,value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current =current.next
        return False
    # count nodes

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count +=1
            current =current.next
        return count
        
    # delet first occurrence
    def delete(self , value):
        if self.head is None:
            return
        
        # deleting head
        if self.head.data == value:
            self.head = self.head.next
            return
        
        prev = None
        current = self.head

        while current is not None:

            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current =current.next
        print("value not found")

    def reverse(self):
        current =self.head
        prev =None
        while current is not None:
            next_node =current.next
            current.next =prev
            prev =current
            current = next_node
        self.head =prev



    
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

# ll.prepend(60)

ll.display()
# print(ll.search_value(50))

# print(ll.length())


# ll.delete(60)

ll.reverse()

ll.display()