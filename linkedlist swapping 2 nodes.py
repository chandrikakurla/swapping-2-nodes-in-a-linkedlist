#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #inserting elements into linkedlist
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while True:
            if lastnode.next is None:
                break
            lastnode=lastnode.next
        lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        print("elements in linkedlist are:")
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #function to swap two nodes in linkedlist
    def swap_nodes(self,a,b):
        #if both the nodes contain same data then swaping doesnt change linkedlist
        if a is b:
            return
        previous_a=None
        current_a=self.head
        #recording previous node,current node of a
        while current_a is not None and current_a.data!=a:
            previous_a=current_a
            current_a=current_a.next
        previous_b=None
        current_b=self.head
        #recording previous node,current node of b
        while current_b is not None and current_b.data!=b:
            previous_b=current_b
            current_b=current_b.next
        #if any one of given element is not present then we cannot swap
        if current_a is None or current_b is None:
            return
        if previous_a is not None:
            previous_a.next=current_b
        else:
            self.head=current_b
        if previous_b is not None:
            previous_b.next=current_a
        else:
            self.head=current_a
        temp=current_a.next
        current_a.next=current_b.next
        current_b.next=temp
if __name__ == "__main__":
    llist=LinkedList()
    firstnode=Node(1)
    secondnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    fifthnode=Node(5)
    llist.insert(firstnode)
    llist.insert(secondnode)
    llist.insert(thirdnode)
    llist.insert(fourthnode)
    llist.insert(fifthnode)
    print("linkedlist before swapping")
    llist.printllist()
    llist.swap_nodes(1,5)
    print("linkedlist after swapping")
    llist.printllist()


    
    


