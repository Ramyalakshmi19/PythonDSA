import linked_list as LL
create= LL.Node(0)
linkedlist=LL.operations()

#method 1(slow pointer and fast pointer)
def middle_elem1(): 
    fast=slow=linkedlist.head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next 
    print(slow.data)
    
#method 2 (find the length of the linked list and return the middle elemnt)
def middle_elem2():
    temp=linkedlist.head
    c=linkedlist.length()
    print("Length:",c)
    middleNum= (int(c/2))+1
    print("MiddleNum:",middleNum)
    for i in range(1,middleNum):
        temp=temp.next 
    print(temp.data)
    
# Method 2 (use the variable count instead of fast)
def middle_elem3():
    temp=linkedlist.head
    mid_elem=linkedlist.head
    count=1
    while temp is not None:
        count+=1
        if count%2==0:
            temp=temp.next
            continue
        else:
            mid_elem=mid_elem.next 
            temp=temp.next
    print(mid_elem.data)

#-------------------------------------------------
# To find the middle element of the linked list 
linkedlist.getInput()
linkedlist.traverse()
print("----------")
middle_elem3()
#--------------------------------------------------
# to find the number of times a given integer occurs in the linked list
c=linkedlist.searchelem(5) 
print(" The count of the element 5 is",c)  