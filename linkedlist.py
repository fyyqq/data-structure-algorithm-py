
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next
        else:
            print("None")
    
    def search(self, value):
        current = self.head
        checkValue = False
        while current:
            if current.data == value:
                checkValue = True
            current = current.next

        return checkValue, value
    
    def delete(self, value):
        if not self.head:
            print("Data unavailable !")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
            current = current.next


linkedList = LinkedList()
linkedList.prepend(2)
linkedList.prepend(1)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)
linkedList.delete(3)
linkedList.display()
isHasValue, value = linkedList.search(3)
print(f"{value} exists") if isHasValue else print(f"{value} doesn't exists")




