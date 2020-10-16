

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # add nodes
    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    # find the value 
    def findval(self, fval):
        if fval < self.data:
            if self.left is None:
                return str(fval)+" Not Found"
            return self.left.findval(fval)
        elif fval > self.data:
            if self.right is None:
                return str(fval)+" Not Found"
            return self.right.findval(fval)
        else:
            return str(self.data) + ' is found'

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.add(6) # 12 left side
root.add(14) # 12 right side
root.add(3) # 12 -- 6 left side 
root.add(8) # 12 -- 6 right side 
root.add(18) # 12 -- 14 right side 
root.add(13) # 12 -- 14 left side 
root.add(7) # 12 -- 8 left side 

print(root.findval(7))
print(root.findval(14))
print("-----------")
root.PrintTree()