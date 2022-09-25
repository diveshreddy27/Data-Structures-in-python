class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.top=None
    
    def push(self,value):
        temp=Node(value,self.top)
        self.top=temp
    def pop(self):
        if(self.top==None):
            print("stack is empty")
        else:
            value=self.top.data
            self.top=self.top.next
            print("popped : ",value)
    def display(self):
        if(self.top==None):
            print("stack is empty")
        else:
            ptr=self.top
            while(ptr!=None):
                print(ptr.data,end=" <-- ")
                ptr=ptr.next
link=Linkedlist()
while(1):
    print("\n1.Inserting Elements\n2.Deleting elements\n3.Display Elements\n4.Exit\n")
    op=int(input("select an option from above list : "))
    if(op==1):
        x=input("\nenter the inserting value : ")
        link.push(x)
    elif(op==2):
        link.pop()
    elif(op==3):
        link.display()
    else:
        break


