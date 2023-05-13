class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class operations:
    def __init__(self):
        self.head=None
        self.tail=None
    def getInput(self):
        inputList=[int(element) for element in input().split()]
        for element in inputList:
            if element!=-1:
                newnode=Node(element)
                if self.head==None:
                    self.head=self.tail=newnode
                else:
                    self.tail.next=newnode
                    self.tail=newnode
            else:
                break  
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def insert(self,pos,data):
        newnode=Node(data)
        if self.head==None:
            head=newnode
        elif pos==1:
            print("true")
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            for i in range(0,pos-2):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
    def delete(self,pos):
        if self.head is None:
            print("List is empty")
        elif pos==1:
            self.head=self.head.next
        else:
            i=1
            temp=self.head
            while i<pos and temp.next is not None:
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next
    def searchelem(self,key):
        c=0
        temp=self.head
        while temp is not None:
            if temp.data is key:
                temp=temp.next 
                c+=1
            else:
                temp=temp.next
                continue
        return c
    def length(self):
        c=0
        temp=self.head
        while temp is not None:
            c+=1
            temp=temp.next
        return c
    def conversionToCircular(self):
        self.tail.next=self.head

