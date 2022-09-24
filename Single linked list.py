class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def display_elements(self):
        temp=self.head
        flag=0
        while(temp!=None):
            print(temp.data, end="  ")
            temp=temp.next
            flag=1
        if(flag==0):
            print("Linked List is empty")
    def insert(self):
        def insert_beg():
            temp=Node(int(input("enter the node data need to be inserted : ")))
            temp.next=self.head
            self.head=temp
        def insert_end():
            temp=Node(int(input("enter the node data need to be inserted : ")))
            ptr=self.head
            if(ptr==None):
                temp.next=self.head
                self.head=temp
            else:
                while(True):
                    if(ptr.next!=None):
                        ptr=ptr.next
                    else:
                        break
                ptr.next=temp
        def insert_after():
            after=int(input("after which element the node need to be insert : "))
            ptr=self.head
            while(True):
                if(ptr.data==after):
                    temp1=ptr.next
                    break
                elif(ptr==None):
                    print("after element is not in the linked list")
                    break
                else:
                    ptr=ptr.next
            temp=Node(int(input("enter the node data need to be inserted : ")))
            ptr.next=temp
            temp.next=temp1
        def insert_before():
            before=int(input("before which element the node need to be insert : "))
            ptr=self.head
            preptr=ptr
            if(ptr.data==before):
                insert_beg()
            else:
                ptr=ptr.next
                temp=Node(int(input("enter the node data need to be inserted : ")))
                while(True):
                    if(ptr.data==before):
                        preptr.next=temp
                        temp.next=ptr
                        break
                    elif(ptr==None):
                        print("after element is not in the linked list")
                        break
                    else:
                        preptr=ptr
                        ptr=ptr.next
                    
        print("1.Insert at beggining of linked list\n2.Insert at last of linked list\n3.Insert after an element\n4.Insert before an element\n")
        o=int(input("select an option from above list : "))
        if(o==1):
            insert_beg()
        elif(o==2):
            insert_end()
        elif(o==3):
            insert_after()
        elif(o==4):
            insert_before()
    def delete(self):
        def del_beg():
            ptr=self.head
            self.head=ptr.next
        def del_end():
            ptr=self.head
            preptr=ptr
            while(True):
                if(ptr.next==None):
                    break
                else:
                    preptr=ptr
                    ptr=ptr.next
            if(self.head==ptr):
                del_beg
            else:
                preptr.next=None
        def del_par():
            ptr=self.head
            preptr=ptr
            temp=int(input("enter the node need to be delected : "))
            if(ptr.next==None):
                del_beg()
            else:
                while(True):
                    if(ptr.data==temp):
                        break
                    elif(ptr.next==None):
                        print("the entered particular element is not in the linked list")
                    else:
                        preptr=ptr
                        ptr=ptr.next
                if(ptr.next==None):
                    preptr.next=None
                else:
                    temp1=ptr.next
                    preptr.next=temp1
        print("\n1.Delete first Element\n2.Delete Last Element\n3.Delete particular Element\n")
        o=int(input("select an option from above list : "))
        if(o==1):
            del_beg()
        elif(o==2):
            del_end()
        elif(o==3):
            del_par()        
def create():
    print("         CREATING  LINKED  LIST         \n")
    n=int(input("Enter the number of nodes to be created : "))
    link=Linkedlist()
    print("Enter the data in nodes to be : \n")
    temp=Node(int(input()))
    link.head=temp
    for i in range(2,n+1):
        temp1=Node(int(input()))
        temp.next=temp1
        temp=temp1
    
    while(1):
        print("\n\n1.Inserting\n2.Deleting\n3.Display Elements \n4.Exit\n")
        op=int(input("select the options from above list  : "))
        if(op==1):
            link.insert()
        elif(op==2):
            link.delete()
        elif(op==3):
            print("LINKED LIST IS :- \n")
            link.display_elements()
        else:
            break
    
create()


