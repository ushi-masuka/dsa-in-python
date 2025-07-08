class Node:

    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
       self.head=None
       self.size=0
    
    def repr(self):
        if self.head is None:
            print("[]")
        else:
            last=self.head
            print(last.value)
            while last.next is not None:
                print(last.next.value)
                last=last.next

    def __contains__(self,value):
        last=self.head
        while last is not None:
            if last==value:
                return True
            last=last.next
        return False            

    def __len__(self):
        return self.size

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.size=1
        else:
            last=self.head
            while last.next is not None:
                last=last.next
            last.next=Node(value)
        
            self.size+=1
 
    def prepend(self,value):
        first_node=Node(value)
        first_node.next=self.head
        self.head=first_node
        self.size+=1

    def insert(self,value,loc):
        if loc==0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("index not in bounds")
            else:
                last=self.head
                
                for i in range(loc-1):
                    if last.next is None:
                        raise ValueError("index not in bounds")
                    last=last.next

            new_node=Node(value)
            new_node.next=last.next
            last.next=new_node
            self.size+=1

    def delete(self,value):
        last=self.head
        if last.value==value:
            self.head=last.next
        else:
            while last.next is not None:
                if last.next.value==value:
                    last.next=last.next.next
                    break
                last=last.next
        self.size-=1   

    def pop(self,index):
        if self.head is None:
            raise ValueError("index not in bounds")
        else:
            last=self.head
            if index==0: 
                self.head=last.next
            else:
                for i in range(index-1):
                    if last is None:
                        raise ValueError("index not in bounds")
                    else:
                        last=last.next
                last.next=last.next.next
        self.size-=1
        
            

    def get(self,index):
        if self.head is None:
            raise ValueError("list empty")
        else:
            last=self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("index out of bounds")
                else:
                    last=last.next
            return last.value
             

if __name__=="__main__":
    ll=LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.delete(0)
    ll.append(5)
    ll.append(4)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    ll.append(11)
    ll.pop(0)
    ll.pop(0)
    ll.pop(0)
    ll.delete(11)
    ll.insert(150,2)
    ll.insert(300,4)
    ll.repr()
    print(ll.get(3))

