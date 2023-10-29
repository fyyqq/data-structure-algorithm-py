
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            return self.inserts(self.head, newNode)
    
    def inserts(self, oldNode, newNode):
        if newNode.value < oldNode.value:
            if not oldNode.left:
                oldNode.left = newNode
            else:
                self.inserts(oldNode.left, newNode)
        else:
            if not oldNode.right:
                oldNode.right = newNode
            else:
                self.inserts(oldNode.right, newNode)
                
    def search(self, value):
        checkValue = False
        
        if not self.head:
            print("There's no data")

        current = self.head
        while current:
            if value < self.head.value:
                if current.value == value:
                    checkValue = True
                current = current.left
            else:
                if current.value == value:
                    checkValue = True
                current = current.right

        print(f"{value} is found") if checkValue else print(f"{value} isn't found")
    
    def delete(self, value):

        if not self.head:
            print("There's no data")
            
        if value == self.head.value:
            self.head.value = self.head.right.value
            self.head.right = self.head.right.right
            return
        
        current = self.head
        checkValue = False
        while current:
            if value < self.head.value:
                if current.left.value == value:
                    current.left = current.left.left
                    checkValue = True
                    break
                current = current.left
            else:
                if current.right.value == value:
                    current.right = current.right.right
                    checkValue = True
                    break
                current = current.right
        
        print(f"{value} is deleted") if checkValue else print(f"{value} isn't found")

        

    def displayMin(self):
        current = self.head
        print("Left: ", end="")
        while current:
            print(current.value, end=" => ")
            current = current.left
        else:
            print("end")
            
    def displayMax(self):
        current = self.head
        print("Right: ", end="")
        while current:
            print(current.value, end=" => ")
            current = current.right
        else:
            print("end")


binaryTree = BinaryTree()
binaryTree.insert(5) # head
binaryTree.insert(4)
binaryTree.insert(3)
binaryTree.insert(2)
binaryTree.insert(6)
binaryTree.insert(7)
binaryTree.insert(8)

binaryTree.delete(6)

binaryTree.search(6)

binaryTree.displayMin()
binaryTree.displayMax()


