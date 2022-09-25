

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
                self.head.next=self.head
            else:
                ptr=self.head
                while(ptr.next!=self.head):
                    ptr=ptr.next
                temp.next=self.head
                self.head=temp
                ptr.next=self.head
        def end():
            temp=Node(input("enter the inserting element : "))
            if(self.head==None):
                self.head=temp
                self.head.next=self.head7
            else:
                ptr=self.head
                while(ptr.next!=self.head):
                    ptr=ptr.next
                ptr.next=temp
                temp.next=self.head
        def after():
            af=input("enter the element after which the insertion should be done : ")
            ptr=self.head
            f=0
            while(True):
                if(ptr.data==af):
                    temp1=ptr.next
                    break
                elif(ptr.next==self.head):
                    print("\nthe after element is not in the linked list\n")
                    f=1
                    break
                else:
                    ptr=ptr.next
            if(f==0):
                temp=Node(input("\nenter the inserting element : "))
                ptr.next=temp
                temp.next=temp1

        def before():
            bef=input("\nenter the element before which the insertion should be done : ")
            ptr=self.head
            if(ptr.data==bef):
                beg()
            else:
                f=0
                preptr=ptr
                ptr=ptr.next
                while(1):
                    if(ptr.data==bef):
                        break
                    elif(ptr.next==self.head):
                        print("\nthe before element is not in the linked list\n")
                        f=1
                        break
                    else:
                        preptr=ptr
                        ptr=ptr.next
                if(f==0):
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
            if(self.head.next==self.head):
                self.head=None
            else:
                ptr=self.head
                while(ptr.next!=self.head):
                    ptr=ptr.next
                self.head=self.head.next
                ptr.next=self.head
        def del_end():
            if(self.head.next==self.head):
                self.head=None
            else:
                preptr=self.head
                ptr=preptr
                while(ptr.next!=self.head):
                    preptr=ptr
                    ptr=ptr.next
                preptr.next=self.head
        def del_par():
            ptr=self.head
            preptr=ptr
            temp=input("enter the node need to be delected : ")
            if(self.head==None):
                print("there are no elements in the list to delete")
            elif(ptr.data==temp):
                del_beg()
            else:
                f=0
                while(True):
                    if(ptr.data==temp):
                        break
                    elif(ptr.next==self.head):
                        f=1
                        print("the entered particular element is not in the linked list")
                        break
                    else:
                        preptr=ptr
                        ptr=ptr.next
                if(f==0):
                    if(ptr.next==self.head):
                        preptr.next=self.head
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
                    elif(ptr.next==self.head):
                        f=1
                        print("there is no such element in the linked list as",val)
                        break
                    else:
                        ptr=ptr.next
                if(f==0):
                    if(temp1==self.head):
                        del_beg()
                    else:
                        temp=temp1.next
                        ptr.next=temp


        print("\n1.Delete first Element\n2.Delete Last Element\n3.Delete after a particular Element\n4.Delete particular Element\n")
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
        ptr=self.head
        flag=0
        if(self.head==None):
            print("the linked list is empty")
        else:
            while(ptr.next!=self.head):
                print("",end="  -->  ")
                print(ptr.data,end="")
                ptr=ptr.next
            print(" -->  ",ptr.data," --> ")


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