class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self):
        temp=Node(input("enter the inserting Element : "))
        if(self.front==None):
            self.rear=temp
            self.front=temp
        else:
            self.rear.next=temp
            self.rear=temp

    def dequeue(self):
        if(self.front==None):
            print("\nthere are no elements in the queue ")
        else:
            print("deleting  : ",self.front.data)
            self.front=self.front.next

    def display(self):
        if(self.front==None):
            print("the Queue is Empty\n")
        else:
            ptr=self.front
            while(ptr!=self.rear):
                print(ptr.data,end=" --> ")
                ptr=ptr.next
            print(ptr.data)

    
link=Linkedlist()
while(1):
    print("\n\n1.Inserting \n2.delecting\n3.display elements\n4.Exit\n")
    op=int(input("select an option from above list : "))
    if(op==1):
        link.enqueue()
    elif(op==2):
        link.dequeue()
    elif(op==3):
        link.display()
    else:
        break