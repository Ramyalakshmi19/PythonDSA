import linked_list as LL
create= LL.Node(0)
linkedlist=LL.operations()

#To check if a linked list is circular        
def check_circular():
    flag=0
    temp=linkedlist.head
    while temp.next is not None:
        if temp.next==linkedlist.head:
            print("A circular linked list")
            flag+=1
            break
        else:
            temp=temp.next
            continue
    if flag==0:
        print("Not a circular linked list")
            
#To count the number of nodes in circular linked list
def count_circular():
    nodeCount=1
    temp=linkedlist.head
    while temp.next!=linkedlist.head:
        nodeCount+=1
        temp=temp.next
    print("Total num of nodes in circular linked list:",nodeCount)

def exchangeNodes():
    temp=linkedlist.head
    while temp.next!=linkedlist.head:
        temp=temp.next
    temp.data,linkedlist.head.data=linkedlist.head.data,temp.data
    

    
def traverseCircularLL():
    print(linkedlist.head.data)
    temp=linkedlist.head.next
    while temp!=linkedlist.head:
        print(temp.data)
        temp=temp.next
    
linkedlist.getInput()
linkedlist.conversionToCircular()
traverseCircularLL()
exchangeNodes()
traverseCircularLL()
