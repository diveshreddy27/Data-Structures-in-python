

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None


    def inserting(self):
        def beg():
            temp=Node(input("enter the inserting element : "))
            if(self.head==None):
                self.head=temp
            else:
                temp.next=self.head
                self.head=temp

        def end():
            temp=Node(input("enter the inserting element : "))
            if(self.head==None):
                self.head=temp
            else:
                ptr=self.head
                while(ptr.next!=None):
                    ptr=ptr.next
                ptr.next=temp
        def after():
            af=input("enter the element after which the insertion should be done : ")
            ptr=self.head
            while(True):
                if(ptr.data==af):
                    temp1=ptr.next
                    break
                elif(ptr==None):
                    print("\nthe after element is not in the linked list\n")
                    break
                else:
                    ptr=ptr.next
            temp=Node(input("\nenter the inserting element : "))
            ptr.next=temp
            temp.next=temp1

        def before():
            bef=input("\nenter the element before which the insertion should be done : ")
            ptr=self.head
            if(ptr.data==bef):
                beg()
            else:
                preptr=ptr
                ptr=ptr.next
                while(1):
                    if(ptr.data==bef):
                        break
                    elif(ptr==None):
                        print("\nthe before element is not in the linked list\n")
                        break
                    else:
                        preptr=ptr
                        ptr=ptr.next
                temp=Node(input("enter the inserting element : "))
                preptr.next=temp
                temp.next=ptr
        print("\n1.Insert Beggining\n2.Insert End\n3.Insert after\n4.Insert Before\n")
        o=int(input("select an option from above list : "))
        if(o==1):
            beg()
        elif(o==2):
            end()
        elif(o==3):
            after()
        elif(o==4):
            before()


    def deleting(self):
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
            if(self.head==None):
                print("there are no elements in the list to delete")
            elif(ptr.next==None):
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
        
        def del_afpar():
            ptr=self.head()
            if(self.head==None):
                print("there are no elements in the list to delete\n")
            else:
                val=input("\nenter after which element the deletion should be done : ")
                f=0
                while(1):
                    if(ptr.data==val):
                        temp1=ptr.next
                        break
                    elif(ptr.next==None):
                        f=1
                        print("there is no element in the linked list as",val)
                        break
                    else:
                        ptr=ptr.next
                if(f==0):
                    if(temp1==None):
                        print("there is no elements in the linked list after ",val)
                    else:
                        temp=temp1.next
                        ptr.next=temp


        print("\n1.Delete first Element\n2.Delete Last Element\n3.Delete after particular Element\n4.Delete particular Element\n")
        o=int(input("select an option from above list : "))
        if(o==1):
            del_beg()
        elif(o==2):
            del_end()
        elif(o==3):
            del_afpar()
        elif(o==4):
            del_par()


    def display(self):
        temp=self.head
        flag=0
        while(temp!=None):
            print("",end="  -->  ")
            print(temp.data, end="")
            temp=temp.next
            flag=1
        if(flag==0):
            print("Linked List is empty")


link=Linkedlist()
while(1):
    print("\n1.Inserting elements\n2.Deleting Elements\n3.Display Elements\n4.Exit\n")
    op=int(input("select an option from above list : "))
    if(op==1):
        link.inserting()
    elif(op==2):
        link.deleting()
    elif(op==3):
        link.display()
    else:
        break