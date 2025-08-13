class Node:

    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:

    def __init__(self,value):
        self.head=value
        self.next=None
        self.prev=None
    
    def __repr_(self):
        if self.head is None:
            print("[]")
        else:
            last=self.head;
            print(last.value)
            while last.next:
                print(last.next.value)
                last=last.next

    def append(self,value):
        if self.head is None:
                 