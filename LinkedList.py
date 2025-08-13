class Node:

    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def __repr__(self):
        if self.size==0:
            return "[]"

        else:
            last=self.head
            return_string= f"[{last.value}" 
            while last.next:
                last=last.next
                return_string+= f"->{last.value}"  
            return_string+=f"]" 
            return return_string         
    
    def __contains__(self,value):
        if self.head.value==value:
            return 1
        else:
            last=self.head
            while last.next:
                last=last.next
                if last.value==value:
                    return 1
                    break
            return 0

    def __len__(self):
        return self.size

    def append(self,value):
        if self.size==0:
            self.head=Node(value)
            self.size=1
        else: 
            last=self.head
            while last.next:
                last=last.next
            last.next=Node(value)
            self.size+=1


    def prepend(self,value):
        new_head=Node(value)
        new_head.next=self.head
        self.head=new_head
        self.size+=1


    def insert(self,value,index):
        if index==0:
            self.prepend(value)
        else:
            if index>self.size:
                raise ValueError("index out of bounds")
            else:
                last=self.head
                for i in range(1,index):
                    last=last.next
                temp=last.next
                last.next=Node(value)
                last.next.next=temp
                self.size+=1


    def delete(self,value):
        last=self.head
        if self.head==None:
            raise ValueError("list is empty")
        elif self.head.value==value:
            self.head=last.next
            self.size-=1
        else:
            for i in range(1,self.size):
                if last.next.value==value:
                    last.next=last.next.next
                    self.size-=1
                    break
                    
                else:
                    last=last.next
        
            

    def pop(self,index):
        if index>=self.size:
            raise ValueError("index out of range.")
        else:
            last=self.head
            if index==0:
                topop=self.head
                self.head=last.next
                self.size-=1
                return topop.value 
            else:
                for i in range(1,index):
                    last=last.next
                topop=last.next    
                last.next=last.next.next
                self.size-=1
                return topop.value


    def get(self,index):
        if index>=self.size:
            raise ValueError("index out of bounds")
        else:
            last=self.head
            if index==0:
                return last.value
            else:
                for i in range(1,index):
                    last=last.next
                return last.next.value   


if __name__=="__main__":
    ll=LinkedList()
    ll.prepend(10)
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    
    print(0 in ll)

    ll.prepend(0)
    print(0 in ll)
    print(3 in ll)

    print(ll)
    print(len(ll))
    ll.prepend(30)
    print(ll)
    print(30 in ll)
    print(ll)
    ll.delete(2)
    ll.delete(0)
    ll.append(5)
    ll.append(6)
    ll.delete(7)
    print(ll)
    ll.pop(1)
    print(ll)
    print(ll.get(0))
    print(ll.get(1))
    print(ll.get(2))
    print(ll.get(6))
    ll.pop(0)
    ll.pop(0)
    ll.pop(0)
    ll.pop(0)
    ll.pop(0)
    print(ll.pop(0))
    print(ll)
    print(6 in ll)
    print(1 in ll)
    ll.insert(1,1)
    print(ll)