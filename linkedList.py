class Node:
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None

class Linked_List:
    def __init__(self):
        self.head_value = None

    # Print the linked list
    def list_print(self):
        printval = self.head_value
        while printval is not None:
            print (printval.data_value)
            printval = printval.next_value


    def atBegining(self,new_data):
        New_Node = Node(new_data)
        # add the node that in head_value in next_value of the New_Node
        New_Node.next_value = self.head_value
        # add the New_Node to head_avalue of the list
        self.head_value = New_Node

    # Function to add New_Node
    def atEnd(self, new_data):
        New_Node = Node(new_data)
        # check if head_value is empty, if true add the New_Node
        if self.head_value is None:
            self.head_value = New_Node
            return
        # at first set the head of the nodes list
        last = self.head_value
        # check if next node not None
        while(last.next_value):
            # if not None set the next_value in last, then check new lext_value if has next_value too
            last = last.next_value
        # if last.next_value == None, that mean this is the last Node in the list, add New_Node in its next_value
        last.next_value = New_Node

    # Function to add node
    def inbetween(self,middle_node,new_data):
        if middle_node is None:
            print("the middle node is not exist")
            return

        New_Node = Node(new_data)
        # get the next_value of the middle node and set it in New_Node 
        New_Node.next_value = middle_node.next_value
        # change the next_value in middle_node to New_Node
        middle_node.next_value = New_Node

    # Function to delete an element/Node
    def Delete_Node(self, delete_node):
        Head_Value = self.head_value
        
        # this part to delete the first node
        if Head_Value is not None:
            # check in data_value of this node is equel the delete_node
            if Head_Value.data_value == delete_node:
                self.head_value = Head_Value.next_value
                Head_Value = None
                return

        # this check loop over the nodes after first node
        while (Head_Value is not None):
            # This loop will be broken if this is the node that we want to delete
            if Head_Value.data_value == delete_node:
                break
            # set the next_value of the current Node in Parevius to use
            previous_node = Head_Value
            # set the next node in list to check it
            Head_Value = Head_Value.next_value
        
        # tis is another check
        if (Head_Value == None):
            return
        # this to store the previous node of the delete node, to add next_value of the delete node in previous node
        previous_node.next_value = Head_Value.next_value
        # delete the node
        Head_Value = None

list = Linked_List()
list.head_value = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")

# Link first Node to second node
list.head_value.next_value = n2
# Link secound Node to threed node
n2.next_value = n3

# add a node at the begining of the nodes list
list.atBegining("Sun")

# add a new node at the end of the nodes list
list.atEnd("Thu")

#!"§$%&/()=" ?????? !!!!!!!! I need search! I don't now
list.inbetween(list.head_value.next_value.next_value,"Fri")
list.list_print()
print("=============")
list.Delete_Node("Fri")
list.list_print()